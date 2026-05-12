from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class GUI:

    pass


class Player:

    def __init__(self, points: int, hand: Deck, deck4: "Deck" = None, gameBoard8: "GameBoard" = None):
        self.points = points
        self.hand = hand
        self.deck4 = deck4
        self.gameBoard8 = gameBoard8
        
        pass
    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Deck):
        self.__hand = hand

    @property
    def deck4(self):
        return self.__deck4
    @deck4.setter
    def deck4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__deck4", None)
        self.__deck4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player5"):
                opp_val = getattr(old_value, "player5", None)
                if opp_val == self:
                    setattr(old_value, "player5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player5"):
                opp_val = getattr(value, "player5", None)
                setattr(value, "player5", self)

    @property
    def gameBoard8(self):
        return self.__gameBoard8
    @gameBoard8.setter
    def gameBoard8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__gameBoard8", None)
        self.__gameBoard8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player9"):
                opp_val = getattr(old_value, "player9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player9"):
                opp_val = getattr(value, "player9", None)
                if opp_val is None:
                    setattr(value, "player9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class GameBoard:

    def __init__(self, garbagePile: str, discardPile: str, shelf: str, deck2: "Deck" = None, gUI6: "GUI" = None, player9: set["Player"] = None):
        self.garbagePile = garbagePile
        self.discardPile = discardPile
        self.shelf = shelf
        self.deck2 = deck2
        self.gUI6 = gUI6
        self.player9 = player9 if player9 is not None else set()
        
        pass
    @property
    def shelf(self):
        return self.__shelf
    @shelf.setter
    def shelf(self, shelf: str):
        self.__shelf = shelf

    @property
    def garbagePile(self):
        return self.__garbagePile
    @garbagePile.setter
    def garbagePile(self, garbagePile: str):
        self.__garbagePile = garbagePile

    @property
    def discardPile(self):
        return self.__discardPile
    @discardPile.setter
    def discardPile(self, discardPile: str):
        self.__discardPile = discardPile

    @property
    def gUI6(self):
        return self.__gUI6
    @gUI6.setter
    def gUI6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameBoard__gUI6", None)
        self.__gUI6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameBoard7"):
                opp_val = getattr(old_value, "gameBoard7", None)
                if opp_val == self:
                    setattr(old_value, "gameBoard7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameBoard7"):
                opp_val = getattr(value, "gameBoard7", None)
                setattr(value, "gameBoard7", self)

    @property
    def deck2(self):
        return self.__deck2
    @deck2.setter
    def deck2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameBoard__deck2", None)
        self.__deck2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameBoard3"):
                opp_val = getattr(old_value, "gameBoard3", None)
                if opp_val == self:
                    setattr(old_value, "gameBoard3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameBoard3"):
                opp_val = getattr(value, "gameBoard3", None)
                setattr(value, "gameBoard3", self)

    @property
    def player9(self):
        return self.__player9
    @player9.setter
    def player9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameBoard__player9", None)
        self.__player9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gameBoard8"):
                    opp_val = getattr(item, "gameBoard8", None)
                    
                    if opp_val == self:
                        setattr(item, "gameBoard8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gameBoard8"):
                    opp_val = getattr(item, "gameBoard8", None)
                    
                    setattr(item, "gameBoard8", self)
                    



class Deck:

    pass


class Card:

    def __init__(self, value: int, suit: int, deck1: "Deck" = None):
        self.value = value
        self.suit = suit
        self.deck1 = deck1
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit

    @property
    def deck1(self):
        return self.__deck1
    @deck1.setter
    def deck1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck1", None)
        self.__deck1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card0"):
                opp_val = getattr(old_value, "card0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card0"):
                opp_val = getattr(value, "card0", None)
                if opp_val is None:
                    setattr(value, "card0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

