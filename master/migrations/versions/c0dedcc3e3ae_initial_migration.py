"""Initial migration

Revision ID: c0dedcc3e3ae
Revises: 
Create Date: 2024-05-19 23:41:32.624231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0dedcc3e3ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('server',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hostname')
    )
    op.create_table('server_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pretty_name', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('role', sa.Enum('USER', 'ADMIN', name='enumuserrole'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pretty_name'),
    sa.UniqueConstraint('username')
    )
    op.create_table('server_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('cpu_perc', sa.Float(), nullable=False),
    sa.Column('loadavg', sa.JSON(), nullable=False),
    sa.Column('mem_perc', sa.Float(), nullable=False),
    sa.Column('partitions', sa.JSON(), nullable=False),
    sa.Column('bytes_received', sa.Integer(), nullable=True),
    sa.Column('bytes_sent', sa.Integer(), nullable=True),
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['server.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('server_server_group_helper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.Column('server_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['server_group_id'], ['server_group.id'], ),
    sa.ForeignKeyConstraint(['server_id'], ['server.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('server_server_group_helper')
    op.drop_table('server_data')
    op.drop_table('user')
    op.drop_table('server_group')
    op.drop_table('server')
    # ### end Alembic commands ###
