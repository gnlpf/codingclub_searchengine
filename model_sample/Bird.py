# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:54:37 2015

@author: frosch
"""

class Bird:
    "Abstrakte Bird-Klasse"
    
    def __init__(self, kind, food, home):
        self.kind = kind
        self.food = food
        self.home = home
        
    def tell_info(self):
        print "I am %s, I eat %s, and I come from %s" % (self.kind, self.food, self.home)