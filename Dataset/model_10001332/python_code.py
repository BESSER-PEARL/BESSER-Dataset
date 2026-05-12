from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Cards:

    def __init__(self, card: CardGame, attribute2: int, attribute3: str, cardGame0: "CardGame" = None):
        self.card = card
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.cardGame0 = cardGame0
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: int):
        self.__attribute2 = attribute2

    @property
    def card(self):
        return self.__card
    @card.setter
    def card(self, card: CardGame):
        self.__card = card

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def cardGame0(self):
        return self.__cardGame0
    @cardGame0.setter
    def cardGame0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards__cardGame0", None)
        self.__cardGame0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards1"):
                opp_val = getattr(old_value, "cards1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards1"):
                opp_val = getattr(value, "cards1", None)
                if opp_val is None:
                    setattr(value, "cards1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class CardGame:

    def __init__(self, CardNumber: int, suit: str, cards1: set["Cards"] = None):
        self.CardNumber = CardNumber
        self.suit = suit
        self.cards1 = cards1 if cards1 is not None else set()
        
        pass
    @property
    def CardNumber(self):
        return self.__CardNumber
    @CardNumber.setter
    def CardNumber(self, CardNumber: int):
        self.__CardNumber = CardNumber

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def cards1(self):
        return self.__cards1
    @cards1.setter
    def cards1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CardGame__cards1", None)
        self.__cards1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cardGame0"):
                    opp_val = getattr(item, "cardGame0", None)
                    
                    if opp_val == self:
                        setattr(item, "cardGame0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cardGame0"):
                    opp_val = getattr(item, "cardGame0", None)
                    
                    setattr(item, "cardGame0", self)
                    

