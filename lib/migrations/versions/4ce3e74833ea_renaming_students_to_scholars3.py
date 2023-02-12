"""Renaming students to scholars3

Revision ID: 4ce3e74833ea
Revises: 1a1ede7d9993
Create Date: 2023-02-11 11:16:53.063928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ce3e74833ea'
down_revision = '1a1ede7d9993'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')