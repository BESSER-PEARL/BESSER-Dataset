from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CardType(Enum):
    pass
class Color(Enum):
    pass

############################################
# Definition of Classes
############################################










class Dice:

    def __init__(self, value: int, player3: "Player" = None):
        self.value = value
        self.player3 = player3
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def player3(self):
        return self.__player3
    @player3.setter
    def player3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dice__player3", None)
        self.__player3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dice2"):
                opp_val = getattr(old_value, "dice2", None)
                if opp_val == self:
                    setattr(old_value, "dice2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dice2"):
                opp_val = getattr(value, "dice2", None)
                setattr(value, "dice2", self)



class Pawn:

    def __init__(self, position: int, color: Color, player1: "Player" = None):
        self.position = position
        self.color = color
        self.player1 = player1
        
        pass
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: Color):
        self.__color = color

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pawn__player1", None)
        self.__player1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pawn0"):
                opp_val = getattr(old_value, "pawn0", None)
                if opp_val == self:
                    setattr(old_value, "pawn0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pawn0"):
                opp_val = getattr(value, "pawn0", None)
                setattr(value, "pawn0", self)



class Card:

    def __init__(self, card: CardType, board5: "Board" = None):
        self.card = card
        self.board5 = board5
        
        pass
    @property
    def card(self):
        return self.__card
    @card.setter
    def card(self, card: CardType):
        self.__card = card

    @property
    def board5(self):
        return self.__board5
    @board5.setter
    def board5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__board5", None)
        self.__board5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card4"):
                opp_val = getattr(old_value, "card4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card4"):
                opp_val = getattr(value, "card4", None)
                if opp_val is None:
                    setattr(value, "card4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Board:

    pass


class Player:

    def __init__(self, name: str, board7: "Board" = None, pawn0: "Pawn" = None, dice2: "Dice" = None):
        self.name = name
        self.board7 = board7
        self.pawn0 = pawn0
        self.dice2 = dice2
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def board7(self):
        return self.__board7
    @board7.setter
    def board7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__board7", None)
        self.__board7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player6"):
                opp_val = getattr(old_value, "player6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player6"):
                opp_val = getattr(value, "player6", None)
                if opp_val is None:
                    setattr(value, "player6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pawn0(self):
        return self.__pawn0
    @pawn0.setter
    def pawn0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__pawn0", None)
        self.__pawn0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player1"):
                opp_val = getattr(old_value, "player1", None)
                if opp_val == self:
                    setattr(old_value, "player1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player1"):
                opp_val = getattr(value, "player1", None)
                setattr(value, "player1", self)

