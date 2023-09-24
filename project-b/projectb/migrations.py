from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from alembic import op

from reahl.component.migration import Migration


class CreateDB(Migration):
    def schedule_upgrades(self):
        self.schedule('alter', op.create_table, 'bobject',
                      Column('key', Integer(), nullable=False),
                      Column('to_c_key', Integer()),
                      PrimaryKeyConstraint('key', name='pk_bobject')
                      )
        self.schedule('create_fk', op.create_foreign_key, 'fk_bobject_to_c_key_cobject',
                      'bobject', 'cobject', ['to_c_key'], ['keyc'])


class ToNewC31(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_bobject_to_c_key_cobject', 'bobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_bobject_to_c_key_cobject',
                      'bobject', 'cobject', ['to_c_key'], ['keyc1'])


class ToNewC40(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_bobject_to_c_key_cobject', 'bobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_bobject_to_c_key_cobject',
                      'bobject', 'cobject', ['to_c_key'], ['keyc3'])
        

