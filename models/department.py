from database import Base

from sqlalchemy import Column, Integer, String
class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    bio = Column(String)

    def __repr__(self):
        return "<Department(id='%d', name='%s')>" % (self.id, self.name)