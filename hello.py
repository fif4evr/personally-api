from flask import Flask, jsonify, request
from models.employee import Employee
from database import db_session, init_db
import json
init_db()
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/employees', methods=['GET'])
def employees():
    employee_list = db_session.query(Employee).all()
    employee_dict = map(lambda y:y.to_dict(), employee_list)

    return jsonify(employees=employee_dict)

@app.route('/employees/<id>', methods=['GET'])
def employees_by_id(id):
    x = db_session.query(Employee).filter(Employee.id==id).first()
    return jsonify(x.to_dict())    

@app.route('/employees', methods=['POST'])
def create_employee():
    employee = Employee()
    data = json.loads(request.data)
    employee.name = data['name']
    db_session.add(employee)
    db_session.commit()
    return jsonify(employee.to_dict())

if __name__ == "__main__":
    app.run()