from random import shuffle

from Solution import Solution


class Population(list):
    def __init__(self, instance, size, maint_prob):
        super().__init__()
        self.size = size
        self.extend(Solution(instance, maint_prob) for _ in range(size))

    def mutate(self, mutation):
        for i in range(len(self)):
            cp = self[i].copy()
            mutation(cp)
            if cp.calculate() < self[i].score:
                self[i] = cp

    def crossover(self):
        for i in range(len(self) - 1):
            self.append(Solution(self[i], self[i + 1]))
            self.append(Solution(self[i + 1], self[i]))

    def calculate(self):
        for sol in self:
            sol.calculate()

    def ranking(self):
        self.sort()

    def random(self):
        shuffle(self)

    def every_other(self):
        self.ranking()
        for i in range(1, len(self) - 1, 4):
            self[i], self[i + 1] = self[i + 1], self[i]

    def first_to_half(self):
        self.ranking()
        half_len = int(len(self) / 2)
        for i in range(0, half_len, 2):
            self[i], self[i + half_len] = self[i + half_len], self[i]

    def cutoff(self):
        self.ranking()
        del self[self.size:]

    def dedup(self):
        s = set(self)
        self.clear()
        self.extend(s)
