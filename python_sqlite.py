# import sqlite3
# conn = sqlite3.connect('test.db')

# c = conn.cursor()
# # c.execute("INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score) VALUES ('Pilot','Pilot is another dog',1,2,'2014-12-31','M','ESTJ','80','13','11','45')")
# for row in c.execute("SELECT * FROM employee"):
# 	print row

# # print c.execute("SELECT * FROM employee").fetchall()

# conn.commit()


# conn.close()
from models.personality_type import Personality_Type
from models.employee import Employee
from models.company import Company
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sql_experiments/test.db',echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()
x = session.query(Employee).filter(Employee.personality_type=='ESTJ').all()

print x

print map(lambda y:y.personality, x)