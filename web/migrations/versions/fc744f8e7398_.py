"""Initial db scheme

Revision ID: fc744f8e7398
Revises: 
Create Date: 2016-11-22 20:42:01.551610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc744f8e7398'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('title_ru', sa.String(length=256), nullable=True),
    sa.Column('title_en', sa.String(length=256), nullable=True),
    sa.Column('text_ru', sa.Text(), nullable=True),
    sa.Column('text_en', sa.Text(), nullable=True),
    sa.Column('last_edit', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_page_name'), 'page', ['name'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('full_text', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('cover_image', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_role_title'), 'role', ['title'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('full_name', sa.String(length=50), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('second_name', sa.String(length=20), nullable=True),
    sa.Column('initials', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_uid'), 'user', ['uid'], unique=True)
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('file_size', sa.Integer(), nullable=True),
    sa.Column('file_name', sa.String(length=512), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('page_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['page_id'], ['page.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.drop_table('file')
    op.drop_index(op.f('ix_user_uid'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_role_title'), table_name='role')
    op.drop_table('role')
    op.drop_table('post')
    op.drop_index(op.f('ix_page_name'), table_name='page')
    op.drop_table('page')
    ### end Alembic commands ###
