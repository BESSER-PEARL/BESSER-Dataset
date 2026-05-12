from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Cards_Cardinality(Enum):
    pass

############################################
# Definition of Classes
############################################










class Card___Interface:

    pass


class Main_MainGame:

    def __init__(self, Players: str, screen: Game_GUI, SmallBlind: int, Bigblind: int, Dealer: int, HighestBid: int, gUI3: "Game_GUI" = None):
        self.Players = Players
        self.screen = screen
        self.SmallBlind = SmallBlind
        self.Bigblind = Bigblind
        self.Dealer = Dealer
        self.HighestBid = HighestBid
        self.gUI3 = gUI3
        
        pass
    @property
    def Dealer(self):
        return self.__Dealer
    @Dealer.setter
    def Dealer(self, Dealer: int):
        self.__Dealer = Dealer

    @property
    def Players(self):
        return self.__Players
    @Players.setter
    def Players(self, Players: str):
        self.__Players = Players

    @property
    def SmallBlind(self):
        return self.__SmallBlind
    @SmallBlind.setter
    def SmallBlind(self, SmallBlind: int):
        self.__SmallBlind = SmallBlind

    @property
    def HighestBid(self):
        return self.__HighestBid
    @HighestBid.setter
    def HighestBid(self, HighestBid: int):
        self.__HighestBid = HighestBid

    @property
    def screen(self):
        return self.__screen
    @screen.setter
    def screen(self, screen: Game_GUI):
        self.__screen = screen

    @property
    def Bigblind(self):
        return self.__Bigblind
    @Bigblind.setter
    def Bigblind(self, Bigblind: int):
        self.__Bigblind = Bigblind

    @property
    def gUI3(self):
        return self.__gUI3
    @gUI3.setter
    def gUI3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Main_MainGame__gUI3", None)
        self.__gUI3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Owner2"):
                opp_val = getattr(old_value, "Owner2", None)
                if opp_val == self:
                    setattr(old_value, "Owner2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Owner2"):
                opp_val = getattr(value, "Owner2", None)
                setattr(value, "Owner2", self)



class Players_Wallet:

    def __init__(self, balance: int, player10: "Players_Player" = None):
        self.balance = balance
        self.player10 = player10
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: int):
        self.__balance = balance

    @property
    def player10(self):
        return self.__player10
    @player10.setter
    def player10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players_Wallet__player10", None)
        self.__player10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner11"):
                opp_val = getattr(old_value, "owner11", None)
                if opp_val == self:
                    setattr(old_value, "owner11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner11"):
                opp_val = getattr(value, "owner11", None)
                setattr(value, "owner11", self)



class Players_Person:

    def __init__(self, name: str, personNumber: str):
        self.name = name
        self.personNumber = personNumber
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def personNumber(self):
        return self.__personNumber
    @personNumber.setter
    def personNumber(self, personNumber: str):
        self.__personNumber = personNumber



class Players_PokerHand:

    def __init__(self, highCard: Cards_Cardinality, value: int, Cards: Card___Interface, card6: set["Cards_Card_Interface"] = None, Holder9: "Players_Player" = None):
        self.highCard = highCard
        self.value = value
        self.Cards = Cards
        self.card6 = card6 if card6 is not None else set()
        self.Holder9 = Holder9
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def highCard(self):
        return self.__highCard
    @highCard.setter
    def highCard(self, highCard: Cards_Cardinality):
        self.__highCard = highCard

    @property
    def Cards(self):
        return self.__Cards
    @Cards.setter
    def Cards(self, Cards: Card___Interface):
        self.__Cards = Cards

    @property
    def card6(self):
        return self.__card6
    @card6.setter
    def card6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players_PokerHand__card6", None)
        self.__card6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pokerHand7"):
                    opp_val = getattr(item, "pokerHand7", None)
                    
                    if opp_val == self:
                        setattr(item, "pokerHand7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pokerHand7"):
                    opp_val = getattr(item, "pokerHand7", None)
                    
                    setattr(item, "pokerHand7", self)
                    

    @property
    def Holder9(self):
        return self.__Holder9
    @Holder9.setter
    def Holder9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players_PokerHand__Holder9", None)
        self.__Holder9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerHand8"):
                opp_val = getattr(old_value, "pokerHand8", None)
                if opp_val == self:
                    setattr(old_value, "pokerHand8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerHand8"):
                opp_val = getattr(value, "pokerHand8", None)
                setattr(value, "pokerHand8", self)



class Players_Player:

    def __init__(self, isSmallBlind: bool, isBigBlind: bool, isDealer: bool, Hand: Players_PokerHand, hasFolded: bool, chips: Players_Wallet, deck4: "Cards_Deck" = None, pokerHand8: "Players_PokerHand" = None, owner11: "Players_Wallet" = None):
        self.isSmallBlind = isSmallBlind
        self.isBigBlind = isBigBlind
        self.isDealer = isDealer
        self.Hand = Hand
        self.hasFolded = hasFolded
        self.chips = chips
        self.deck4 = deck4
        self.pokerHand8 = pokerHand8
        self.owner11 = owner11
        
        pass
    @property
    def hasFolded(self):
        return self.__hasFolded
    @hasFolded.setter
    def hasFolded(self, hasFolded: bool):
        self.__hasFolded = hasFolded

    @property
    def Hand(self):
        return self.__Hand
    @Hand.setter
    def Hand(self, Hand: Players_PokerHand):
        self.__Hand = Hand

    @property
    def chips(self):
        return self.__chips
    @chips.setter
    def chips(self, chips: Players_Wallet):
        self.__chips = chips

    @property
    def isDealer(self):
        return self.__isDealer
    @isDealer.setter
    def isDealer(self, isDealer: bool):
        self.__isDealer = isDealer

    @property
    def isBigBlind(self):
        return self.__isBigBlind
    @isBigBlind.setter
    def isBigBlind(self, isBigBlind: bool):
        self.__isBigBlind = isBigBlind

    @property
    def isSmallBlind(self):
        return self.__isSmallBlind
    @isSmallBlind.setter
    def isSmallBlind(self, isSmallBlind: bool):
        self.__isSmallBlind = isSmallBlind

    @property
    def owner11(self):
        return self.__owner11
    @owner11.setter
    def owner11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players_Player__owner11", None)
        self.__owner11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player10"):
                opp_val = getattr(old_value, "player10", None)
                if opp_val == self:
                    setattr(old_value, "player10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player10"):
                opp_val = getattr(value, "player10", None)
                setattr(value, "player10", self)

    @property
    def pokerHand8(self):
        return self.__pokerHand8
    @pokerHand8.setter
    def pokerHand8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players_Player__pokerHand8", None)
        self.__pokerHand8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Holder9"):
                opp_val = getattr(old_value, "Holder9", None)
                if opp_val == self:
                    setattr(old_value, "Holder9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Holder9"):
                opp_val = getattr(value, "Holder9", None)
                setattr(value, "Holder9", self)

    @property
    def deck4(self):
        return self.__deck4
    @deck4.setter
    def deck4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Players_Player__deck4", None)
        self.__deck4 = value
        
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



class Game_Ranker:

    def __init__(self, hand: Players_PokerHand):
        self.hand = hand
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Players_PokerHand):
        self.__hand = hand



class Game_GUI:

    pass


class Cards_Deck:

    def __init__(self, list: str, burnt: Cards_Card_Interface, card0: set["Cards_Card_Interface"] = None, player5: "Players_Player" = None):
        self.list = list
        self.burnt = burnt
        self.card0 = card0 if card0 is not None else set()
        self.player5 = player5
        
        pass
    @property
    def burnt(self):
        return self.__burnt
    @burnt.setter
    def burnt(self, burnt: Cards_Card_Interface):
        self.__burnt = burnt

    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self, list: str):
        self.__list = list

    @property
    def player5(self):
        return self.__player5
    @player5.setter
    def player5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards_Deck__player5", None)
        self.__player5 = value
        
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
    def card0(self):
        return self.__card0
    @card0.setter
    def card0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards_Deck__card0", None)
        self.__card0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck1"):
                    opp_val = getattr(item, "deck1", None)
                    
                    if opp_val == self:
                        setattr(item, "deck1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck1"):
                    opp_val = getattr(item, "deck1", None)
                    
                    setattr(item, "deck1", self)
                    



class Cards_Card_Interface:

    pass


class Cards_CardImpl:

    def __init__(self, Suit: str, Cardinality: Cards_Cardinality, isMarked: bool):
        self.Suit = Suit
        self.Cardinality = Cardinality
        self.isMarked = isMarked
        
        pass
    @property
    def isMarked(self):
        return self.__isMarked
    @isMarked.setter
    def isMarked(self, isMarked: bool):
        self.__isMarked = isMarked

    @property
    def Cardinality(self):
        return self.__Cardinality
    @Cardinality.setter
    def Cardinality(self, Cardinality: Cards_Cardinality):
        self.__Cardinality = Cardinality

    @property
    def Suit(self):
        return self.__Suit
    @Suit.setter
    def Suit(self, Suit: str):
        self.__Suit = Suit

