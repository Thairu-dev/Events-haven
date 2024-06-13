"""Create events table

Revision ID: 122eb80c610c
Revises: a89b852b8fd7
Create Date: 2023-09-04 20:46:10.206301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '122eb80c610c'
down_revision = 'a89b852b8fd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###