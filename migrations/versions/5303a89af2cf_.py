"""empty message

Revision ID: 5303a89af2cf
Revises: 2fb814fcd2b
Create Date: 2015-11-17 11:40:38.463934

"""

# revision identifiers, used by Alembic.
revision = '5303a89af2cf'
down_revision = '2fb814fcd2b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###
