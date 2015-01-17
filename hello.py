import os
from flask import Flask, jsonify
from models.personality_type import Personality_Type
from models.employee import Employee
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sql_experiments/test.db',echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/employees')
def employees():
    session = Session()     
    x = session.query(Employee).all()
    a = map(lambda y:y.to_dict(), x)

    return jsonify(employees=a)

if __name__ == "__main__":
    app.run()