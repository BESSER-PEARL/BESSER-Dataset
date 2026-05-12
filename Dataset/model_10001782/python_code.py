from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Board(Enum):
    pass

############################################
# Definition of Classes
############################################










class Card_Interface:

    pass


class ElevensGame:

    def __init__(self, win: bool, Board_9_: int, deck0: "Deck" = None, player2: "Player" = None):
        self.win = win
        self.Board_9_ = Board_9_
        self.deck0 = deck0
        self.player2 = player2
        
        pass
    @property
    def win(self):
        return self.__win
    @win.setter
    def win(self, win: bool):
        self.__win = win

    @property
    def Board_9_(self):
        return self.__Board_9_
    @Board_9_.setter
    def Board_9_(self, Board_9_: int):
        self.__Board_9_ = Board_9_

    @property
    def deck0(self):
        return self.__deck0
    @deck0.setter
    def deck0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElevensGame__deck0", None)
        self.__deck0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevensGame1"):
                opp_val = getattr(old_value, "elevensGame1", None)
                if opp_val == self:
                    setattr(old_value, "elevensGame1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevensGame1"):
                opp_val = getattr(value, "elevensGame1", None)
                setattr(value, "elevensGame1", self)

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElevensGame__player2", None)
        self.__player2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevensGame3"):
                opp_val = getattr(old_value, "elevensGame3", None)
                if opp_val == self:
                    setattr(old_value, "elevensGame3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevensGame3"):
                opp_val = getattr(value, "elevensGame3", None)
                setattr(value, "elevensGame3", self)



class Player:

    pass


class Deck:

    def __init__(self, Topcard: int, Deck_ArrayList_: int, elevensGame1: "ElevensGame" = None, interface5: "Card_Interface" = None):
        self.Topcard = Topcard
        self.Deck_ArrayList_ = Deck_ArrayList_
        self.elevensGame1 = elevensGame1
        self.interface5 = interface5
        
        pass
    @property
    def Deck_ArrayList_(self):
        return self.__Deck_ArrayList_
    @Deck_ArrayList_.setter
    def Deck_ArrayList_(self, Deck_ArrayList_: int):
        self.__Deck_ArrayList_ = Deck_ArrayList_

    @property
    def Topcard(self):
        return self.__Topcard
    @Topcard.setter
    def Topcard(self, Topcard: int):
        self.__Topcard = Topcard

    @property
    def elevensGame1(self):
        return self.__elevensGame1
    @elevensGame1.setter
    def elevensGame1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__elevensGame1", None)
        self.__elevensGame1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck0"):
                opp_val = getattr(old_value, "deck0", None)
                if opp_val == self:
                    setattr(old_value, "deck0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck0"):
                opp_val = getattr(value, "deck0", None)
                setattr(value, "deck0", self)

    @property
    def interface5(self):
        return self.__interface5
    @interface5.setter
    def interface5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__interface5", None)
        self.__interface5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck4"):
                opp_val = getattr(old_value, "deck4", None)
                if opp_val == self:
                    setattr(old_value, "deck4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck4"):
                opp_val = getattr(value, "deck4", None)
                setattr(value, "deck4", self)

