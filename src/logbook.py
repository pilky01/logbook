#!/usr/bin/env python3

##############################################################################
## 
## 
## 
##############################################################################


from logbook_gui import logbook_gui as gui
from logbook_db import logbook_db as db


###############
##  Classes  ##
###############

class Airport(object):

    def __init__(self):
        pass

class Aircraft(object):

    def __init__(self):
        pass

##########################
## Main Application GUI ##
##########################
    
def main():
    app = gui.Application(gui.root)
    app.mainloop()

if __name__ == "__main__":
    main()
