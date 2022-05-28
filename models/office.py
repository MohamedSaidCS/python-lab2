from services.db_service import DBService


class Office:
    def __init__(self, name):
        self.name = name
        self.db = DBService('localhost', 'root', '', 'lab2')

    def get_employees(self):
        return self.db.get_employees()

    def get_employee(self, id):
        return self.db.get_employee(id)

    def hire_employee(self, employee):
        self.db.add_employee(employee)

    def fire_employee(self, id):
        self.db.delete_employee(id)
