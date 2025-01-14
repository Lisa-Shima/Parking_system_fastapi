"""Initial migration for my models

Revision ID: 0a0c4a349169
Revises: 
Create Date: 2024-11-22 10:47:14.372792

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a0c4a349169'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parking_lots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parking_lots_id'), 'parking_lots', ['id'], unique=False)
    op.create_index(op.f('ix_parking_lots_name'), 'parking_lots', ['name'], unique=False)
    op.create_table('parking_spots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lot_id', sa.Integer(), nullable=True),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lot_id'], ['parking_lots.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parking_spots_id'), 'parking_spots', ['id'], unique=False)
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('spot_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['spot_id'], ['parking_spots.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reservations_id'), 'reservations', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reservations_id'), table_name='reservations')
    op.drop_table('reservations')
    op.drop_index(op.f('ix_parking_spots_id'), table_name='parking_spots')
    op.drop_table('parking_spots')
    op.drop_index(op.f('ix_parking_lots_name'), table_name='parking_lots')
    op.drop_index(op.f('ix_parking_lots_id'), table_name='parking_lots')
    op.drop_table('parking_lots')
    # ### end Alembic commands ###
