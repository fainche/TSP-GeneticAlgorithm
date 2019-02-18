from random import randrange

from Constants import JOBS_NUMBER
from Job import Job
from sys import maxsize


class Instance:
    def __init__(self):
        self.number = randrange(maxsize)
        self.jobs = [Job(i) for i in range(JOBS_NUMBER)]

    def tofile(self):
        lines = [str(self.number), str(JOBS_NUMBER)]
        lines += ["{},{},1,2,0".format(job.task1.length, job.task2.length) for job in self.jobs]
        with open("instances/I{}.txt".format(self.number), "w") as F:
            F.writelines(lines)
