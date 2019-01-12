#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Post
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@x.x.x.x/msc102_tests'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='stelios')
        u.set_password('yolo')
        self.assertFalse(u.check_password('lol'))
        self.assertTrue(u.check_password('yolo'))

    def test_avatar(self):
        u = User(username='stelios', email='stelios@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/55582ec0ebb6f377322e54ed30183197?d=retro&s=128'))

    def test_follow(self):
        u1 = User(username='stelios', email='stelios@example.com')
        u2 = User(username='sofia', email='sofia@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'sofia')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'stelios')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        # create four users
        u1 = User(username='stelios', email='stelios@example.com')
        u2 = User(username='sofia', email='sofia@example.com')
        u3 = User(username='maria', email='maria@example.com')
        u4 = User(username='george', email='george@example.com')
        db.session.add_all([u1, u2, u3, u4])

        # create four posts
        now = datetime.utcnow()
        p1 = Post(body="post from stelios", author=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from sofia", author=u2,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from maria", author=u3,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from george", author=u4,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # setup the followers
        u1.follow(u2)  # stelios follows sofia
        u1.follow(u4)  # stelios follows george
        u2.follow(u3)  # sogia follows maria
        u3.follow(u4)  # maria follows george
        db.session.commit()

        # check the followed posts of each user
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])


if __name__ == '__main__':
    unittest.main(verbosity=2)
