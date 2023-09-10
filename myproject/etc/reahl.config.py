import os
from reahl.sqlalchemysupport import SqlAlchemyControl

reahlsystem.root_egg = 'myproject'
#reahlsystem.connection_uri = 'postgresql:///reahl'
reahlsystem.connection_uri = 'sqlite:////tmp/test.db'
#reahlsystem.connection_uri = 'sqlite:///:memory:'
#reahlsystem.connection_uri = os.environ.get('REAHL_TEST_CONNECTION_URI', 'postgresql:///reahl')

reahlsystem.orm_control = SqlAlchemyControl(echo=False)




