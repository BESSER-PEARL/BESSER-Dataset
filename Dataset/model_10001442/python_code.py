from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class blackjack_Suit(Enum):
    pass
class blackjack_Value(Enum):
    pass
class blackjack_GameState(Enum):
    pass

############################################
# Definition of Classes
############################################










class Iterable_Card__Interface:

    pass


class Comparable_BlackjackHand__Interface:

    pass


class genmymodelreverse_android_support_v7_app_AppCompatActivity:

    pass


class genmymodelreverse_C12:

    pass


class genmymodelreverse_java_lang_Iterable_Interface(ABC):

    pass


class genmymodelreverse_C11:

    pass


class genmymodelreverse_java_util_Iterator_Interface(ABC):

    pass


class genmymodelreverse_C1:

    pass


class genmymodelreverse_java_lang_Comparable_Interface(ABC):

    pass


class blackjack_ExampleUnitTest:

    pass


class blackjack_MainActivity:

    pass


class blackjack_Deck:

    pass


class blackjack_DealerBot:

    pass


class blackjack_CardSet(ABC):

    pass


class blackjack_Card:

    def __init__(self, suit: blackjack_Suit, value: blackjack_Value, MAX_VALUE_OF_ACE: int, BLACKJACK_VALUE: int, cardset6: "blackjack_CardSet" = None):
        self.suit = suit
        self.value = value
        self.MAX_VALUE_OF_ACE = MAX_VALUE_OF_ACE
        self.BLACKJACK_VALUE = BLACKJACK_VALUE
        self.cardset6 = cardset6
        
        pass
    @property
    def MAX_VALUE_OF_ACE(self):
        return self.__MAX_VALUE_OF_ACE
    @MAX_VALUE_OF_ACE.setter
    def MAX_VALUE_OF_ACE(self, MAX_VALUE_OF_ACE: int):
        self.__MAX_VALUE_OF_ACE = MAX_VALUE_OF_ACE

    @property
    def BLACKJACK_VALUE(self):
        return self.__BLACKJACK_VALUE
    @BLACKJACK_VALUE.setter
    def BLACKJACK_VALUE(self, BLACKJACK_VALUE: int):
        self.__BLACKJACK_VALUE = BLACKJACK_VALUE

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: blackjack_Value):
        self.__value = value

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: blackjack_Suit):
        self.__suit = suit

    @property
    def cardset6(self):
        return self.__cardset6
    @cardset6.setter
    def cardset6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blackjack_Card__cardset6", None)
        self.__cardset6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards7"):
                opp_val = getattr(old_value, "cards7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards7"):
                opp_val = getattr(value, "cards7", None)
                if opp_val is None:
                    setattr(value, "cards7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class blackjack_BlackjackHand:

    pass


class blackjack_DeckShuffledListener_Interface:

    pass


class blackjack_BlackjackGame:

    def __init__(self, MAX_HITS: int, MAX_CARDS_PULLED: int, gstate: blackjack_GameState, hitButton: str, stayButton: str, gameResultTextView: str, playersHandTextView: str, dealersHandTextView: str, playerHandValueTextView: str, dealersHandValueTextView: str, playerHand3: "blackjack_BlackjackHand" = None, deckShuffledListener9: "blackjack_DeckShuffledListener_Interface" = None, theDeck11: "blackjack_Deck" = None, dealerBot13: "blackjack_DealerBot" = None):
        self.MAX_HITS = MAX_HITS
        self.MAX_CARDS_PULLED = MAX_CARDS_PULLED
        self.gstate = gstate
        self.hitButton = hitButton
        self.stayButton = stayButton
        self.gameResultTextView = gameResultTextView
        self.playersHandTextView = playersHandTextView
        self.dealersHandTextView = dealersHandTextView
        self.playerHandValueTextView = playerHandValueTextView
        self.dealersHandValueTextView = dealersHandValueTextView
        self.playerHand3 = playerHand3
        self.deckShuffledListener9 = deckShuffledListener9
        self.theDeck11 = theDeck11
        self.dealerBot13 = dealerBot13
        
        pass
    @property
    def gameResultTextView(self):
        return self.__gameResultTextView
    @gameResultTextView.setter
    def gameResultTextView(self, gameResultTextView: str):
        self.__gameResultTextView = gameResultTextView

    @property
    def playerHandValueTextView(self):
        return self.__playerHandValueTextView
    @playerHandValueTextView.setter
    def playerHandValueTextView(self, playerHandValueTextView: str):
        self.__playerHandValueTextView = playerHandValueTextView

    @property
    def dealersHandTextView(self):
        return self.__dealersHandTextView
    @dealersHandTextView.setter
    def dealersHandTextView(self, dealersHandTextView: str):
        self.__dealersHandTextView = dealersHandTextView

    @property
    def MAX_HITS(self):
        return self.__MAX_HITS
    @MAX_HITS.setter
    def MAX_HITS(self, MAX_HITS: int):
        self.__MAX_HITS = MAX_HITS

    @property
    def MAX_CARDS_PULLED(self):
        return self.__MAX_CARDS_PULLED
    @MAX_CARDS_PULLED.setter
    def MAX_CARDS_PULLED(self, MAX_CARDS_PULLED: int):
        self.__MAX_CARDS_PULLED = MAX_CARDS_PULLED

    @property
    def dealersHandValueTextView(self):
        return self.__dealersHandValueTextView
    @dealersHandValueTextView.setter
    def dealersHandValueTextView(self, dealersHandValueTextView: str):
        self.__dealersHandValueTextView = dealersHandValueTextView

    @property
    def hitButton(self):
        return self.__hitButton
    @hitButton.setter
    def hitButton(self, hitButton: str):
        self.__hitButton = hitButton

    @property
    def gstate(self):
        return self.__gstate
    @gstate.setter
    def gstate(self, gstate: blackjack_GameState):
        self.__gstate = gstate

    @property
    def playersHandTextView(self):
        return self.__playersHandTextView
    @playersHandTextView.setter
    def playersHandTextView(self, playersHandTextView: str):
        self.__playersHandTextView = playersHandTextView

    @property
    def stayButton(self):
        return self.__stayButton
    @stayButton.setter
    def stayButton(self, stayButton: str):
        self.__stayButton = stayButton

    @property
    def deckShuffledListener9(self):
        return self.__deckShuffledListener9
    @deckShuffledListener9.setter
    def deckShuffledListener9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blackjack_BlackjackGame__deckShuffledListener9", None)
        self.__deckShuffledListener9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjackgame8"):
                opp_val = getattr(old_value, "blackjackgame8", None)
                if opp_val == self:
                    setattr(old_value, "blackjackgame8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjackgame8"):
                opp_val = getattr(value, "blackjackgame8", None)
                setattr(value, "blackjackgame8", self)

    @property
    def theDeck11(self):
        return self.__theDeck11
    @theDeck11.setter
    def theDeck11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blackjack_BlackjackGame__theDeck11", None)
        self.__theDeck11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjackgame10"):
                opp_val = getattr(old_value, "blackjackgame10", None)
                if opp_val == self:
                    setattr(old_value, "blackjackgame10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjackgame10"):
                opp_val = getattr(value, "blackjackgame10", None)
                setattr(value, "blackjackgame10", self)

    @property
    def dealerBot13(self):
        return self.__dealerBot13
    @dealerBot13.setter
    def dealerBot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blackjack_BlackjackGame__dealerBot13", None)
        self.__dealerBot13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjackgame12"):
                opp_val = getattr(old_value, "blackjackgame12", None)
                if opp_val == self:
                    setattr(old_value, "blackjackgame12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjackgame12"):
                opp_val = getattr(value, "blackjackgame12", None)
                setattr(value, "blackjackgame12", self)

    @property
    def playerHand3(self):
        return self.__playerHand3
    @playerHand3.setter
    def playerHand3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_blackjack_BlackjackGame__playerHand3", None)
        self.__playerHand3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjackgame2"):
                opp_val = getattr(old_value, "blackjackgame2", None)
                if opp_val == self:
                    setattr(old_value, "blackjackgame2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjackgame2"):
                opp_val = getattr(value, "blackjackgame2", None)
                setattr(value, "blackjackgame2", self)



class blackjack_ExampleInstrumentedTest:

    pass
