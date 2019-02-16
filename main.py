from Instance import Instance
from Population import Population
from Solution import Solution

if __name__ == '__main__':
    i = Instance()
    p = Population(i, 20, 25)
    p.calculate()
    p.ranking()
    print(p[0].score)
    for i in range(1000):
        p.crossover()
        p.calculate()
        p.mutate(Solution.mutate4)
        p.dedup()
        p.ranking()
        p.cutoff()
    print(p[0].score)

