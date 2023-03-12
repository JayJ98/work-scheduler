from flask import Flask, render_template, url_for, jsonify
import datetime
from database import load_employees, load_employee

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
                           form_action='/employee/add')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
