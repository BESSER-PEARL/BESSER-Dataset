from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class JFrame:

    pass


class BlackjackGUI:

    pass


class BlackjackDriver:

    pass


class Card:

    def __init__(self, value: int, suit: str, rank: int, blackjack1: "Blackjack" = None):
        self.value = value
        self.suit = suit
        self.rank = rank
        self.blackjack1 = blackjack1
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def blackjack1(self):
        return self.__blackjack1
    @blackjack1.setter
    def blackjack1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__blackjack1", None)
        self.__blackjack1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card0"):
                opp_val = getattr(old_value, "card0", None)
                if opp_val == self:
                    setattr(old_value, "card0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card0"):
                opp_val = getattr(value, "card0", None)
                setattr(value, "card0", self)



class Dealer:

    pass


class Player:

    def __init__(self, totalAmount: int):
        self.totalAmount = totalAmount
        
        pass
    @property
    def totalAmount(self):
        return self.__totalAmount
    @totalAmount.setter
    def totalAmount(self, totalAmount: int):
        self.__totalAmount = totalAmount



class Blackjack:

    def __init__(self, count: int, playerName: str, hand__: Card, players: int, card0: "Card" = None):
        self.count = count
        self.playerName = playerName
        self.hand__ = hand__
        self.players = players
        self.card0 = card0
        
        pass
    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def playerName(self):
        return self.__playerName
    @playerName.setter
    def playerName(self, playerName: str):
        self.__playerName = playerName

    @property
    def hand__(self):
        return self.__hand__
    @hand__.setter
    def hand__(self, hand__: Card):
        self.__hand__ = hand__

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: int):
        self.__players = players

    @property
    def card0(self):
        return self.__card0
    @card0.setter
    def card0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Blackjack__card0", None)
        self.__card0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack1"):
                opp_val = getattr(old_value, "blackjack1", None)
                if opp_val == self:
                    setattr(old_value, "blackjack1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack1"):
                opp_val = getattr(value, "blackjack1", None)
                setattr(value, "blackjack1", self)

