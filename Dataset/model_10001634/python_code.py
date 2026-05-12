from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class table_Rank(Enum):
    pass
class common_Ranks(Enum):
    pass
class table_Suit(Enum):
    pass
class common_States(Enum):
    pass
class table_UpcomingCards(Enum):
    pass

############################################
# Definition of Classes
############################################










class genmymodelreverse_java_io_IOException:

    pass


class genmymodelreverse_java_io_PrintWriter:

    pass


class genmymodelreverse_java_io_BufferedReader:

    pass


class table_Table:

    def __init__(self, upcomingCards: table_UpcomingCards, turnedCards: str, amountOfCards: int, deck1: "table_Deck" = None, players9: "player_Players" = None, gamemanager26: "managers_GameManager" = None, burnedCard31: "table_Card" = None):
        self.upcomingCards = upcomingCards
        self.turnedCards = turnedCards
        self.amountOfCards = amountOfCards
        self.deck1 = deck1
        self.players9 = players9
        self.gamemanager26 = gamemanager26
        self.burnedCard31 = burnedCard31
        
        pass
    @property
    def amountOfCards(self):
        return self.__amountOfCards
    @amountOfCards.setter
    def amountOfCards(self, amountOfCards: int):
        self.__amountOfCards = amountOfCards

    @property
    def upcomingCards(self):
        return self.__upcomingCards
    @upcomingCards.setter
    def upcomingCards(self, upcomingCards: table_UpcomingCards):
        self.__upcomingCards = upcomingCards

    @property
    def turnedCards(self):
        return self.__turnedCards
    @turnedCards.setter
    def turnedCards(self, turnedCards: str):
        self.__turnedCards = turnedCards

    @property
    def players9(self):
        return self.__players9
    @players9.setter
    def players9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Table__players9", None)
        self.__players9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table8"):
                opp_val = getattr(old_value, "table8", None)
                if opp_val == self:
                    setattr(old_value, "table8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table8"):
                opp_val = getattr(value, "table8", None)
                setattr(value, "table8", self)

    @property
    def burnedCard31(self):
        return self.__burnedCard31
    @burnedCard31.setter
    def burnedCard31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Table__burnedCard31", None)
        self.__burnedCard31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table30"):
                opp_val = getattr(old_value, "table30", None)
                if opp_val == self:
                    setattr(old_value, "table30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table30"):
                opp_val = getattr(value, "table30", None)
                setattr(value, "table30", self)

    @property
    def deck1(self):
        return self.__deck1
    @deck1.setter
    def deck1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Table__deck1", None)
        self.__deck1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table0"):
                opp_val = getattr(old_value, "table0", None)
                if opp_val == self:
                    setattr(old_value, "table0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table0"):
                opp_val = getattr(value, "table0", None)
                setattr(value, "table0", self)

    @property
    def gamemanager26(self):
        return self.__gamemanager26
    @gamemanager26.setter
    def gamemanager26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Table__gamemanager26", None)
        self.__gamemanager26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table27"):
                opp_val = getattr(old_value, "table27", None)
                if opp_val == self:
                    setattr(old_value, "table27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table27"):
                opp_val = getattr(value, "table27", None)
                setattr(value, "table27", self)



class table_Deck:

    def __init__(self, suit: table_Suit, rank: table_Rank, numCardsInDeck: int, randomNumbers: int, table0: "table_Table" = None, cardBelow11: "table_Card" = None, topCard25: "table_Card" = None):
        self.suit = suit
        self.rank = rank
        self.numCardsInDeck = numCardsInDeck
        self.randomNumbers = randomNumbers
        self.table0 = table0
        self.cardBelow11 = cardBelow11
        self.topCard25 = topCard25
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: table_Suit):
        self.__suit = suit

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: table_Rank):
        self.__rank = rank

    @property
    def numCardsInDeck(self):
        return self.__numCardsInDeck
    @numCardsInDeck.setter
    def numCardsInDeck(self, numCardsInDeck: int):
        self.__numCardsInDeck = numCardsInDeck

    @property
    def randomNumbers(self):
        return self.__randomNumbers
    @randomNumbers.setter
    def randomNumbers(self, randomNumbers: int):
        self.__randomNumbers = randomNumbers

    @property
    def topCard25(self):
        return self.__topCard25
    @topCard25.setter
    def topCard25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Deck__topCard25", None)
        self.__topCard25 = value
        
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

    @property
    def cardBelow11(self):
        return self.__cardBelow11
    @cardBelow11.setter
    def cardBelow11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Deck__cardBelow11", None)
        self.__cardBelow11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck10"):
                opp_val = getattr(old_value, "deck10", None)
                if opp_val == self:
                    setattr(old_value, "deck10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck10"):
                opp_val = getattr(value, "deck10", None)
                setattr(value, "deck10", self)

    @property
    def table0(self):
        return self.__table0
    @table0.setter
    def table0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Deck__table0", None)
        self.__table0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck1"):
                opp_val = getattr(old_value, "deck1", None)
                if opp_val == self:
                    setattr(old_value, "deck1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck1"):
                opp_val = getattr(value, "deck1", None)
                setattr(value, "deck1", self)



class table_Card:

    def __init__(self, suit: table_Suit, rank: table_Rank, deck10: "table_Deck" = None, hand4: "common_Hand" = None, hand12: "common_Hand" = None, deck24: "table_Deck" = None, card28: "table_Card" = None, reference29: "table_Card" = None, table30: "table_Table" = None):
        self.suit = suit
        self.rank = rank
        self.deck10 = deck10
        self.hand4 = hand4
        self.hand12 = hand12
        self.deck24 = deck24
        self.card28 = card28
        self.reference29 = reference29
        self.table30 = table30
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: table_Rank):
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: table_Suit):
        self.__suit = suit

    @property
    def deck24(self):
        return self.__deck24
    @deck24.setter
    def deck24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Card__deck24", None)
        self.__deck24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "topCard25"):
                opp_val = getattr(old_value, "topCard25", None)
                if opp_val == self:
                    setattr(old_value, "topCard25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "topCard25"):
                opp_val = getattr(value, "topCard25", None)
                setattr(value, "topCard25", self)

    @property
    def card28(self):
        return self.__card28
    @card28.setter
    def card28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Card__card28", None)
        self.__card28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reference29"):
                opp_val = getattr(old_value, "reference29", None)
                if opp_val == self:
                    setattr(old_value, "reference29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reference29"):
                opp_val = getattr(value, "reference29", None)
                setattr(value, "reference29", self)

    @property
    def hand12(self):
        return self.__hand12
    @hand12.setter
    def hand12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Card__hand12", None)
        self.__hand12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card213"):
                opp_val = getattr(old_value, "card213", None)
                if opp_val == self:
                    setattr(old_value, "card213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card213"):
                opp_val = getattr(value, "card213", None)
                setattr(value, "card213", self)

    @property
    def reference29(self):
        return self.__reference29
    @reference29.setter
    def reference29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Card__reference29", None)
        self.__reference29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card28"):
                opp_val = getattr(old_value, "card28", None)
                if opp_val == self:
                    setattr(old_value, "card28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card28"):
                opp_val = getattr(value, "card28", None)
                setattr(value, "card28", self)

    @property
    def deck10(self):
        return self.__deck10
    @deck10.setter
    def deck10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Card__deck10", None)
        self.__deck10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cardBelow11"):
                opp_val = getattr(old_value, "cardBelow11", None)
                if opp_val == self:
                    setattr(old_value, "cardBelow11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cardBelow11"):
                opp_val = getattr(value, "cardBelow11", None)
                setattr(value, "cardBelow11", self)

    @property
    def hand4(self):
        return self.__hand4
    @hand4.setter
    def hand4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Card__hand4", None)
        self.__hand4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card15"):
                opp_val = getattr(old_value, "card15", None)
                if opp_val == self:
                    setattr(old_value, "card15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card15"):
                opp_val = getattr(value, "card15", None)
                setattr(value, "card15", self)

    @property
    def table30(self):
        return self.__table30
    @table30.setter
    def table30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Card__table30", None)
        self.__table30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "burnedCard31"):
                opp_val = getattr(old_value, "burnedCard31", None)
                if opp_val == self:
                    setattr(old_value, "burnedCard31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "burnedCard31"):
                opp_val = getattr(value, "burnedCard31", None)
                setattr(value, "burnedCard31", self)



class server_MultiServer:

    pass


class player_Players:

    def __init__(self, goodToGo: bool, MaxAmountOfPlayers: int, wealth: float, AmountOfPlayers: int, table8: "table_Table" = None, loginmanager16: "managers_LoginManager" = None, gameManager23: "managers_GameManager" = None, gamemanager32: "managers_GameManager" = None, players35: set["common_Observer_Interface"] = None):
        self.goodToGo = goodToGo
        self.MaxAmountOfPlayers = MaxAmountOfPlayers
        self.wealth = wealth
        self.AmountOfPlayers = AmountOfPlayers
        self.table8 = table8
        self.loginmanager16 = loginmanager16
        self.gameManager23 = gameManager23
        self.gamemanager32 = gamemanager32
        self.players35 = players35 if players35 is not None else set()
        
        pass
    @property
    def wealth(self):
        return self.__wealth
    @wealth.setter
    def wealth(self, wealth: float):
        self.__wealth = wealth

    @property
    def MaxAmountOfPlayers(self):
        return self.__MaxAmountOfPlayers
    @MaxAmountOfPlayers.setter
    def MaxAmountOfPlayers(self, MaxAmountOfPlayers: int):
        self.__MaxAmountOfPlayers = MaxAmountOfPlayers

    @property
    def goodToGo(self):
        return self.__goodToGo
    @goodToGo.setter
    def goodToGo(self, goodToGo: bool):
        self.__goodToGo = goodToGo

    @property
    def AmountOfPlayers(self):
        return self.__AmountOfPlayers
    @AmountOfPlayers.setter
    def AmountOfPlayers(self, AmountOfPlayers: int):
        self.__AmountOfPlayers = AmountOfPlayers

    @property
    def gameManager23(self):
        return self.__gameManager23
    @gameManager23.setter
    def gameManager23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_player_Players__gameManager23", None)
        self.__gameManager23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players22"):
                opp_val = getattr(old_value, "players22", None)
                if opp_val == self:
                    setattr(old_value, "players22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players22"):
                opp_val = getattr(value, "players22", None)
                setattr(value, "players22", self)

    @property
    def loginmanager16(self):
        return self.__loginmanager16
    @loginmanager16.setter
    def loginmanager16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_player_Players__loginmanager16", None)
        self.__loginmanager16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players17"):
                opp_val = getattr(old_value, "players17", None)
                if opp_val == self:
                    setattr(old_value, "players17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players17"):
                opp_val = getattr(value, "players17", None)
                setattr(value, "players17", self)

    @property
    def players35(self):
        return self.__players35
    @players35.setter
    def players35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_player_Players__players35", None)
        self.__players35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "players34"):
                    opp_val = getattr(item, "players34", None)
                    
                    if opp_val == self:
                        setattr(item, "players34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "players34"):
                    opp_val = getattr(item, "players34", None)
                    
                    setattr(item, "players34", self)
                    

    @property
    def gamemanager32(self):
        return self.__gamemanager32
    @gamemanager32.setter
    def gamemanager32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_player_Players__gamemanager32", None)
        self.__gamemanager32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playersObj33"):
                opp_val = getattr(old_value, "playersObj33", None)
                if opp_val == self:
                    setattr(old_value, "playersObj33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playersObj33"):
                opp_val = getattr(value, "playersObj33", None)
                setattr(value, "playersObj33", self)

    @property
    def table8(self):
        return self.__table8
    @table8.setter
    def table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_player_Players__table8", None)
        self.__table8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players9"):
                opp_val = getattr(old_value, "players9", None)
                if opp_val == self:
                    setattr(old_value, "players9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players9"):
                opp_val = getattr(value, "players9", None)
                setattr(value, "players9", self)



class player_Player:

    def __init__(self, name: str, wealth: float, bigB: float, state: common_States, dealer: bool, observerIDTracker: int, observerID: int, hand7: "common_Hand" = None, gameManager15: "managers_GameManager" = None, loginmanager18: "managers_LoginManager" = None):
        self.name = name
        self.wealth = wealth
        self.bigB = bigB
        self.state = state
        self.dealer = dealer
        self.observerIDTracker = observerIDTracker
        self.observerID = observerID
        self.hand7 = hand7
        self.gameManager15 = gameManager15
        self.loginmanager18 = loginmanager18
        
        pass
    @property
    def wealth(self):
        return self.__wealth
    @wealth.setter
    def wealth(self, wealth: float):
        self.__wealth = wealth

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: common_States):
        self.__state = state

    @property
    def observerIDTracker(self):
        return self.__observerIDTracker
    @observerIDTracker.setter
    def observerIDTracker(self, observerIDTracker: int):
        self.__observerIDTracker = observerIDTracker

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def observerID(self):
        return self.__observerID
    @observerID.setter
    def observerID(self, observerID: int):
        self.__observerID = observerID

    @property
    def bigB(self):
        return self.__bigB
    @bigB.setter
    def bigB(self, bigB: float):
        self.__bigB = bigB

    @property
    def dealer(self):
        return self.__dealer
    @dealer.setter
    def dealer(self, dealer: bool):
        self.__dealer = dealer

    @property
    def hand7(self):
        return self.__hand7
    @hand7.setter
    def hand7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_player_Player__hand7", None)
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

    @property
    def loginmanager18(self):
        return self.__loginmanager18
    @loginmanager18.setter
    def loginmanager18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_player_Player__loginmanager18", None)
        self.__loginmanager18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player19"):
                opp_val = getattr(old_value, "player19", None)
                if opp_val == self:
                    setattr(old_value, "player19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player19"):
                opp_val = getattr(value, "player19", None)
                setattr(value, "player19", self)

    @property
    def gameManager15(self):
        return self.__gameManager15
    @gameManager15.setter
    def gameManager15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_player_Player__gameManager15", None)
        self.__gameManager15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player14"):
                opp_val = getattr(old_value, "player14", None)
                if opp_val == self:
                    setattr(old_value, "player14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player14"):
                opp_val = getattr(value, "player14", None)
                setattr(value, "player14", self)



class managers_LoginManager:

    def __init__(self, inputLine: str, out: genmymodelreverse_java_io_PrintWriter, in1: genmymodelreverse_java_io_BufferedReader, players17: "player_Players" = None, player19: "player_Player" = None):
        self.inputLine = inputLine
        self.out = out
        self.in1 = in1
        self.players17 = players17
        self.player19 = player19
        
        pass
    @property
    def out(self):
        return self.__out
    @out.setter
    def out(self, out: genmymodelreverse_java_io_PrintWriter):
        self.__out = out

    @property
    def in1(self):
        return self.__in1
    @in1.setter
    def in1(self, in1: genmymodelreverse_java_io_BufferedReader):
        self.__in = in1

    @property
    def inputLine(self):
        return self.__inputLine
    @inputLine.setter
    def inputLine(self, inputLine: str):
        self.__inputLine = inputLine

    @property
    def player19(self):
        return self.__player19
    @player19.setter
    def player19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_managers_LoginManager__player19", None)
        self.__player19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loginmanager18"):
                opp_val = getattr(old_value, "loginmanager18", None)
                if opp_val == self:
                    setattr(old_value, "loginmanager18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loginmanager18"):
                opp_val = getattr(value, "loginmanager18", None)
                setattr(value, "loginmanager18", self)

    @property
    def players17(self):
        return self.__players17
    @players17.setter
    def players17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_managers_LoginManager__players17", None)
        self.__players17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loginmanager16"):
                opp_val = getattr(old_value, "loginmanager16", None)
                if opp_val == self:
                    setattr(old_value, "loginmanager16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loginmanager16"):
                opp_val = getattr(value, "loginmanager16", None)
                setattr(value, "loginmanager16", self)



class managers_GameManager:

    def __init__(self, newRound: bool, smallblind: float, raise1: float, dealer: int, playerTurn: int, initialBigID: int, initialSmallID: int, playerIDs: str, stateOfPlayersArr: str, playerNames: str, playerHands: str, playerBets: str, tableCards: str, minimumState: common_States, playersLeftInTheGame: int, pokerRules3: "calculations_PokerRules" = None, player14: "player_Player" = None, players21: set["common_Observer_Interface"] = None, players22: "player_Players" = None, table27: "table_Table" = None, playersObj33: "player_Players" = None):
        self.newRound = newRound
        self.smallblind = smallblind
        self.raise1 = raise1
        self.dealer = dealer
        self.playerTurn = playerTurn
        self.initialBigID = initialBigID
        self.initialSmallID = initialSmallID
        self.playerIDs = playerIDs
        self.stateOfPlayersArr = stateOfPlayersArr
        self.playerNames = playerNames
        self.playerHands = playerHands
        self.playerBets = playerBets
        self.tableCards = tableCards
        self.minimumState = minimumState
        self.playersLeftInTheGame = playersLeftInTheGame
        self.pokerRules3 = pokerRules3
        self.player14 = player14
        self.players21 = players21 if players21 is not None else set()
        self.players22 = players22
        self.table27 = table27
        self.playersObj33 = playersObj33
        
        pass
    @property
    def playerNames(self):
        return self.__playerNames
    @playerNames.setter
    def playerNames(self, playerNames: str):
        self.__playerNames = playerNames

    @property
    def playerTurn(self):
        return self.__playerTurn
    @playerTurn.setter
    def playerTurn(self, playerTurn: int):
        self.__playerTurn = playerTurn

    @property
    def smallblind(self):
        return self.__smallblind
    @smallblind.setter
    def smallblind(self, smallblind: float):
        self.__smallblind = smallblind

    @property
    def dealer(self):
        return self.__dealer
    @dealer.setter
    def dealer(self, dealer: int):
        self.__dealer = dealer

    @property
    def minimumState(self):
        return self.__minimumState
    @minimumState.setter
    def minimumState(self, minimumState: common_States):
        self.__minimumState = minimumState

    @property
    def playerHands(self):
        return self.__playerHands
    @playerHands.setter
    def playerHands(self, playerHands: str):
        self.__playerHands = playerHands

    @property
    def initialBigID(self):
        return self.__initialBigID
    @initialBigID.setter
    def initialBigID(self, initialBigID: int):
        self.__initialBigID = initialBigID

    @property
    def raise1(self):
        return self.__raise
    @raise1.setter
    def raise1(self, raise1: float):
        self.__raise1 = raise1

    @property
    def playersLeftInTheGame(self):
        return self.__playersLeftInTheGame
    @playersLeftInTheGame.setter
    def playersLeftInTheGame(self, playersLeftInTheGame: int):
        self.__playersLeftInTheGame = playersLeftInTheGame

    @property
    def playerBets(self):
        return self.__playerBets
    @playerBets.setter
    def playerBets(self, playerBets: str):
        self.__playerBets = playerBets

    @property
    def stateOfPlayersArr(self):
        return self.__stateOfPlayersArr
    @stateOfPlayersArr.setter
    def stateOfPlayersArr(self, stateOfPlayersArr: str):
        self.__stateOfPlayersArr = stateOfPlayersArr

    @property
    def playerIDs(self):
        return self.__playerIDs
    @playerIDs.setter
    def playerIDs(self, playerIDs: str):
        self.__playerIDs = playerIDs

    @property
    def initialSmallID(self):
        return self.__initialSmallID
    @initialSmallID.setter
    def initialSmallID(self, initialSmallID: int):
        self.__initialSmallID = initialSmallID

    @property
    def newRound(self):
        return self.__newRound
    @newRound.setter
    def newRound(self, newRound: bool):
        self.__newRound = newRound

    @property
    def tableCards(self):
        return self.__tableCards
    @tableCards.setter
    def tableCards(self, tableCards: str):
        self.__tableCards = tableCards

    @property
    def playersObj33(self):
        return self.__playersObj33
    @playersObj33.setter
    def playersObj33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_managers_GameManager__playersObj33", None)
        self.__playersObj33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gamemanager32"):
                opp_val = getattr(old_value, "gamemanager32", None)
                if opp_val == self:
                    setattr(old_value, "gamemanager32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gamemanager32"):
                opp_val = getattr(value, "gamemanager32", None)
                setattr(value, "gamemanager32", self)

    @property
    def players22(self):
        return self.__players22
    @players22.setter
    def players22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_managers_GameManager__players22", None)
        self.__players22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameManager23"):
                opp_val = getattr(old_value, "gameManager23", None)
                if opp_val == self:
                    setattr(old_value, "gameManager23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameManager23"):
                opp_val = getattr(value, "gameManager23", None)
                setattr(value, "gameManager23", self)

    @property
    def pokerRules3(self):
        return self.__pokerRules3
    @pokerRules3.setter
    def pokerRules3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_managers_GameManager__pokerRules3", None)
        self.__pokerRules3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gamemanager2"):
                opp_val = getattr(old_value, "gamemanager2", None)
                if opp_val == self:
                    setattr(old_value, "gamemanager2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gamemanager2"):
                opp_val = getattr(value, "gamemanager2", None)
                setattr(value, "gamemanager2", self)

    @property
    def table27(self):
        return self.__table27
    @table27.setter
    def table27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_managers_GameManager__table27", None)
        self.__table27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gamemanager26"):
                opp_val = getattr(old_value, "gamemanager26", None)
                if opp_val == self:
                    setattr(old_value, "gamemanager26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gamemanager26"):
                opp_val = getattr(value, "gamemanager26", None)
                setattr(value, "gamemanager26", self)

    @property
    def player14(self):
        return self.__player14
    @player14.setter
    def player14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_managers_GameManager__player14", None)
        self.__player14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameManager15"):
                opp_val = getattr(old_value, "gameManager15", None)
                if opp_val == self:
                    setattr(old_value, "gameManager15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameManager15"):
                opp_val = getattr(value, "gameManager15", None)
                setattr(value, "gameManager15", self)

    @property
    def players21(self):
        return self.__players21
    @players21.setter
    def players21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_managers_GameManager__players21", None)
        self.__players21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gamemanager20"):
                    opp_val = getattr(item, "gamemanager20", None)
                    
                    if opp_val == self:
                        setattr(item, "gamemanager20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gamemanager20"):
                    opp_val = getattr(item, "gamemanager20", None)
                    
                    setattr(item, "gamemanager20", self)
                    



class common_Subject_Interface:

    pass


class common_Observer_Interface:

    pass


class common_Hand:

    def __init__(self, rank: common_Ranks, card15: "table_Card" = None, player6: "player_Player" = None, card213: "table_Card" = None):
        self.rank = rank
        self.card15 = card15
        self.player6 = player6
        self.card213 = card213
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: common_Ranks):
        self.__rank = rank

    @property
    def card213(self):
        return self.__card213
    @card213.setter
    def card213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_common_Hand__card213", None)
        self.__card213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand12"):
                opp_val = getattr(old_value, "hand12", None)
                if opp_val == self:
                    setattr(old_value, "hand12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand12"):
                opp_val = getattr(value, "hand12", None)
                setattr(value, "hand12", self)

    @property
    def player6(self):
        return self.__player6
    @player6.setter
    def player6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_common_Hand__player6", None)
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
    def card15(self):
        return self.__card15
    @card15.setter
    def card15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_common_Hand__card15", None)
        self.__card15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand4"):
                opp_val = getattr(old_value, "hand4", None)
                if opp_val == self:
                    setattr(old_value, "hand4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand4"):
                opp_val = getattr(value, "hand4", None)
                setattr(value, "hand4", self)



class calculations_PokerRules:

    def __init__(self, tableCardRank: common_Ranks, numberOfPlayers: int, cardsOnTable: str, arrayWithHands: str, highestCardStraight: str, gamemanager2: "managers_GameManager" = None):
        self.tableCardRank = tableCardRank
        self.numberOfPlayers = numberOfPlayers
        self.cardsOnTable = cardsOnTable
        self.arrayWithHands = arrayWithHands
        self.highestCardStraight = highestCardStraight
        self.gamemanager2 = gamemanager2
        
        pass
    @property
    def highestCardStraight(self):
        return self.__highestCardStraight
    @highestCardStraight.setter
    def highestCardStraight(self, highestCardStraight: str):
        self.__highestCardStraight = highestCardStraight

    @property
    def numberOfPlayers(self):
        return self.__numberOfPlayers
    @numberOfPlayers.setter
    def numberOfPlayers(self, numberOfPlayers: int):
        self.__numberOfPlayers = numberOfPlayers

    @property
    def tableCardRank(self):
        return self.__tableCardRank
    @tableCardRank.setter
    def tableCardRank(self, tableCardRank: common_Ranks):
        self.__tableCardRank = tableCardRank

    @property
    def arrayWithHands(self):
        return self.__arrayWithHands
    @arrayWithHands.setter
    def arrayWithHands(self, arrayWithHands: str):
        self.__arrayWithHands = arrayWithHands

    @property
    def cardsOnTable(self):
        return self.__cardsOnTable
    @cardsOnTable.setter
    def cardsOnTable(self, cardsOnTable: str):
        self.__cardsOnTable = cardsOnTable

    @property
    def gamemanager2(self):
        return self.__gamemanager2
    @gamemanager2.setter
    def gamemanager2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculations_PokerRules__gamemanager2", None)
        self.__gamemanager2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pokerRules3"):
                opp_val = getattr(old_value, "pokerRules3", None)
                if opp_val == self:
                    setattr(old_value, "pokerRules3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pokerRules3"):
                opp_val = getattr(value, "pokerRules3", None)
                setattr(value, "pokerRules3", self)

