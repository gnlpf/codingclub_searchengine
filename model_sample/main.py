# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:57:44 2015

@author: frosch
"""

"""
from Bird import Bird

def main():
    print "\n\n****************"    
    
    myBird = Bird("Pinguin", "Fisch", "Antarktis")
    myBird.tell_info()
    
    pass
"""


from Birds import Pinguin,Adler

def main():
    print "****************"
    
    pinguin = Pinguin()
    pinguin.tell_info()
    
    adler = Adler()
    adler.setKindAndFood("Adler", "Kleine Kinder")
    adler.setHome("Alpen")
    adler.setHome("Sahara")
    adler.tell_info()


if __name__ == '__main__':
    main()
