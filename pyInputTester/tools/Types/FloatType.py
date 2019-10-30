import random

class FloatType:

    def __init__(self, minimum, maximum, decimal):
        self.minimum = minimum
        self.maximum = maximum
        self.decimal = decimal

    def get_float(self):
        while True:
            float_ = (random.random()) * self.maximum
            if float_ >= self.minimum: break
    
        return round(float_, self.decimal)
