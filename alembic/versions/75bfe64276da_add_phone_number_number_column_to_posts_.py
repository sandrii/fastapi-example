"""add phone number number column to posts table, second try

Revision ID: 75bfe64276da
Revises: 1e4809a59ee1
Create Date: 2022-01-25 20:14:27.390195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75bfe64276da'
down_revision = '1e4809a59ee1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'phone_number')
    # ### end Alembic commands ###