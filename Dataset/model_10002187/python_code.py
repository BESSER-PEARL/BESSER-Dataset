from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class War_Rank1(Enum):
    pass
class War_Suit1(Enum):
    pass
class War_Rank(Enum):
    pass
class War_Suit(Enum):
    pass

############################################
# Definition of Classes
############################################










class Iterator_Card__Interface:

    pass


class Iterable_Card__Interface:

    pass


class Comparable_Card__Interface:

    pass


class War_WarVariationWithPoints1:

    def __init__(self, logger: str, inWar: bool, logger1: str, inWar1: bool):
        self.logger = logger
        self.inWar = inWar
        self.logger1 = logger1
        self.inWar1 = inWar1
        
        pass
    @property
    def logger(self):
        return self.__logger
    @logger.setter
    def logger(self, logger: str):
        self.__logger = logger

    @property
    def inWar1(self):
        return self.__inWar1
    @inWar1.setter
    def inWar1(self, inWar1: bool):
        self.__inWar1 = inWar1

    @property
    def inWar(self):
        return self.__inWar
    @inWar.setter
    def inWar(self, inWar: bool):
        self.__inWar = inWar

    @property
    def logger1(self):
        return self.__logger1
    @logger1.setter
    def logger1(self, logger1: str):
        self.__logger1 = logger1



class War_WarVariationClassic1:

    def __init__(self, numOfRounds: int, numOfRounds1: int, player215: "War_Player1" = None, player127: "War_Player1" = None, player229: "War_Player1" = None, player133: "War_Player1" = None):
        self.numOfRounds = numOfRounds
        self.numOfRounds1 = numOfRounds1
        self.player215 = player215
        self.player127 = player127
        self.player229 = player229
        self.player133 = player133
        
        pass
    @property
    def numOfRounds1(self):
        return self.__numOfRounds1
    @numOfRounds1.setter
    def numOfRounds1(self, numOfRounds1: int):
        self.__numOfRounds1 = numOfRounds1

    @property
    def numOfRounds(self):
        return self.__numOfRounds
    @numOfRounds.setter
    def numOfRounds(self, numOfRounds: int):
        self.__numOfRounds = numOfRounds

    @property
    def player133(self):
        return self.__player133
    @player133.setter
    def player133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarVariationClassic1__player133", None)
        self.__player133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "warvariationclassic32"):
                opp_val = getattr(old_value, "warvariationclassic32", None)
                if opp_val == self:
                    setattr(old_value, "warvariationclassic32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "warvariationclassic32"):
                opp_val = getattr(value, "warvariationclassic32", None)
                setattr(value, "warvariationclassic32", self)

    @property
    def player229(self):
        return self.__player229
    @player229.setter
    def player229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarVariationClassic1__player229", None)
        self.__player229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "warvariationclassic28"):
                opp_val = getattr(old_value, "warvariationclassic28", None)
                if opp_val == self:
                    setattr(old_value, "warvariationclassic28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "warvariationclassic28"):
                opp_val = getattr(value, "warvariationclassic28", None)
                setattr(value, "warvariationclassic28", self)

    @property
    def player215(self):
        return self.__player215
    @player215.setter
    def player215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarVariationClassic1__player215", None)
        self.__player215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "warvariationclassic14"):
                opp_val = getattr(old_value, "warvariationclassic14", None)
                if opp_val == self:
                    setattr(old_value, "warvariationclassic14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "warvariationclassic14"):
                opp_val = getattr(value, "warvariationclassic14", None)
                setattr(value, "warvariationclassic14", self)

    @property
    def player127(self):
        return self.__player127
    @player127.setter
    def player127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarVariationClassic1__player127", None)
        self.__player127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "warvariationclassic26"):
                opp_val = getattr(old_value, "warvariationclassic26", None)
                if opp_val == self:
                    setattr(old_value, "warvariationclassic26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "warvariationclassic26"):
                opp_val = getattr(value, "warvariationclassic26", None)
                setattr(value, "warvariationclassic26", self)



class War_WarGameVariation1(ABC):

    def __init__(self, numOfPlayers: int, numOfPlayers1: int, players1: set["War_Player1"] = None, warLogger13: "War_GameLogger1" = None, winPile17: "War_Deck1" = None, warLogger25: "War_GameLogger1" = None, winPile31: "War_Deck1" = None, players35: set["War_Player1"] = None, deck43: "War_Deck1" = None, deck41: "War_Deck1" = None):
        self.numOfPlayers = numOfPlayers
        self.numOfPlayers1 = numOfPlayers1
        self.players1 = players1 if players1 is not None else set()
        self.warLogger13 = warLogger13
        self.winPile17 = winPile17
        self.warLogger25 = warLogger25
        self.winPile31 = winPile31
        self.players35 = players35 if players35 is not None else set()
        self.deck43 = deck43
        self.deck41 = deck41
        
        pass
    @property
    def numOfPlayers(self):
        return self.__numOfPlayers
    @numOfPlayers.setter
    def numOfPlayers(self, numOfPlayers: int):
        self.__numOfPlayers = numOfPlayers

    @property
    def numOfPlayers1(self):
        return self.__numOfPlayers1
    @numOfPlayers1.setter
    def numOfPlayers1(self, numOfPlayers1: int):
        self.__numOfPlayers1 = numOfPlayers1

    @property
    def deck43(self):
        return self.__deck43
    @deck43.setter
    def deck43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarGameVariation1__deck43", None)
        self.__deck43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wargamevariation42"):
                opp_val = getattr(old_value, "wargamevariation42", None)
                if opp_val == self:
                    setattr(old_value, "wargamevariation42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wargamevariation42"):
                opp_val = getattr(value, "wargamevariation42", None)
                setattr(value, "wargamevariation42", self)

    @property
    def players35(self):
        return self.__players35
    @players35.setter
    def players35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarGameVariation1__players35", None)
        self.__players35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wargamevariation34"):
                    opp_val = getattr(item, "wargamevariation34", None)
                    
                    if opp_val == self:
                        setattr(item, "wargamevariation34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wargamevariation34"):
                    opp_val = getattr(item, "wargamevariation34", None)
                    
                    setattr(item, "wargamevariation34", self)
                    

    @property
    def warLogger25(self):
        return self.__warLogger25
    @warLogger25.setter
    def warLogger25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarGameVariation1__warLogger25", None)
        self.__warLogger25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wargamevariation24"):
                opp_val = getattr(old_value, "wargamevariation24", None)
                if opp_val == self:
                    setattr(old_value, "wargamevariation24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wargamevariation24"):
                opp_val = getattr(value, "wargamevariation24", None)
                setattr(value, "wargamevariation24", self)

    @property
    def winPile31(self):
        return self.__winPile31
    @winPile31.setter
    def winPile31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarGameVariation1__winPile31", None)
        self.__winPile31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wargamevariation30"):
                opp_val = getattr(old_value, "wargamevariation30", None)
                if opp_val == self:
                    setattr(old_value, "wargamevariation30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wargamevariation30"):
                opp_val = getattr(value, "wargamevariation30", None)
                setattr(value, "wargamevariation30", self)

    @property
    def deck41(self):
        return self.__deck41
    @deck41.setter
    def deck41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarGameVariation1__deck41", None)
        self.__deck41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wargamevariation40"):
                opp_val = getattr(old_value, "wargamevariation40", None)
                if opp_val == self:
                    setattr(old_value, "wargamevariation40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wargamevariation40"):
                opp_val = getattr(value, "wargamevariation40", None)
                setattr(value, "wargamevariation40", self)

    @property
    def winPile17(self):
        return self.__winPile17
    @winPile17.setter
    def winPile17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarGameVariation1__winPile17", None)
        self.__winPile17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wargamevariation16"):
                opp_val = getattr(old_value, "wargamevariation16", None)
                if opp_val == self:
                    setattr(old_value, "wargamevariation16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wargamevariation16"):
                opp_val = getattr(value, "wargamevariation16", None)
                setattr(value, "wargamevariation16", self)

    @property
    def players1(self):
        return self.__players1
    @players1.setter
    def players1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarGameVariation1__players1", None)
        self.__players1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wargamevariation0"):
                    opp_val = getattr(item, "wargamevariation0", None)
                    
                    if opp_val == self:
                        setattr(item, "wargamevariation0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wargamevariation0"):
                    opp_val = getattr(item, "wargamevariation0", None)
                    
                    setattr(item, "wargamevariation0", self)
                    

    @property
    def warLogger13(self):
        return self.__warLogger13
    @warLogger13.setter
    def warLogger13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_WarGameVariation1__warLogger13", None)
        self.__warLogger13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wargamevariation12"):
                opp_val = getattr(old_value, "wargamevariation12", None)
                if opp_val == self:
                    setattr(old_value, "wargamevariation12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wargamevariation12"):
                opp_val = getattr(value, "wargamevariation12", None)
                setattr(value, "wargamevariation12", self)



class War_WarVariationWithPoints:

    pass


class War_WarVariationClassic:

    pass


class War_WarGameVariation(ABC):

    pass


class War_TwoPlayerPointPile1:

    def __init__(self, logger: str, inWar: bool, logger1: str, inWar1: bool):
        self.logger = logger
        self.inWar = inWar
        self.logger1 = logger1
        self.inWar1 = inWar1
        
        pass
    @property
    def logger(self):
        return self.__logger
    @logger.setter
    def logger(self, logger: str):
        self.__logger = logger

    @property
    def logger1(self):
        return self.__logger1
    @logger1.setter
    def logger1(self, logger1: str):
        self.__logger1 = logger1

    @property
    def inWar1(self):
        return self.__inWar1
    @inWar1.setter
    def inWar1(self, inWar1: bool):
        self.__inWar1 = inWar1

    @property
    def inWar(self):
        return self.__inWar
    @inWar.setter
    def inWar(self, inWar: bool):
        self.__inWar = inWar



class War_ThreePlayerPointPile1:

    def __init__(self, logger: str, inWar: bool, logger1: str, inWar1: bool):
        self.logger = logger
        self.inWar = inWar
        self.logger1 = logger1
        self.inWar1 = inWar1
        
        pass
    @property
    def logger(self):
        return self.__logger
    @logger.setter
    def logger(self, logger: str):
        self.__logger = logger

    @property
    def inWar(self):
        return self.__inWar
    @inWar.setter
    def inWar(self, inWar: bool):
        self.__inWar = inWar

    @property
    def inWar1(self):
        return self.__inWar1
    @inWar1.setter
    def inWar1(self, inWar1: bool):
        self.__inWar1 = inWar1

    @property
    def logger1(self):
        return self.__logger1
    @logger1.setter
    def logger1(self, logger1: str):
        self.__logger1 = logger1



class War_Player1:

    def __init__(self, score: int, name: str, score1: int, name1: str, wargamevariation0: "War_WarGameVariation1" = None, hand5: "War_Deck1" = None, warvariationclassic14: "War_WarVariationClassic1" = None, warvariationclassic26: "War_WarVariationClassic1" = None, warvariationclassic28: "War_WarVariationClassic1" = None, warvariationclassic32: "War_WarVariationClassic1" = None, wargamevariation34: "War_WarGameVariation1" = None, cardsWon37: "War_Deck1" = None, cardsWon39: "War_Deck1" = None, hand11: "War_Deck1" = None):
        self.score = score
        self.name = name
        self.score1 = score1
        self.name1 = name1
        self.wargamevariation0 = wargamevariation0
        self.hand5 = hand5
        self.warvariationclassic14 = warvariationclassic14
        self.warvariationclassic26 = warvariationclassic26
        self.warvariationclassic28 = warvariationclassic28
        self.warvariationclassic32 = warvariationclassic32
        self.wargamevariation34 = wargamevariation34
        self.cardsWon37 = cardsWon37
        self.cardsWon39 = cardsWon39
        self.hand11 = hand11
        
        pass
    @property
    def score1(self):
        return self.__score1
    @score1.setter
    def score1(self, score1: int):
        self.__score1 = score1

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def name1(self):
        return self.__name1
    @name1.setter
    def name1(self, name1: str):
        self.__name1 = name1

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def warvariationclassic26(self):
        return self.__warvariationclassic26
    @warvariationclassic26.setter
    def warvariationclassic26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__warvariationclassic26", None)
        self.__warvariationclassic26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player127"):
                opp_val = getattr(old_value, "player127", None)
                if opp_val == self:
                    setattr(old_value, "player127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player127"):
                opp_val = getattr(value, "player127", None)
                setattr(value, "player127", self)

    @property
    def warvariationclassic32(self):
        return self.__warvariationclassic32
    @warvariationclassic32.setter
    def warvariationclassic32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__warvariationclassic32", None)
        self.__warvariationclassic32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player133"):
                opp_val = getattr(old_value, "player133", None)
                if opp_val == self:
                    setattr(old_value, "player133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player133"):
                opp_val = getattr(value, "player133", None)
                setattr(value, "player133", self)

    @property
    def wargamevariation0(self):
        return self.__wargamevariation0
    @wargamevariation0.setter
    def wargamevariation0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__wargamevariation0", None)
        self.__wargamevariation0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players1"):
                opp_val = getattr(old_value, "players1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players1"):
                opp_val = getattr(value, "players1", None)
                if opp_val is None:
                    setattr(value, "players1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hand11(self):
        return self.__hand11
    @hand11.setter
    def hand11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__hand11", None)
        self.__hand11 = value
        
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

    @property
    def warvariationclassic28(self):
        return self.__warvariationclassic28
    @warvariationclassic28.setter
    def warvariationclassic28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__warvariationclassic28", None)
        self.__warvariationclassic28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player229"):
                opp_val = getattr(old_value, "player229", None)
                if opp_val == self:
                    setattr(old_value, "player229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player229"):
                opp_val = getattr(value, "player229", None)
                setattr(value, "player229", self)

    @property
    def cardsWon39(self):
        return self.__cardsWon39
    @cardsWon39.setter
    def cardsWon39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__cardsWon39", None)
        self.__cardsWon39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player38"):
                opp_val = getattr(old_value, "player38", None)
                if opp_val == self:
                    setattr(old_value, "player38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player38"):
                opp_val = getattr(value, "player38", None)
                setattr(value, "player38", self)

    @property
    def warvariationclassic14(self):
        return self.__warvariationclassic14
    @warvariationclassic14.setter
    def warvariationclassic14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__warvariationclassic14", None)
        self.__warvariationclassic14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player215"):
                opp_val = getattr(old_value, "player215", None)
                if opp_val == self:
                    setattr(old_value, "player215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player215"):
                opp_val = getattr(value, "player215", None)
                setattr(value, "player215", self)

    @property
    def cardsWon37(self):
        return self.__cardsWon37
    @cardsWon37.setter
    def cardsWon37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__cardsWon37", None)
        self.__cardsWon37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player36"):
                opp_val = getattr(old_value, "player36", None)
                if opp_val == self:
                    setattr(old_value, "player36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player36"):
                opp_val = getattr(value, "player36", None)
                setattr(value, "player36", self)

    @property
    def hand5(self):
        return self.__hand5
    @hand5.setter
    def hand5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__hand5", None)
        self.__hand5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player4"):
                opp_val = getattr(old_value, "player4", None)
                if opp_val == self:
                    setattr(old_value, "player4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player4"):
                opp_val = getattr(value, "player4", None)
                setattr(value, "player4", self)

    @property
    def wargamevariation34(self):
        return self.__wargamevariation34
    @wargamevariation34.setter
    def wargamevariation34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Player1__wargamevariation34", None)
        self.__wargamevariation34 = value
        
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



class War_PlayGame1:

    pass


class War_GameLogger1:

    def __init__(self, gameLogWriter: str, gameLogWriter1: str, wargamevariation12: "War_WarGameVariation1" = None, wargamevariation24: "War_WarGameVariation1" = None):
        self.gameLogWriter = gameLogWriter
        self.gameLogWriter1 = gameLogWriter1
        self.wargamevariation12 = wargamevariation12
        self.wargamevariation24 = wargamevariation24
        
        pass
    @property
    def gameLogWriter(self):
        return self.__gameLogWriter
    @gameLogWriter.setter
    def gameLogWriter(self, gameLogWriter: str):
        self.__gameLogWriter = gameLogWriter

    @property
    def gameLogWriter1(self):
        return self.__gameLogWriter1
    @gameLogWriter1.setter
    def gameLogWriter1(self, gameLogWriter1: str):
        self.__gameLogWriter1 = gameLogWriter1

    @property
    def wargamevariation12(self):
        return self.__wargamevariation12
    @wargamevariation12.setter
    def wargamevariation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_GameLogger1__wargamevariation12", None)
        self.__wargamevariation12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "warLogger13"):
                opp_val = getattr(old_value, "warLogger13", None)
                if opp_val == self:
                    setattr(old_value, "warLogger13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "warLogger13"):
                opp_val = getattr(value, "warLogger13", None)
                setattr(value, "warLogger13", self)

    @property
    def wargamevariation24(self):
        return self.__wargamevariation24
    @wargamevariation24.setter
    def wargamevariation24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_GameLogger1__wargamevariation24", None)
        self.__wargamevariation24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "warLogger25"):
                opp_val = getattr(old_value, "warLogger25", None)
                if opp_val == self:
                    setattr(old_value, "warLogger25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "warLogger25"):
                opp_val = getattr(value, "warLogger25", None)
                setattr(value, "warLogger25", self)



class War_DeckIterator1:

    def __init__(self, current: int, current1: int, deck7: "War_Deck1" = None, deck23: "War_Deck1" = None):
        self.current = current
        self.current1 = current1
        self.deck7 = deck7
        self.deck23 = deck23
        
        pass
    @property
    def current1(self):
        return self.__current1
    @current1.setter
    def current1(self, current1: int):
        self.__current1 = current1

    @property
    def current(self):
        return self.__current
    @current.setter
    def current(self, current: int):
        self.__current = current

    @property
    def deck7(self):
        return self.__deck7
    @deck7.setter
    def deck7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_DeckIterator1__deck7", None)
        self.__deck7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deckiterator6"):
                opp_val = getattr(old_value, "deckiterator6", None)
                if opp_val == self:
                    setattr(old_value, "deckiterator6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deckiterator6"):
                opp_val = getattr(value, "deckiterator6", None)
                setattr(value, "deckiterator6", self)

    @property
    def deck23(self):
        return self.__deck23
    @deck23.setter
    def deck23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_DeckIterator1__deck23", None)
        self.__deck23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deckiterator22"):
                opp_val = getattr(old_value, "deckiterator22", None)
                if opp_val == self:
                    setattr(old_value, "deckiterator22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deckiterator22"):
                opp_val = getattr(value, "deckiterator22", None)
                setattr(value, "deckiterator22", self)



class War_Deck1:

    def __init__(self, TOP_CARD: int, NUMERIC_CARDS_IN_SUIT: int, LOWEST_NUMERIC_VALUE: int, TOP_CARD1: int, NUMERIC_CARDS_IN_SUIT1: int, LOWEST_NUMERIC_VALUE1: int, deck3: set["War_Card1"] = None, player4: "War_Player1" = None, deckiterator6: "War_DeckIterator1" = None, wargamevariation16: "War_WarGameVariation1" = None, card19: "War_Card1" = None, card21: "War_Card1" = None, deckiterator22: "War_DeckIterator1" = None, wargamevariation30: "War_WarGameVariation1" = None, player36: "War_Player1" = None, player38: "War_Player1" = None, deck9: set["War_Card1"] = None, player10: "War_Player1" = None, wargamevariation42: "War_WarGameVariation1" = None, wargamevariation40: "War_WarGameVariation1" = None):
        self.TOP_CARD = TOP_CARD
        self.NUMERIC_CARDS_IN_SUIT = NUMERIC_CARDS_IN_SUIT
        self.LOWEST_NUMERIC_VALUE = LOWEST_NUMERIC_VALUE
        self.TOP_CARD1 = TOP_CARD1
        self.NUMERIC_CARDS_IN_SUIT1 = NUMERIC_CARDS_IN_SUIT1
        self.LOWEST_NUMERIC_VALUE1 = LOWEST_NUMERIC_VALUE1
        self.deck3 = deck3 if deck3 is not None else set()
        self.player4 = player4
        self.deckiterator6 = deckiterator6
        self.wargamevariation16 = wargamevariation16
        self.card19 = card19
        self.card21 = card21
        self.deckiterator22 = deckiterator22
        self.wargamevariation30 = wargamevariation30
        self.player36 = player36
        self.player38 = player38
        self.deck9 = deck9 if deck9 is not None else set()
        self.player10 = player10
        self.wargamevariation42 = wargamevariation42
        self.wargamevariation40 = wargamevariation40
        
        pass
    @property
    def NUMERIC_CARDS_IN_SUIT(self):
        return self.__NUMERIC_CARDS_IN_SUIT
    @NUMERIC_CARDS_IN_SUIT.setter
    def NUMERIC_CARDS_IN_SUIT(self, NUMERIC_CARDS_IN_SUIT: int):
        self.__NUMERIC_CARDS_IN_SUIT = NUMERIC_CARDS_IN_SUIT

    @property
    def TOP_CARD1(self):
        return self.__TOP_CARD1
    @TOP_CARD1.setter
    def TOP_CARD1(self, TOP_CARD1: int):
        self.__TOP_CARD1 = TOP_CARD1

    @property
    def TOP_CARD(self):
        return self.__TOP_CARD
    @TOP_CARD.setter
    def TOP_CARD(self, TOP_CARD: int):
        self.__TOP_CARD = TOP_CARD

    @property
    def NUMERIC_CARDS_IN_SUIT1(self):
        return self.__NUMERIC_CARDS_IN_SUIT1
    @NUMERIC_CARDS_IN_SUIT1.setter
    def NUMERIC_CARDS_IN_SUIT1(self, NUMERIC_CARDS_IN_SUIT1: int):
        self.__NUMERIC_CARDS_IN_SUIT1 = NUMERIC_CARDS_IN_SUIT1

    @property
    def LOWEST_NUMERIC_VALUE(self):
        return self.__LOWEST_NUMERIC_VALUE
    @LOWEST_NUMERIC_VALUE.setter
    def LOWEST_NUMERIC_VALUE(self, LOWEST_NUMERIC_VALUE: int):
        self.__LOWEST_NUMERIC_VALUE = LOWEST_NUMERIC_VALUE

    @property
    def LOWEST_NUMERIC_VALUE1(self):
        return self.__LOWEST_NUMERIC_VALUE1
    @LOWEST_NUMERIC_VALUE1.setter
    def LOWEST_NUMERIC_VALUE1(self, LOWEST_NUMERIC_VALUE1: int):
        self.__LOWEST_NUMERIC_VALUE1 = LOWEST_NUMERIC_VALUE1

    @property
    def deck3(self):
        return self.__deck3
    @deck3.setter
    def deck3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__deck3", None)
        self.__deck3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck2"):
                    opp_val = getattr(item, "deck2", None)
                    
                    if opp_val == self:
                        setattr(item, "deck2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck2"):
                    opp_val = getattr(item, "deck2", None)
                    
                    setattr(item, "deck2", self)
                    

    @property
    def player4(self):
        return self.__player4
    @player4.setter
    def player4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__player4", None)
        self.__player4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand5"):
                opp_val = getattr(old_value, "hand5", None)
                if opp_val == self:
                    setattr(old_value, "hand5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand5"):
                opp_val = getattr(value, "hand5", None)
                setattr(value, "hand5", self)

    @property
    def player36(self):
        return self.__player36
    @player36.setter
    def player36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__player36", None)
        self.__player36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cardsWon37"):
                opp_val = getattr(old_value, "cardsWon37", None)
                if opp_val == self:
                    setattr(old_value, "cardsWon37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cardsWon37"):
                opp_val = getattr(value, "cardsWon37", None)
                setattr(value, "cardsWon37", self)

    @property
    def player38(self):
        return self.__player38
    @player38.setter
    def player38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__player38", None)
        self.__player38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cardsWon39"):
                opp_val = getattr(old_value, "cardsWon39", None)
                if opp_val == self:
                    setattr(old_value, "cardsWon39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cardsWon39"):
                opp_val = getattr(value, "cardsWon39", None)
                setattr(value, "cardsWon39", self)

    @property
    def card21(self):
        return self.__card21
    @card21.setter
    def card21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__card21", None)
        self.__card21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck20"):
                opp_val = getattr(old_value, "deck20", None)
                if opp_val == self:
                    setattr(old_value, "deck20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck20"):
                opp_val = getattr(value, "deck20", None)
                setattr(value, "deck20", self)

    @property
    def wargamevariation40(self):
        return self.__wargamevariation40
    @wargamevariation40.setter
    def wargamevariation40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__wargamevariation40", None)
        self.__wargamevariation40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck41"):
                opp_val = getattr(old_value, "deck41", None)
                if opp_val == self:
                    setattr(old_value, "deck41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck41"):
                opp_val = getattr(value, "deck41", None)
                setattr(value, "deck41", self)

    @property
    def deckiterator6(self):
        return self.__deckiterator6
    @deckiterator6.setter
    def deckiterator6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__deckiterator6", None)
        self.__deckiterator6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck7"):
                opp_val = getattr(old_value, "deck7", None)
                if opp_val == self:
                    setattr(old_value, "deck7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck7"):
                opp_val = getattr(value, "deck7", None)
                setattr(value, "deck7", self)

    @property
    def player10(self):
        return self.__player10
    @player10.setter
    def player10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__player10", None)
        self.__player10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand11"):
                opp_val = getattr(old_value, "hand11", None)
                if opp_val == self:
                    setattr(old_value, "hand11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand11"):
                opp_val = getattr(value, "hand11", None)
                setattr(value, "hand11", self)

    @property
    def wargamevariation42(self):
        return self.__wargamevariation42
    @wargamevariation42.setter
    def wargamevariation42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__wargamevariation42", None)
        self.__wargamevariation42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck43"):
                opp_val = getattr(old_value, "deck43", None)
                if opp_val == self:
                    setattr(old_value, "deck43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck43"):
                opp_val = getattr(value, "deck43", None)
                setattr(value, "deck43", self)

    @property
    def deckiterator22(self):
        return self.__deckiterator22
    @deckiterator22.setter
    def deckiterator22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__deckiterator22", None)
        self.__deckiterator22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck23"):
                opp_val = getattr(old_value, "deck23", None)
                if opp_val == self:
                    setattr(old_value, "deck23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck23"):
                opp_val = getattr(value, "deck23", None)
                setattr(value, "deck23", self)

    @property
    def card19(self):
        return self.__card19
    @card19.setter
    def card19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__card19", None)
        self.__card19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck18"):
                opp_val = getattr(old_value, "deck18", None)
                if opp_val == self:
                    setattr(old_value, "deck18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck18"):
                opp_val = getattr(value, "deck18", None)
                setattr(value, "deck18", self)

    @property
    def wargamevariation16(self):
        return self.__wargamevariation16
    @wargamevariation16.setter
    def wargamevariation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__wargamevariation16", None)
        self.__wargamevariation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "winPile17"):
                opp_val = getattr(old_value, "winPile17", None)
                if opp_val == self:
                    setattr(old_value, "winPile17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "winPile17"):
                opp_val = getattr(value, "winPile17", None)
                setattr(value, "winPile17", self)

    @property
    def deck9(self):
        return self.__deck9
    @deck9.setter
    def deck9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__deck9", None)
        self.__deck9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck8"):
                    opp_val = getattr(item, "deck8", None)
                    
                    if opp_val == self:
                        setattr(item, "deck8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck8"):
                    opp_val = getattr(item, "deck8", None)
                    
                    setattr(item, "deck8", self)
                    

    @property
    def wargamevariation30(self):
        return self.__wargamevariation30
    @wargamevariation30.setter
    def wargamevariation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Deck1__wargamevariation30", None)
        self.__wargamevariation30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "winPile31"):
                opp_val = getattr(old_value, "winPile31", None)
                if opp_val == self:
                    setattr(old_value, "winPile31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "winPile31"):
                opp_val = getattr(value, "winPile31", None)
                setattr(value, "winPile31", self)



class War_ClassicTwoPlayer1:

    pass


class War_Card1:

    def __init__(self, value: int, suit: War_Suit1, rank: War_Rank1, value1: int, suit1: War_Suit1, rank1: War_Rank1, deck2: "War_Deck1" = None, deck18: "War_Deck1" = None, deck20: "War_Deck1" = None, deck8: "War_Deck1" = None):
        self.value = value
        self.suit = suit
        self.rank = rank
        self.value1 = value1
        self.suit1 = suit1
        self.rank1 = rank1
        self.deck2 = deck2
        self.deck18 = deck18
        self.deck20 = deck20
        self.deck8 = deck8
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def suit1(self):
        return self.__suit1
    @suit1.setter
    def suit1(self, suit1: War_Suit1):
        self.__suit1 = suit1

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: War_Suit1):
        self.__suit = suit

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: War_Rank1):
        self.__rank = rank

    @property
    def value1(self):
        return self.__value1
    @value1.setter
    def value1(self, value1: int):
        self.__value1 = value1

    @property
    def rank1(self):
        return self.__rank1
    @rank1.setter
    def rank1(self, rank1: War_Rank1):
        self.__rank1 = rank1

    @property
    def deck18(self):
        return self.__deck18
    @deck18.setter
    def deck18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Card1__deck18", None)
        self.__deck18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card19"):
                opp_val = getattr(old_value, "card19", None)
                if opp_val == self:
                    setattr(old_value, "card19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card19"):
                opp_val = getattr(value, "card19", None)
                setattr(value, "card19", self)

    @property
    def deck8(self):
        return self.__deck8
    @deck8.setter
    def deck8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Card1__deck8", None)
        self.__deck8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck9"):
                opp_val = getattr(old_value, "deck9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck9"):
                opp_val = getattr(value, "deck9", None)
                if opp_val is None:
                    setattr(value, "deck9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deck2(self):
        return self.__deck2
    @deck2.setter
    def deck2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Card1__deck2", None)
        self.__deck2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck3"):
                opp_val = getattr(old_value, "deck3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck3"):
                opp_val = getattr(value, "deck3", None)
                if opp_val is None:
                    setattr(value, "deck3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deck20(self):
        return self.__deck20
    @deck20.setter
    def deck20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_War_Card1__deck20", None)
        self.__deck20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card21"):
                opp_val = getattr(old_value, "card21", None)
                if opp_val == self:
                    setattr(old_value, "card21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card21"):
                opp_val = getattr(value, "card21", None)
                setattr(value, "card21", self)



class War_TwoPlayerPointPile:

    pass


class War_ThreePlayerPointPile:

    pass


class War_Player:

    pass


class War_PlayGame:

    pass


class War_GameLogger:

    pass


class War_DeckIterator:

    pass


class War_Deck:

    pass


class War_ClassicTwoPlayer:

    pass


class War_Card:

    pass
