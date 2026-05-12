from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CardName(Enum):
    pass
class Suit(Enum):
    pass
class CardName1(Enum):
    pass

############################################
# Definition of Classes
############################################










class Dealer_Interface:

    pass


class Gambler_Interface:

    pass


class HandDeck:

    def __init__(self, stand: bool, naturalBlackJack: bool, pair: bool, bust: bool):
        self.stand = stand
        self.naturalBlackJack = naturalBlackJack
        self.pair = pair
        self.bust = bust
        
        pass
    @property
    def bust(self):
        return self.__bust
    @bust.setter
    def bust(self, bust: bool):
        self.__bust = bust

    @property
    def stand(self):
        return self.__stand
    @stand.setter
    def stand(self, stand: bool):
        self.__stand = stand

    @property
    def pair(self):
        return self.__pair
    @pair.setter
    def pair(self, pair: bool):
        self.__pair = pair

    @property
    def naturalBlackJack(self):
        return self.__naturalBlackJack
    @naturalBlackJack.setter
    def naturalBlackJack(self, naturalBlackJack: bool):
        self.__naturalBlackJack = naturalBlackJack



class BJPlayer:

    def __init__(self, bet: int, hands: str):
        self.bet = bet
        self.hands = hands
        
        pass
    @property
    def hands(self):
        return self.__hands
    @hands.setter
    def hands(self, hands: str):
        self.__hands = hands

    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet



class Deck:

    pass


class StandardCard:

    def __init__(self, suit: str, standardCard: bool, cardName: CardName):
        self.suit = suit
        self.standardCard = standardCard
        self.cardName = cardName
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def cardName(self):
        return self.__cardName
    @cardName.setter
    def cardName(self, cardName: CardName):
        self.__cardName = cardName

    @property
    def standardCard(self):
        return self.__standardCard
    @standardCard.setter
    def standardCard(self, standardCard: bool):
        self.__standardCard = standardCard



class JokerCard:

    def __init__(self, jokerCard: bool, red: bool):
        self.jokerCard = jokerCard
        self.red = red
        
        pass
    @property
    def jokerCard(self):
        return self.__jokerCard
    @jokerCard.setter
    def jokerCard(self, jokerCard: bool):
        self.__jokerCard = jokerCard

    @property
    def red(self):
        return self.__red
    @red.setter
    def red(self, red: bool):
        self.__red = red



class StandCard:

    pass


class PlayingCard:

    def __init__(self, jokerCard: bool, standardCard: bool, faceUp: bool):
        self.jokerCard = jokerCard
        self.standardCard = standardCard
        self.faceUp = faceUp
        
        pass
    @property
    def jokerCard(self):
        return self.__jokerCard
    @jokerCard.setter
    def jokerCard(self, jokerCard: bool):
        self.__jokerCard = jokerCard

    @property
    def faceUp(self):
        return self.__faceUp
    @faceUp.setter
    def faceUp(self, faceUp: bool):
        self.__faceUp = faceUp

    @property
    def standardCard(self):
        return self.__standardCard
    @standardCard.setter
    def standardCard(self, standardCard: bool):
        self.__standardCard = standardCard



class Player:

    def __init__(self, name: str, pocket: int):
        self.name = name
        self.pocket = pocket
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pocket(self):
        return self.__pocket
    @pocket.setter
    def pocket(self, pocket: int):
        self.__pocket = pocket

