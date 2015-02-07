from flask import Flask, jsonify, request
from models.employee import Employee
from models.company import Company
from models.department import Department
from models.personality_type import Personality_Type
from models.letter import Letter
from database import db_session, init_db
import json
from decorator import crossdomain
init_db()
app = Flask(__name__)

@app.route('/')
@crossdomain(origin='*')
def hello():
    return 'Hello, World!'

@app.route('/employees', methods=['GET'])
@crossdomain(origin='*')
def employees():
    employee_list = db_session.query(Employee).all()
    employee_dict = map(lambda y:y.to_dict(), employee_list)

    return jsonify(employees=employee_dict)

@app.route('/employees/<id>', methods=['GET'])
@crossdomain(origin='*')
def employees_by_id(id):
    x = db_session.query(Employee).filter(Employee.id==id).first()
    return jsonify(x.to_dict())    

@app.route('/employees', methods=['POST'])
@crossdomain(origin='*')
def create_employee():
    employee = Employee()
    data = json.loads(request.data)
    update_employee_info(employee, data)
    db_session.add(employee)
    db_session.commit()
    return jsonify(employee.to_dict())

@app.route('/employees/<id>', methods=['PUT'])
@crossdomain(origin='*')
def update_employee(id):
    employee = db_session.query(Employee).filter(Employee.id==id).first()
    data = json.loads(request.data)
    update_employee_info(employee, data)
    db_session.commit()
    return jsonify(employee.to_dict()) 

@app.route('/employees/<id>', methods=['DELETE'])
@crossdomain(origin='*')
def delete_employee(id):
    employee = db_session.query(Employee).filter(Employee.id==id).first()
    db_session.delete(employee)
    db_session.commit()
    return True

@app.route('/companies', methods=['GET'])
@crossdomain(origin='*')
def companies():
    company_list = db_session.query(Company).all()
    company_dict = map(lambda y:y.to_dict(), company_list)

    return jsonify(companies=company_dict)

@app.route('/companies/<id>', methods=['GET'])
@crossdomain(origin='*')
def companies_by_id(id):
    x = db_session.query(Company).filter(Company.id==id).first()
    return jsonify(x.to_dict()) 

@app.route('/companies', methods=['POST'])
@crossdomain(origin='*')
def create_company():
    company = Company()
    company_data = json.loads(request.data)
    update_company_data(company, company_data)
    db_session.add(company)
    db_session.commit()
    return jsonify(company.to_dict())

@app.route('/companies/<id>', methods=['PUT'])
@crossdomain(origin='*')
def update_company(id):
    company = db_session.query(Company).filter(Company.id==id).first()
    company_data = json.loads(request.data)
    update_company_data(company, company_data)
    db_session.commit()
    return jsonify(company.to_dict())

@app.route('/companies/<id>', methods=['DELETE'])
@crossdomain(origin='*')
def delete_company(id):
    company = db_session.query(Company).filter(Company.id==id).first()
    db_session.delete(company)
    db_session.commit()
    return True

@app.route('/departments', methods=['GET'])
@crossdomain(origin='*')
def departments():
    department_list = db_session.query(Department).all()
    department_dict = map(lambda y:y.to_dict(), department_list)

    return jsonify(departments=department_dict)

@app.route('/departments/<id>', methods=['GET'])
@crossdomain(origin='*')
def departments_by_id(id):
    retrieved_department = db_session.query(Department).filter(Department.id==id).first()
    return jsonify(retrieved_department.to_dict())

@app.route('/departments', methods=['POST'])
@crossdomain(origin='*')
def create_department():
    department = Department()
    department_data = json.loads(request.data)
    update_department_data(department, department_data)
    db_session.add(department)
    db_session.commit()
    return jsonify(department.to_dict())

@app.route('/departments/<id>', methods=['PUT'])
@crossdomain(origin='*')
def update_department(id):
    department = db_session.query(Department).filter(Department.id==id).first()
    department_data = json.loads(request.data)
    update_department_data(department, department_data)
    db_session.commit()
    return jsonify(department.to_dict())

@app.route('/departments/<id>', methods=['DELETE'])
@crossdomain(origin='*')
def delete_department(id):
    department = db_session.query(Department).filter(Department.id==id).first()
    db_session.delete(department)
    db_session.commit()
    return True

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