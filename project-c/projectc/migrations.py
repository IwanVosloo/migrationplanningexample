from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from alembic import op

from reahl.component.migration import Migration


class CreateDB(Migration):
    def schedule_upgrades(self):
        self.schedule('alter', op.create_table, 'cobject',
                      Column('keyc', Integer(), nullable=False),
                      Column('another_c', Integer()),
                      PrimaryKeyConstraint('keyc', name='pk_cobject')
                      )
        self.schedule('create_fk', op.create_foreign_key, 'fk_cobject_another_c_cobject',
                      'cobject', 'cobject', ['another_c'], ['keyc'])



class Migration31(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_cobject_another_c_cobject', 'cobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_cobject_another_c_cobject',
                      'cobject', 'cobject', ['another_c'], ['keyc1'])

        self.schedule('drop_pk', op.drop_constraint, 'pk_cobject', 'cobject')
        self.schedule('alter', op.alter_column, 'cobject', 'keyc', new_column_name='keyc1')
        self.schedule('create_pk', op.create_primary_key, 'pk_cobject', 'cobject', ['keyc1'])


class Migration35(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_cobject_another_c_cobject', 'cobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_cobject_another_c_cobject',
                      'cobject', 'cobject', ['another_c'], ['keyc2'])

        self.schedule('drop_pk', op.drop_constraint, 'pk_cobject', 'cobject')
        self.schedule('alter', op.alter_column, 'cobject', 'keyc1', new_column_name='keyc2')
        self.schedule('create_pk', op.create_primary_key, 'pk_cobject', 'cobject', ['keyc2'])

        
class Migration40(Migration):
    def schedule_upgrades(self):
        self.schedule('drop_fk', op.drop_constraint, 'fk_cobject_another_c_cobject', 'cobject')
        self.schedule('create_fk', op.create_foreign_key, 'fk_cobject_another_c_cobject',
                      'cobject', 'cobject', ['another_c'], ['keyc3'])

        self.schedule('drop_pk', op.drop_constraint, 'pk_cobject', 'cobject')
        self.schedule('alter', op.alter_column, 'cobject', 'keyc2', new_column_name='keyc3')
        self.schedule('create_pk', op.create_primary_key, 'pk_cobject', 'cobject', ['keyc3'])
