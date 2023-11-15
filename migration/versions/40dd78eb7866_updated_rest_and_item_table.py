"""updated rest and item table

Revision ID: 40dd78eb7866
Revises: 4af741dd24ba
Create Date: 2023-11-02 09:40:22.496939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40dd78eb7866'
down_revision: Union[str, None] = '4af741dd24ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
   pass


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurants', 'image')
    op.drop_column('items', 'image')
    # ### end Alembic commands ###
