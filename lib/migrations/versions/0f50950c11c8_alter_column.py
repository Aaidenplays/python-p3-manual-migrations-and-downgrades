"""alter column

Revision ID: 0f50950c11c8
Revises: 4ce3e74833ea
Create Date: 2023-02-12 12:22:33.798758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f50950c11c8'
down_revision = '4ce3e74833ea'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name='first_name')


def downgrade() -> None:
    op.alter_column('scholars', 'first_name', new_column_name='name')
