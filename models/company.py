from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    departments = relationship("Department", backref="department")


    def to_dict(self):
        # import pdb; pdb.set_trace()
        return {
            'id': self.id,
            'name': self.name,
            'departments': map(lambda y:y.to_dict(), self.departments),
            'employees': map(lambda y:y.to_dict(), self.employee)
        }

    def __repr__(self):
        return "<Company(id='%d', name='%s')>" % (self.id, self.name)