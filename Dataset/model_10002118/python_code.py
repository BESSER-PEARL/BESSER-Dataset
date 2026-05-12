from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MainGame_Hand:

    def __init__(self, Hand: str, straightFlush: bool, fourKind: bool, fullHouse: bool, flush: bool, straight: bool, threeKing: bool, twoPair: bool, onePair: bool, highCard: bool, card4: set["Cards_Card"] = None, player6: "Players_Player" = None):
        self.Hand = Hand
        self.straightFlush = straightFlush
        self.fourKind = fourKind
        self.fullHouse = fullHouse
        self.flush = flush
        self.straight = straight
        self.threeKing = threeKing
        self.twoPair = twoPair
        self.onePair = onePair
        self.highCard = highCard
        self.card4 = card4 if card4 is not None else set()
        self.player6 = player6
        
        pass
    @property
    def flush(self):
        return self.__flush
    @flush.setter
    def flush(self, flush: bool):
        self.__flush = flush

    @property
    def fullHouse(self):
        return self.__fullHouse
    @fullHouse.setter
    def fullHouse(self, fullHouse: bool):
        self.__fullHouse = fullHouse

    @property
    def threeKing(self):
        return self.__threeKing
    @threeKing.setter
    def threeKing(self, threeKing: bool):
        self.__threeKing = threeKing

    @property
    def fourKind(self):
        return self.__fourKind
    @fourKind.setter
    def fourKind(self, fourKind: bool):
        self.__fourKind = fourKind

    @property
    def twoPair(self):
        return self.__twoPair
    @twoPair.setter
    def twoPair(self, twoPair: bool):
        self.__twoPair = twoPair

    @property
    def onePair(self):
        return self.__onePair
    @onePair.setter
    def onePair(self, onePair: bool):
        self.__onePair = onePair

    @property
    def Hand(self):
        return self.__Hand
    @Hand.setter
    def Hand(self, Hand: str):
        self.__Hand = Hand

    @property
    def straight(self):
        return self.__straight
    @straight.setter
    def straight(self, straight: bool):
        self.__straight = straight

    @property
    def highCard(self):
        return self.__highCard
    @highCard.setter
    def highCard(self, highCard: bool):
        self.__highCard = highCard

    @property
    def straightFlush(self):
        return self.__straightFlush
    @straightFlush.setter
    def straightFlush(self, straightFlush: bool):
        self.__straightFlush = straightFlush

    @property
    def player6(self):
        return self.__player6
    @player6.setter
    def player6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MainGame_Hand__player6", None)
        self.__player6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand7"):
                opp_val = getattr(old_value, "hand7", None)
                if opp_val == self:
                    setattr(old_value, "hand7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand7"):
                opp_val = getattr(value, "hand7", None)
                setattr(value, "hand7", self)

    @property
    def card4(self):
        return self.__card4
    @card4.setter
    def card4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MainGame_Hand__card4", None)
        self.__card4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand5"):
                    opp_val = getattr(item, "hand5", None)
                    
                    if opp_val == self:
                        setattr(item, "hand5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand5"):
                    opp_val = getattr(item, "hand5", None)
                    
                    setattr(item, "hand5", self)
                    



class MainGame_GUI:

    pass


class MainGame_Deck:

    def __init__(self, Cards: str, card1: set["Cards_Card"] = None, main2: "MainGame_Main" = None):
        self.Cards = Cards
        self.card1 = card1 if card1 is not None else set()
        self.main2 = main2
        
        pass
    @property
    def Cards(self):
        return self.__Cards
    @Cards.setter
    def Cards(self, Cards: str):
        self.__Cards = Cards

    @property
    def main2(self):
        return self.__main2
    @main2.setter
    def main2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MainGame_Deck__main2", None)
        self.__main2 = value
        
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

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MainGame_Deck__card1", None)
        self.__card1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck0"):
                    opp_val = getattr(item, "deck0", None)
                    
                    if opp_val == self:
                        setattr(item, "deck0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck0"):
                    opp_val = getattr(item, "deck0", None)
                    
                    setattr(item, "deck0", self)
                    



class MainGame_Main:

    def __init__(self, dealNumber: int, deck: MainGame_Deck, deck3: "MainGame_Deck" = None, gUI9: "MainGame_GUI" = None):
        self.dealNumber = dealNumber
        self.deck = deck
        self.deck3 = deck3
        self.gUI9 = gUI9
        
        pass
    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: MainGame_Deck):
        self.__deck = deck

    @property
    def dealNumber(self):
        return self.__dealNumber
    @dealNumber.setter
    def dealNumber(self, dealNumber: int):
        self.__dealNumber = dealNumber

    @property
    def deck3(self):
        return self.__deck3
    @deck3.setter
    def deck3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MainGame_Main__deck3", None)
        self.__deck3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "main2"):
                opp_val = getattr(old_value, "main2", None)
                if opp_val == self:
                    setattr(old_value, "main2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "main2"):
                opp_val = getattr(value, "main2", None)
                setattr(value, "main2", self)

    @property
    def gUI9(self):
        return self.__gUI9
    @gUI9.setter
    def gUI9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MainGame_Main__gUI9", None)
        self.__gUI9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "main8"):
                opp_val = getattr(old_value, "main8", None)
                if opp_val == self:
                    setattr(old_value, "main8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "main8"):
                opp_val = getattr(value, "main8", None)
                setattr(value, "main8", self)



class Players_Player:

    def __init__(self, name: str, bet: int, hand: MainGame_Hand, hand7: "MainGame_Hand" = None):
        self.name = name
        self.bet = bet
        self.hand = hand
        self.hand7 = hand7
        
        pass
    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet

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
    def hand(self, hand: MainGame_Hand):
        self.__hand = hand

    @property
    def hand7(self):
        return self.__hand7
    @hand7.setter
    def hand7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players_Player__hand7", None)
        self.__hand7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player6"):
                opp_val = getattr(old_value, "player6", None)
                if opp_val == self:
                    setattr(old_value, "player6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player6"):
                opp_val = getattr(value, "player6", None)
                setattr(value, "player6", self)



class Cards_Card:

    def __init__(self, suit: str, value: int, deck0: "MainGame_Deck" = None, hand5: "MainGame_Hand" = None):
        self.suit = suit
        self.value = value
        self.deck0 = deck0
        self.hand5 = hand5
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def deck0(self):
        return self.__deck0
    @deck0.setter
    def deck0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards_Card__deck0", None)
        self.__deck0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card1"):
                opp_val = getattr(old_value, "card1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card1"):
                opp_val = getattr(value, "card1", None)
                if opp_val is None:
                    setattr(value, "card1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hand5(self):
        return self.__hand5
    @hand5.setter
    def hand5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards_Card__hand5", None)
        self.__hand5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card4"):
                opp_val = getattr(old_value, "card4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card4"):
                opp_val = getattr(value, "card4", None)
                if opp_val is None:
                    setattr(value, "card4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

