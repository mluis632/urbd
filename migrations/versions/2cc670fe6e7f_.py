"""empty message

Revision ID: 2cc670fe6e7f
Revises: 
Create Date: 2020-12-05 14:42:26.856375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cc670fe6e7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('number_unit', sa.String(length=100), nullable=True))
    op.drop_column('clients', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('address', sa.VARCHAR(length=100), nullable=True))
    op.drop_column('clients', 'number_unit')
    # ### end Alembic commands ###
