from random import randint
from Constants import MAX_MAINTENENANCE_TIME


class Maintenance:
    def __init__(self, min, no):
        self.number = no
        self.length = randint(min, MAX_MAINTENENANCE_TIME)

    def __eq__(self, other):
        return type(other) is Maintenance and self.number == other.number
