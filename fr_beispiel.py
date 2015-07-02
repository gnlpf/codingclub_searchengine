# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:28:56 2015

@author: frosch
"""

text = "blablubb"
print text


if text.find('<a') != -1:
    print "nicht drin"
    
else:
    print "drin"