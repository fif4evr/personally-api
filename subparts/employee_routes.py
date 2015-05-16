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
    num_matches = int(request.args['num_matches'])
    import pdb; pdb.set_trace()
    employee_by_id = db_session.query(Employee).filter(Employee.id==id).first()
    employee_personality_type = employee_by_id.personality_type
    employee_company_relationship = employee_by_id.company_relationship
    similar_employees = db_session.query(Employee).filter(Employee.company_relationship==employee_company_relationship).all()
    # this is only to temporarily get it to run
    # similar_employees_dict = map(lambda y:y.to_dict(), similar_employees) 
    ranked_employees = []
    for similar_employee in similar_employees:
        if similar_employee.id != employee_by_id.id:
            ranked_employees.append((similar_employee, get_similarity_score(employee_by_id, similar_employee)))
    ranked_employees = sorted(ranked_employees, key=lambda employee: employee[1])
    if len(ranked_employees) > num_matches:
        ranked_employees = ranked_employees[0:num_matches]
    # TODO find a way to return it
    return json.dumps(ranked_employees_dict)

def get_similarity_score(original_employee, compared_employee):
    similarity_score = 0
    # Get IE difference
    if original_employee.personality_type[0] != compared_employee.personality_type[0]:
        similarity_score = similarity_score + original_employee.ie_score + compared_employee.ie_score
    else:
        similarity_score = similarity_score + original_employee.ie_score - compared_employee.ie_score
    
    # Get SN difference
    if original_employee.personality_type[1] != compared_employee.personality_type[1]:
        similarity_score = similarity_score + original_employee.sn_score + compared_employee.sn_score
    else:
        similarity_score = similarity_score + original_employee.sn_score - compared_employee.sn_score

    # Get TF difference
    if original_employee.personality_type[2] != compared_employee.personality_type[2]:
        similarity_score = similarity_score + original_employee.tf_score + compared_employee.tf_score
    else:
        similarity_score = similarity_score + original_employee.tf_score - compared_employee.tf_score

    # Get JP difference
    if original_employee.personality_type[3] != compared_employee.personality_type[3]:
        similarity_score = similarity_score + original_employee.jp_score + compared_employee.jp_score
    else:
        similarity_score = similarity_score + original_employee.jp_score - compared_employee.jp_score

    return similarity_score