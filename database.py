import os
from sqlalchemy import create_engine, text
import pymysql

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
            print(type(row._asdict()))
            EMPLOYEES.append(row._asdict())
        return EMPLOYEES
