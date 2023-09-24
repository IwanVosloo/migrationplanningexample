from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from reahl.sqlalchemysupport import Base

from projectc.code import CObject

class BObject(Base):
    __tablename__ = 'bobject'

    key = Column(Integer, primary_key=True)
    to_c_key = Column(Integer, ForeignKey('cobject.keyc3'))
    to_c = relationship(CObject)
