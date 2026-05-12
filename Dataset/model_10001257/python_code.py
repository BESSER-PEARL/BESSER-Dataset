from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suit(Enum):
    pass
class Rank(Enum):
    pass
class Color(Enum):
    pass

############################################
# Definition of Classes
############################################










class Session:

    def __init__(self, id: int, players: str, cardDeck: str, discardPile: str, humanTurn: bool, humanPointer: int, currentPlayerPointer: int, gameStatus: str, gameStatusCode: int, card2: "Card" = None, player4: "Player" = None):
        self.id = id
        self.players = players
        self.cardDeck = cardDeck
        self.discardPile = discardPile
        self.humanTurn = humanTurn
        self.humanPointer = humanPointer
        self.currentPlayerPointer = currentPlayerPointer
        self.gameStatus = gameStatus
        self.gameStatusCode = gameStatusCode
        self.card2 = card2
        self.player4 = player4
        
        pass
    @property
    def currentPlayerPointer(self):
        return self.__currentPlayerPointer
    @currentPlayerPointer.setter
    def currentPlayerPointer(self, currentPlayerPointer: int):
        self.__currentPlayerPointer = currentPlayerPointer

    @property
    def gameStatus(self):
        return self.__gameStatus
    @gameStatus.setter
    def gameStatus(self, gameStatus: str):
        self.__gameStatus = gameStatus

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

    @property
    def humanPointer(self):
        return self.__humanPointer
    @humanPointer.setter
    def humanPointer(self, humanPointer: int):
        self.__humanPointer = humanPointer

    @property
    def cardDeck(self):
        return self.__cardDeck
    @cardDeck.setter
    def cardDeck(self, cardDeck: str):
        self.__cardDeck = cardDeck

    @property
    def discardPile(self):
        return self.__discardPile
    @discardPile.setter
    def discardPile(self, discardPile: str):
        self.__discardPile = discardPile

    @property
    def gameStatusCode(self):
        return self.__gameStatusCode
    @gameStatusCode.setter
    def gameStatusCode(self, gameStatusCode: int):
        self.__gameStatusCode = gameStatusCode

    @property
    def humanTurn(self):
        return self.__humanTurn
    @humanTurn.setter
    def humanTurn(self, humanTurn: bool):
        self.__humanTurn = humanTurn

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def card2(self):
        return self.__card2
    @card2.setter
    def card2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Session__card2", None)
        self.__card2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "session3"):
                opp_val = getattr(old_value, "session3", None)
                if opp_val == self:
                    setattr(old_value, "session3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "session3"):
                opp_val = getattr(value, "session3", None)
                setattr(value, "session3", self)

    @property
    def player4(self):
        return self.__player4
    @player4.setter
    def player4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Session__player4", None)
        self.__player4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "session5"):
                opp_val = getattr(old_value, "session5", None)
                if opp_val == self:
                    setattr(old_value, "session5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "session5"):
                opp_val = getattr(value, "session5", None)
                setattr(value, "session5", self)



class Card:

    def __init__(self, suit: Suit, rank: Rank, color: Color, player1: "Player" = None, session3: "Session" = None):
        self.suit = suit
        self.rank = rank
        self.color = color
        self.player1 = player1
        self.session3 = session3
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit):
        self.__suit = suit

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: Color):
        self.__color = color

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: Rank):
        self.__rank = rank

    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player1", None)
        self.__player1 = value
        
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

    @property
    def session3(self):
        return self.__session3
    @session3.setter
    def session3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__session3", None)
        self.__session3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card2"):
                opp_val = getattr(old_value, "card2", None)
                if opp_val == self:
                    setattr(old_value, "card2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card2"):
                opp_val = getattr(value, "card2", None)
                setattr(value, "card2", self)



class Player(ABC):

    def __init__(self, name: str, hand: Card, id: int, cards0: set["Card"] = None, session5: "Session" = None):
        self.name = name
        self.hand = hand
        self.id = id
        self.cards0 = cards0 if cards0 is not None else set()
        self.session5 = session5
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Card):
        self.__hand = hand

    @property
    def session5(self):
        return self.__session5
    @session5.setter
    def session5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__session5", None)
        self.__session5 = value
        
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
    def cards0(self):
        return self.__cards0
    @cards0.setter
    def cards0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__cards0", None)
        self.__cards0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player1"):
                    opp_val = getattr(item, "player1", None)
                    
                    if opp_val == self:
                        setattr(item, "player1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player1"):
                    opp_val = getattr(item, "player1", None)
                    
                    setattr(item, "player1", self)
                    

