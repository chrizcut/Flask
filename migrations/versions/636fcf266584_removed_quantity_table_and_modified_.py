"""removed Quantity table and modified Ingredient table

Revision ID: 636fcf266584
Revises: f1d86c6274a6
Create Date: 2025-02-02 19:48:06.716009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '636fcf266584'
down_revision = 'f1d86c6274a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_ingredient')
    with op.batch_alter_table('ingredient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('recipe_id', sa.Integer(), nullable=False))
        batch_op.create_index(batch_op.f('ix_ingredient_recipe_id'), ['recipe_id'], unique=False)
        batch_op.create_foreign_key('fk_ingredient_recipe', 'recipe', ['recipe_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ingredient', schema=None) as batch_op:
        batch_op.drop_constraint('fk_ingredient_recipe', type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_ingredient_recipe_id'))
        batch_op.drop_column('recipe_id')
        batch_op.drop_column('quantity')

    op.create_table('_alembic_tmp_ingredient',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('quantity', sa.VARCHAR(), nullable=True),
    sa.Column('recipe_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], name='fk_ingredient_recipe'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
