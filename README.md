# SQLALCHEMY

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper(ORM) that gives application developers the full power and flexibility of SQL.

## Getting Started

Here I'm using the MYSQL as my database services. Providing a very simple application that showing how to use the sqlalchemy (a powerful sql tools) do the transaction with database. Without writing any sql statement.

## Installation

Before using the sqlalchemy features, you need to install:
```
    1. $ sudo apt-get install python-sqlalchemy
```

## Example

First, you need to initial the database connection

```
    # Initial the connection
    server = "<ip_address>" # localhost/ 127.0.0.1 (loopback)
    username = "<username>" # db root user
    password = "<password>" # db root password
    database = "<database_name>"
```

Second, initial the connection to database by using sqlalchemy

```
    Base = automap_base()

    # Create an engine that define some configuration with sqlalchemy
    engine = create_engine(db_connection, pool_size=8, max_overflow=0,
                           poolclass=QueuePool, echo_pool=False, pool_recycle=60)
    Base.prepare(engine, reflect=True)
    engine.dispose()

    # Assign the root classes to schema
    # More convinient when doing sql transaction
    schema = Base.classes

```

Third, use the very simple syntax to replace sql statement(CRUD).

```
    # Create
    session.execute(insert(schema.student, values=values))
    
    # Read
    session.query(schema.student).all()
    
    # Update
    session.execute(update(schema.student, values=values).where(schema.student.student_id == studentObj.student_id))

    # Delete
    session.query(schema.student).filter_by(schema.student.student_id == student_id).delete()
```

## Version

Please take note that might minor changes of syntax on different version

```
    python            == 2.7.12
    mysql             == 5.7
    python-sqlalchemy == 1.0.11
```