from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################







class UseCase_UseCase:

    pass


class User_Actor:

    pass





class JButton:

    pass


class Card:

    def __init__(self, name: str, avatar: str, valueSoft: str, valueHard: str, suit: str, rank: str, Count: int, hand11: "Hand" = None, deck13: "Deck" = None):
        self.name = name
        self.avatar = avatar
        self.valueSoft = valueSoft
        self.valueHard = valueHard
        self.suit = suit
        self.rank = rank
        self.Count = Count
        self.hand11 = hand11
        self.deck13 = deck13
        
        pass
    @property
    def Count(self):
        return self.__Count
    @Count.setter
    def Count(self, Count: int):
        self.__Count = Count

    @property
    def avatar(self):
        return self.__avatar
    @avatar.setter
    def avatar(self, avatar: str):
        self.__avatar = avatar

    @property
    def valueSoft(self):
        return self.__valueSoft
    @valueSoft.setter
    def valueSoft(self, valueSoft: str):
        self.__valueSoft = valueSoft

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def valueHard(self):
        return self.__valueHard
    @valueHard.setter
    def valueHard(self, valueHard: str):
        self.__valueHard = valueHard

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

    @property
    def deck13(self):
        return self.__deck13
    @deck13.setter
    def deck13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck13", None)
        self.__deck13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card12"):
                opp_val = getattr(old_value, "card12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card12"):
                opp_val = getattr(value, "card12", None)
                if opp_val is None:
                    setattr(value, "card12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hand11(self):
        return self.__hand11
    @hand11.setter
    def hand11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__hand11", None)
        self.__hand11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card10"):
                opp_val = getattr(old_value, "card10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card10"):
                opp_val = getattr(value, "card10", None)
                if opp_val is None:
                    setattr(value, "card10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Hand:

    def __init__(self, cards: Card, total: int, dealer7: "Dealer" = None, player9: "Player" = None, card10: set["Card"] = None):
        self.cards = cards
        self.total = total
        self.dealer7 = dealer7
        self.player9 = player9
        self.card10 = card10 if card10 is not None else set()
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Card):
        self.__cards = cards

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: int):
        self.__total = total

    @property
    def card10(self):
        return self.__card10
    @card10.setter
    def card10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__card10", None)
        self.__card10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand11"):
                    opp_val = getattr(item, "hand11", None)
                    
                    if opp_val == self:
                        setattr(item, "hand11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand11"):
                    opp_val = getattr(item, "hand11", None)
                    
                    setattr(item, "hand11", self)
                    

    @property
    def dealer7(self):
        return self.__dealer7
    @dealer7.setter
    def dealer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__dealer7", None)
        self.__dealer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand6"):
                opp_val = getattr(old_value, "hand6", None)
                if opp_val == self:
                    setattr(old_value, "hand6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand6"):
                opp_val = getattr(value, "hand6", None)
                setattr(value, "hand6", self)

    @property
    def player9(self):
        return self.__player9
    @player9.setter
    def player9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__player9", None)
        self.__player9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand8"):
                opp_val = getattr(old_value, "hand8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand8"):
                opp_val = getattr(value, "hand8", None)
                if opp_val is None:
                    setattr(value, "hand8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Deck:

    def __init__(self, cards: Card, card12: set["Card"] = None, blackjack5: "BlackjackGame" = None):
        self.cards = cards
        self.card12 = card12 if card12 is not None else set()
        self.blackjack5 = blackjack5
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Card):
        self.__cards = cards

    @property
    def card12(self):
        return self.__card12
    @card12.setter
    def card12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card12", None)
        self.__card12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck13"):
                    opp_val = getattr(item, "deck13", None)
                    
                    if opp_val == self:
                        setattr(item, "deck13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck13"):
                    opp_val = getattr(item, "deck13", None)
                    
                    setattr(item, "deck13", self)
                    

    @property
    def blackjack5(self):
        return self.__blackjack5
    @blackjack5.setter
    def blackjack5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__blackjack5", None)
        self.__blackjack5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck24"):
                opp_val = getattr(old_value, "deck24", None)
                if opp_val == self:
                    setattr(old_value, "deck24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck24"):
                opp_val = getattr(value, "deck24", None)
                setattr(value, "deck24", self)



class BlackjackGame:

    def __init__(self, deck: Deck, dealer: Dealer, player: Player, bet: int, player1: "Player" = None, dealer3: "Dealer" = None, deck24: "Deck" = None):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.bet = bet
        self.player1 = player1
        self.dealer3 = dealer3
        self.deck24 = deck24
        
        pass
    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: Player):
        self.__player = player

    @property
    def dealer(self):
        return self.__dealer
    @dealer.setter
    def dealer(self, dealer: Dealer):
        self.__dealer = dealer

    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet

    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__player1", None)
        self.__player1 = value
        
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
    def deck24(self):
        return self.__deck24
    @deck24.setter
    def deck24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__deck24", None)
        self.__deck24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack5"):
                opp_val = getattr(old_value, "blackjack5", None)
                if opp_val == self:
                    setattr(old_value, "blackjack5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack5"):
                opp_val = getattr(value, "blackjack5", None)
                setattr(value, "blackjack5", self)

    @property
    def dealer3(self):
        return self.__dealer3
    @dealer3.setter
    def dealer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__dealer3", None)
        self.__dealer3 = value
        
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



class Dealer:

    def __init__(self, hand: Hand, cardTotalLimit: int, hand6: "Hand" = None, blackjack2: "BlackjackGame" = None):
        self.hand = hand
        self.cardTotalLimit = cardTotalLimit
        self.hand6 = hand6
        self.blackjack2 = blackjack2
        
        pass
    @property
    def cardTotalLimit(self):
        return self.__cardTotalLimit
    @cardTotalLimit.setter
    def cardTotalLimit(self, cardTotalLimit: int):
        self.__cardTotalLimit = cardTotalLimit

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Hand):
        self.__hand = hand

    @property
    def hand6(self):
        return self.__hand6
    @hand6.setter
    def hand6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__hand6", None)
        self.__hand6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer7"):
                opp_val = getattr(old_value, "dealer7", None)
                if opp_val == self:
                    setattr(old_value, "dealer7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer7"):
                opp_val = getattr(value, "dealer7", None)
                setattr(value, "dealer7", self)

    @property
    def blackjack2(self):
        return self.__blackjack2
    @blackjack2.setter
    def blackjack2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__blackjack2", None)
        self.__blackjack2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer3"):
                opp_val = getattr(old_value, "dealer3", None)
                if opp_val == self:
                    setattr(old_value, "dealer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer3"):
                opp_val = getattr(value, "dealer3", None)
                setattr(value, "dealer3", self)



class Player:

    def __init__(self, hand: Hand, profile: str, money: int, hand8: set["Hand"] = None, blackjack0: "BlackjackGame" = None):
        self.hand = hand
        self.profile = profile
        self.money = money
        self.hand8 = hand8 if hand8 is not None else set()
        self.blackjack0 = blackjack0
        
        pass
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: int):
        self.__money = money

    @property
    def profile(self):
        return self.__profile
    @profile.setter
    def profile(self, profile: str):
        self.__profile = profile

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Hand):
        self.__hand = hand

    @property
    def hand8(self):
        return self.__hand8
    @hand8.setter
    def hand8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__hand8", None)
        self.__hand8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player9"):
                    opp_val = getattr(item, "player9", None)
                    
                    if opp_val == self:
                        setattr(item, "player9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player9"):
                    opp_val = getattr(item, "player9", None)
                    
                    setattr(item, "player9", self)
                    

    @property
    def blackjack0(self):
        return self.__blackjack0
    @blackjack0.setter
    def blackjack0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__blackjack0", None)
        self.__blackjack0 = value
        
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



class JLabel:

    pass


class BasePlayer(ABC):

    def __init__(self, isBusted: bool):
        self.isBusted = isBusted
        
        pass
    @property
    def isBusted(self):
        return self.__isBusted
    @isBusted.setter
    def isBusted(self, isBusted: bool):
        self.__isBusted = isBusted

