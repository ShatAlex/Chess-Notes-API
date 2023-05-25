"""Add Match with GameMode

Revision ID: ebb6536ff4d4
Revises: a34dfca7a30c
Create Date: 2023-05-25 15:54:22.721506

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ebb6536ff4d4'
down_revision = 'a34dfca7a30c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gamemode',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('mode', sa.String(), nullable=False),
                    sa.Column('rules', sa.String(), nullable=False),
                    sa.Column('time_limit', sa.TIMESTAMP(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('match',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('result', sa.String(), nullable=False),
                    sa.Column('opponents_rating', sa.Integer(), nullable=True),
                    sa.Column('played_on', sa.TIMESTAMP(), nullable=True),
                    sa.Column('moves', sa.String(), nullable=True),
                    sa.Column('gamemode', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['gamemode'], ['gamemode.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('match')
    op.drop_table('gamemode')
    # ### end Alembic commands ###