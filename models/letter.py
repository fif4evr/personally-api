from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Letter(Base):
    __tablename__ = 'letter'

    letter = Column(String)
    description = Column(String)
    full_name = Column(String)

    def __repr__(self):
        return "<Letter(letter='%s', description='%s', full_name='%s')>" % (self.letter, self.description, self.full_name)