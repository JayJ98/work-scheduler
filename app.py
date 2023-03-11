from flask import Flask, render_template, url_for, jsonify
import datetime
from database import load_employees

app = Flask(__name__)


@app.route("/")
def index():
    _employees = load_employees()
    return render_template('base.html',
                           datetime=datetime,
                           employees=_employees)


@app.route('/api/employees')
def list_employees():
    _employees = load_employees()
    return jsonify(_employees)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
