from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    company = Column(Integer, ForeignKey('company.id'))
    
    def to_dict(self):
        # import pdb; pdb.set_trace()
        return {
        'id': self.id,
        'name': self.name,
        'company': self.company,
        'employees': map(lambda y:y.to_dict(), self.employee)
        }

    def __repr__(self):
        return "<Department(id='%d', name='%s')>" % (self.id, self.name)