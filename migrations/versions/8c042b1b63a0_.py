"""empty message

Revision ID: 8c042b1b63a0
Revises: 526d8e77cc41
Create Date: 2020-08-29 19:46:22.187959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c042b1b63a0'
down_revision = '526d8e77cc41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('contact_number', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('name')
    # ### end Alembic commands ###
