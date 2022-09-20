"""followers

Revision ID: 499b2ad8d763
Revises: 5c4bbfc5f982
Create Date: 2022-09-20 16:44:27.650828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '499b2ad8d763'
down_revision = '5c4bbfc5f982'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
