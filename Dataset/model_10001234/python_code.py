from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    pass
class PlayerType(Enum):
    pass

############################################
# Definition of Classes
############################################










class Menu:

    pass


class EventHandler:

    pass


class AI:

    pass


class Window:

    pass


class Player:

    def __init__(self, type: PlayerType, color: Color, dice2: "Dice" = None, gameState15: "GameState" = None, aI18: "AI" = None):
        self.type = type
        self.color = color
        self.dice2 = dice2
        self.gameState15 = gameState15
        self.aI18 = aI18
        
        pass
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: Color):
        self.__color = color

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: PlayerType):
        self.__type = type

    @property
    def dice2(self):
        return self.__dice2
    @dice2.setter
    def dice2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__dice2", None)
        self.__dice2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player3"):
                opp_val = getattr(old_value, "player3", None)
                if opp_val == self:
                    setattr(old_value, "player3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player3"):
                opp_val = getattr(value, "player3", None)
                setattr(value, "player3", self)

    @property
    def aI18(self):
        return self.__aI18
    @aI18.setter
    def aI18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__aI18", None)
        self.__aI18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player19"):
                opp_val = getattr(old_value, "player19", None)
                if opp_val == self:
                    setattr(old_value, "player19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player19"):
                opp_val = getattr(value, "player19", None)
                setattr(value, "player19", self)

    @property
    def gameState15(self):
        return self.__gameState15
    @gameState15.setter
    def gameState15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__gameState15", None)
        self.__gameState15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player14"):
                opp_val = getattr(old_value, "player14", None)
                if opp_val == self:
                    setattr(old_value, "player14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player14"):
                opp_val = getattr(value, "player14", None)
                setattr(value, "player14", self)



class Pawn:

    pass


class GraphicsGenerator:

    pass


class IOFilesManagement:

    pass


class GameState:

    pass


class GameEngine:

    pass


class Field:

    def __init__(self, y: int, color: Color, x: int, graphicsGenerator8: "GraphicsGenerator" = None):
        self.y = y
        self.color = color
        self.x = x
        self.graphicsGenerator8 = graphicsGenerator8
        
        pass
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: Color):
        self.__color = color

    @property
    def graphicsGenerator8(self):
        return self.__graphicsGenerator8
    @graphicsGenerator8.setter
    def graphicsGenerator8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Field__graphicsGenerator8", None)
        self.__graphicsGenerator8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "field9"):
                opp_val = getattr(old_value, "field9", None)
                if opp_val == self:
                    setattr(old_value, "field9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "field9"):
                opp_val = getattr(value, "field9", None)
                setattr(value, "field9", self)



class Dice:

    pass


class Board:

    def __init__(self, board: str, graphicsGenerator6: "GraphicsGenerator" = None, gameEngine11: "GameEngine" = None, window16: "Window" = None):
        self.board = board
        self.graphicsGenerator6 = graphicsGenerator6
        self.gameEngine11 = gameEngine11
        self.window16 = window16
        
        pass
    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: str):
        self.__board = board

    @property
    def window16(self):
        return self.__window16
    @window16.setter
    def window16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board__window16", None)
        self.__window16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board17"):
                opp_val = getattr(old_value, "board17", None)
                if opp_val == self:
                    setattr(old_value, "board17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board17"):
                opp_val = getattr(value, "board17", None)
                setattr(value, "board17", self)

    @property
    def gameEngine11(self):
        return self.__gameEngine11
    @gameEngine11.setter
    def gameEngine11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board__gameEngine11", None)
        self.__gameEngine11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board10"):
                opp_val = getattr(old_value, "board10", None)
                if opp_val == self:
                    setattr(old_value, "board10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board10"):
                opp_val = getattr(value, "board10", None)
                setattr(value, "board10", self)

    @property
    def graphicsGenerator6(self):
        return self.__graphicsGenerator6
    @graphicsGenerator6.setter
    def graphicsGenerator6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board__graphicsGenerator6", None)
        self.__graphicsGenerator6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board7"):
                opp_val = getattr(old_value, "board7", None)
                if opp_val == self:
                    setattr(old_value, "board7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board7"):
                opp_val = getattr(value, "board7", None)
                setattr(value, "board7", self)

