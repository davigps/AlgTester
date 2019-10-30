import random
import string

class StringType:
    
    alphabet = string.ascii_letters

    def __init__(self):
        pass

    def get_string(self, length, init, final):
        string = ''
        init = self.alphabet.index(init)
        final = self.alphabet.index(final)
        for letter in range(length):
            string += self.alphabet[random.randint(init, final)]

        return string
