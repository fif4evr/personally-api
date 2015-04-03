from flask import Flask, jsonify, request, Blueprint
from models.employee import Employee
from models.company import Company
from models.department import Department
from models.personality_type import Personality_Type
from models.letter import Letter
from database import db_session, init_db
import json
from decorator import crossdomain

company_routes = Blueprint('company_routes', __name__ )

@company_routes.route('/companies', methods=['GET'])
@crossdomain(origin='*')
def companies():
    company_list = db_session.query(Company).all()
    company_dict = map(lambda y:y.to_dict(), company_list)

    return jsonify(companies=company_dict)

@company_routes.route('/companies/<id>', methods=['GET'])
@crossdomain(origin='*')
def companies_by_id(id):
    company_by_id = db_session.query(Company).filter(Company.id==id).first()
    return jsonify(company_by_id.to_dict()) 

@company_routes.route('/companies/<id>/departments', methods=['GET'])
@crossdomain(origin='*')
def company_department_by_id(id):
    company_by_id_dict = db_session.query(Company).filter(Company.id==id).first().to_dict()
    company_departments = company_by_id_dict['departments']
    company_departments_dict = {'departments': company_departments}
    return jsonify(company_departments_dict)

@company_routes.route('/companies/<id>/employees', methods=['GET'])
@crossdomain(origin='*')
def company_employees_by_id(id):
    company_by_id_dict = db_session.query(Company).filter(Company.id==id).first().to_dict()
    company_employees = company_by_id_dict['employees']
    company_employees_dict = {'employees': company_employees} 
    return jsonify(company_employees_dict)
    
@company_routes.route('/companies', methods=['POST'])
@crossdomain(origin='*')
def create_company():
    company = Company()
    company_data = json.loads(request.data)
    update_company_data(company, company_data)
    db_session.add(company)
    db_session.commit()
    return jsonify(company.to_dict())

@company_routes.route('/companies/<id>', methods=['PUT'])
@crossdomain(origin='*')
def update_company(id):
    company = db_session.query(Company).filter(Company.id==id).first()
    company_data = json.loads(request.data)
    update_company_data(company, company_data)
    db_session.commit()
    return jsonify(company.to_dict())

@company_routes.route('/companies/<id>', methods=['DELETE'])
@crossdomain(origin='*')
def delete_company(id):
    company = db_session.query(Company).filter(Company.id==id).first()
    db_session.delete(company)
    db_session.commit()
    return True