from models.employee import Employee
from models.office import Office

office = Office('office 1')

emp1 = Employee('mohamed', 100, 1, 'email@mail.com', 2000, False)
emp2 = Employee('ahmed', 500, 2, 'ahmed@mail.com', 3000, False)


office.hire_employee(emp1)
office.hire_employee(emp2)

office.fire_employee(2)
