from random import randint
from Constants import *
from math import ceil


class Task:
    def __init__(self, job):
        self.length = randint(MIN_TASK_TIME, MAX_TASK_TIME)
        self.job = job

    def len(self, punishment):
        return ceil(self.length * (1 + punishment * 0.01))

    def other(self):
        return self.job.other(self)

    def __eq__(self, other):
        return type(other) is Task and self.job.number == other.job.number and self.length == other.length
