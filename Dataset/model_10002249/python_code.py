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


class Strategy:

    def __init__(self, game: BlackjackGame, blackjack1: "BlackjackGame" = None):
        self.game = game
        self.blackjack1 = blackjack1
        
        pass
    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: BlackjackGame):
        self.__game = game

    @property
    def blackjack1(self):
        return self.__blackjack1
    @blackjack1.setter
    def blackjack1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Strategy__blackjack1", None)
        self.__blackjack1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "strategy0"):
                opp_val = getattr(old_value, "strategy0", None)
                if opp_val == self:
                    setattr(old_value, "strategy0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "strategy0"):
                opp_val = getattr(value, "strategy0", None)
                setattr(value, "strategy0", self)



class Card:

    def __init__(self, name: str, avatar: str, valueSoft: str, valueHard: str, suit: str, rank: str, Count: int, hand13: "Hand" = None, deck15: "Deck" = None):
        self.name = name
        self.avatar = avatar
        self.valueSoft = valueSoft
        self.valueHard = valueHard
        self.suit = suit
        self.rank = rank
        self.Count = Count
        self.hand13 = hand13
        self.deck15 = deck15
        
        pass
    @property
    def avatar(self):
        return self.__avatar
    @avatar.setter
    def avatar(self, avatar: str):
        self.__avatar = avatar

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def valueSoft(self):
        return self.__valueSoft
    @valueSoft.setter
    def valueSoft(self, valueSoft: str):
        self.__valueSoft = valueSoft

    @property
    def valueHard(self):
        return self.__valueHard
    @valueHard.setter
    def valueHard(self, valueHard: str):
        self.__valueHard = valueHard

    @property
    def Count(self):
        return self.__Count
    @Count.setter
    def Count(self, Count: int):
        self.__Count = Count

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def deck15(self):
        return self.__deck15
    @deck15.setter
    def deck15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck15", None)
        self.__deck15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card14"):
                opp_val = getattr(old_value, "card14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card14"):
                opp_val = getattr(value, "card14", None)
                if opp_val is None:
                    setattr(value, "card14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hand13(self):
        return self.__hand13
    @hand13.setter
    def hand13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__hand13", None)
        self.__hand13 = value
        
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



class Hand:

    def __init__(self, cards: Card, total: int, dealer9: "Dealer" = None, player11: "Player" = None, card12: set["Card"] = None):
        self.cards = cards
        self.total = total
        self.dealer9 = dealer9
        self.player11 = player11
        self.card12 = card12 if card12 is not None else set()
        
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
    def dealer9(self):
        return self.__dealer9
    @dealer9.setter
    def dealer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__dealer9", None)
        self.__dealer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand8"):
                opp_val = getattr(old_value, "hand8", None)
                if opp_val == self:
                    setattr(old_value, "hand8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand8"):
                opp_val = getattr(value, "hand8", None)
                setattr(value, "hand8", self)

    @property
    def card12(self):
        return self.__card12
    @card12.setter
    def card12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__card12", None)
        self.__card12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand13"):
                    opp_val = getattr(item, "hand13", None)
                    
                    if opp_val == self:
                        setattr(item, "hand13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand13"):
                    opp_val = getattr(item, "hand13", None)
                    
                    setattr(item, "hand13", self)
                    

    @property
    def player11(self):
        return self.__player11
    @player11.setter
    def player11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__player11", None)
        self.__player11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand10"):
                opp_val = getattr(old_value, "hand10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand10"):
                opp_val = getattr(value, "hand10", None)
                if opp_val is None:
                    setattr(value, "hand10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Deck:

    def __init__(self, cards: Card, blackjack7: "BlackjackGame" = None, card14: set["Card"] = None):
        self.cards = cards
        self.blackjack7 = blackjack7
        self.card14 = card14 if card14 is not None else set()
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Card):
        self.__cards = cards

    @property
    def card14(self):
        return self.__card14
    @card14.setter
    def card14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card14", None)
        self.__card14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck15"):
                    opp_val = getattr(item, "deck15", None)
                    
                    if opp_val == self:
                        setattr(item, "deck15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck15"):
                    opp_val = getattr(item, "deck15", None)
                    
                    setattr(item, "deck15", self)
                    

    @property
    def blackjack7(self):
        return self.__blackjack7
    @blackjack7.setter
    def blackjack7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__blackjack7", None)
        self.__blackjack7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck26"):
                opp_val = getattr(old_value, "deck26", None)
                if opp_val == self:
                    setattr(old_value, "deck26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck26"):
                opp_val = getattr(value, "deck26", None)
                setattr(value, "deck26", self)



class BlackjackGame:

    def __init__(self, deck: Deck, dealer: Dealer, player: Player, bet: int, strategy0: "Strategy" = None, player3: "Player" = None, dealer5: "Dealer" = None, deck26: "Deck" = None):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.bet = bet
        self.strategy0 = strategy0
        self.player3 = player3
        self.dealer5 = dealer5
        self.deck26 = deck26
        
        pass
    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: Player):
        self.__player = player

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

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
    def deck26(self):
        return self.__deck26
    @deck26.setter
    def deck26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__deck26", None)
        self.__deck26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack7"):
                opp_val = getattr(old_value, "blackjack7", None)
                if opp_val == self:
                    setattr(old_value, "blackjack7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack7"):
                opp_val = getattr(value, "blackjack7", None)
                setattr(value, "blackjack7", self)

    @property
    def strategy0(self):
        return self.__strategy0
    @strategy0.setter
    def strategy0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__strategy0", None)
        self.__strategy0 = value
        
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

    @property
    def player3(self):
        return self.__player3
    @player3.setter
    def player3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__player3", None)
        self.__player3 = value
        
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

    @property
    def dealer5(self):
        return self.__dealer5
    @dealer5.setter
    def dealer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__dealer5", None)
        self.__dealer5 = value
        
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



class Dealer:

    def __init__(self, cardTotalLimit: int, hand: Hand, blackjack4: "BlackjackGame" = None, hand8: "Hand" = None):
        self.cardTotalLimit = cardTotalLimit
        self.hand = hand
        self.blackjack4 = blackjack4
        self.hand8 = hand8
        
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
    def blackjack4(self):
        return self.__blackjack4
    @blackjack4.setter
    def blackjack4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__blackjack4", None)
        self.__blackjack4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer5"):
                opp_val = getattr(old_value, "dealer5", None)
                if opp_val == self:
                    setattr(old_value, "dealer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer5"):
                opp_val = getattr(value, "dealer5", None)
                setattr(value, "dealer5", self)

    @property
    def hand8(self):
        return self.__hand8
    @hand8.setter
    def hand8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__hand8", None)
        self.__hand8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer9"):
                opp_val = getattr(old_value, "dealer9", None)
                if opp_val == self:
                    setattr(old_value, "dealer9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer9"):
                opp_val = getattr(value, "dealer9", None)
                setattr(value, "dealer9", self)



class Player:

    def __init__(self, hand: Hand, profile: str, money: int, blackjack2: "BlackjackGame" = None, hand10: set["Hand"] = None):
        self.hand = hand
        self.profile = profile
        self.money = money
        self.blackjack2 = blackjack2
        self.hand10 = hand10 if hand10 is not None else set()
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Hand):
        self.__hand = hand

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
    def hand10(self):
        return self.__hand10
    @hand10.setter
    def hand10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__hand10", None)
        self.__hand10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player11"):
                    opp_val = getattr(item, "player11", None)
                    
                    if opp_val == self:
                        setattr(item, "player11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player11"):
                    opp_val = getattr(item, "player11", None)
                    
                    setattr(item, "player11", self)
                    

    @property
    def blackjack2(self):
        return self.__blackjack2
    @blackjack2.setter
    def blackjack2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__blackjack2", None)
        self.__blackjack2 = value
        
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

