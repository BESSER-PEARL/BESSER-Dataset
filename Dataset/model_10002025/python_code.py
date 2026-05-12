from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class CardPlayer__:

    pass


class CardGame(ABC):

    pass


class CardPlayer(ABC):

    pass


class CustomException_InvalidCardException:

    pass


class CustomException_DeckOrHandEmptyException:

    pass


class CustomException_CardException:

    pass


class Hand:

    def __init__(self, HandOfCards: str, Hand_Card_02: set["Card"] = None, CardPlayer_Hand_15: set["CardPlayer"] = None):
        self.HandOfCards = HandOfCards
        self.Hand_Card_02 = Hand_Card_02 if Hand_Card_02 is not None else set()
        self.CardPlayer_Hand_15 = CardPlayer_Hand_15 if CardPlayer_Hand_15 is not None else set()
        
        pass
    @property
    def HandOfCards(self):
        return self.__HandOfCards
    @HandOfCards.setter
    def HandOfCards(self, HandOfCards: str):
        self.__HandOfCards = HandOfCards

    @property
    def CardPlayer_Hand_15(self):
        return self.__CardPlayer_Hand_15
    @CardPlayer_Hand_15.setter
    def CardPlayer_Hand_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__CardPlayer_Hand_15", None)
        self.__CardPlayer_Hand_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CardPlayer_Hand_04"):
                    opp_val = getattr(item, "CardPlayer_Hand_04", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CardPlayer_Hand_04"):
                    opp_val = getattr(item, "CardPlayer_Hand_04", None)
                    
                    if opp_val is None:
                        setattr(item, "CardPlayer_Hand_04", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Hand_Card_02(self):
        return self.__Hand_Card_02
    @Hand_Card_02.setter
    def Hand_Card_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__Hand_Card_02", None)
        self.__Hand_Card_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Hand_Card_13"):
                    opp_val = getattr(item, "Hand_Card_13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Hand_Card_13"):
                    opp_val = getattr(item, "Hand_Card_13", None)
                    
                    if opp_val is None:
                        setattr(item, "Hand_Card_13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Deck:

    def __init__(self, CardsList: str, Deck_Card_00: set["Card"] = None):
        self.CardsList = CardsList
        self.Deck_Card_00 = Deck_Card_00 if Deck_Card_00 is not None else set()
        
        pass
    @property
    def CardsList(self):
        return self.__CardsList
    @CardsList.setter
    def CardsList(self, CardsList: str):
        self.__CardsList = CardsList

    @property
    def Deck_Card_00(self):
        return self.__Deck_Card_00
    @Deck_Card_00.setter
    def Deck_Card_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__Deck_Card_00", None)
        self.__Deck_Card_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Deck_Card_11"):
                    opp_val = getattr(item, "Deck_Card_11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Deck_Card_11"):
                    opp_val = getattr(item, "Deck_Card_11", None)
                    
                    if opp_val is None:
                        setattr(item, "Deck_Card_11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Card:

    def __init__(self, Suit: Enumeration, Rank: int, Deck_Card_11: set["Deck"] = None, Hand_Card_13: set["Hand"] = None):
        self.Suit = Suit
        self.Rank = Rank
        self.Deck_Card_11 = Deck_Card_11 if Deck_Card_11 is not None else set()
        self.Hand_Card_13 = Hand_Card_13 if Hand_Card_13 is not None else set()
        
        pass
    @property
    def Rank(self):
        return self.__Rank
    @Rank.setter
    def Rank(self, Rank: int):
        self.__Rank = Rank

    @property
    def Suit(self):
        return self.__Suit
    @Suit.setter
    def Suit(self, Suit: Enumeration):
        self.__Suit = Suit

    @property
    def Hand_Card_13(self):
        return self.__Hand_Card_13
    @Hand_Card_13.setter
    def Hand_Card_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__Hand_Card_13", None)
        self.__Hand_Card_13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Hand_Card_02"):
                    opp_val = getattr(item, "Hand_Card_02", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Hand_Card_02"):
                    opp_val = getattr(item, "Hand_Card_02", None)
                    
                    if opp_val is None:
                        setattr(item, "Hand_Card_02", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Deck_Card_11(self):
        return self.__Deck_Card_11
    @Deck_Card_11.setter
    def Deck_Card_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__Deck_Card_11", None)
        self.__Deck_Card_11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Deck_Card_00"):
                    opp_val = getattr(item, "Deck_Card_00", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Deck_Card_00"):
                    opp_val = getattr(item, "Deck_Card_00", None)
                    
                    if opp_val is None:
                        setattr(item, "Deck_Card_00", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

