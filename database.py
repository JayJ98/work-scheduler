import os
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

# connection to https://planetscale.com/ database
secret_db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(secret_db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

session_obj = sessionmaker(bind=engine)
session = scoped_session(session_obj)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine


class Employee(Base):
    __tablename__ = 'employee'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    hours_requirement = Column(Integer, nullable=True)


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


def add_employee(employee):
    try:
        session.add(employee)
        session.flush()
        session.commit()
    except:
        return 'There was a database error'
