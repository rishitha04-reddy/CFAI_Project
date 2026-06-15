import random

class Agent:

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.score = 0

    def choose_resources(self, available):

        if self.strategy == "Aggressive":
            return min(random.randint(4, 7), available)

        elif self.strategy == "Balanced":
            return min(random.randint(2, 5), available)

        elif self.strategy == "Conservative":
            return min(random.randint(1, 3), available)

        return 1