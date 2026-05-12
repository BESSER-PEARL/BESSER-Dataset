from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suit(Enum):
    pass
class Rank(Enum):
    pass

############################################
# Definition of Classes
############################################










class genmymodelreverse_java_util_Scanner:

    pass


class Strategy_Interface:

    pass


class Stay:

    pass


class Player:

    def __init__(self, firstName: str, h11: "Hand" = None, blackjack16: "BlackJack" = None):
        self.firstName = firstName
        self.h11 = h11
        self.blackjack16 = blackjack16
        
        pass
    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def blackjack16(self):
        return self.__blackjack16
    @blackjack16.setter
    def blackjack16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__blackjack16", None)
        self.__blackjack16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p17"):
                opp_val = getattr(old_value, "p17", None)
                if opp_val == self:
                    setattr(old_value, "p17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p17"):
                opp_val = getattr(value, "p17", None)
                setattr(value, "p17", self)

    @property
    def h11(self):
        return self.__h11
    @h11.setter
    def h11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__h11", None)
        self.__h11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player10"):
                opp_val = getattr(old_value, "player10", None)
                if opp_val == self:
                    setattr(old_value, "player10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player10"):
                opp_val = getattr(value, "player10", None)
                setattr(value, "player10", self)



class Person_Interface:

    pass


class Hit:

    pass


class Hand:

    def __init__(self, startHand: int, blackjack0: "BlackJack" = None, player10: "Player" = None, blackjack2: "BlackJack" = None, hand5: set["Card"] = None, dealer22: "Dealer" = None):
        self.startHand = startHand
        self.blackjack0 = blackjack0
        self.player10 = player10
        self.blackjack2 = blackjack2
        self.hand5 = hand5 if hand5 is not None else set()
        self.dealer22 = dealer22
        
        pass
    @property
    def startHand(self):
        return self.__startHand
    @startHand.setter
    def startHand(self, startHand: int):
        self.__startHand = startHand

    @property
    def player10(self):
        return self.__player10
    @player10.setter
    def player10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__player10", None)
        self.__player10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "h11"):
                opp_val = getattr(old_value, "h11", None)
                if opp_val == self:
                    setattr(old_value, "h11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "h11"):
                opp_val = getattr(value, "h11", None)
                setattr(value, "h11", self)

    @property
    def hand5(self):
        return self.__hand5
    @hand5.setter
    def hand5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__hand5", None)
        self.__hand5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand4"):
                    opp_val = getattr(item, "hand4", None)
                    
                    if opp_val == self:
                        setattr(item, "hand4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand4"):
                    opp_val = getattr(item, "hand4", None)
                    
                    setattr(item, "hand4", self)
                    

    @property
    def dealer22(self):
        return self.__dealer22
    @dealer22.setter
    def dealer22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__dealer22", None)
        self.__dealer22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand23"):
                opp_val = getattr(old_value, "hand23", None)
                if opp_val == self:
                    setattr(old_value, "hand23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand23"):
                opp_val = getattr(value, "hand23", None)
                setattr(value, "hand23", self)

    @property
    def blackjack2(self):
        return self.__blackjack2
    @blackjack2.setter
    def blackjack2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__blackjack2", None)
        self.__blackjack2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand3"):
                opp_val = getattr(old_value, "hand3", None)
                if opp_val == self:
                    setattr(old_value, "hand3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand3"):
                opp_val = getattr(value, "hand3", None)
                setattr(value, "hand3", self)

    @property
    def blackjack0(self):
        return self.__blackjack0
    @blackjack0.setter
    def blackjack0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__blackjack0", None)
        self.__blackjack0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dHand1"):
                opp_val = getattr(old_value, "dHand1", None)
                if opp_val == self:
                    setattr(old_value, "dHand1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dHand1"):
                opp_val = getattr(value, "dHand1", None)
                setattr(value, "dHand1", self)



class Deck:

    pass


class Dealer:

    def __init__(self, firstName: str, d9: "Deck" = None, blackjack12: "BlackJack" = None, hand23: "Hand" = None):
        self.firstName = firstName
        self.d9 = d9
        self.blackjack12 = blackjack12
        self.hand23 = hand23
        
        pass
    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def d9(self):
        return self.__d9
    @d9.setter
    def d9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__d9", None)
        self.__d9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer8"):
                opp_val = getattr(old_value, "dealer8", None)
                if opp_val == self:
                    setattr(old_value, "dealer8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer8"):
                opp_val = getattr(value, "dealer8", None)
                setattr(value, "dealer8", self)

    @property
    def blackjack12(self):
        return self.__blackjack12
    @blackjack12.setter
    def blackjack12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__blackjack12", None)
        self.__blackjack12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer13"):
                opp_val = getattr(old_value, "dealer13", None)
                if opp_val == self:
                    setattr(old_value, "dealer13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer13"):
                opp_val = getattr(value, "dealer13", None)
                setattr(value, "dealer13", self)

    @property
    def hand23(self):
        return self.__hand23
    @hand23.setter
    def hand23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__hand23", None)
        self.__hand23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer22"):
                opp_val = getattr(old_value, "dealer22", None)
                if opp_val == self:
                    setattr(old_value, "dealer22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer22"):
                opp_val = getattr(value, "dealer22", None)
                setattr(value, "dealer22", self)



class Context:

    pass


class Card:

    def __init__(self, suit: Suit, rank: Rank, hand4: "Hand" = None, deck20: "Deck" = None):
        self.suit = suit
        self.rank = rank
        self.hand4 = hand4
        self.deck20 = deck20
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit):
        self.__suit = suit

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: Rank):
        self.__rank = rank

    @property
    def deck20(self):
        return self.__deck20
    @deck20.setter
    def deck20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck20", None)
        self.__deck20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck21"):
                opp_val = getattr(old_value, "deck21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck21"):
                opp_val = getattr(value, "deck21", None)
                if opp_val is None:
                    setattr(value, "deck21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hand4(self):
        return self.__hand4
    @hand4.setter
    def hand4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__hand4", None)
        self.__hand4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand5"):
                opp_val = getattr(old_value, "hand5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand5"):
                opp_val = getattr(value, "hand5", None)
                if opp_val is None:
                    setattr(value, "hand5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class T2:

    pass


class T:

    pass


class BlackJack:

    def __init__(self, scan: genmymodelreverse_java_util_Scanner, dHand1: "Hand" = None, d7: "Deck" = None, dealer13: "Dealer" = None, p17: "Player" = None, hand3: "Hand" = None):
        self.scan = scan
        self.dHand1 = dHand1
        self.d7 = d7
        self.dealer13 = dealer13
        self.p17 = p17
        self.hand3 = hand3
        
        pass
    @property
    def scan(self):
        return self.__scan
    @scan.setter
    def scan(self, scan: genmymodelreverse_java_util_Scanner):
        self.__scan = scan

    @property
    def d7(self):
        return self.__d7
    @d7.setter
    def d7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack__d7", None)
        self.__d7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack6"):
                opp_val = getattr(old_value, "blackjack6", None)
                if opp_val == self:
                    setattr(old_value, "blackjack6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack6"):
                opp_val = getattr(value, "blackjack6", None)
                setattr(value, "blackjack6", self)

    @property
    def p17(self):
        return self.__p17
    @p17.setter
    def p17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack__p17", None)
        self.__p17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack16"):
                opp_val = getattr(old_value, "blackjack16", None)
                if opp_val == self:
                    setattr(old_value, "blackjack16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack16"):
                opp_val = getattr(value, "blackjack16", None)
                setattr(value, "blackjack16", self)

    @property
    def dHand1(self):
        return self.__dHand1
    @dHand1.setter
    def dHand1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack__dHand1", None)
        self.__dHand1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack0"):
                opp_val = getattr(old_value, "blackjack0", None)
                if opp_val == self:
                    setattr(old_value, "blackjack0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack0"):
                opp_val = getattr(value, "blackjack0", None)
                setattr(value, "blackjack0", self)

    @property
    def hand3(self):
        return self.__hand3
    @hand3.setter
    def hand3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack__hand3", None)
        self.__hand3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack2"):
                opp_val = getattr(old_value, "blackjack2", None)
                if opp_val == self:
                    setattr(old_value, "blackjack2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack2"):
                opp_val = getattr(value, "blackjack2", None)
                setattr(value, "blackjack2", self)

    @property
    def dealer13(self):
        return self.__dealer13
    @dealer13.setter
    def dealer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack__dealer13", None)
        self.__dealer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack12"):
                opp_val = getattr(old_value, "blackjack12", None)
                if opp_val == self:
                    setattr(old_value, "blackjack12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack12"):
                opp_val = getattr(value, "blackjack12", None)
                setattr(value, "blackjack12", self)

