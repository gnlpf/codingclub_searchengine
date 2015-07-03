# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 06:43:26 2015

@author: frosch
"""

class Car:

    # Eigenschaften (Variablen)    
    carType = ""
    color = ""
    length = None
    width = None
    
    # Funktionen (Methods)
    def printInfo(self):
        print "Die ist ein %s-er %s mit den Maßen %.2f x %.2f" % (self.color, self.carType, self.length, self.width)
        pass
    
    def accellerate(self):
        # dein Code
        pass
    
    def decellerate(self):
        # dein Code
        pass
    
    def breaking(self):
        # dein Code
        pass
    
    
class Jeep(Car):
    
    def pull(self):
        # dein Code um das Seil einzuziehen
        pass
    
    def printInfo(self):
        Car.printInfo(self)
        print "Ich bin der Größte!"