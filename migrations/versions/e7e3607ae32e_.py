"""empty message

Revision ID: e7e3607ae32e
Revises: 93bb371a64b2
Create Date: 2016-08-14 18:58:20.665686

"""

# revision identifiers, used by Alembic.
revision = 'e7e3607ae32e'
down_revision = '93bb371a64b2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_column('posts', 'title')
    ### end Alembic commands ###
