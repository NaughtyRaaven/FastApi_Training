"""add content column to posts table

Revision ID: c64e78c5fcd6
Revises: e175c5c7cf61
Create Date: 2024-02-15 18:08:31.706275

"""

from tokenize import String
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c64e78c5fcd6"
down_revision: Union[str, None] = "e175c5c7cf61"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
