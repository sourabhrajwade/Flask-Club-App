"""privacy table added

Revision ID: bf62573d393a
Revises: 
Create Date: 2020-08-09 12:23:40.215226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf62573d393a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('private',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('setting', sa.Boolean(), nullable=True),
    sa.Column('club_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['club_id'], ['clubs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('private')
    # ### end Alembic commands ###
