

from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from alembic import op

from reahl.component.migration import Migration


class CreateDB(Migration):
    def schedule_upgrades(self):
        self.schedule('alter', op.create_table, 'myobject',
                      Column('key', Integer(), nullable=False),
                      Column('to_c_key', Integer()),
                      PrimaryKeyConstraint('key', name='pk_myobject')
                      )
        self.schedule('create_fk', op.create_foreign_key, 'fk_myobject_to_c_key_cobject',
                      'myobject', 'cobject', ['to_c_key'], ['keyc'])


class ToNewC(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_myobject_to_c_key_cobject', 'myobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_myobject_to_c_key_cobject',
                      'myobject', 'cobject', ['to_c_key'], ['keyc3'])


