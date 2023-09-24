from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from alembic import op

from reahl.component.migration import Migration

class CreateDB(Migration):
    def schedule_upgrades(self):
        self.schedule('alter', op.create_table, 'cobject',
                      Column('keyc', Integer(), nullable=False),
                      Column('another_c_key', Integer()),
                      PrimaryKeyConstraint('keyc', name='pk_cobject')
                      )
        self.schedule('create_fk', op.create_foreign_key, 'fk_cobject_another_c_key_cobject',
                      'cobject', 'cobject', ['another_c_key'], ['keyc'])



class To31(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_cobject_another_c_key_cobject', 'cobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_cobject_another_c_key_cobject',
                      'cobject', 'cobject', ['another_c_key'], ['keyc1'])

        self.schedule('alter', op.alter_column, 'cobject', 'keyc', new_column_name='keyc1')


class To35(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_cobject_another_c_key_cobject', 'cobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_cobject_another_c_key_cobject',
                      'cobject', 'cobject', ['another_c_key'], ['keyc2'])

        self.schedule('alter', op.alter_column, 'cobject', 'keyc1', new_column_name='keyc2')

        
class To40(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_cobject_another_c_key_cobject', 'cobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_cobject_another_c_key_cobject',
                      'cobject', 'cobject', ['another_c_key'], ['keyc3'])

        self.schedule('alter', op.alter_column, 'cobject', 'keyc2', new_column_name='keyc3')
