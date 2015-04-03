from flask import Flask, jsonify, request, Blueprint
from models.employee import Employee
from models.company import Company
from models.department import Department
from models.personality_type import Personality_Type
from models.letter import Letter
from database import db_session, init_db
import json
from decorator import crossdomain

department_routes = Blueprint('department_routes', __name__ )

@department_routes.route('/departments', methods=['GET'])
@crossdomain(origin='*')
def departments():
    department_list = db_session.query(Department).all()
    department_dict = map(lambda y:y.to_dict(), department_list)
    return jsonify(departments=department_dict)

@department_routes.route('/departments/<id>', methods=['GET'])
@crossdomain(origin='*')
def departments_by_id(id):
    retrieved_department = db_session.query(Department).filter(Department.id==id).first()
    return jsonify(retrieved_department.to_dict())

@department_routes.route('/departments/<id>/employees', methods = ['GET'])
@crossdomain(origin='*')
def department_employees_by_id(id):
    department_by_id_dict = db_session.query(Department).filter(Department.id==id).first().to_dict()
    department_employees_dict = {'employees': department_by_id_dict['employees']}
    return jsonify(department_employees_dict)

@department_routes.route('/departments', methods=['POST'])
@crossdomain(origin='*')
def create_department():
    department = Department()
    department_data = json.loads(request.data)
    update_department_data(department, department_data)
    db_session.add(department)
    db_session.commit()
    return jsonify(department.to_dict())

@department_routes.route('/departments/<id>', methods=['PUT'])
@crossdomain(origin='*')
def update_department(id):
    department = db_session.query(Department).filter(Department.id==id).first()
    department_data = json.loads(request.data)
    update_department_data(department, department_data)
    db_session.commit()
    return jsonify(department.to_dict())

@department_routes.route('/departments/<id>', methods=['DELETE'])
@crossdomain(origin='*')
def delete_department(id):
    department = db_session.query(Department).filter(Department.id==id).first()
    db_session.delete(department)
    db_session.commit()
    return True