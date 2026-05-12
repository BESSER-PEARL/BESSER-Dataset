from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suit(Enum):
    pass
class Kind(Enum):
    pass

############################################
# Definition of Classes
############################################










class Card:

    def __init__(self, suit: Suit, kind: Kind, deck1: "Deck" = None, player11: "Player" = None):
        self.suit = suit
        self.kind = kind
        self.deck1 = deck1
        self.player11 = player11
        
        pass
    @property
    def kind(self):
        return self.__kind
    @kind.setter
    def kind(self, kind: Kind):
        self.__kind = kind

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit):
        self.__suit = suit

    @property
    def player11(self):
        return self.__player11
    @player11.setter
    def player11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player11", None)
        self.__player11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards10"):
                opp_val = getattr(old_value, "cards10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards10"):
                opp_val = getattr(value, "cards10", None)
                if opp_val is None:
                    setattr(value, "cards10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "cards0"):
                opp_val = getattr(old_value, "cards0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards0"):
                opp_val = getattr(value, "cards0", None)
                if opp_val is None:
                    setattr(value, "cards0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Player(ABC):

    def __init__(self, name: str, avatar4: "Avatar" = None, games7: set["Game"] = None, cards10: set["Card"] = None):
        self.name = name
        self.avatar4 = avatar4
        self.games7 = games7 if games7 is not None else set()
        self.cards10 = cards10 if cards10 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cards10(self):
        return self.__cards10
    @cards10.setter
    def cards10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__cards10", None)
        self.__cards10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player11"):
                    opp_val = getattr(item, "player11", None)
                    
                    if opp_val == self:
                        setattr(item, "player11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player11"):
                    opp_val = getattr(item, "player11", None)
                    
                    setattr(item, "player11", self)
                    

    @property
    def games7(self):
        return self.__games7
    @games7.setter
    def games7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__games7", None)
        self.__games7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "players6"):
                    opp_val = getattr(item, "players6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "players6"):
                    opp_val = getattr(item, "players6", None)
                    
                    if opp_val is None:
                        setattr(item, "players6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def avatar4(self):
        return self.__avatar4
    @avatar4.setter
    def avatar4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__avatar4", None)
        self.__avatar4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players5"):
                opp_val = getattr(old_value, "players5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players5"):
                opp_val = getattr(value, "players5", None)
                if opp_val is None:
                    setattr(value, "players5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Game(ABC):

    def __init__(self, name: str, players6: set["Player"] = None, decks8: set["Deck"] = None):
        self.name = name
        self.players6 = players6 if players6 is not None else set()
        self.decks8 = decks8 if decks8 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def players6(self):
        return self.__players6
    @players6.setter
    def players6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__players6", None)
        self.__players6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "games7"):
                    opp_val = getattr(item, "games7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "games7"):
                    opp_val = getattr(item, "games7", None)
                    
                    if opp_val is None:
                        setattr(item, "games7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def decks8(self):
        return self.__decks8
    @decks8.setter
    def decks8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__decks8", None)
        self.__decks8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "games9"):
                    opp_val = getattr(item, "games9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "games9"):
                    opp_val = getattr(item, "games9", None)
                    
                    if opp_val is None:
                        setattr(item, "games9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Avatar:

    pass


class Theme:

    pass


class Deck:

    pass
