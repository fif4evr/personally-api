from base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.company import Company
from models.department import Department

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    bio = Column(String)
    ie_score = Column(Integer)
    sn_score = Column(Integer)
    tf_score = Column(Integer)
    jp_score = Column(Integer)
    personality_type = Column(String, ForeignKey('personality_type.signature'))
    personality = relationship('Personality_Type')
    hire_date = Column(Date)
    gender = Column(String)
    company = Column(Integer, ForeignKey('company.id'))
    company_relationship = relationship('Company')
    department = Column(Integer, ForeignKey('department.id'))
    department_relationship = relationship('Department')

    def __repr__(self):
        return "<Employee(name='%s', bio='%s', personality_type='%s')>" % (self.name, self.bio, self.personality_type)

    def to_dict(self):
       return {
           'id': self.id,
           'name': self.name,
           'bio' : self.bio
       }