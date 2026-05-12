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
class en2(Enum):
    pass
class en(Enum):
    pass

############################################
# Definition of Classes
############################################










class PlayerOne_external:

    pass


class PlayerTwo_external:

    pass


class Function:

    def __init__(self, Score: int, removedCard: int, players28: "Players" = None, playerCPU10: "PlayerTwo_external" = None, playerUser12: "PlayerOne_external" = None, card14: "Card_Interface" = None, deck17: "Deck" = None):
        self.Score = Score
        self.removedCard = removedCard
        self.players28 = players28
        self.playerCPU10 = playerCPU10
        self.playerUser12 = playerUser12
        self.card14 = card14
        self.deck17 = deck17
        
        pass
    @property
    def Score(self):
        return self.__Score
    @Score.setter
    def Score(self, Score: int):
        self.__Score = Score

    @property
    def removedCard(self):
        return self.__removedCard
    @removedCard.setter
    def removedCard(self, removedCard: int):
        self.__removedCard = removedCard

    @property
    def card14(self):
        return self.__card14
    @card14.setter
    def card14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Function__card14", None)
        self.__card14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "function15"):
                opp_val = getattr(old_value, "function15", None)
                if opp_val == self:
                    setattr(old_value, "function15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "function15"):
                opp_val = getattr(value, "function15", None)
                setattr(value, "function15", self)

    @property
    def playerCPU10(self):
        return self.__playerCPU10
    @playerCPU10.setter
    def playerCPU10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Function__playerCPU10", None)
        self.__playerCPU10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "function11"):
                opp_val = getattr(old_value, "function11", None)
                if opp_val == self:
                    setattr(old_value, "function11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "function11"):
                opp_val = getattr(value, "function11", None)
                setattr(value, "function11", self)

    @property
    def players28(self):
        return self.__players28
    @players28.setter
    def players28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Function__players28", None)
        self.__players28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "function9"):
                opp_val = getattr(old_value, "function9", None)
                if opp_val == self:
                    setattr(old_value, "function9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "function9"):
                opp_val = getattr(value, "function9", None)
                setattr(value, "function9", self)

    @property
    def deck17(self):
        return self.__deck17
    @deck17.setter
    def deck17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Function__deck17", None)
        self.__deck17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "function16"):
                opp_val = getattr(old_value, "function16", None)
                if opp_val == self:
                    setattr(old_value, "function16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "function16"):
                opp_val = getattr(value, "function16", None)
                setattr(value, "function16", self)

    @property
    def playerUser12(self):
        return self.__playerUser12
    @playerUser12.setter
    def playerUser12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Function__playerUser12", None)
        self.__playerUser12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "function13"):
                opp_val = getattr(old_value, "function13", None)
                if opp_val == self:
                    setattr(old_value, "function13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "function13"):
                opp_val = getattr(value, "function13", None)
                setattr(value, "function13", self)



class Players:

    def __init__(self, Player1: Card_Interface, Player2: Card_Interface, wAR5: "WAR" = None, wAR6: "WAR" = None, function9: "Function" = None):
        self.Player1 = Player1
        self.Player2 = Player2
        self.wAR5 = wAR5
        self.wAR6 = wAR6
        self.function9 = function9
        
        pass
    @property
    def Player1(self):
        return self.__Player1
    @Player1.setter
    def Player1(self, Player1: Card_Interface):
        self.__Player1 = Player1

    @property
    def Player2(self):
        return self.__Player2
    @Player2.setter
    def Player2(self, Player2: Card_Interface):
        self.__Player2 = Player2

    @property
    def wAR6(self):
        return self.__wAR6
    @wAR6.setter
    def wAR6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players__wAR6", None)
        self.__wAR6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players7"):
                opp_val = getattr(old_value, "players7", None)
                if opp_val == self:
                    setattr(old_value, "players7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players7"):
                opp_val = getattr(value, "players7", None)
                setattr(value, "players7", self)

    @property
    def wAR5(self):
        return self.__wAR5
    @wAR5.setter
    def wAR5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players__wAR5", None)
        self.__wAR5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players4"):
                opp_val = getattr(old_value, "players4", None)
                if opp_val == self:
                    setattr(old_value, "players4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players4"):
                opp_val = getattr(value, "players4", None)
                setattr(value, "players4", self)

    @property
    def function9(self):
        return self.__function9
    @function9.setter
    def function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players__function9", None)
        self.__function9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players28"):
                opp_val = getattr(old_value, "players28", None)
                if opp_val == self:
                    setattr(old_value, "players28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players28"):
                opp_val = getattr(value, "players28", None)
                setattr(value, "players28", self)



class Card_Interface:

    pass


class Deck:

    def __init__(self, topcard: int, draw__: str, shuffle__: str, deck__: Deck, isEmpty__: bool, card2: "Card_Interface" = None, wAR0: "WAR" = None, function16: "Function" = None):
        self.topcard = topcard
        self.draw__ = draw__
        self.shuffle__ = shuffle__
        self.deck__ = deck__
        self.isEmpty__ = isEmpty__
        self.card2 = card2
        self.wAR0 = wAR0
        self.function16 = function16
        
        pass
    @property
    def isEmpty__(self):
        return self.__isEmpty__
    @isEmpty__.setter
    def isEmpty__(self, isEmpty__: bool):
        self.__isEmpty__ = isEmpty__

    @property
    def deck__(self):
        return self.__deck__
    @deck__.setter
    def deck__(self, deck__: Deck):
        self.__deck__ = deck__

    @property
    def topcard(self):
        return self.__topcard
    @topcard.setter
    def topcard(self, topcard: int):
        self.__topcard = topcard

    @property
    def shuffle__(self):
        return self.__shuffle__
    @shuffle__.setter
    def shuffle__(self, shuffle__: str):
        self.__shuffle__ = shuffle__

    @property
    def draw__(self):
        return self.__draw__
    @draw__.setter
    def draw__(self, draw__: str):
        self.__draw__ = draw__

    @property
    def function16(self):
        return self.__function16
    @function16.setter
    def function16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__function16", None)
        self.__function16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck17"):
                opp_val = getattr(old_value, "deck17", None)
                if opp_val == self:
                    setattr(old_value, "deck17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck17"):
                opp_val = getattr(value, "deck17", None)
                setattr(value, "deck17", self)

    @property
    def wAR0(self):
        return self.__wAR0
    @wAR0.setter
    def wAR0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__wAR0", None)
        self.__wAR0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck1"):
                opp_val = getattr(old_value, "deck1", None)
                if opp_val == self:
                    setattr(old_value, "deck1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck1"):
                opp_val = getattr(value, "deck1", None)
                setattr(value, "deck1", self)

    @property
    def card2(self):
        return self.__card2
    @card2.setter
    def card2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card2", None)
        self.__card2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck3"):
                opp_val = getattr(old_value, "deck3", None)
                if opp_val == self:
                    setattr(old_value, "deck3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck3"):
                opp_val = getattr(value, "deck3", None)
                setattr(value, "deck3", self)



class WAR:

    pass
