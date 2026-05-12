from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Blackjack:

    def __init__(self, cards: Cards, players: str, dealer: Player, player5: "Player" = None):
        self.cards = cards
        self.players = players
        self.dealer = dealer
        self.player5 = player5
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Cards):
        self.__cards = cards

    @property
    def dealer(self):
        return self.__dealer
    @dealer.setter
    def dealer(self, dealer: Player):
        self.__dealer = dealer

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

    @property
    def player5(self):
        return self.__player5
    @player5.setter
    def player5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Blackjack__player5", None)
        self.__player5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack4"):
                opp_val = getattr(old_value, "blackjack4", None)
                if opp_val == self:
                    setattr(old_value, "blackjack4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack4"):
                opp_val = getattr(value, "blackjack4", None)
                setattr(value, "blackjack4", self)



class Player:

    def __init__(self, name: str, hand: str, card3: "Card" = None, blackjack4: "Blackjack" = None):
        self.name = name
        self.hand = hand
        self.card3 = card3
        self.blackjack4 = blackjack4
        
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
    def card3(self):
        return self.__card3
    @card3.setter
    def card3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__card3", None)
        self.__card3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player2"):
                opp_val = getattr(old_value, "player2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player2"):
                opp_val = getattr(value, "player2", None)
                if opp_val is None:
                    setattr(value, "player2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def blackjack4(self):
        return self.__blackjack4
    @blackjack4.setter
    def blackjack4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__blackjack4", None)
        self.__blackjack4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player5"):
                opp_val = getattr(old_value, "player5", None)
                if opp_val == self:
                    setattr(old_value, "player5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player5"):
                opp_val = getattr(value, "player5", None)
                setattr(value, "player5", self)



class Card:

    def __init__(self, value_dict: str, cards0: "Cards" = None, player2: set["Player"] = None):
        self.value_dict = value_dict
        self.cards0 = cards0
        self.player2 = player2 if player2 is not None else set()
        
        pass
    @property
    def value_dict(self):
        return self.__value_dict
    @value_dict.setter
    def value_dict(self, value_dict: str):
        self.__value_dict = value_dict

    @property
    def cards0(self):
        return self.__cards0
    @cards0.setter
    def cards0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__cards0", None)
        self.__cards0 = value
        
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

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player2", None)
        self.__player2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "card3"):
                    opp_val = getattr(item, "card3", None)
                    
                    if opp_val == self:
                        setattr(item, "card3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "card3"):
                    opp_val = getattr(item, "card3", None)
                    
                    setattr(item, "card3", self)
                    



class Cards:

    def __init__(self, color: str, number: str, card1: "Card" = None):
        self.color = color
        self.number = number
        self.card1 = card1
        
        pass
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards__card1", None)
        self.__card1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards0"):
                opp_val = getattr(old_value, "cards0", None)
                if opp_val == self:
                    setattr(old_value, "cards0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards0"):
                opp_val = getattr(value, "cards0", None)
                setattr(value, "cards0", self)

