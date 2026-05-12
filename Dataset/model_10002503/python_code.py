from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Driver:

    def __init__(self, Score: int, removedCard: int, Players8: "Players" = None, card10: "Card_Interface" = None, deck13: "Deck" = None):
        self.Score = Score
        self.removedCard = removedCard
        self.Players8 = Players8
        self.card10 = card10
        self.deck13 = deck13
        
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
    def card10(self):
        return self.__card10
    @card10.setter
    def card10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Driver__card10", None)
        self.__card10 = value
        
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
    def deck13(self):
        return self.__deck13
    @deck13.setter
    def deck13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Driver__deck13", None)
        self.__deck13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "function12"):
                opp_val = getattr(old_value, "function12", None)
                if opp_val == self:
                    setattr(old_value, "function12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "function12"):
                opp_val = getattr(value, "function12", None)
                setattr(value, "function12", self)

    @property
    def Players8(self):
        return self.__Players8
    @Players8.setter
    def Players8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Driver__Players8", None)
        self.__Players8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver9"):
                opp_val = getattr(old_value, "driver9", None)
                if opp_val == self:
                    setattr(old_value, "driver9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver9"):
                opp_val = getattr(value, "driver9", None)
                setattr(value, "driver9", self)



class T:

    pass


class Players:

    def __init__(self, Player1: Card_Interface, Player2: Card_Interface, Planet: Card_Interface, driver9: "Driver" = None, Strategy1___25: "Strategy1___Strategy2" = None, Strategy1_26: "Strategy1___Strategy2" = None):
        self.Player1 = Player1
        self.Player2 = Player2
        self.Planet = Planet
        self.driver9 = driver9
        self.Strategy1___25 = Strategy1___25
        self.Strategy1_26 = Strategy1_26
        
        pass
    @property
    def Player2(self):
        return self.__Player2
    @Player2.setter
    def Player2(self, Player2: Card_Interface):
        self.__Player2 = Player2

    @property
    def Planet(self):
        return self.__Planet
    @Planet.setter
    def Planet(self, Planet: Card_Interface):
        self.__Planet = Planet

    @property
    def Player1(self):
        return self.__Player1
    @Player1.setter
    def Player1(self, Player1: Card_Interface):
        self.__Player1 = Player1

    @property
    def driver9(self):
        return self.__driver9
    @driver9.setter
    def driver9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players__driver9", None)
        self.__driver9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Players8"):
                opp_val = getattr(old_value, "Players8", None)
                if opp_val == self:
                    setattr(old_value, "Players8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Players8"):
                opp_val = getattr(value, "Players8", None)
                setattr(value, "Players8", self)

    @property
    def Strategy1___25(self):
        return self.__Strategy1___25
    @Strategy1___25.setter
    def Strategy1___25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players__Strategy1___25", None)
        self.__Strategy1___25 = value
        
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
    def Strategy1_26(self):
        return self.__Strategy1_26
    @Strategy1_26.setter
    def Strategy1_26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players__Strategy1_26", None)
        self.__Strategy1_26 = value
        
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



class Card_Interface:

    pass


class Deck:

    def __init__(self, shuffle__: str, deck__: Deck, isEmpty__: bool, function12: "Driver" = None, Strategy1_20: "Strategy1___Strategy2" = None, card2: "Card_Interface" = None):
        self.shuffle__ = shuffle__
        self.deck__ = deck__
        self.isEmpty__ = isEmpty__
        self.function12 = function12
        self.Strategy1_20 = Strategy1_20
        self.card2 = card2
        
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
    def shuffle__(self):
        return self.__shuffle__
    @shuffle__.setter
    def shuffle__(self, shuffle__: str):
        self.__shuffle__ = shuffle__

    @property
    def function12(self):
        return self.__function12
    @function12.setter
    def function12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__function12", None)
        self.__function12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck13"):
                opp_val = getattr(old_value, "deck13", None)
                if opp_val == self:
                    setattr(old_value, "deck13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck13"):
                opp_val = getattr(value, "deck13", None)
                setattr(value, "deck13", self)

    @property
    def Strategy1_20(self):
        return self.__Strategy1_20
    @Strategy1_20.setter
    def Strategy1_20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__Strategy1_20", None)
        self.__Strategy1_20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Strategy1_21"):
                opp_val = getattr(old_value, "Strategy1_21", None)
                if opp_val == self:
                    setattr(old_value, "Strategy1_21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Strategy1_21"):
                opp_val = getattr(value, "Strategy1_21", None)
                setattr(value, "Strategy1_21", self)

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



class Strategy1___Strategy2:

    pass
