from Instance import Instance
from Machine import Machine
from random import shuffle, randint
from Constants import JOBS_NUMBER
from math import ceil
from Maintenance import Maintenance


class Solution:
    def __init__(self, *argv):
        if not argv:
            self.M1 = Machine(1, self)
            self.M2 = Machine(2, self)
            return
        if len(argv) not in (0, 2): raise TypeError("Too many arguments to Solution constructor.")
        if type(argv[0]) is Instance and type(argv[1]) is int:  # instance nad maintenance generation probability
            self.instance = argv[0]
            self.M1 = Machine(1, self)
            self.M2 = Machine(2, self)
            self.score = 0

            mait_min = int(ceil(sum((j.task2.length for j in self.instance.jobs)) / JOBS_NUMBER))
            mno = 0
            for j in self.instance.jobs:
                self.M1.append(j.task1)
                self.M2.append(j.task2)
                if randint(0, 100) < argv[1]:
                    self.M2.append(Maintenance(mait_min, mno))
                    mno += 1

            shuffle(self.M1)
            shuffle(self.M2)
        elif all(type(i) is Solution for i in argv):  # crossover
            self.instance = argv[0].instance
            self.score = 0
            self.M1 = Machine(1, self)
            self.M2 = Machine(2, self)
            m1h = argv[0].M1[:int(JOBS_NUMBER / 2)]
            self.M1.extend(m1h + [task for task in argv[1].M1 if task not in m1h])
            m2h = argv[0].M2[:int(len(argv[0].M2) / 2)]
            self.M2.extend(m2h + [task for task in argv[1].M2 if task not in m2h])

    def calculate(self):
        self.score = self.score or self.M1.calculate() + self.M2.calculate()
        return self.score

    def mutate1(self):  # get two random ints and swap tasks with these numbers on M1 and M2
        x, y = randint(0, JOBS_NUMBER - 1), randint(0, JOBS_NUMBER - 1)
        self.M1[x], self.M1[y] = self.M1[y], self.M1[x]
        self.M2[x], self.M2[y] = self.M2[y], self.M2[x]
        self.score = 0

    def mutate2(self):  # swap random tasks on M1 and other randoms tasks on M2
        r = tuple(randint(0, JOBS_NUMBER - 1) for _ in range(4))
        self.M1[r[0]], self.M1[r[1]] = self.M1[r[1]], self.M1[r[0]]
        self.M1[r[2]], self.M1[r[3]] = self.M1[r[3]], self.M1[r[2]]
        self.score = 0

    def mutate3(self):  # swap two consecutive tasks on M1 and M2
        x, y = randint(0, JOBS_NUMBER - 2), randint(0, JOBS_NUMBER - 2)
        self.M1[x], self.M1[x + 1] = self.M1[x + 1], self.M1[x]
        self.M1[y], self.M1[y + 1] = self.M1[y + 1], self.M1[y]
        self.score = 0

    def mutate4(self):  # swap two consecutive tasks on M1 OR M2
        m = (self.M1, self.M2)[randint(0, 1)]
        x = randint(0, JOBS_NUMBER - 2)
        m[x], m[x + 1] = m[x + 1], m[x]
        self.score = 0

    def mutate5(self): # swap random tasks on M1 or M2
        m = (self.M1, self.M2)[randint(0, 1)]
        x, y = randint(0, JOBS_NUMBER - 2), randint(0, JOBS_NUMBER - 2)
        m[x], m[y] = m[y], m[x]
        self.score = 0

    def copy(self):
        s = Solution()
        s.instance = self.instance
        s.M1 = self.M1.copy()
        s.M2 = self.M2.copy()
        s.score = self.score
        return s

    def tofile(self, random_solution_time):
        F = open("solutions/I{}.txt".format(self.instance.number), "w")
        F.writelines((str(self.instance.number), "{};{}".format(self.score, random_solution_time)))
        F.write("M1: ")
        F.write(' '.join("op1_{},{},{},{};".format(k, *v) for k, v in self.M1.params.items()))
        F.write("M@: ")
        t, idles, idlestime, maints, maintstime = 0, 0, 0, 0, 0
        for key, val in self.M2.params.items():
            if t < val[0]:
                idles += 1
                F.write("idle{}_M2,{},{}".format(idles, t, val[0]-t))
                idlestime += val[0]-t
            if type(key) is str and key.startswith("m"):
                maints += 1
                F.write("{}_M2,{},{};".format(key, *val))
                maintstime += val[1]
            else:
                F.write("op2_{},{},{},{}".format(key, *val))
        F.write("\n0,0;\n{},{};\n0,0;\n{},{};\n".format(maints, maintstime, idles, idlestime))

        F.close()

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score and all(
            self.M1[i] == other.M1[i] and self.M2[i] == other.M2[i] for i in range(JOBS_NUMBER))

    def __hash__(self):
        return self.score + int(''.join(map(str, self.M1.params.keys()))) + int(''.join(map(str, self.M2.params.keys())).replace("m", "0"))
