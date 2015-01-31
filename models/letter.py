from database import Base
from sqlalchemy import Column, Integer, String
class Letter(Base):
    __tablename__ = 'letter'

    letter = Column(String, primary_key = True)
    description = Column(String)
    full_name = Column(String)

    def to_dict(self):
        return {
        'letter': self.letter,
        'description': self.description,
        'full_name': self.full_name
        }

    def __repr__(self):
        return "<Letter(letter='%s', description='%s', full_name='%s')>" % (self.letter, self.description, self.full_name)