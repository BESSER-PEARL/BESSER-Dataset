from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Player:

    def __init__(self, type: str, value: str, cards: str, card2: set["Card"] = None):
        self.type = type
        self.value = value
        self.cards = cards
        self.card2 = card2 if card2 is not None else set()
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def card2(self):
        return self.__card2
    @card2.setter
    def card2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__card2", None)
        self.__card2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player3"):
                    opp_val = getattr(item, "player3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player3"):
                    opp_val = getattr(item, "player3", None)
                    
                    if opp_val is None:
                        setattr(item, "player3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Deck:

    def __init__(self, deck: str, usedCards: str, card1: set["Card"] = None):
        self.deck = deck
        self.usedCards = usedCards
        self.card1 = card1 if card1 is not None else set()
        
        pass
    @property
    def usedCards(self):
        return self.__usedCards
    @usedCards.setter
    def usedCards(self, usedCards: str):
        self.__usedCards = usedCards

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

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
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck0"):
                    opp_val = getattr(item, "deck0", None)
                    
                    if opp_val is None:
                        setattr(item, "deck0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Card:

    def __init__(self, faceUp: bool, value: int, display: str, suit: int, deck0: set["Deck"] = None, player3: set["Player"] = None):
        self.faceUp = faceUp
        self.value = value
        self.display = display
        self.suit = suit
        self.deck0 = deck0 if deck0 is not None else set()
        self.player3 = player3 if player3 is not None else set()
        
        pass
    @property
    def faceUp(self):
        return self.__faceUp
    @faceUp.setter
    def faceUp(self, faceUp: bool):
        self.__faceUp = faceUp

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def display(self):
        return self.__display
    @display.setter
    def display(self, display: str):
        self.__display = display

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit

    @property
    def deck0(self):
        return self.__deck0
    @deck0.setter
    def deck0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck0", None)
        self.__deck0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "card1"):
                    opp_val = getattr(item, "card1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "card1"):
                    opp_val = getattr(item, "card1", None)
                    
                    if opp_val is None:
                        setattr(item, "card1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def player3(self):
        return self.__player3
    @player3.setter
    def player3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player3", None)
        self.__player3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "card2"):
                    opp_val = getattr(item, "card2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "card2"):
                    opp_val = getattr(item, "card2", None)
                    
                    if opp_val is None:
                        setattr(item, "card2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

