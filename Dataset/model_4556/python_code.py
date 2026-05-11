from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class CMD:

    pass
class myDsl_RIGHT(CMD):

    def __init__(self, amount: int):
        self.amount = amount
        
        pass
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount


class myDsl_LEFT(CMD):

    def __init__(self, amount: int):
        self.amount = amount
        
        pass
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount


class myDsl_PENCOLOUR(CMD):

    def __init__(self, colour: str):
        self.colour = colour
        
        pass
    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour: str):
        self.__colour = colour


class myDsl_PENSTATE(CMD):

    def __init__(self, penState: str):
        self.penState = penState
        
        pass
    @property
    def penState(self):
        return self.__penState

    @penState.setter
    def penState(self, penState: str):
        self.__penState = penState


class myDsl_TURTLE(CMD):

    def __init__(self, startPosX: int, startPosY: int):
        self.startPosX = startPosX
        self.startPosY = startPosY
        
        pass
    @property
    def startPosX(self):
        return self.__startPosX

    @startPosX.setter
    def startPosX(self, startPosX: int):
        self.__startPosX = startPosX


    @property
    def startPosY(self):
        return self.__startPosY

    @startPosY.setter
    def startPosY(self, startPosY: int):
        self.__startPosY = startPosY


class myDsl_MOVE(CMD):

    def __init__(self, amount: int):
        self.amount = amount
        
        pass
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount


class myDsl_PAPER(CMD):

    def __init__(self, sizeX: int, sizeY: int, paperColour: str):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.paperColour = paperColour
        
        pass
    @property
    def paperColour(self):
        return self.__paperColour

    @paperColour.setter
    def paperColour(self, paperColour: str):
        self.__paperColour = paperColour


    @property
    def sizeX(self):
        return self.__sizeX

    @sizeX.setter
    def sizeX(self, sizeX: int):
        self.__sizeX = sizeX


    @property
    def sizeY(self):
        return self.__sizeY

    @sizeY.setter
    def sizeY(self, sizeY: int):
        self.__sizeY = sizeY


class myDsl_CMD:

    pass
class myDsl_PROGRAM:

    pass