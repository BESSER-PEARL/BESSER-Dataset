from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ElevensGame:

    def __init__(self, creates_Play_and_Deck: Deck):
        self.creates_Play_and_Deck = creates_Play_and_Deck
        
        pass
    @property
    def creates_Play_and_Deck(self):
        return self.__creates_Play_and_Deck
    @creates_Play_and_Deck.setter
    def creates_Play_and_Deck(self, creates_Play_and_Deck: Deck):
        self.__creates_Play_and_Deck = creates_Play_and_Deck



class Deck:

    def __init__(self, creates_and_shuffles: card):
        self.creates_and_shuffles = creates_and_shuffles
        
        pass
    @property
    def creates_and_shuffles(self):
        return self.__creates_and_shuffles
    @creates_and_shuffles.setter
    def creates_and_shuffles(self, creates_and_shuffles: card):
        self.__creates_and_shuffles = creates_and_shuffles



class Player:

    def __init__(self, has_a: card):
        self.has_a = has_a
        
        pass
    @property
    def has_a(self):
        return self.__has_a
    @has_a.setter
    def has_a(self, has_a: card):
        self.__has_a = has_a



class cardValue:

    def __init__(self, Ace: cardValue, King: cardValue, Queen: cardValue, Jack: cardValue):
        self.Ace = Ace
        self.King = King
        self.Queen = Queen
        self.Jack = Jack
        
        pass
    @property
    def King(self):
        return self.__King
    @King.setter
    def King(self, King: cardValue):
        self.__King = King

    @property
    def Jack(self):
        return self.__Jack
    @Jack.setter
    def Jack(self, Jack: cardValue):
        self.__Jack = Jack

    @property
    def Queen(self):
        return self.__Queen
    @Queen.setter
    def Queen(self, Queen: cardValue):
        self.__Queen = Queen

    @property
    def Ace(self):
        return self.__Ace
    @Ace.setter
    def Ace(self, Ace: cardValue):
        self.__Ace = Ace



class cardFace:

    def __init__(self, Club: cardFace, has_a: cardValue):
        self.Club = Club
        self.has_a = has_a
        
        pass
    @property
    def has_a(self):
        return self.__has_a
    @has_a.setter
    def has_a(self, has_a: cardValue):
        self.__has_a = has_a

    @property
    def Club(self):
        return self.__Club
    @Club.setter
    def Club(self, Club: cardFace):
        self.__Club = Club



class card:

    def __init__(self, has_a: cardFace, has_a1: cardValue):
        self.has_a = has_a
        self.has_a1 = has_a1
        
        pass
    @property
    def has_a1(self):
        return self.__has_a1
    @has_a1.setter
    def has_a1(self, has_a1: cardValue):
        self.__has_a1 = has_a1

    @property
    def has_a(self):
        return self.__has_a
    @has_a.setter
    def has_a(self, has_a: cardFace):
        self.__has_a = has_a

