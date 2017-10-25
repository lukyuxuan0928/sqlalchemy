from model import *
import db

if __name__ == "__main__":
    # Initial a student
    student_1 = Student("Luke", 24)

    # Create
    db.create_student(student_1)

    # Read
    for student in db.get_students():
        print student

    # Update
    student_1.name = "Richard"
    db.update_student(student_1)

    # Delete
    db.delete_student(student_1.id)

    