import mysql.connector


class DBService:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                full_name VARCHAR(255),
                money INTEGER,
                sleep_mood VARCHAR(255),
                health_rate INTEGER,
                email VARCHAR(255),
                work_mood VARCHAR(255),
                salary INTEGER,
                is_manager BOOLEAN
            );
        ''')
        self.connection.commit()

    def add_employee(self, employee):
        self.cursor.execute('''
            INSERT INTO employees (id, full_name, money, sleep_mood, health_rate, email, work_mood, salary, is_manager)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (employee._id, employee._full_name, employee._money, employee._sleep_mood, employee._health_rate, employee._email, employee._work_mood, employee._salary, employee._is_manager))
        self.connection.commit()

    def get_employee(self, id):
        self.cursor.execute('''
            SELECT * FROM employees WHERE id = %s
        ''', (id,))
        employee = self.cursor.fetchone()
        return employee

    def get_employees(self):
        self.cursor.execute('''
            SELECT * FROM employees
        ''')
        employees = self.cursor.fetchall()
        return employees

    def delete_employee(self, id):
        self.cursor.execute('''
            DELETE FROM employees WHERE id = %s
        ''', (id,))
        self.connection.commit()





