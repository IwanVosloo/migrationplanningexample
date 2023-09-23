

from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from alembic import op

from reahl.component.migration import Migration


class CreateDB(Migration):
    def schedule_upgrades(self):
        self.schedule('alter', op.create_table, 'myobject',
                      Column('id', Integer(), nullable=False),
                      Column('to_c', Integer()),
                      PrimaryKeyConstraint('id', name='pk_myobject')
                      )
        self.schedule('create_fk', op.create_foreign_key, 'fk_myobject_to_c_cobject',
                      'myobject', 'cobject', ['to_c'], ['keyc'])



class ToNewC(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_myobject_to_c_cobject', 'myobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_myobject_to_c_cobject',
                      'myobject', 'cobject', ['to_c'], ['keyc3'])


