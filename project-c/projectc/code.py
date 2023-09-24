from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from reahl.sqlalchemysupport import Base

class CObject(Base):
    __tablename__ = 'cobject'

    keyc3 = Column(Integer, primary_key=True)
    another_c_key = Column(Integer, ForeignKey('cobject.keyc3'))
    another_c = relationship('CObject')

