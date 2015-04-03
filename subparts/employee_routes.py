from flask import Flask, jsonify, request, Blueprint
from models.employee import Employee
from models.company import Company
from models.department import Department
from models.personality_type import Personality_Type
from models.letter import Letter
from database import db_session, init_db
import json
from decorator import crossdomain

employee_routes = Blueprint('employee_routes', __name__ )
# @simple_pemployee_routes.route('/<page>')
# def show(page):
#     # stuff


@employee_routes.route('/employees', methods=['GET'])
@crossdomain(origin='*')
def employees():
    employee_list = db_session.query(Employee).all()
    employee_dict = map(lambda y:y.to_dict(), employee_list)

    return jsonify(employees=employee_dict)

@employee_routes.route('/employees/<id>', methods=['GET'])
@crossdomain(origin='*')
def employees_by_id(id):
    employee_by_id = db_session.query(Employee).filter(Employee.id==id).first()
    return jsonify(employee_by_id.to_dict())    

@employee_routes.route('/employees', methods=['POST'])
@crossdomain(origin='*')
def create_employee():
    employee = Employee()
    data = json.loads(request.data)
    update_employee_info(employee, data)
    db_session.add(employee)
    db_session.commit()
    return jsonify(employee.to_dict())

@employee_routes.route('/employees/<id>', methods=['PUT'])
@crossdomain(origin='*')
def update_employee(id):
    employee = db_session.query(Employee).filter(Employee.id==id).first()
    data = json.loads(request.data)
    update_employee_info(employee, data)
    db_session.commit()
    return jsonify(employee.to_dict()) 

@employee_routes.route('/employees/<id>', methods=['DELETE'])
@crossdomain(origin='*')
def delete_employee(id):
    employee = db_session.query(Employee).filter(Employee.id==id).first()
    db_session.delete(employee)
    db_session.commit()
    return True
# http://localhost:5000/employees/1/similar?num_matches=1
@employee_routes.route('/employees/<id>/similar', methods=['GET'])
@crossdomain(origin='*')
def get_similar_employee(id):
    employee_by_id = db_session.query(Employee).filter(Employee.id==id).first()
    import pdb; pdb.set_trace()
    return True