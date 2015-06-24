# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:58:11 2015

@author: frosch
"""

from Bird import Bird


class Pinguin(Bird):
    ''' Child-Klasse von "bird" '''
    
    def __init__(self):
        Bird.__init__(self, "Pinguin", "Fisch", "Antarktis")
        
        
        
        
        
        
# mehrere Klassen können in einer Datei gemacht werden.
        
class Adler(Bird):
    ''' Child-Klasse von "bird" '''
    
    def __init__(self):
        Bird.__init__(self, "Adler", "Hasen", "Alpen")