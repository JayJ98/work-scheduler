from flask import Flask, render_template, url_for, jsonify, redirect, request
import datetime
from database import session, load_employees, load_employee, add_employee, Employee

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('/layout/base.html', datetime=datetime)


@app.route('/employees')
def show_an_employee():
    _employee = load_employees()
    return render_template('/employee/employees.html',
                           datetime=datetime,
                           employees=_employee,
                           form_action='/employee/add',
                           bttn_value='Add')


@app.route('/employee/add', methods=['POST'])
def add_new_employee():
    _employee = Employee(first_name=request.form['first_name'],
                         last_name=request.form['last_name'],
                         phone=request.form['phone'],
                         email=request.form['email'],
                         hours_requirement=request.form['hours_requirement'])

    add_employee(_employee)
    return redirect('/employees')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
