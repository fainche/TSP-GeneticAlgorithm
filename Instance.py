from Constants import JOBS_NUMBER
from Job import Job


class Instance:
    def __init__(self):
        self.jobs = [Job(i) for i in range(JOBS_NUMBER)]
