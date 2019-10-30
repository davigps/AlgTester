import random

class IntegerType:

    def __init__(self):
        pass

    def get_integer(self, minimum, maximum):
        integer = random.randint(minimum, maximum)
        return integer
