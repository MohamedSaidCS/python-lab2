class Person(object):
    def __init__(self, full_name, money):
        self._full_name = full_name
        self._money = money
        self._sleep_mood = ''
        self._health_rate = 0

    def sleep(self, hours):
        if hours < 7:
            self._sleep_mood = 'tired'
        elif hours > 7:
            self._sleep_mood = 'lazy'
        else:
            self._sleep_mood = 'happy'

    def eat(self, meals):
        if meals == 3:
            self._health_rate = 100
        elif meals == 2:
            self._health_rate = 75
        elif meals == 1:
            self._health_rate = 50
        else:
            pass

    def buy(self, items):
        self._money -= items * 10

    @property
    def health_rate(self):
        return self._health_rate

    @health_rate.setter
    def health_rate(self, value):
        if value > 100:
            self._health_rate = 100
        elif value < 0:
            self._health_rate = 0
        else:
            self._health_rate = value
