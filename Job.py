from Task import Task


class Job:
    def __init__(self, number):
        self.number = number
        self.task1 = Task(self)
        self.task2 = Task(self)

    def other(self, task):
        if task is self.task1: return self.task2
        if task is self.task2: return self.task1
        raise AttributeError("Task nie pasuje do zadania")
