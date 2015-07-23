"""
Created on 25.06.2015

@author: hohausjs
@author: froeser
"""
from Controller import Controller


def getLinkToPage():
    """ fragt nach einer url """
    urlInput = raw_input("Bitte gib eine URL ein:")
    if urlInput.find('http://') == -1 or urlInput.find('https://') == -1:
        urlInput = "http://" + urlInput
    return urlInput

def run():

    # get an instance of the Controller
    Controller().start_simple()

    print "---------------------"
    print "programm has finished\n\nGood Bye"

if __name__ == '__main__':
    # main()
    run()