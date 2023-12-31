"""updated vendor and cart

Revision ID: 8101ba6a8480
Revises: 71ebb44b451e
Create Date: 2023-11-20 13:59:47.905626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8101ba6a8480'
down_revision: Union[str, None] = '71ebb44b451e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart_items', sa.Column('vendor_id', sa.String(length=60), nullable=True))
    op.alter_column('cart_items', 'customer_id',
               existing_type=sa.VARCHAR(length=60),
               nullable=True)
    op.create_foreign_key(None, 'cart_items', 'vendors', ['vendor_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cart_items', type_='foreignkey')
    op.alter_column('cart_items', 'customer_id',
               existing_type=sa.VARCHAR(length=60),
               nullable=False)
    op.drop_column('cart_items', 'vendor_id')
    # ### end Alembic commands ###
