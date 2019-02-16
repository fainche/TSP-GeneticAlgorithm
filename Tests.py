from Instance import Instance


class Tests:
    def __init__(self, instances_n):
        self.instances = (Instance() for _ in range(instances_n))

