from Instance import Instance
from Population import Population
from Solution import Solution
import csv


class Tests:
    def __init__(self, instances_n):
        instances = tuple(Instance() for _ in range(instances_n))
        for i in instances: i.tofile()
        self.populations = tuple(Population(i, 20, 25) for i in instances)

    def test1(self):
        print("test1")
        with open('test1mut.csv', 'w') as f:
            writer = csv.writer(f)
            for population in self.populations:
                p = population.copy()
                p.calculate()
                startscore = p[0].score
                for i in range(10000):
                    p.mutate(Solution.mutate1)
                    p.ranking()
                    #p.crossover()
                    #p.calculate()
                    #p.dedup()
                    #p.ranking()
                    #p.cutoff()
                writer.writerow((startscore, p[0].score))

    def test2(self):
        print("test2")
        with open('test2mut.csv', 'w') as f:
            writer = csv.writer(f)
            for population in self.populations:
                p = population.copy()
                p.calculate()
                startscore = p[0].score
                for i in range(1000):
                    p.mutate(Solution.mutate2)
                    p.ranking()
                    #p.crossover()
                    #p.calculate()
                    #p.dedup()
                    #p.ranking()
                    #p.cutoff()
                writer.writerow((startscore, p[0].score))

    def test3(self):
        print("test3")
        with open('test3mut.csv', 'w') as f:
            writer = csv.writer(f)
            for population in self.populations:
                p = population.copy()
                p.calculate()
                startscore = p[0].score
                for i in range(1000):
                    p.mutate(Solution.mutate3)
                    p.ranking()
                    #p.crossover()
                    #p.calculate()
                    #p.dedup()
                    #p.ranking()
                    #p.cutoff()
                writer.writerow((startscore, p[0].score))

    def test4(self):
        print("test4")
        with open('test4mut.csv', 'w') as f:
            writer = csv.writer(f)
            for population in self.populations:
                p = population.copy()
                p.calculate()
                startscore = p[0].score
                for i in range(1000):
                    p.mutate(Solution.mutate4)
                    p.ranking()
                    #p.crossover()
                    #p.calculate()
                    #p.dedup()
                    #p.ranking()
                    #p.cutoff()
                writer.writerow((startscore, p[0].score))

    def test5(self):
        print("po strojeniu")
        with open('po strojeniu.csv', 'w') as f:
            writer = csv.writer(f)
            for population in self.populations:
                p = population.copy()
                p.calculate()
                startscore = p[0].score
                for i in range(1000):
                    p.mutate(Solution.mutate5)
                    p.ranking
                    p.crossover()
                    p.calculate()
                    p.dedup()
                    p.ranking()
                    p.cutoff()
                writer.writerow((startscore, p[0].score))
                p[0].tofile(startscore)

    def test(self):
        print("test5")
        with open('test5mut.csv', 'w') as f:
            writer = csv.writer(f)
            for population in self.populations:
                p = population.copy()
                p.calculate()
                startscore = p[0].score
                for i in range(1000):
                    p.mutate(Solution.mutate5)
                    p.ranking()
                    #p.crossover()
                    #p.calculate()
                    #p.dedup()
                    #p.ranking()
                    #p.cutoff()
                writer.writerow((startscore, p[0].score))

    def test_crossover(self):
        print("test crossover")
        with open('test_cross.csv', 'w') as f:
            writer = csv.writer(f)
            for population in self.populations:
                p = population.copy()
                p.calculate()
                startscore = p[0].score
                for i in range(1000):
                    p.ranking()
                    p.crossover()
                    p.calculate()
                    p.dedup()
                    p.ranking()
                    p.cutoff()
                writer.writerow((startscore, p[0].score))
