from base import Base
from sqlalchemy import Column, String
class Personality_Type(Base):
    __tablename__ = 'personality_type'

    signature = Column(String, primary_key = True)
    # TODO: create relationships for each of these
    ie = Column(String)
    sn = Column(String)
    tf = Column(String)
    jp = Column(String)
    description = Column(String)

    def __repr__(self):
        return "<Personality_Type(signature='%s', description='%s')>" % (self.signature, self.description)