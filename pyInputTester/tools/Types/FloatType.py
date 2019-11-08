import random

class FloatType:

    def __init__(self):
        pass
    def get_float(self, minimum, maximum, decimal):
        minimum, maximum, decimal = float(minimum), float(maximum), int(decimal)
        while True:
            float_ = (random.random()) * maximum
            if float_ >= minimum: break
    
        return round(float_, decimal)
