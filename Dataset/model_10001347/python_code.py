from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Change_Deck__Image_Changes__UseCase:

    pass


class Quit_UseCase:

    pass


class Shuffle_Deck__Restart_Game__UseCase:

    pass


class Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase:

    pass


class Begin_Game_UseCase:

    pass


class Player_Actor:

    pass





class MemoryGame_Deck:

    def __init__(self, id: int, image: str, cards: MemoryGame_Card, card0: set["MemoryGame_Card"] = None):
        self.id = id
        self.image = image
        self.cards = cards
        self.card0 = card0 if card0 is not None else set()
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: MemoryGame_Card):
        self.__cards = cards

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def card0(self):
        return self.__card0
    @card0.setter
    def card0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MemoryGame_Deck__card0", None)
        self.__card0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck1"):
                    opp_val = getattr(item, "deck1", None)
                    
                    if opp_val == self:
                        setattr(item, "deck1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck1"):
                    opp_val = getattr(item, "deck1", None)
                    
                    setattr(item, "deck1", self)
                    



class MemoryGame_Card:

    def __init__(self, position: int, id: int, image: str, isShowing: bool, deck: MemoryGame_Deck, deck1: "MemoryGame_Deck" = None):
        self.position = position
        self.id = id
        self.image = image
        self.isShowing = isShowing
        self.deck = deck
        self.deck1 = deck1
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def isShowing(self):
        return self.__isShowing
    @isShowing.setter
    def isShowing(self, isShowing: bool):
        self.__isShowing = isShowing

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: MemoryGame_Deck):
        self.__deck = deck

    @property
    def deck1(self):
        return self.__deck1
    @deck1.setter
    def deck1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MemoryGame_Card__deck1", None)
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

