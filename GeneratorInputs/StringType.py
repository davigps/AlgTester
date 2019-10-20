import random

class StringType:
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    
    def __init__(self, length, init_caracter, final_caracter):
        self.init = self.index_caracter(init_caracter)
        self.final = self.index_caracter(final_caracter)
        self.length = length

    def getString(self):
        string = ''
        for letter in range(self.length):
            string += self.alphabet[random.randint(self.init, self.final)]

        return string
        
    def index_caracter(self, caracter):
        
        for char in self.alphabet:
            if caracter.lower() == char:
                return self.alphabet.index(char)

        return 'Error'
