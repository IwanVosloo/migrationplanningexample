from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from alembic import op

from reahl.component.migration import Migration


class CreateDB(Migration):
    def schedule_upgrades(self):
        self.schedule('alter', op.create_table, 'tablec',
                      Column('keyc', Integer(), nullable=False),
                      Column('another_key', Integer()),
                      PrimaryKeyConstraint('keyc', name='pk_tablec')
                      )
        self.schedule('create_fk', op.create_foreign_key, 'fk_tablec_another_key_tablec',
                      'tablec', 'tablec', ['another_key'], ['keyc'])



class Migration31(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_tablec_another_key_tablec', 'tablec')
        self.schedule('create_fk', op.create_foreign_key, 'fk_tablec_another_key_tablec',
                      'tablec', 'tablec', ['another_key'], ['keyc1'])

        self.schedule('drop_pk', op.drop_constraint, 'pk_tablec', 'tablec')
        self.schedule('alter', op.alter_column, 'tablec', 'keyc', new_column_name='keyc1')
        self.schedule('create_pk', op.create_primary_key, 'pk_tablec', 'tablec', ['keyc1'])
        
