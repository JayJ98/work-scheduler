import os
from sqlalchemy import create_engine, text

secret_db_connection_string = os.environ['DB_CONNECTION_STRING']


def row_to_dict(row):
    return dict(zip([t[0] for t in row.cursor_description], row))


engine = create_engine(secret_db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_employees():
    EMPLOYEES = []
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM employee"))
        for row in result:
            EMPLOYEES.append(row._asdict())
        return EMPLOYEES


def load_employee(id):
    EMPLOYEE = []
    with engine.connect() as conn:
        query_string = text('SELECT * FROM employee WHERE id = :id')
        result = conn.execute(query_string, [{'id': id}])
        for row in result:
            EMPLOYEE.append(row._asdict())
        return EMPLOYEE
