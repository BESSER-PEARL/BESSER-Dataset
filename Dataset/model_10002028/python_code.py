from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class Cards_external:

    pass


class Human_Player_external:

    pass


class Interface_Interface:

    pass


class Business_Owner:

    def __init__(self, _Card_cards_5_: int, cards5: "Cards_external" = None):
        self._Card_cards_5_ = _Card_cards_5_
        self.cards5 = cards5
        
        pass
    @property
    def _Card_cards_5_(self):
        return self.___Card_cards_5_
    @_Card_cards_5_.setter
    def _Card_cards_5_(self, _Card_cards_5_: int):
        self.___Card_cards_5_ = _Card_cards_5_

    @property
    def cards5(self):
        return self.__cards5
    @cards5.setter
    def cards5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Business_Owner__cards5", None)
        self.__cards5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "make_up_possible_hand4"):
                opp_val = getattr(old_value, "make_up_possible_hand4", None)
                if opp_val == self:
                    setattr(old_value, "make_up_possible_hand4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "make_up_possible_hand4"):
                opp_val = getattr(value, "make_up_possible_hand4", None)
                setattr(value, "make_up_possible_hand4", self)



class Banker:

    def __init__(self, _Card_cards_52_: int):
        self._Card_cards_52_ = _Card_cards_52_
        
        pass
    @property
    def _Card_cards_52_(self):
        return self.___Card_cards_52_
    @_Card_cards_52_.setter
    def _Card_cards_52_(self, _Card_cards_52_: int):
        self.___Card_cards_52_ = _Card_cards_52_



class ComputerPlayer:

    def __init__(self, difficulty: int, player1: "Creator" = None):
        self.difficulty = difficulty
        self.player1 = player1
        
        pass
    @property
    def difficulty(self):
        return self.__difficulty
    @difficulty.setter
    def difficulty(self, difficulty: int):
        self.__difficulty = difficulty

    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ComputerPlayer__player1", None)
        self.__player1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "computerPlayer0"):
                opp_val = getattr(old_value, "computerPlayer0", None)
                if opp_val == self:
                    setattr(old_value, "computerPlayer0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "computerPlayer0"):
                opp_val = getattr(value, "computerPlayer0", None)
                setattr(value, "computerPlayer0", self)



class Creator:

    def __init__(self, name: str, money: float, currentBet: float, folded: bool, computerPlayer0: "ComputerPlayer" = None, human_Player2: "Human_Player_external" = None):
        self.name = name
        self.money = money
        self.currentBet = currentBet
        self.folded = folded
        self.computerPlayer0 = computerPlayer0
        self.human_Player2 = human_Player2
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def currentBet(self):
        return self.__currentBet
    @currentBet.setter
    def currentBet(self, currentBet: float):
        self.__currentBet = currentBet

    @property
    def folded(self):
        return self.__folded
    @folded.setter
    def folded(self, folded: bool):
        self.__folded = folded

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: float):
        self.__money = money

    @property
    def computerPlayer0(self):
        return self.__computerPlayer0
    @computerPlayer0.setter
    def computerPlayer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Creator__computerPlayer0", None)
        self.__computerPlayer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player1"):
                opp_val = getattr(old_value, "player1", None)
                if opp_val == self:
                    setattr(old_value, "player1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player1"):
                opp_val = getattr(value, "player1", None)
                setattr(value, "player1", self)

    @property
    def human_Player2(self):
        return self.__human_Player2
    @human_Player2.setter
    def human_Player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Creator__human_Player2", None)
        self.__human_Player2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player3"):
                opp_val = getattr(old_value, "player3", None)
                if opp_val == self:
                    setattr(old_value, "player3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player3"):
                opp_val = getattr(value, "player3", None)
                setattr(value, "player3", self)

