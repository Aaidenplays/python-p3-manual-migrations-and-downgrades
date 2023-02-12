"""Renaming students to scholars2

Revision ID: 1a1ede7d9993
Revises: 27dd49c2a1b9
Create Date: 2023-02-11 11:15:27.479104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a1ede7d9993'
down_revision = '27dd49c2a1b9'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
