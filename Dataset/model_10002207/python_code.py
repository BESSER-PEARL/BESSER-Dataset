from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Blackjack_Exit_UseCase:

    pass


class Blackjack_Play_Again_UseCase:

    pass


class Blackjack_Start_Game_UseCase:

    pass


class Blackjack_Bet_UseCase:

    pass


class Blackjack_Double_Down_UseCase:

    pass


class Blackjack_Split_UseCase:

    pass


class Blackjack_Stay_UseCase:

    pass


class Blackjack_Check_Win_Condition_UseCase:

    pass


class Blackjack_Deal_UseCase:

    pass


class Blackjack_Hit_UseCase:

    pass


class Dealer_Actor:

    pass


class Player_Actor:

    pass





class BlackJackPlayer:

    def __init__(self, cardCount: int, cards__: Card, MaxNumCards: int, blackJack29: "BlackJack" = None):
        self.cardCount = cardCount
        self.cards__ = cards__
        self.MaxNumCards = MaxNumCards
        self.blackJack29 = blackJack29
        
        pass
    @property
    def MaxNumCards(self):
        return self.__MaxNumCards
    @MaxNumCards.setter
    def MaxNumCards(self, MaxNumCards: int):
        self.__MaxNumCards = MaxNumCards

    @property
    def cardCount(self):
        return self.__cardCount
    @cardCount.setter
    def cardCount(self, cardCount: int):
        self.__cardCount = cardCount

    @property
    def cards__(self):
        return self.__cards__
    @cards__.setter
    def cards__(self, cards__: Card):
        self.__cards__ = cards__

    @property
    def blackJack29(self):
        return self.__blackJack29
    @blackJack29.setter
    def blackJack29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJackPlayer__blackJack29", None)
        self.__blackJack29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackJackPlayer28"):
                opp_val = getattr(old_value, "blackJackPlayer28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackJackPlayer28"):
                opp_val = getattr(value, "blackJackPlayer28", None)
                if opp_val is None:
                    setattr(value, "blackJackPlayer28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Deck:

    def __init__(self, cardsUsed: int, deck: Card, blackJack25: "BlackJack" = None, card26: set["Card"] = None):
        self.cardsUsed = cardsUsed
        self.deck = deck
        self.blackJack25 = blackJack25
        self.card26 = card26 if card26 is not None else set()
        
        pass
    @property
    def cardsUsed(self):
        return self.__cardsUsed
    @cardsUsed.setter
    def cardsUsed(self, cardsUsed: int):
        self.__cardsUsed = cardsUsed

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Card):
        self.__deck = deck

    @property
    def card26(self):
        return self.__card26
    @card26.setter
    def card26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card26", None)
        self.__card26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck27"):
                    opp_val = getattr(item, "deck27", None)
                    
                    if opp_val == self:
                        setattr(item, "deck27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck27"):
                    opp_val = getattr(item, "deck27", None)
                    
                    setattr(item, "deck27", self)
                    

    @property
    def blackJack25(self):
        return self.__blackJack25
    @blackJack25.setter
    def blackJack25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__blackJack25", None)
        self.__blackJack25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck224"):
                opp_val = getattr(old_value, "deck224", None)
                if opp_val == self:
                    setattr(old_value, "deck224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck224"):
                opp_val = getattr(value, "deck224", None)
                setattr(value, "deck224", self)



class BlackJackDriver:

    pass


class Card:

    def __init__(self, value: int, suit: str, faceValue: str, deck27: "Deck" = None):
        self.value = value
        self.suit = suit
        self.faceValue = faceValue
        self.deck27 = deck27
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def faceValue(self):
        return self.__faceValue
    @faceValue.setter
    def faceValue(self, faceValue: str):
        self.__faceValue = faceValue

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def deck27(self):
        return self.__deck27
    @deck27.setter
    def deck27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck27", None)
        self.__deck27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card26"):
                opp_val = getattr(old_value, "card26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card26"):
                opp_val = getattr(value, "card26", None)
                if opp_val is None:
                    setattr(value, "card26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class BlackJack:

    def __init__(self, handCount: int, bet: int, money: int, deck: Deck, dealersHand: BlackJackPlayer, playersHand: BlackJackPlayer, deck224: "Deck" = None, blackJackPlayer28: set["BlackJackPlayer"] = None):
        self.handCount = handCount
        self.bet = bet
        self.money = money
        self.deck = deck
        self.dealersHand = dealersHand
        self.playersHand = playersHand
        self.deck224 = deck224
        self.blackJackPlayer28 = blackJackPlayer28 if blackJackPlayer28 is not None else set()
        
        pass
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: int):
        self.__money = money

    @property
    def dealersHand(self):
        return self.__dealersHand
    @dealersHand.setter
    def dealersHand(self, dealersHand: BlackJackPlayer):
        self.__dealersHand = dealersHand

    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet

    @property
    def handCount(self):
        return self.__handCount
    @handCount.setter
    def handCount(self, handCount: int):
        self.__handCount = handCount

    @property
    def playersHand(self):
        return self.__playersHand
    @playersHand.setter
    def playersHand(self, playersHand: BlackJackPlayer):
        self.__playersHand = playersHand

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

    @property
    def blackJackPlayer28(self):
        return self.__blackJackPlayer28
    @blackJackPlayer28.setter
    def blackJackPlayer28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack__blackJackPlayer28", None)
        self.__blackJackPlayer28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "blackJack29"):
                    opp_val = getattr(item, "blackJack29", None)
                    
                    if opp_val == self:
                        setattr(item, "blackJack29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "blackJack29"):
                    opp_val = getattr(item, "blackJack29", None)
                    
                    setattr(item, "blackJack29", self)
                    

    @property
    def deck224(self):
        return self.__deck224
    @deck224.setter
    def deck224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack__deck224", None)
        self.__deck224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackJack25"):
                opp_val = getattr(old_value, "blackJack25", None)
                if opp_val == self:
                    setattr(old_value, "blackJack25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackJack25"):
                opp_val = getattr(value, "blackJack25", None)
                setattr(value, "blackJack25", self)

