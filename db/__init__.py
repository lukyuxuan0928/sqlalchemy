from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.pool import QueuePool
from sqlalchemy import update, insert, delete


try:
    # Initial the connection
    server = "localhost" # 127.0.0.1 (loopback)
    username = "luke" # db root user
    password = "luke" # db root password
    database = "student"

    db_connection = 'mysql+mysqlconnector://' + username + ':' + password + '@' + server + '/' + database
    
    # Here we are using the automap_base as our Base
    # It will auto mapping our all tables structure
    Base = automap_base()

    # Create an engine that define some configuration with sqlalchemy
    engine = create_engine(db_connection, pool_size=8, max_overflow=0,
                           poolclass=QueuePool, echo_pool=False, pool_recycle=60)
    Base.prepare(engine, reflect=True)
    engine.dispose()

    # Assign the root classes to schema
    # More convinient when doing sql transaction
    schema = Base.classes

except Exception as ex:
    raise ex


def create_session():
    # Used to connect the db with specified engine
    session = Session(engine)
    return session

'''
Create Method
'''
def create_student(studentObj):
    try:
        # Get the session 1st
        session = create_session()

        # Fit in the value to column from studentObj
        # schema.<table_name>.<column_name>
        values = {
            schema.student.name: studentObj.name,
            schema.student.age: studentObj.age
        }

        # Execute the insert query
        result = session.execute(insert(schema.student, values=values))

        # Commit the session
        session.commit()
        # Close the session
        session.close()

        # Getting the primary key on last inserted
        if len(result.inserted_primary_key) > 0:
            return result.inserted_primary_key[0]
        else:
            return -1

    except Exception as ex:
        # Rollback the query
        session.rollback()
        session.close()
        raise ex

'''
Read
'''
def get_students():
    try:
        # Get the session 1st
        session = create_session()

        # Query all the student data
        # first() 
        # scalar() 
        # one()
        # all()
        students = session.query(schema.student).all()
        session.close()

        return students

    except Exception as ex:
        # Rollback the query
        session.rollback()
        session.close()
        raise ex


'''
Update
'''
def update_student(studentObj):
    try:
        session = create_session()

        values = {
            schema.student.name: studentObj.name,
            schema.student.age: studentObj.age
        }

        # Execute the update query
        session.execute(
            update(schema.student, values=values).where(schema.student.student_id == studentObj.student_id))

        # Commit the session
        session.commit()
        # Close the session
        session.close()

        return True

    except Exception as ex:
        # Rollback the query
        session.rollback()
        session.close()
        raise ex

'''
Delete
'''
def delete_student(student_id):
    try:
        session = create_session()

        # Delete
        session.query(schema.student).filter_by(schema.student.student_id == student_id).delete()
        # Commit the session
        session.commit()
        # Close the session
        session.close()

        return True

    except Exception as ex:
        # Rollback the query
        session.rollback()
        session.close()
        raise ex





