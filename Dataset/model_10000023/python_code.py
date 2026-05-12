from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class en(Enum):
    pass
class Suit(Enum):
    pass
class Rank(Enum):
    pass
class en2(Enum):
    pass

############################################
# Definition of Classes
############################################







class Winner_UseCase:

    pass


class War_UseCase:

    pass


class Play_UseCase:

    pass


class Player2_Actor:

    pass


class Player1_Actor:

    pass





class Play:

    def __init__(self, Score: int, removedCard: int, players28: "Players" = None, playerTwo10: "playerTwo_external" = None, playerOne12: "playerOne_external" = None, card14: "Card_Interface" = None, deck17: "Deck" = None):
        self.Score = Score
        self.removedCard = removedCard
        self.players28 = players28
        self.playerTwo10 = playerTwo10
        self.playerOne12 = playerOne12
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
        old_value = getattr(self, f"_Play__card14", None)
        self.__card14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "play15"):
                opp_val = getattr(old_value, "play15", None)
                if opp_val == self:
                    setattr(old_value, "play15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "play15"):
                opp_val = getattr(value, "play15", None)
                setattr(value, "play15", self)

    @property
    def playerTwo10(self):
        return self.__playerTwo10
    @playerTwo10.setter
    def playerTwo10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Play__playerTwo10", None)
        self.__playerTwo10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "play11"):
                opp_val = getattr(old_value, "play11", None)
                if opp_val == self:
                    setattr(old_value, "play11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "play11"):
                opp_val = getattr(value, "play11", None)
                setattr(value, "play11", self)

    @property
    def deck17(self):
        return self.__deck17
    @deck17.setter
    def deck17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Play__deck17", None)
        self.__deck17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "play16"):
                opp_val = getattr(old_value, "play16", None)
                if opp_val == self:
                    setattr(old_value, "play16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "play16"):
                opp_val = getattr(value, "play16", None)
                setattr(value, "play16", self)

    @property
    def players28(self):
        return self.__players28
    @players28.setter
    def players28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Play__players28", None)
        self.__players28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "play9"):
                opp_val = getattr(old_value, "play9", None)
                if opp_val == self:
                    setattr(old_value, "play9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "play9"):
                opp_val = getattr(value, "play9", None)
                setattr(value, "play9", self)

    @property
    def playerOne12(self):
        return self.__playerOne12
    @playerOne12.setter
    def playerOne12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Play__playerOne12", None)
        self.__playerOne12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "play13"):
                opp_val = getattr(old_value, "play13", None)
                if opp_val == self:
                    setattr(old_value, "play13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "play13"):
                opp_val = getattr(value, "play13", None)
                setattr(value, "play13", self)



class Players:

    def __init__(self, Player1: Card_Interface, Player2: Card_Interface, wAR5: "WAR" = None, wAR6: "WAR" = None, play9: "Play" = None):
        self.Player1 = Player1
        self.Player2 = Player2
        self.wAR5 = wAR5
        self.wAR6 = wAR6
        self.play9 = play9
        
        pass
    @property
    def Player2(self):
        return self.__Player2
    @Player2.setter
    def Player2(self, Player2: Card_Interface):
        self.__Player2 = Player2

    @property
    def Player1(self):
        return self.__Player1
    @Player1.setter
    def Player1(self, Player1: Card_Interface):
        self.__Player1 = Player1

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
    def play9(self):
        return self.__play9
    @play9.setter
    def play9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players__play9", None)
        self.__play9 = value
        
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



class Card_Interface:

    pass


class Deck:

    def __init__(self, topcard: int, draw__: str, shuffle__: str, deck__: Deck, isEmpty__: bool, wAR0: "WAR" = None, card2: "Card_Interface" = None, play16: "Play" = None):
        self.topcard = topcard
        self.draw__ = draw__
        self.shuffle__ = shuffle__
        self.deck__ = deck__
        self.isEmpty__ = isEmpty__
        self.wAR0 = wAR0
        self.card2 = card2
        self.play16 = play16
        
        pass
    @property
    def isEmpty__(self):
        return self.__isEmpty__
    @isEmpty__.setter
    def isEmpty__(self, isEmpty__: bool):
        self.__isEmpty__ = isEmpty__

    @property
    def topcard(self):
        return self.__topcard
    @topcard.setter
    def topcard(self, topcard: int):
        self.__topcard = topcard

    @property
    def draw__(self):
        return self.__draw__
    @draw__.setter
    def draw__(self, draw__: str):
        self.__draw__ = draw__

    @property
    def shuffle__(self):
        return self.__shuffle__
    @shuffle__.setter
    def shuffle__(self, shuffle__: str):
        self.__shuffle__ = shuffle__

    @property
    def deck__(self):
        return self.__deck__
    @deck__.setter
    def deck__(self, deck__: Deck):
        self.__deck__ = deck__

    @property
    def play16(self):
        return self.__play16
    @play16.setter
    def play16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__play16", None)
        self.__play16 = value
        
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


class playerOne_external:

    pass


class playerTwo_external:

    pass


class Play_UseCase1:

    pass


class War_UseCase1:

    pass
