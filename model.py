class Student():
    # Initial the class
    def __init__(self, name, age, id = None):
        self.name = name
        self.age = age
        self.id = id

    # Printer features
    def printer(self):
        print "Student name:", self.name
        print "Student age:", self.age