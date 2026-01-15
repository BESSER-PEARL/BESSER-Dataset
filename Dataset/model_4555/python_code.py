from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class CMD:

    pass
class myDsl_PENCOLOUR(CMD):

    def __init__(self, colour: str):
        self.colour = colour
        
    @property
    def colour(self) -> str:
        return self.__colour

    @colour.setter
    def colour(self, colour: str):
        self.__colour = colour

class myDsl_PENSTATE(CMD):

    def __init__(self, penState: str):
        self.penState = penState
        
    @property
    def penState(self) -> str:
        return self.__penState

    @penState.setter
    def penState(self, penState: str):
        self.__penState = penState

class myDsl_RIGHT(CMD):

    def __init__(self, amount: int):
        self.amount = amount
        
    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

class myDsl_LEFT(CMD):

    def __init__(self, amount: int):
        self.amount = amount
        
    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

class myDsl_TURTLE(CMD):

    def __init__(self, startPosX: int, startPosY: int):
        self.startPosX = startPosX
        self.startPosY = startPosY
        
    @property
    def startPosX(self) -> int:
        return self.__startPosX

    @startPosX.setter
    def startPosX(self, startPosX: int):
        self.__startPosX = startPosX

    @property
    def startPosY(self) -> int:
        return self.__startPosY

    @startPosY.setter
    def startPosY(self, startPosY: int):
        self.__startPosY = startPosY

class myDsl_MOVE(CMD):

    def __init__(self, amount: int):
        self.amount = amount
        
    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

class myDsl_PAPER(CMD):

    def __init__(self, sizeX: int, sizeY: int, paperColour: str):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.paperColour = paperColour
        
    @property
    def sizeY(self) -> int:
        return self.__sizeY

    @sizeY.setter
    def sizeY(self, sizeY: int):
        self.__sizeY = sizeY

    @property
    def paperColour(self) -> str:
        return self.__paperColour

    @paperColour.setter
    def paperColour(self, paperColour: str):
        self.__paperColour = paperColour

    @property
    def sizeX(self) -> int:
        return self.__sizeX

    @sizeX.setter
    def sizeX(self, sizeX: int):
        self.__sizeX = sizeX

class myDsl_CMD:

    pass
class myDsl_PROGRAM:

    pass