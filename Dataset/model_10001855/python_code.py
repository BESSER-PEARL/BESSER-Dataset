from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class CardDeckInterface:

    def __init__(self, draw: Card, shuffle: str, size: int, card1: "Card" = None):
        self.draw = draw
        self.shuffle = shuffle
        self.size = size
        self.card1 = card1
        
        pass
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def shuffle(self):
        return self.__shuffle
    @shuffle.setter
    def shuffle(self, shuffle: str):
        self.__shuffle = shuffle

    @property
    def draw(self):
        return self.__draw
    @draw.setter
    def draw(self, draw: Card):
        self.__draw = draw

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CardDeckInterface__card1", None)
        self.__card1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cardDeckInterface0"):
                opp_val = getattr(old_value, "cardDeckInterface0", None)
                if opp_val == self:
                    setattr(old_value, "cardDeckInterface0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cardDeckInterface0"):
                opp_val = getattr(value, "cardDeckInterface0", None)
                setattr(value, "cardDeckInterface0", self)



class Class:

    pass


class Card:

    def __init__(self, Clubs: str, Hearts: str, Spades: str, Diamonds: str, Ace___14: int, King_13: int, Queen_12: int, Jack_11: int, suit: str, face: int, cardDeckInterface0: "CardDeckInterface" = None):
        self.Clubs = Clubs
        self.Hearts = Hearts
        self.Spades = Spades
        self.Diamonds = Diamonds
        self.Ace___14 = Ace___14
        self.King_13 = King_13
        self.Queen_12 = Queen_12
        self.Jack_11 = Jack_11
        self.suit = suit
        self.face = face
        self.cardDeckInterface0 = cardDeckInterface0
        
        pass
    @property
    def Diamonds(self):
        return self.__Diamonds
    @Diamonds.setter
    def Diamonds(self, Diamonds: str):
        self.__Diamonds = Diamonds

    @property
    def Ace___14(self):
        return self.__Ace___14
    @Ace___14.setter
    def Ace___14(self, Ace___14: int):
        self.__Ace___14 = Ace___14

    @property
    def face(self):
        return self.__face
    @face.setter
    def face(self, face: int):
        self.__face = face

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def Jack_11(self):
        return self.__Jack_11
    @Jack_11.setter
    def Jack_11(self, Jack_11: int):
        self.__Jack_11 = Jack_11

    @property
    def Clubs(self):
        return self.__Clubs
    @Clubs.setter
    def Clubs(self, Clubs: str):
        self.__Clubs = Clubs

    @property
    def Hearts(self):
        return self.__Hearts
    @Hearts.setter
    def Hearts(self, Hearts: str):
        self.__Hearts = Hearts

    @property
    def Spades(self):
        return self.__Spades
    @Spades.setter
    def Spades(self, Spades: str):
        self.__Spades = Spades

    @property
    def King_13(self):
        return self.__King_13
    @King_13.setter
    def King_13(self, King_13: int):
        self.__King_13 = King_13

    @property
    def Queen_12(self):
        return self.__Queen_12
    @Queen_12.setter
    def Queen_12(self, Queen_12: int):
        self.__Queen_12 = Queen_12

    @property
    def cardDeckInterface0(self):
        return self.__cardDeckInterface0
    @cardDeckInterface0.setter
    def cardDeckInterface0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__cardDeckInterface0", None)
        self.__cardDeckInterface0 = value
        
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

