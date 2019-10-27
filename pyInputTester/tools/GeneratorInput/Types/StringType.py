import random
import string

class StringType:
    
    alphabet = string.ascii_letters

    def __init__(self, length, init_charecter, final_charecter):
        self.init = self.alphabet.index(init_charecter)
        self.final = self.alphabet.index(final_charecter)
        self.length = length

    def get_string(self):
        string = ''
        for letter in range(self.length):
            string += self.alphabet[random.randint(self.init, self.final)]

        return string
