"""Bookmark Scheme

Revision ID: dd790f425d0c
Revises: 17f11a285f85
Create Date: 2019-01-09 16:38:18.464324

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd790f425d0c'
down_revision = '17f11a285f85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookmark', sa.Column('title', sa.String(length=255), nullable=True))
    op.drop_column('bookmark', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookmark', sa.Column('description', mysql.VARCHAR(collation='utf8_unicode_ci', length=255), nullable=True))
    op.drop_column('bookmark', 'title')
    # ### end Alembic commands ###
