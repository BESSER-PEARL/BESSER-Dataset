from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Computer:

    pass


class Human:

    pass


class Bank:

    def __init__(self, total: str, player16: "Player" = None):
        self.total = total
        self.player16 = player16
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: str):
        self.__total = total

    @property
    def player16(self):
        return self.__player16
    @player16.setter
    def player16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__player16", None)
        self.__player16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank217"):
                opp_val = getattr(old_value, "bank217", None)
                if opp_val == self:
                    setattr(old_value, "bank217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank217"):
                opp_val = getattr(value, "bank217", None)
                setattr(value, "bank217", self)



class HandStrength:

    def __init__(self, STRAIGHT_FLUSH: int, dealer14: "Dealer" = None):
        self.STRAIGHT_FLUSH = STRAIGHT_FLUSH
        self.dealer14 = dealer14
        
        pass
    @property
    def STRAIGHT_FLUSH(self):
        return self.__STRAIGHT_FLUSH
    @STRAIGHT_FLUSH.setter
    def STRAIGHT_FLUSH(self, STRAIGHT_FLUSH: int):
        self.__STRAIGHT_FLUSH = STRAIGHT_FLUSH

    @property
    def dealer14(self):
        return self.__dealer14
    @dealer14.setter
    def dealer14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HandStrength__dealer14", None)
        self.__dealer14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "handStrength15"):
                opp_val = getattr(old_value, "handStrength15", None)
                if opp_val == self:
                    setattr(old_value, "handStrength15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "handStrength15"):
                opp_val = getattr(value, "handStrength15", None)
                setattr(value, "handStrength15", self)



class Dealer:

    def __init__(self, deck: Deck, analyzeHand: HandStrength, deck212: "Deck" = None, handStrength15: "HandStrength" = None, texasHoldEm4: "Poker" = None):
        self.deck = deck
        self.analyzeHand = analyzeHand
        self.deck212 = deck212
        self.handStrength15 = handStrength15
        self.texasHoldEm4 = texasHoldEm4
        
        pass
    @property
    def analyzeHand(self):
        return self.__analyzeHand
    @analyzeHand.setter
    def analyzeHand(self, analyzeHand: HandStrength):
        self.__analyzeHand = analyzeHand

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

    @property
    def deck212(self):
        return self.__deck212
    @deck212.setter
    def deck212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__deck212", None)
        self.__deck212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer13"):
                opp_val = getattr(old_value, "dealer13", None)
                if opp_val == self:
                    setattr(old_value, "dealer13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer13"):
                opp_val = getattr(value, "dealer13", None)
                setattr(value, "dealer13", self)

    @property
    def handStrength15(self):
        return self.__handStrength15
    @handStrength15.setter
    def handStrength15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__handStrength15", None)
        self.__handStrength15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer14"):
                opp_val = getattr(old_value, "dealer14", None)
                if opp_val == self:
                    setattr(old_value, "dealer14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer14"):
                opp_val = getattr(value, "dealer14", None)
                setattr(value, "dealer14", self)

    @property
    def texasHoldEm4(self):
        return self.__texasHoldEm4
    @texasHoldEm4.setter
    def texasHoldEm4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__texasHoldEm4", None)
        self.__texasHoldEm4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer25"):
                opp_val = getattr(old_value, "dealer25", None)
                if opp_val == self:
                    setattr(old_value, "dealer25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer25"):
                opp_val = getattr(value, "dealer25", None)
                setattr(value, "dealer25", self)



class Deck:

    def __init__(self, cards: str, dealer13: "Dealer" = None, card1: set["Card"] = None):
        self.cards = cards
        self.dealer13 = dealer13
        self.card1 = card1 if card1 is not None else set()
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card1", None)
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
                    

    @property
    def dealer13(self):
        return self.__dealer13
    @dealer13.setter
    def dealer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__dealer13", None)
        self.__dealer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck212"):
                opp_val = getattr(old_value, "deck212", None)
                if opp_val == self:
                    setattr(old_value, "deck212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck212"):
                opp_val = getattr(value, "deck212", None)
                setattr(value, "deck212", self)



class RecordBook:

    def __init__(self, recordList: str, texasHoldEm3: "Poker" = None):
        self.recordList = recordList
        self.texasHoldEm3 = texasHoldEm3
        
        pass
    @property
    def recordList(self):
        return self.__recordList
    @recordList.setter
    def recordList(self, recordList: str):
        self.__recordList = recordList

    @property
    def texasHoldEm3(self):
        return self.__texasHoldEm3
    @texasHoldEm3.setter
    def texasHoldEm3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RecordBook__texasHoldEm3", None)
        self.__texasHoldEm3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recordBook2"):
                opp_val = getattr(old_value, "recordBook2", None)
                if opp_val == self:
                    setattr(old_value, "recordBook2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recordBook2"):
                opp_val = getattr(value, "recordBook2", None)
                setattr(value, "recordBook2", self)



class Player(ABC):

    def __init__(self, name: str, hand: Hand, bank: Bank, bank217: "Bank" = None, texasHoldEm6: "Poker" = None, hand28: "Hand" = None):
        self.name = name
        self.hand = hand
        self.bank = bank
        self.bank217 = bank217
        self.texasHoldEm6 = texasHoldEm6
        self.hand28 = hand28
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Hand):
        self.__hand = hand

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bank(self):
        return self.__bank
    @bank.setter
    def bank(self, bank: Bank):
        self.__bank = bank

    @property
    def bank217(self):
        return self.__bank217
    @bank217.setter
    def bank217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__bank217", None)
        self.__bank217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player16"):
                opp_val = getattr(old_value, "player16", None)
                if opp_val == self:
                    setattr(old_value, "player16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player16"):
                opp_val = getattr(value, "player16", None)
                setattr(value, "player16", self)

    @property
    def texasHoldEm6(self):
        return self.__texasHoldEm6
    @texasHoldEm6.setter
    def texasHoldEm6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__texasHoldEm6", None)
        self.__texasHoldEm6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player7"):
                opp_val = getattr(old_value, "player7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player7"):
                opp_val = getattr(value, "player7", None)
                if opp_val is None:
                    setattr(value, "player7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hand28(self):
        return self.__hand28
    @hand28.setter
    def hand28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__hand28", None)
        self.__hand28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player9"):
                opp_val = getattr(old_value, "player9", None)
                if opp_val == self:
                    setattr(old_value, "player9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player9"):
                opp_val = getattr(value, "player9", None)
                setattr(value, "player9", self)



class Hand:

    def __init__(self, handCollection: str, card10: set["Card"] = None, player9: "Player" = None):
        self.handCollection = handCollection
        self.card10 = card10 if card10 is not None else set()
        self.player9 = player9
        
        pass
    @property
    def handCollection(self):
        return self.__handCollection
    @handCollection.setter
    def handCollection(self, handCollection: str):
        self.__handCollection = handCollection

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
            if hasattr(old_value, "hand28"):
                opp_val = getattr(old_value, "hand28", None)
                if opp_val == self:
                    setattr(old_value, "hand28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand28"):
                opp_val = getattr(value, "hand28", None)
                setattr(value, "hand28", self)

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
                    



class Card:

    def __init__(self, name: str, val: str, img: str, suit: str, hand11: "Hand" = None, deck0: "Deck" = None):
        self.name = name
        self.val = val
        self.img = img
        self.suit = suit
        self.hand11 = hand11
        self.deck0 = deck0
        
        pass
    @property
    def val(self):
        return self.__val
    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, img: str):
        self.__img = img

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



class Poker:

    def __init__(self, player1: Player, player2: Player, dealer: Dealer, recordBook2: "RecordBook" = None, dealer25: "Dealer" = None, player7: set["Player"] = None):
        self.player1 = player1
        self.player2 = player2
        self.dealer = dealer
        self.recordBook2 = recordBook2
        self.dealer25 = dealer25
        self.player7 = player7 if player7 is not None else set()
        
        pass
    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, player2: Player):
        self.__player2 = player2

    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self, player1: Player):
        self.__player1 = player1

    @property
    def dealer(self):
        return self.__dealer
    @dealer.setter
    def dealer(self, dealer: Dealer):
        self.__dealer = dealer

    @property
    def dealer25(self):
        return self.__dealer25
    @dealer25.setter
    def dealer25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Poker__dealer25", None)
        self.__dealer25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "texasHoldEm4"):
                opp_val = getattr(old_value, "texasHoldEm4", None)
                if opp_val == self:
                    setattr(old_value, "texasHoldEm4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "texasHoldEm4"):
                opp_val = getattr(value, "texasHoldEm4", None)
                setattr(value, "texasHoldEm4", self)

    @property
    def player7(self):
        return self.__player7
    @player7.setter
    def player7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Poker__player7", None)
        self.__player7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "texasHoldEm6"):
                    opp_val = getattr(item, "texasHoldEm6", None)
                    
                    if opp_val == self:
                        setattr(item, "texasHoldEm6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "texasHoldEm6"):
                    opp_val = getattr(item, "texasHoldEm6", None)
                    
                    setattr(item, "texasHoldEm6", self)
                    

    @property
    def recordBook2(self):
        return self.__recordBook2
    @recordBook2.setter
    def recordBook2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Poker__recordBook2", None)
        self.__recordBook2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "texasHoldEm3"):
                opp_val = getattr(old_value, "texasHoldEm3", None)
                if opp_val == self:
                    setattr(old_value, "texasHoldEm3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "texasHoldEm3"):
                opp_val = getattr(value, "texasHoldEm3", None)
                setattr(value, "texasHoldEm3", self)

