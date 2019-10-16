#Campina Grande - PB
#Class BooleanType
#coding: utf-8

class BooleanType:

    def __init__(self):
        self.calls = -1

    def getBoolean(self):
        self.calls += 1
        return True if self.calls % 2 == 0 else False
