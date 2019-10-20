import random

class IntegerType:

    def __init__(self, minimum, maximum):
        self.maximum = maximum
        self.minimum = minimum

    def getInteger(self):
        integer = random.randint(self.minimum, self.maximum)
        return integer
