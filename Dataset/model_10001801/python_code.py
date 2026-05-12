from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Deck:

    def __init__(self, deck_of_cards: str, deck_position: int, card1: set["Card"] = None):
        self.deck_of_cards = deck_of_cards
        self.deck_position = deck_position
        self.card1 = card1 if card1 is not None else set()
        
        pass
    @property
    def deck_of_cards(self):
        return self.__deck_of_cards
    @deck_of_cards.setter
    def deck_of_cards(self, deck_of_cards: str):
        self.__deck_of_cards = deck_of_cards

    @property
    def deck_position(self):
        return self.__deck_position
    @deck_position.setter
    def deck_position(self, deck_position: int):
        self.__deck_position = deck_position

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card1", None)
        self.__card1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck0"):
                    opp_val = getattr(item, "deck0", None)
                    
                    if opp_val == self:
                        setattr(item, "deck0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck0"):
                    opp_val = getattr(item, "deck0", None)
                    
                    setattr(item, "deck0", self)
                    



class Card:

    def __init__(self, value: str, front: str, suit: str, deck0: "Deck" = None):
        self.value = value
        self.front = front
        self.suit = suit
        self.deck0 = deck0
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def front(self):
        return self.__front
    @front.setter
    def front(self, front: str):
        self.__front = front

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def deck0(self):
        return self.__deck0
    @deck0.setter
    def deck0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck0", None)
        self.__deck0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card1"):
                opp_val = getattr(old_value, "card1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card1"):
                opp_val = getattr(value, "card1", None)
                if opp_val is None:
                    setattr(value, "card1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Player:

    def __init__(self, name: str, points: str):
        self.name = name
        self.points = points
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: str):
        self.__points = points

