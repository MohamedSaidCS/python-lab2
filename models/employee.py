import re

from models.person import Person


class Employee(Person):
    def __init__(self, full_name, money, id, email, salary, is_manager):
        super().__init__(full_name, money)
        self._id = id
        self._email = email
        self._work_mood = ''
        self._salary = salary
        self._is_manager = is_manager

    def work(self, hours):
        if hours > 8:
            self._work_mood = 'tired'
        elif hours < 8:
            self._work_mood = 'lazy'
        else:
            self._work_mood = 'happy'

    def send_email(self, to, subject, message):
        file = open(f'emails/email.txt', 'w')
        file.write(f'From: {self._email}\n')
        file.write(f'To: {to}\n')
        file.write(f'Subject: {subject}\n')
        file.write(f'{message}')

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 1000:
            self._salary = 1000
        else:
            self._salary = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', value):
            self._email = value
        else:
            pass
