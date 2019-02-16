from random import randint
from Constants import MAX_MAINTENENANCE_TIME


class Maintenance:
    def __init__(self, min, no):
        self.no = no
        self.length = randint(min, MAX_MAINTENENANCE_TIME)

    def __eq__(self, other):
        return type(other) is Maintenance and self.no == other.no
