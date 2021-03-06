"""remove adjclose price from table

Revision ID: 23ae6815d2a2
Revises: 96229a79420d
Create Date: 2022-04-17 01:12:47.498813

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "23ae6815d2a2"
down_revision = "96229a79420d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("LBG_OHLC_1DAY", "ADJ_CLOSE")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("LBG_OHLC_1DAY", sa.Column("ADJ_CLOSE", mysql.FLOAT(), nullable=True))
    # ### end Alembic commands ###
