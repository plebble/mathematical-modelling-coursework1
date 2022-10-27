
class Ground:


    def __init__(self):
        # this will eventually convert some kind of input into something that python can deal with.
        pass

    def getDisplacement(x):
        # this should get the height of the speedbump at the position x

        if x >=2 and x < 4:
            return (0.25*x)-0.5

        elif x >=6 and x < 8:
            return (-0.25*x)+1.5
        
        else:
            return 0
        