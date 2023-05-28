"""empty message

Revision ID: aa01fc72001a
Revises: a90a924da8f1
Create Date: 2023-05-29 01:24:07.159554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa01fc72001a'
down_revision = 'a90a924da8f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('cover_image', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'cover_image')
    # ### end Alembic commands ###
