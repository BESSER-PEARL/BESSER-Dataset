from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class AI:

    pass


class makeNewPlayer:

    pass


class Game:

    def __init__(self, players: str, pot: int, bigBlindValue: int, currentDeck: Deck, currentCommunityCards: CommunityCards, currentBigBlind: int, player3: "Player" = None, deckOfCards5: "Deck" = None, communityCards8: "CommunityCards" = None, makeNewPlayer12: set["makeNewPlayer"] = None):
        self.players = players
        self.pot = pot
        self.bigBlindValue = bigBlindValue
        self.currentDeck = currentDeck
        self.currentCommunityCards = currentCommunityCards
        self.currentBigBlind = currentBigBlind
        self.player3 = player3
        self.deckOfCards5 = deckOfCards5
        self.communityCards8 = communityCards8
        self.makeNewPlayer12 = makeNewPlayer12 if makeNewPlayer12 is not None else set()
        
        pass
    @property
    def currentDeck(self):
        return self.__currentDeck
    @currentDeck.setter
    def currentDeck(self, currentDeck: Deck):
        self.__currentDeck = currentDeck

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

    @property
    def bigBlindValue(self):
        return self.__bigBlindValue
    @bigBlindValue.setter
    def bigBlindValue(self, bigBlindValue: int):
        self.__bigBlindValue = bigBlindValue

    @property
    def pot(self):
        return self.__pot
    @pot.setter
    def pot(self, pot: int):
        self.__pot = pot

    @property
    def currentBigBlind(self):
        return self.__currentBigBlind
    @currentBigBlind.setter
    def currentBigBlind(self, currentBigBlind: int):
        self.__currentBigBlind = currentBigBlind

    @property
    def currentCommunityCards(self):
        return self.__currentCommunityCards
    @currentCommunityCards.setter
    def currentCommunityCards(self, currentCommunityCards: CommunityCards):
        self.__currentCommunityCards = currentCommunityCards

    @property
    def player3(self):
        return self.__player3
    @player3.setter
    def player3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__player3", None)
        self.__player3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game2"):
                opp_val = getattr(old_value, "game2", None)
                if opp_val == self:
                    setattr(old_value, "game2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game2"):
                opp_val = getattr(value, "game2", None)
                setattr(value, "game2", self)

    @property
    def makeNewPlayer12(self):
        return self.__makeNewPlayer12
    @makeNewPlayer12.setter
    def makeNewPlayer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__makeNewPlayer12", None)
        self.__makeNewPlayer12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game13"):
                    opp_val = getattr(item, "game13", None)
                    
                    if opp_val == self:
                        setattr(item, "game13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game13"):
                    opp_val = getattr(item, "game13", None)
                    
                    setattr(item, "game13", self)
                    

    @property
    def deckOfCards5(self):
        return self.__deckOfCards5
    @deckOfCards5.setter
    def deckOfCards5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__deckOfCards5", None)
        self.__deckOfCards5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game4"):
                opp_val = getattr(old_value, "game4", None)
                if opp_val == self:
                    setattr(old_value, "game4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game4"):
                opp_val = getattr(value, "game4", None)
                setattr(value, "game4", self)

    @property
    def communityCards8(self):
        return self.__communityCards8
    @communityCards8.setter
    def communityCards8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__communityCards8", None)
        self.__communityCards8 = value
        
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



class CommunityCards:

    def __init__(self, cards: str, card6: "Card" = None, game9: "Game" = None):
        self.cards = cards
        self.card6 = card6
        self.game9 = game9
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def game9(self):
        return self.__game9
    @game9.setter
    def game9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommunityCards__game9", None)
        self.__game9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "communityCards8"):
                opp_val = getattr(old_value, "communityCards8", None)
                if opp_val == self:
                    setattr(old_value, "communityCards8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "communityCards8"):
                opp_val = getattr(value, "communityCards8", None)
                setattr(value, "communityCards8", self)

    @property
    def card6(self):
        return self.__card6
    @card6.setter
    def card6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommunityCards__card6", None)
        self.__card6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "communityCards7"):
                opp_val = getattr(old_value, "communityCards7", None)
                if opp_val == self:
                    setattr(old_value, "communityCards7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "communityCards7"):
                opp_val = getattr(value, "communityCards7", None)
                setattr(value, "communityCards7", self)



class Player:

    def __init__(self, hand: str, isBigBlind: bool, isSmallBlind: bool, playerNumber: int, chips: int, isFolded: bool, handValue: int, name: str, isAllIn: bool, isAI: bool, game2: "Game" = None, card10: "Card" = None):
        self.hand = hand
        self.isBigBlind = isBigBlind
        self.isSmallBlind = isSmallBlind
        self.playerNumber = playerNumber
        self.chips = chips
        self.isFolded = isFolded
        self.handValue = handValue
        self.name = name
        self.isAllIn = isAllIn
        self.isAI = isAI
        self.game2 = game2
        self.card10 = card10
        
        pass
    @property
    def isAllIn(self):
        return self.__isAllIn
    @isAllIn.setter
    def isAllIn(self, isAllIn: bool):
        self.__isAllIn = isAllIn

    @property
    def chips(self):
        return self.__chips
    @chips.setter
    def chips(self, chips: int):
        self.__chips = chips

    @property
    def isFolded(self):
        return self.__isFolded
    @isFolded.setter
    def isFolded(self, isFolded: bool):
        self.__isFolded = isFolded

    @property
    def isSmallBlind(self):
        return self.__isSmallBlind
    @isSmallBlind.setter
    def isSmallBlind(self, isSmallBlind: bool):
        self.__isSmallBlind = isSmallBlind

    @property
    def isAI(self):
        return self.__isAI
    @isAI.setter
    def isAI(self, isAI: bool):
        self.__isAI = isAI

    @property
    def handValue(self):
        return self.__handValue
    @handValue.setter
    def handValue(self, handValue: int):
        self.__handValue = handValue

    @property
    def playerNumber(self):
        return self.__playerNumber
    @playerNumber.setter
    def playerNumber(self, playerNumber: int):
        self.__playerNumber = playerNumber

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: str):
        self.__hand = hand

    @property
    def isBigBlind(self):
        return self.__isBigBlind
    @isBigBlind.setter
    def isBigBlind(self, isBigBlind: bool):
        self.__isBigBlind = isBigBlind

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def card10(self):
        return self.__card10
    @card10.setter
    def card10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__card10", None)
        self.__card10 = value
        
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
    def game2(self):
        return self.__game2
    @game2.setter
    def game2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__game2", None)
        self.__game2 = value
        
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



class Card:

    def __init__(self, suit: str, value: int, DeckOfCards1: "Deck" = None, communityCards7: "CommunityCards" = None, player11: "Player" = None):
        self.suit = suit
        self.value = value
        self.DeckOfCards1 = DeckOfCards1
        self.communityCards7 = communityCards7
        self.player11 = player11
        
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
    def communityCards7(self):
        return self.__communityCards7
    @communityCards7.setter
    def communityCards7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__communityCards7", None)
        self.__communityCards7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card6"):
                opp_val = getattr(old_value, "card6", None)
                if opp_val == self:
                    setattr(old_value, "card6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card6"):
                opp_val = getattr(value, "card6", None)
                setattr(value, "card6", self)

    @property
    def DeckOfCards1(self):
        return self.__DeckOfCards1
    @DeckOfCards1.setter
    def DeckOfCards1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__DeckOfCards1", None)
        self.__DeckOfCards1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card0"):
                opp_val = getattr(old_value, "card0", None)
                if opp_val == self:
                    setattr(old_value, "card0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card0"):
                opp_val = getattr(value, "card0", None)
                setattr(value, "card0", self)

    @property
    def player11(self):
        return self.__player11
    @player11.setter
    def player11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player11", None)
        self.__player11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card10"):
                opp_val = getattr(old_value, "card10", None)
                if opp_val == self:
                    setattr(old_value, "card10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card10"):
                opp_val = getattr(value, "card10", None)
                setattr(value, "card10", self)



class Deck:

    def __init__(self, cards: str, positionInDeck: int, card0: "Card" = None, game4: "Game" = None):
        self.cards = cards
        self.positionInDeck = positionInDeck
        self.card0 = card0
        self.game4 = game4
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def positionInDeck(self):
        return self.__positionInDeck
    @positionInDeck.setter
    def positionInDeck(self, positionInDeck: int):
        self.__positionInDeck = positionInDeck

    @property
    def game4(self):
        return self.__game4
    @game4.setter
    def game4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__game4", None)
        self.__game4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deckOfCards5"):
                opp_val = getattr(old_value, "deckOfCards5", None)
                if opp_val == self:
                    setattr(old_value, "deckOfCards5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deckOfCards5"):
                opp_val = getattr(value, "deckOfCards5", None)
                setattr(value, "deckOfCards5", self)

    @property
    def card0(self):
        return self.__card0
    @card0.setter
    def card0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card0", None)
        self.__card0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeckOfCards1"):
                opp_val = getattr(old_value, "DeckOfCards1", None)
                if opp_val == self:
                    setattr(old_value, "DeckOfCards1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeckOfCards1"):
                opp_val = getattr(value, "DeckOfCards1", None)
                setattr(value, "DeckOfCards1", self)

