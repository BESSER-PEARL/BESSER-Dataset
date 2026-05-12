from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Stack:

    def __init__(self, cards__: Card, numOfCards: int, card3: "Card" = None, deals5: "Deck" = None, stack6: "Stack" = None, moves7: "Stack" = None):
        self.cards__ = cards__
        self.numOfCards = numOfCards
        self.card3 = card3
        self.deals5 = deals5
        self.stack6 = stack6
        self.moves7 = moves7
        
        pass
    @property
    def cards__(self):
        return self.__cards__
    @cards__.setter
    def cards__(self, cards__: Card):
        self.__cards__ = cards__

    @property
    def numOfCards(self):
        return self.__numOfCards
    @numOfCards.setter
    def numOfCards(self, numOfCards: int):
        self.__numOfCards = numOfCards

    @property
    def stack6(self):
        return self.__stack6
    @stack6.setter
    def stack6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stack__stack6", None)
        self.__stack6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moves7"):
                opp_val = getattr(old_value, "moves7", None)
                if opp_val == self:
                    setattr(old_value, "moves7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moves7"):
                opp_val = getattr(value, "moves7", None)
                setattr(value, "moves7", self)

    @property
    def card3(self):
        return self.__card3
    @card3.setter
    def card3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stack__card3", None)
        self.__card3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conatins2"):
                opp_val = getattr(old_value, "Conatins2", None)
                if opp_val == self:
                    setattr(old_value, "Conatins2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conatins2"):
                opp_val = getattr(value, "Conatins2", None)
                setattr(value, "Conatins2", self)

    @property
    def moves7(self):
        return self.__moves7
    @moves7.setter
    def moves7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stack__moves7", None)
        self.__moves7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stack6"):
                opp_val = getattr(old_value, "stack6", None)
                if opp_val == self:
                    setattr(old_value, "stack6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stack6"):
                opp_val = getattr(value, "stack6", None)
                setattr(value, "stack6", self)

    @property
    def deals5(self):
        return self.__deals5
    @deals5.setter
    def deals5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stack__deals5", None)
        self.__deals5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stack4"):
                opp_val = getattr(old_value, "stack4", None)
                if opp_val == self:
                    setattr(old_value, "stack4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stack4"):
                opp_val = getattr(value, "stack4", None)
                setattr(value, "stack4", self)



class Card:

    def __init__(self, suit: int, value: int, Contains0: "Deck" = None, Conatins2: "Stack" = None):
        self.suit = suit
        self.value = value
        self.Contains0 = Contains0
        self.Conatins2 = Conatins2
        
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
    def Conatins2(self):
        return self.__Conatins2
    @Conatins2.setter
    def Conatins2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__Conatins2", None)
        self.__Conatins2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card3"):
                opp_val = getattr(old_value, "card3", None)
                if opp_val == self:
                    setattr(old_value, "card3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card3"):
                opp_val = getattr(value, "card3", None)
                setattr(value, "card3", self)

    @property
    def Contains0(self):
        return self.__Contains0
    @Contains0.setter
    def Contains0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__Contains0", None)
        self.__Contains0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card1"):
                opp_val = getattr(old_value, "card1", None)
                if opp_val == self:
                    setattr(old_value, "card1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card1"):
                opp_val = getattr(value, "card1", None)
                setattr(value, "card1", self)



class Deck:

    def __init__(self, numOfCards: int, Card__: Card, card1: "Card" = None, stack4: "Stack" = None):
        self.numOfCards = numOfCards
        self.Card__ = Card__
        self.card1 = card1
        self.stack4 = stack4
        
        pass
    @property
    def Card__(self):
        return self.__Card__
    @Card__.setter
    def Card__(self, Card__: Card):
        self.__Card__ = Card__

    @property
    def numOfCards(self):
        return self.__numOfCards
    @numOfCards.setter
    def numOfCards(self, numOfCards: int):
        self.__numOfCards = numOfCards

    @property
    def stack4(self):
        return self.__stack4
    @stack4.setter
    def stack4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__stack4", None)
        self.__stack4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deals5"):
                opp_val = getattr(old_value, "deals5", None)
                if opp_val == self:
                    setattr(old_value, "deals5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deals5"):
                opp_val = getattr(value, "deals5", None)
                setattr(value, "deals5", self)

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card1", None)
        self.__card1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Contains0"):
                opp_val = getattr(old_value, "Contains0", None)
                if opp_val == self:
                    setattr(old_value, "Contains0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Contains0"):
                opp_val = getattr(value, "Contains0", None)
                setattr(value, "Contains0", self)

