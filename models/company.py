from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key = True)
    name = Column(String)

    def __repr__(self):
        return "<Company(id='%d', name='%s')>" % (self.id, self.name)