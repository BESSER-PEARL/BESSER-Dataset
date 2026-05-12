from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Rank(Enum):
    pass
class Suit(Enum):
    pass

############################################
# Definition of Classes
############################################










class List_Card__external:

    pass


class BlackJackMain:

    pass


class Game:

    def __init__(self, dealerCards: str, playerCards: str, deck7: "Deck" = None, blackJackMain8: "BlackJackMain" = None):
        self.dealerCards = dealerCards
        self.playerCards = playerCards
        self.deck7 = deck7
        self.blackJackMain8 = blackJackMain8
        
        pass
    @property
    def playerCards(self):
        return self.__playerCards
    @playerCards.setter
    def playerCards(self, playerCards: str):
        self.__playerCards = playerCards

    @property
    def dealerCards(self):
        return self.__dealerCards
    @dealerCards.setter
    def dealerCards(self, dealerCards: str):
        self.__dealerCards = dealerCards

    @property
    def blackJackMain8(self):
        return self.__blackJackMain8
    @blackJackMain8.setter
    def blackJackMain8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__blackJackMain8", None)
        self.__blackJackMain8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game9"):
                opp_val = getattr(old_value, "game9", None)
                if opp_val == self:
                    setattr(old_value, "game9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game9"):
                opp_val = getattr(value, "game9", None)
                setattr(value, "game9", self)

    @property
    def deck7(self):
        return self.__deck7
    @deck7.setter
    def deck7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__deck7", None)
        self.__deck7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game6"):
                opp_val = getattr(old_value, "game6", None)
                if opp_val == self:
                    setattr(old_value, "game6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game6"):
                opp_val = getattr(value, "game6", None)
                setattr(value, "game6", self)



class Player:

    def __init__(self, money: int, name: str, deck2: "Deck" = None, blackJackMain10: "BlackJackMain" = None):
        self.money = money
        self.name = name
        self.deck2 = deck2
        self.blackJackMain10 = blackJackMain10
        
        pass
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: int):
        self.__money = money

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def blackJackMain10(self):
        return self.__blackJackMain10
    @blackJackMain10.setter
    def blackJackMain10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__blackJackMain10", None)
        self.__blackJackMain10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player11"):
                opp_val = getattr(old_value, "player11", None)
                if opp_val == self:
                    setattr(old_value, "player11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player11"):
                opp_val = getattr(value, "player11", None)
                setattr(value, "player11", self)

    @property
    def deck2(self):
        return self.__deck2
    @deck2.setter
    def deck2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__deck2", None)
        self.__deck2 = value
        
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



class Deck:

    def __init__(self, deck: str, cardsDealt: str, card1: "Card" = None, player3: "Player" = None, list_Card_5: "List_Card__external" = None, game6: "Game" = None):
        self.deck = deck
        self.cardsDealt = cardsDealt
        self.card1 = card1
        self.player3 = player3
        self.list_Card_5 = list_Card_5
        self.game6 = game6
        
        pass
    @property
    def cardsDealt(self):
        return self.__cardsDealt
    @cardsDealt.setter
    def cardsDealt(self, cardsDealt: str):
        self.__cardsDealt = cardsDealt

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card1", None)
        self.__card1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck0"):
                opp_val = getattr(old_value, "deck0", None)
                if opp_val == self:
                    setattr(old_value, "deck0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck0"):
                opp_val = getattr(value, "deck0", None)
                setattr(value, "deck0", self)

    @property
    def game6(self):
        return self.__game6
    @game6.setter
    def game6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__game6", None)
        self.__game6 = value
        
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
    def list_Card_5(self):
        return self.__list_Card_5
    @list_Card_5.setter
    def list_Card_5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__list_Card_5", None)
        self.__list_Card_5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck4"):
                opp_val = getattr(old_value, "deck4", None)
                if opp_val == self:
                    setattr(old_value, "deck4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck4"):
                opp_val = getattr(value, "deck4", None)
                setattr(value, "deck4", self)

    @property
    def player3(self):
        return self.__player3
    @player3.setter
    def player3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__player3", None)
        self.__player3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck2"):
                opp_val = getattr(old_value, "deck2", None)
                if opp_val == self:
                    setattr(old_value, "deck2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck2"):
                opp_val = getattr(value, "deck2", None)
                setattr(value, "deck2", self)



class Card:

    def __init__(self, suit: Suit, rank: Rank, deck0: "Deck" = None):
        self.suit = suit
        self.rank = rank
        self.deck0 = deck0
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: Rank):
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit):
        self.__suit = suit

    @property
    def deck0(self):
        return self.__deck0
    @deck0.setter
    def deck0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck0", None)
        self.__deck0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card1"):
                opp_val = getattr(old_value, "card1", None)
                if opp_val == self:
                    setattr(old_value, "card1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card1"):
                opp_val = getattr(value, "card1", None)
                setattr(value, "card1", self)

