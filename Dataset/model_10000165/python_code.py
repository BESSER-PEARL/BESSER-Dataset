from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suit(Enum):
    pass
class Rank(Enum):
    pass

############################################
# Definition of Classes
############################################










class List_Card__external:

    pass


class PitchDealer:

    def __init__(self, Randomcards: Card1, displaycard: Card1, SelectDealer: Dealer_Interface):
        self.Randomcards = Randomcards
        self.displaycard = displaycard
        self.SelectDealer = SelectDealer
        
        pass
    @property
    def Randomcards(self):
        return self.__Randomcards
    @Randomcards.setter
    def Randomcards(self, Randomcards: Card1):
        self.__Randomcards = Randomcards

    @property
    def SelectDealer(self):
        return self.__SelectDealer
    @SelectDealer.setter
    def SelectDealer(self, SelectDealer: Dealer_Interface):
        self.__SelectDealer = SelectDealer

    @property
    def displaycard(self):
        return self.__displaycard
    @displaycard.setter
    def displaycard(self, displaycard: Card1):
        self.__displaycard = displaycard



class Pitch1:

    def __init__(self, TotalDealer: Dealer_Type_Interface):
        self.TotalDealer = TotalDealer
        
        pass
    @property
    def TotalDealer(self):
        return self.__TotalDealer
    @TotalDealer.setter
    def TotalDealer(self, TotalDealer: Dealer_Type_Interface):
        self.__TotalDealer = TotalDealer



class Rank1:

    def __init__(self, intCard_value: int):
        self.intCard_value = intCard_value
        
        pass
    @property
    def intCard_value(self):
        return self.__intCard_value
    @intCard_value.setter
    def intCard_value(self, intCard_value: int):
        self.__intCard_value = intCard_value



class Home:

    pass


class Dealer_Type_Interface:

    pass


class Dealer_Interface:

    pass


class Al_player:

    def __init__(self, bet: int, points: int):
        self.bet = bet
        self.points = points
        
        pass
    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet

    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: int):
        self.__points = points



class Player1:

    def __init__(self, id: str, bet: int, points: int):
        self.id = id
        self.bet = bet
        self.points = points
        
        pass
    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet



class Deck1:

    def __init__(self, Totalcards: int):
        self.Totalcards = Totalcards
        
        pass
    @property
    def Totalcards(self):
        return self.__Totalcards
    @Totalcards.setter
    def Totalcards(self, Totalcards: int):
        self.__Totalcards = Totalcards



class cardType:

    def __init__(self, Heart: cardType, Diamond: cardType, Spades: cardType, club: cardType):
        self.Heart = Heart
        self.Diamond = Diamond
        self.Spades = Spades
        self.club = club
        
        pass
    @property
    def Diamond(self):
        return self.__Diamond
    @Diamond.setter
    def Diamond(self, Diamond: cardType):
        self.__Diamond = Diamond

    @property
    def club(self):
        return self.__club
    @club.setter
    def club(self, club: cardType):
        self.__club = club

    @property
    def Heart(self):
        return self.__Heart
    @Heart.setter
    def Heart(self, Heart: cardType):
        self.__Heart = Heart

    @property
    def Spades(self):
        return self.__Spades
    @Spades.setter
    def Spades(self, Spades: cardType):
        self.__Spades = Spades



class Card1:

    def __init__(self, suit: Suit, Rank: Rank, total_card: str, cardsRemianing: int):
        self.suit = suit
        self.Rank = Rank
        self.total_card = total_card
        self.cardsRemianing = cardsRemianing
        
        pass
    @property
    def total_card(self):
        return self.__total_card
    @total_card.setter
    def total_card(self, total_card: str):
        self.__total_card = total_card

    @property
    def cardsRemianing(self):
        return self.__cardsRemianing
    @cardsRemianing.setter
    def cardsRemianing(self, cardsRemianing: int):
        self.__cardsRemianing = cardsRemianing

    @property
    def Rank(self):
        return self.__Rank
    @Rank.setter
    def Rank(self, Rank: Rank):
        self.__Rank = Rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit):
        self.__suit = suit



class Pitch:

    pass


class Game:

    def __init__(self, dealerCards: str, playerCards: str, deck7: "Deck" = None, blackJackMain8: "Pitch" = None):
        self.dealerCards = dealerCards
        self.playerCards = playerCards
        self.deck7 = deck7
        self.blackJackMain8 = blackJackMain8
        
        pass
    @property
    def dealerCards(self):
        return self.__dealerCards
    @dealerCards.setter
    def dealerCards(self, dealerCards: str):
        self.__dealerCards = dealerCards

    @property
    def playerCards(self):
        return self.__playerCards
    @playerCards.setter
    def playerCards(self, playerCards: str):
        self.__playerCards = playerCards

    @property
    def blackJackMain8(self):
        return self.__blackJackMain8
    @blackJackMain8.setter
    def blackJackMain8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__blackJackMain8", None)
        self.__blackJackMain8 = value
        
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

    @property
    def deck7(self):
        return self.__deck7
    @deck7.setter
    def deck7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__deck7", None)
        self.__deck7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game6"):
                opp_val = getattr(old_value, "game6", None)
                if opp_val == self:
                    setattr(old_value, "game6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game6"):
                opp_val = getattr(value, "game6", None)
                setattr(value, "game6", self)



class Player:

    def __init__(self, bet: int, ID: str, deck2: "Deck" = None, blackJackMain10: "Pitch" = None):
        self.bet = bet
        self.ID = ID
        self.deck2 = deck2
        self.blackJackMain10 = blackJackMain10
        
        pass
    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def deck2(self):
        return self.__deck2
    @deck2.setter
    def deck2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__deck2", None)
        self.__deck2 = value
        
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

    @property
    def blackJackMain10(self):
        return self.__blackJackMain10
    @blackJackMain10.setter
    def blackJackMain10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__blackJackMain10", None)
        self.__blackJackMain10 = value
        
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



class Deck:

    def __init__(self, deck: str, cardsDealt: str, card1: "Card" = None, player3: "Player" = None, list_Card_5: "List_Card__external" = None, game6: "Game" = None):
        self.deck = deck
        self.cardsDealt = cardsDealt
        self.card1 = card1
        self.player3 = player3
        self.list_Card_5 = list_Card_5
        self.game6 = game6
        
        pass
    @property
    def cardsDealt(self):
        return self.__cardsDealt
    @cardsDealt.setter
    def cardsDealt(self, cardsDealt: str):
        self.__cardsDealt = cardsDealt

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card1", None)
        self.__card1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck0"):
                opp_val = getattr(old_value, "deck0", None)
                if opp_val == self:
                    setattr(old_value, "deck0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck0"):
                opp_val = getattr(value, "deck0", None)
                setattr(value, "deck0", self)

    @property
    def game6(self):
        return self.__game6
    @game6.setter
    def game6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__game6", None)
        self.__game6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck7"):
                opp_val = getattr(old_value, "deck7", None)
                if opp_val == self:
                    setattr(old_value, "deck7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck7"):
                opp_val = getattr(value, "deck7", None)
                setattr(value, "deck7", self)

    @property
    def list_Card_5(self):
        return self.__list_Card_5
    @list_Card_5.setter
    def list_Card_5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__list_Card_5", None)
        self.__list_Card_5 = value
        
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
    def player3(self):
        return self.__player3
    @player3.setter
    def player3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__player3", None)
        self.__player3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck2"):
                opp_val = getattr(old_value, "deck2", None)
                if opp_val == self:
                    setattr(old_value, "deck2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck2"):
                opp_val = getattr(value, "deck2", None)
                setattr(value, "deck2", self)



class Card:

    def __init__(self, rank: Rank, suit: Suit, deck0: "Deck" = None):
        self.rank = rank
        self.suit = suit
        self.deck0 = deck0
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: Rank):
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit):
        self.__suit = suit

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
                if opp_val == self:
                    setattr(old_value, "card1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card1"):
                opp_val = getattr(value, "card1", None)
                setattr(value, "card1", self)

