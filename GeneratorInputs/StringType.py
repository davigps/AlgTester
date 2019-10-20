import random

class StringType:
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    
    def __init__(self, length, init_charecter, final_charecter):
        self.init = self.index_charecter(init_charecter)
        self.final = self.index_charecter(final_charecter)
        self.length = length

    def getString(self):
        string = ''
        for letter in range(self.length):
            string += self.alphabet[random.randint(self.init, self.final)]

        return string
        
    def index_charecter(self, charecter):
        
        for char in self.alphabet:
            if charecter.lower() == char:
                return self.alphabet.index(char)

        return 'Error'
