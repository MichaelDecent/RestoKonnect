"""updated the database

Revision ID: bab370e140b1
Revises: ebbb99f58fa6
Create Date: 2023-11-22 10:49:49.937625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bab370e140b1'
down_revision: Union[str, None] = 'ebbb99f58fa6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart_items', sa.Column('restaurant_id', sa.String(length=60), nullable=False))
    op.drop_constraint('cart_items_vendor_id_fkey', 'cart_items', type_='foreignkey')
    op.drop_constraint('cart_items_customer_id_fkey', 'cart_items', type_='foreignkey')
    op.create_foreign_key(None, 'cart_items', 'restaurants', ['restaurant_id'], ['id'])
    op.drop_column('cart_items', 'vendor_id')
    op.drop_column('cart_items', 'customer_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart_items', sa.Column('customer_id', sa.VARCHAR(length=60), autoincrement=False, nullable=True))
    op.add_column('cart_items', sa.Column('vendor_id', sa.VARCHAR(length=60), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'cart_items', type_='foreignkey')
    op.create_foreign_key('cart_items_customer_id_fkey', 'cart_items', 'customers', ['customer_id'], ['id'])
    op.create_foreign_key('cart_items_vendor_id_fkey', 'cart_items', 'vendors', ['vendor_id'], ['id'])
    op.drop_column('cart_items', 'restaurant_id')
    # ### end Alembic commands ###
