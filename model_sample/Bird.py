# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:54:37 2015

@author: frosch
"""

# Definiere eine neue Klasse "Bird"
class Bird:
    "Abstrakte Bird-Klasse"
    
    # initialisierungs-methode
    def __init__(self, kind, food, home):
        self.kind = kind
        self.food = food
        self.home = home
        
    # irgendeine andere Methode/Funktion
    def tell_info(self):
        print "I am %s, I eat %s, and I come from the %s." % (self.kind, self.food, self.home)
        