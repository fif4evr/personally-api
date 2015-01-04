from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Date
class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    bio = Column(String)
    ie_score = Column(Integer)
    sn_score = Column(Integer)
    tf_score = Column(Integer)
    jp_score = Column(Integer)
    personality_type = Column(String)
    hire_date = Column(Date)
    gender = Column(String)
    company = Column(Integer)
    department = Column(Integer)

    def __repr__(self):
        return "<Employee(name='%s', bio='%s', personality_type='%s')>" % (self.name, self.bio, self.personality_type)