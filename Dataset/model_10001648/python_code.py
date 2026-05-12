from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class CardDeck:

    def __init__(self, cards: str, suits: str, CardDeck_Card_00: set["Card"] = None):
        self.cards = cards
        self.suits = suits
        self.CardDeck_Card_00 = CardDeck_Card_00 if CardDeck_Card_00 is not None else set()
        
        pass
    @property
    def suits(self):
        return self.__suits
    @suits.setter
    def suits(self, suits: str):
        self.__suits = suits

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def CardDeck_Card_00(self):
        return self.__CardDeck_Card_00
    @CardDeck_Card_00.setter
    def CardDeck_Card_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CardDeck__CardDeck_Card_00", None)
        self.__CardDeck_Card_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Has1"):
                    opp_val = getattr(item, "Has1", None)
                    
                    if opp_val == self:
                        setattr(item, "Has1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Has1"):
                    opp_val = getattr(item, "Has1", None)
                    
                    setattr(item, "Has1", self)
                    



class Card:

    def __init__(self, cardSuit: str, cardFace: int, Has1: "CardDeck" = None):
        self.cardSuit = cardSuit
        self.cardFace = cardFace
        self.Has1 = Has1
        
        pass
    @property
    def cardFace(self):
        return self.__cardFace
    @cardFace.setter
    def cardFace(self, cardFace: int):
        self.__cardFace = cardFace

    @property
    def cardSuit(self):
        return self.__cardSuit
    @cardSuit.setter
    def cardSuit(self, cardSuit: str):
        self.__cardSuit = cardSuit

    @property
    def Has1(self):
        return self.__Has1
    @Has1.setter
    def Has1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__Has1", None)
        self.__Has1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CardDeck_Card_00"):
                opp_val = getattr(old_value, "CardDeck_Card_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CardDeck_Card_00"):
                opp_val = getattr(value, "CardDeck_Card_00", None)
                if opp_val is None:
                    setattr(value, "CardDeck_Card_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

