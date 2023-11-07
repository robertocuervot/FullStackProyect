from employee import Employee
from declarative_base import Session, engine, Base


def add(name, position, skills):
    db = Session() # Create a new database session
    new_employee = Employee(name=name, position=position, skills=skills) # Create an EmployeeDB instance and set its attributes
    db.add(new_employee) # Add the employee to the database session
    db.commit() # Commit the changes to the databas
    db.close() # Close the database session




if __name__ == '__main__':
    #Creates the database
    Base.metadata.create_all(engine)

    name = "Robert Joe"
    position = "Mechatronics Engineer"
    skills = "C++,C,Docker"
    add(name,position, skills)