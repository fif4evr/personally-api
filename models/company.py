from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    departments = relationship("Department", backref="company_reference")



    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'departments': map(lambda y:y.to_dict(), self.departments)
        }

    def __repr__(self):
        return "<Company(id='%d', name='%s', departments='%s')>" % (self.id, self.name, self.departments)