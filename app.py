from flask import Flask, jsonify, request, Blueprint
from models.employee import Employee
from models.company import Company
from models.department import Department
from models.personality_type import Personality_Type
from models.letter import Letter
from database import db_session, init_db
import json
from decorator import crossdomain
from subparts.employee_routes import employee_routes
from subparts.company_routes import company_routes
from subparts.department_routes import department_routes
init_db()
app = Flask(__name__)
app.register_blueprint(employee_routes)
app.register_blueprint(company_routes)
app.register_blueprint(department_routes)

@app.route('/')
@crossdomain(origin='*')
def hello():
    return 'Welcome to the Personally API'

@app.route('/personality_types', methods=['GET'])
@crossdomain(origin='*')
def personality_types():
    personality_types_list = db_session.query(Personality_Type).all()
    personality_types_dict = map(lambda y:y.to_dict(), personality_types_list)
    return jsonify(personality_types=personality_types_dict)

@app.route('/personality_types/<id>', methods=['GET'])
@crossdomain(origin='*')
def personality_types_by_id(id):
    retrieved_personality_type = db_session.query(Personality_Type).filter(Personality_Type.signature==id).first()
    return jsonify(retrieved_personality_type.to_dict())

@app.route('/letters', methods=['GET'])
@crossdomain(origin='*')
def letters():
    letters_list = db_session.query(Letter).all()
    letters_dict = map(lambda y:y.to_dict(), letters_list)
    return jsonify(letters=letters_dict)

@app.route('/letters/<id>', methods=['GET'])
@crossdomain(origin='*')
def letter_by_id(id):
    retrieved_letter = db_session.query(Letter).filter(Letter.letter==id).first()
    return jsonify(retrieved_letter.to_dict())

def update_company_data(company, company_data):
    company.name = company_data['name']

def update_department_data(department, department_data):
    department.name = department_data['name']

def update_employee_info(employee, employee_data):
    employee.name = employee_data['name']
    employee.bio = employee_data['bio']
    employee.ie_score = employee_data['ie_score']
    employee.sn_score = employee_data['sn_score']
    employee.tf_score = employee_data['tf_score']
    employee.jp_score = employee_data['jp_score']
    employee.personality_type = employee_data['personality_type']
    employee.hire_date = employee_data['hire_date']
    employee.gender = employee_data['gender']
    employee.company = employee_data['company']
    employee.department = employee_data['department']

if __name__ == "__main__":
    app.run(debug=True)