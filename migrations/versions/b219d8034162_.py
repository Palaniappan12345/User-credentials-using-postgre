"""empty message

Revision ID: b219d8034162
Revises: e1d5c2850ccf
Create Date: 2020-05-04 20:47:58.130741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b219d8034162'
down_revision = 'e1d5c2850ccf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('state', sa.String(length=50), nullable=True),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city')
    # ### end Alembic commands ###
