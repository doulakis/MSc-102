"""Change length of bookmarks #3

Revision ID: 27a51010f13c
Revises: 06ca56f6ce37
Create Date: 2018-12-18 14:33:06.903446

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '27a51010f13c'
down_revision = '06ca56f6ce37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_bookmark_url', table_name='bookmark')
    op.drop_column('bookmark', 'url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookmark', sa.Column('url', mysql.VARCHAR(collation='utf8_unicode_ci', length=512), nullable=True))
    op.create_index('ix_bookmark_url', 'bookmark', ['url'], unique=False)
    # ### end Alembic commands ###
