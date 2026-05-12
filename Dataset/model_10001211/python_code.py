from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MatchingGame:

    pass


class TrickGame:

    pass


class SheddingGame:

    pass


class Player:

    def __init__(self, hand: str, score: int, card3: set["Card"] = None, game5: "Game" = None):
        self.hand = hand
        self.score = score
        self.card3 = card3 if card3 is not None else set()
        self.game5 = game5
        
        pass
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: str):
        self.__hand = hand

    @property
    def game5(self):
        return self.__game5
    @game5.setter
    def game5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__game5", None)
        self.__game5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player4"):
                opp_val = getattr(old_value, "player4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player4"):
                opp_val = getattr(value, "player4", None)
                if opp_val is None:
                    setattr(value, "player4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def card3(self):
        return self.__card3
    @card3.setter
    def card3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__card3", None)
        self.__card3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player2"):
                    opp_val = getattr(item, "player2", None)
                    
                    if opp_val == self:
                        setattr(item, "player2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player2"):
                    opp_val = getattr(item, "player2", None)
                    
                    setattr(item, "player2", self)
                    



class Game:

    def __init__(self, players: str, round: int, winner: Player, player4: set["Player"] = None, deck6: "Deck" = None):
        self.players = players
        self.round = round
        self.winner = winner
        self.player4 = player4 if player4 is not None else set()
        self.deck6 = deck6
        
        pass
    @property
    def round(self):
        return self.__round
    @round.setter
    def round(self, round: int):
        self.__round = round

    @property
    def winner(self):
        return self.__winner
    @winner.setter
    def winner(self, winner: Player):
        self.__winner = winner

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

    @property
    def deck6(self):
        return self.__deck6
    @deck6.setter
    def deck6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__deck6", None)
        self.__deck6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game7"):
                opp_val = getattr(old_value, "game7", None)
                if opp_val == self:
                    setattr(old_value, "game7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game7"):
                opp_val = getattr(value, "game7", None)
                setattr(value, "game7", self)

    @property
    def player4(self):
        return self.__player4
    @player4.setter
    def player4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__player4", None)
        self.__player4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game5"):
                    opp_val = getattr(item, "game5", None)
                    
                    if opp_val == self:
                        setattr(item, "game5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game5"):
                    opp_val = getattr(item, "game5", None)
                    
                    setattr(item, "game5", self)
                    



class Deck:

    def __init__(self, deck: str, card0: set["Card"] = None, game7: "Game" = None):
        self.deck = deck
        self.card0 = card0 if card0 is not None else set()
        self.game7 = game7
        
        pass
    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def card0(self):
        return self.__card0
    @card0.setter
    def card0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card0", None)
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
                    

    @property
    def game7(self):
        return self.__game7
    @game7.setter
    def game7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__game7", None)
        self.__game7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck6"):
                opp_val = getattr(old_value, "deck6", None)
                if opp_val == self:
                    setattr(old_value, "deck6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck6"):
                opp_val = getattr(value, "deck6", None)
                setattr(value, "deck6", self)



class Card:

    def __init__(self, value: int, suit: str, deck1: "Deck" = None, player2: "Player" = None):
        self.value = value
        self.suit = suit
        self.deck1 = deck1
        self.player2 = player2
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player2", None)
        self.__player2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card3"):
                opp_val = getattr(old_value, "card3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card3"):
                opp_val = getattr(value, "card3", None)
                if opp_val is None:
                    setattr(value, "card3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deck1(self):
        return self.__deck1
    @deck1.setter
    def deck1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck1", None)
        self.__deck1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card0"):
                opp_val = getattr(old_value, "card0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card0"):
                opp_val = getattr(value, "card0", None)
                if opp_val is None:
                    setattr(value, "card0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

