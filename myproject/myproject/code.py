from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from reahl.sqlalchemysupport import Base

from projectc.code import CObject

class MyObject(Base):
    __tablename__ = 'myobject'

    key = Column(Integer, primary_key=True)
    to_c_key = Column(Integer, ForeignKey('cobject.keyc3'))
    to_c = relationship(CObject)
    
