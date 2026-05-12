from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CardSuits(Enum):
    pass

############################################
# Definition of Classes
############################################







class Display_Rulebook_UseCase:

    pass


class Display_leaderboard_UseCase:

    pass


class Amalgamate_Middle_Cards_UseCase:

    pass


class Print_Cards_text_form__UseCase:

    pass


class Automatic_play_UseCase:

    pass


class Move_a_Card_two_Spaces_UseCase:

    pass


class User_Actor:

    pass





class Move_a_Card_one_Space_external:

    pass


class Shuffle_Deck_external:

    pass


class Deal_A_Card_external:

    pass


class Deck:

    def __init__(self, card: Card, deck___: str, game23: "Game" = None, card24: set["Card"] = None):
        self.card = card
        self.deck___ = deck___
        self.game23 = game23
        self.card24 = card24 if card24 is not None else set()
        
        pass
    @property
    def card(self):
        return self.__card
    @card.setter
    def card(self, card: Card):
        self.__card = card

    @property
    def deck___(self):
        return self.__deck___
    @deck___.setter
    def deck___(self, deck___: str):
        self.__deck___ = deck___

    @property
    def card24(self):
        return self.__card24
    @card24.setter
    def card24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card24", None)
        self.__card24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck25"):
                    opp_val = getattr(item, "deck25", None)
                    
                    if opp_val == self:
                        setattr(item, "deck25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck25"):
                    opp_val = getattr(item, "deck25", None)
                    
                    setattr(item, "deck25", self)
                    

    @property
    def game23(self):
        return self.__game23
    @game23.setter
    def game23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__game23", None)
        self.__game23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck22"):
                opp_val = getattr(old_value, "deck22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck22"):
                opp_val = getattr(value, "deck22", None)
                if opp_val is None:
                    setattr(value, "deck22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Rules:

    pass


class CardTable:

    def __init__(self, stage: str, cards: Card, done: bool):
        self.stage = stage
        self.cards = cards
        self.done = done
        
        pass
    @property
    def stage(self):
        return self.__stage
    @stage.setter
    def stage(self, stage: str):
        self.__stage = stage

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Card):
        self.__cards = cards

    @property
    def done(self):
        return self.__done
    @done.setter
    def done(self, done: bool):
        self.__done = done



class Board:

    def __init__(self, scores: Card, board: Card, boardGui: Card, game21: "Game" = None):
        self.scores = scores
        self.board = board
        self.boardGui = boardGui
        self.game21 = game21
        
        pass
    @property
    def boardGui(self):
        return self.__boardGui
    @boardGui.setter
    def boardGui(self, boardGui: Card):
        self.__boardGui = boardGui

    @property
    def scores(self):
        return self.__scores
    @scores.setter
    def scores(self, scores: Card):
        self.__scores = scores

    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: Card):
        self.__board = board

    @property
    def game21(self):
        return self.__game21
    @game21.setter
    def game21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board__game21", None)
        self.__game21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board20"):
                opp_val = getattr(old_value, "board20", None)
                if opp_val == self:
                    setattr(old_value, "board20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board20"):
                opp_val = getattr(value, "board20", None)
                setattr(value, "board20", self)



class Card:

    def __init__(self, suit: CardSuits, name: str, cardNames: str, deck25: "Deck" = None):
        self.suit = suit
        self.name = name
        self.cardNames = cardNames
        self.deck25 = deck25
        
        pass
    @property
    def cardNames(self):
        return self.__cardNames
    @cardNames.setter
    def cardNames(self, cardNames: str):
        self.__cardNames = cardNames

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: CardSuits):
        self.__suit = suit

    @property
    def deck25(self):
        return self.__deck25
    @deck25.setter
    def deck25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck25", None)
        self.__deck25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card24"):
                opp_val = getattr(old_value, "card24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card24"):
                opp_val = getattr(value, "card24", None)
                if opp_val is None:
                    setattr(value, "card24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Game:

    def __init__(self, deck: Deck, board: Board, scan: str, rules18: "Rules" = None, board20: "Board" = None, deck22: set["Deck"] = None):
        self.deck = deck
        self.board = board
        self.scan = scan
        self.rules18 = rules18
        self.board20 = board20
        self.deck22 = deck22 if deck22 is not None else set()
        
        pass
    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: Board):
        self.__board = board

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

    @property
    def scan(self):
        return self.__scan
    @scan.setter
    def scan(self, scan: str):
        self.__scan = scan

    @property
    def rules18(self):
        return self.__rules18
    @rules18.setter
    def rules18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__rules18", None)
        self.__rules18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game19"):
                opp_val = getattr(old_value, "game19", None)
                if opp_val == self:
                    setattr(old_value, "game19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game19"):
                opp_val = getattr(value, "game19", None)
                setattr(value, "game19", self)

    @property
    def deck22(self):
        return self.__deck22
    @deck22.setter
    def deck22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__deck22", None)
        self.__deck22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game23"):
                    opp_val = getattr(item, "game23", None)
                    
                    if opp_val == self:
                        setattr(item, "game23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game23"):
                    opp_val = getattr(item, "game23", None)
                    
                    setattr(item, "game23", self)
                    

    @property
    def board20(self):
        return self.__board20
    @board20.setter
    def board20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__board20", None)
        self.__board20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game21"):
                opp_val = getattr(old_value, "game21", None)
                if opp_val == self:
                    setattr(old_value, "game21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game21"):
                opp_val = getattr(value, "game21", None)
                setattr(value, "game21", self)



class Game_Component:

    pass
