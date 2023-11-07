from employee import Employee
from declarative_base import Session, engine, Base


def retrieve():
    db = Session()
    employees = db.query(Employee).all()
    return employees




if __name__ == '__main__':
    employees = retrieve()
    for employee in employees:
      print("ID:" + str(employee.id) + 
            " Name:" + employee.name +
            " Position:" + employee.position + 
            " Skills:" + employee.skills)