from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suit(Enum):
    pass
class Suit2(Enum):
    pass
class Kind2(Enum):
    pass
class Kind(Enum):
    pass
class Suit1(Enum):
    pass
class Kind1(Enum):
    pass

############################################
# Definition of Classes
############################################










class Player1(ABC):

    def __init__(self, name: str, hand: str, games31: set["Game1"] = None, cards32: set["Card1"] = None, avatar34: "Avatar1" = None):
        self.name = name
        self.hand = hand
        self.games31 = games31 if games31 is not None else set()
        self.cards32 = cards32 if cards32 is not None else set()
        self.avatar34 = avatar34
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: str):
        self.__hand = hand

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cards32(self):
        return self.__cards32
    @cards32.setter
    def cards32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player1__cards32", None)
        self.__cards32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player33"):
                    opp_val = getattr(item, "player33", None)
                    
                    if opp_val == self:
                        setattr(item, "player33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player33"):
                    opp_val = getattr(item, "player33", None)
                    
                    setattr(item, "player33", self)
                    

    @property
    def games31(self):
        return self.__games31
    @games31.setter
    def games31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player1__games31", None)
        self.__games31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "players30"):
                    opp_val = getattr(item, "players30", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "players30"):
                    opp_val = getattr(item, "players30", None)
                    
                    if opp_val is None:
                        setattr(item, "players30", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def avatar34(self):
        return self.__avatar34
    @avatar34.setter
    def avatar34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player1__avatar34", None)
        self.__avatar34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players35"):
                opp_val = getattr(old_value, "players35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players35"):
                opp_val = getattr(value, "players35", None)
                if opp_val is None:
                    setattr(value, "players35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Avatar1:

    pass


class Card1:

    def __init__(self, suit: Suit1, kind: Kind1, deck27: "Deck1" = None, player33: "Player1" = None):
        self.suit = suit
        self.kind = kind
        self.deck27 = deck27
        self.player33 = player33
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit1):
        self.__suit = suit

    @property
    def kind(self):
        return self.__kind
    @kind.setter
    def kind(self, kind: Kind1):
        self.__kind = kind

    @property
    def deck27(self):
        return self.__deck27
    @deck27.setter
    def deck27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card1__deck27", None)
        self.__deck27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards26"):
                opp_val = getattr(old_value, "cards26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards26"):
                opp_val = getattr(value, "cards26", None)
                if opp_val is None:
                    setattr(value, "cards26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def player33(self):
        return self.__player33
    @player33.setter
    def player33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card1__player33", None)
        self.__player33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards32"):
                opp_val = getattr(old_value, "cards32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards32"):
                opp_val = getattr(value, "cards32", None)
                if opp_val is None:
                    setattr(value, "cards32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Game1(ABC):

    def __init__(self, name: str, decks28: set["Deck1"] = None, players30: set["Player1"] = None):
        self.name = name
        self.decks28 = decks28 if decks28 is not None else set()
        self.players30 = players30 if players30 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def players30(self):
        return self.__players30
    @players30.setter
    def players30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game1__players30", None)
        self.__players30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "games31"):
                    opp_val = getattr(item, "games31", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "games31"):
                    opp_val = getattr(item, "games31", None)
                    
                    if opp_val is None:
                        setattr(item, "games31", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def decks28(self):
        return self.__decks28
    @decks28.setter
    def decks28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game1__decks28", None)
        self.__decks28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "games29"):
                    opp_val = getattr(item, "games29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "games29"):
                    opp_val = getattr(item, "games29", None)
                    
                    if opp_val is None:
                        setattr(item, "games29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Deck1:

    def __init__(self, Card_cards_52_: Card, theme24: "Theme1" = None, cards26: set["Card1"] = None, games29: set["Game1"] = None):
        self.Card_cards_52_ = Card_cards_52_
        self.theme24 = theme24
        self.cards26 = cards26 if cards26 is not None else set()
        self.games29 = games29 if games29 is not None else set()
        
        pass
    @property
    def Card_cards_52_(self):
        return self.__Card_cards_52_
    @Card_cards_52_.setter
    def Card_cards_52_(self, Card_cards_52_: Card):
        self.__Card_cards_52_ = Card_cards_52_

    @property
    def cards26(self):
        return self.__cards26
    @cards26.setter
    def cards26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck1__cards26", None)
        self.__cards26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck27"):
                    opp_val = getattr(item, "deck27", None)
                    
                    if opp_val == self:
                        setattr(item, "deck27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck27"):
                    opp_val = getattr(item, "deck27", None)
                    
                    setattr(item, "deck27", self)
                    

    @property
    def theme24(self):
        return self.__theme24
    @theme24.setter
    def theme24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck1__theme24", None)
        self.__theme24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decks25"):
                opp_val = getattr(old_value, "decks25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decks25"):
                opp_val = getattr(value, "decks25", None)
                if opp_val is None:
                    setattr(value, "decks25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def games29(self):
        return self.__games29
    @games29.setter
    def games29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck1__games29", None)
        self.__games29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "decks28"):
                    opp_val = getattr(item, "decks28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "decks28"):
                    opp_val = getattr(item, "decks28", None)
                    
                    if opp_val is None:
                        setattr(item, "decks28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Theme1:

    pass


class Player2(ABC):

    def __init__(self, name: str, games19: set["Game2"] = None, cards20: set["Card2"] = None, avatar22: "Avatar2" = None):
        self.name = name
        self.games19 = games19 if games19 is not None else set()
        self.cards20 = cards20 if cards20 is not None else set()
        self.avatar22 = avatar22
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def avatar22(self):
        return self.__avatar22
    @avatar22.setter
    def avatar22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player2__avatar22", None)
        self.__avatar22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players23"):
                opp_val = getattr(old_value, "players23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players23"):
                opp_val = getattr(value, "players23", None)
                if opp_val is None:
                    setattr(value, "players23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cards20(self):
        return self.__cards20
    @cards20.setter
    def cards20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player2__cards20", None)
        self.__cards20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player21"):
                    opp_val = getattr(item, "player21", None)
                    
                    if opp_val == self:
                        setattr(item, "player21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player21"):
                    opp_val = getattr(item, "player21", None)
                    
                    setattr(item, "player21", self)
                    

    @property
    def games19(self):
        return self.__games19
    @games19.setter
    def games19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player2__games19", None)
        self.__games19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "players18"):
                    opp_val = getattr(item, "players18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "players18"):
                    opp_val = getattr(item, "players18", None)
                    
                    if opp_val is None:
                        setattr(item, "players18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Avatar2:

    pass


class Card2:

    def __init__(self, suit: Suit2, kind: Kind2, deck15: "Deck2" = None, player21: "Player2" = None):
        self.suit = suit
        self.kind = kind
        self.deck15 = deck15
        self.player21 = player21
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit2):
        self.__suit = suit

    @property
    def kind(self):
        return self.__kind
    @kind.setter
    def kind(self, kind: Kind2):
        self.__kind = kind

    @property
    def player21(self):
        return self.__player21
    @player21.setter
    def player21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card2__player21", None)
        self.__player21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards20"):
                opp_val = getattr(old_value, "cards20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards20"):
                opp_val = getattr(value, "cards20", None)
                if opp_val is None:
                    setattr(value, "cards20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deck15(self):
        return self.__deck15
    @deck15.setter
    def deck15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card2__deck15", None)
        self.__deck15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards14"):
                opp_val = getattr(old_value, "cards14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards14"):
                opp_val = getattr(value, "cards14", None)
                if opp_val is None:
                    setattr(value, "cards14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Game2(ABC):

    def __init__(self, name: str, decks16: set["Deck2"] = None, players18: set["Player2"] = None):
        self.name = name
        self.decks16 = decks16 if decks16 is not None else set()
        self.players18 = players18 if players18 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def players18(self):
        return self.__players18
    @players18.setter
    def players18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game2__players18", None)
        self.__players18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "games19"):
                    opp_val = getattr(item, "games19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "games19"):
                    opp_val = getattr(item, "games19", None)
                    
                    if opp_val is None:
                        setattr(item, "games19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def decks16(self):
        return self.__decks16
    @decks16.setter
    def decks16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game2__decks16", None)
        self.__decks16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "games17"):
                    opp_val = getattr(item, "games17", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "games17"):
                    opp_val = getattr(item, "games17", None)
                    
                    if opp_val is None:
                        setattr(item, "games17", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Deck2:

    pass


class Theme2:

    pass


class Player(ABC):

    def __init__(self, name: str, games7: set["Game"] = None, cards8: set["Card"] = None, avatar10: "Avatar" = None):
        self.name = name
        self.games7 = games7 if games7 is not None else set()
        self.cards8 = cards8 if cards8 is not None else set()
        self.avatar10 = avatar10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def cards8(self):
        return self.__cards8
    @cards8.setter
    def cards8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__cards8", None)
        self.__cards8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player9"):
                    opp_val = getattr(item, "player9", None)
                    
                    if opp_val == self:
                        setattr(item, "player9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player9"):
                    opp_val = getattr(item, "player9", None)
                    
                    setattr(item, "player9", self)
                    

    @property
    def avatar10(self):
        return self.__avatar10
    @avatar10.setter
    def avatar10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__avatar10", None)
        self.__avatar10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players11"):
                opp_val = getattr(old_value, "players11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players11"):
                opp_val = getattr(value, "players11", None)
                if opp_val is None:
                    setattr(value, "players11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Avatar:

    pass


class Card:

    def __init__(self, suit: Suit, kind: Kind, deck3: "Deck" = None, player9: "Player" = None):
        self.suit = suit
        self.kind = kind
        self.deck3 = deck3
        self.player9 = player9
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit):
        self.__suit = suit

    @property
    def kind(self):
        return self.__kind
    @kind.setter
    def kind(self, kind: Kind):
        self.__kind = kind

    @property
    def player9(self):
        return self.__player9
    @player9.setter
    def player9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player9", None)
        self.__player9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards8"):
                opp_val = getattr(old_value, "cards8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards8"):
                opp_val = getattr(value, "cards8", None)
                if opp_val is None:
                    setattr(value, "cards8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deck3(self):
        return self.__deck3
    @deck3.setter
    def deck3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck3", None)
        self.__deck3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards2"):
                opp_val = getattr(old_value, "cards2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards2"):
                opp_val = getattr(value, "cards2", None)
                if opp_val is None:
                    setattr(value, "cards2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Game(ABC):

    def __init__(self, name: str, decks4: set["Deck"] = None, players6: set["Player"] = None):
        self.name = name
        self.decks4 = decks4 if decks4 is not None else set()
        self.players6 = players6 if players6 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def decks4(self):
        return self.__decks4
    @decks4.setter
    def decks4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__decks4", None)
        self.__decks4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "games5"):
                    opp_val = getattr(item, "games5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "games5"):
                    opp_val = getattr(item, "games5", None)
                    
                    if opp_val is None:
                        setattr(item, "games5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

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
                    



class Deck:

    pass


class Theme:

    pass
