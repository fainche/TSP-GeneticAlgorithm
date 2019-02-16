from Maintenance import Maintenance
from Task import Task


class Machine(list):
    def __init__(self, number, solution):
        super().__init__()
        self.number = number
        self.solution = solution
        self.params = dict()
        self.score = 0

    def calculate(self):
        self.params = dict()
        self.score = 0
        if self.number == 1:
            start_time = 0
            self.score = 0
            for task in self:
                self.params[task.job.number] = (start_time, task.length, task.length)
                start_time += task.length
                self.score += start_time

        elif self.number == 2:
            start_time = 0
            punishment = 0
            m = 0
            for task in self:
                if type(task) is Task:
                    start_time = max(start_time,
                                     self.solution.M1.params[task.job.number][0] +
                                     self.solution.M1.params[task.job.number][2])
                    real_len = task.len(punishment)
                    self.params[task.job.number] = (start_time, task.length, real_len)
                    start_time += real_len
                    self.score += start_time
                    punishment += 10
                elif type(task) is Maintenance:
                    punishment = 0
                    self.params["m"+str(m)] = (start_time, task.length, task.length)
                    start_time += task.length
                    m += 1
                else:
                    raise TypeError("The object in Machine ordering list is not Task nor Maintenance.")
        return self.score

    def copy(self):
        m = Machine(self.number, self.solution)
        m.extend(self)
        return m
