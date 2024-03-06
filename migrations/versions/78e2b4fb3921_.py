"""empty message

Revision ID: 78e2b4fb3921
Revises: 
Create Date: 2024-03-05 21:07:12.243546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78e2b4fb3921'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###