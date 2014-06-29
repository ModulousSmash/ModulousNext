"""Add reddit name to profiles

Revision ID: 275951252d
Revises: 217af36c820
Create Date: 2014-06-29 15:28:28.417917

"""

# revision identifiers, used by Alembic.
revision = '275951252d'
down_revision = '217af36c820'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('redditUsername', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'redditUsername')
    ### end Alembic commands ###
