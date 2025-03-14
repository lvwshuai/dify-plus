"""add_tenant_model_sync_extend

Revision ID: d8929f29057c
Revises: 41e6e402d572
Create Date: 2024-07-22 12:17:28.093253

"""
import sqlalchemy as sa
from alembic import op

import models as models

# revision identifiers, used by Alembic.
revision = 'd8929f29057c'
down_revision = '41e6e402d572'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model_sync_config_extend',
    sa.Column('id', models.types.StringUUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('model_id', models.types.StringUUID(), nullable=True),
    sa.Column('is_all', sa.Boolean(), server_default=sa.text('true'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='model_sync_config_extend_pkey'),
    sa.UniqueConstraint('model_id', name='unique_model_id')
    )
    op.create_table('tenant_model_sync_extend',
    sa.Column('id', models.types.StringUUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', models.types.StringUUID(), nullable=False),
    sa.Column('model_id', models.types.StringUUID(), nullable=False),
    sa.Column('origin_model_id', sa.String(length=255), nullable=False),
    sa.Column('is_all', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='tenant_model_sync_extend_pkey')
    )
    with op.batch_alter_table('tenant_model_sync_extend', schema=None) as batch_op:
        batch_op.create_index('tenant_model_sync_extend_model_idx', ['model_id'], unique=False)
        batch_op.create_index('tenant_model_sync_extend_tenant_idx', ['tenant_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tenant_model_sync_extend', schema=None) as batch_op:
        batch_op.drop_index('tenant_model_sync_extend_tenant_idx')
        batch_op.drop_index('tenant_model_sync_extend_model_idx')

    op.drop_table('tenant_model_sync_extend')
    op.drop_table('model_sync_config_extend')
    # ### end Alembic commands ###
