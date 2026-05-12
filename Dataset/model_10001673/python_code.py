from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Face(Enum):
    pass
class Face1(Enum):
    pass

############################################
# Definition of Classes
############################################










class Rules:

    def __init__(self, card1: Face1, card2: Face1, card3: Face1, game7: set["Game"] = None):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.game7 = game7 if game7 is not None else set()
        
        pass
    @property
    def card3(self):
        return self.__card3
    @card3.setter
    def card3(self, card3: Face1):
        self.__card3 = card3

    @property
    def card2(self):
        return self.__card2
    @card2.setter
    def card2(self, card2: Face1):
        self.__card2 = card2

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, card1: Face1):
        self.__card1 = card1

    @property
    def game7(self):
        return self.__game7
    @game7.setter
    def game7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rules__game7", None)
        self.__game7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rules6"):
                    opp_val = getattr(item, "rules6", None)
                    
                    if opp_val == self:
                        setattr(item, "rules6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rules6"):
                    opp_val = getattr(item, "rules6", None)
                    
                    setattr(item, "rules6", self)
                    



class Game:

    def __init__(self, numGames: int, numWins: int, numLose: int, player5: "Player" = None, rules6: "Rules" = None):
        self.numGames = numGames
        self.numWins = numWins
        self.numLose = numLose
        self.player5 = player5
        self.rules6 = rules6
        
        pass
    @property
    def numWins(self):
        return self.__numWins
    @numWins.setter
    def numWins(self, numWins: int):
        self.__numWins = numWins

    @property
    def numLose(self):
        return self.__numLose
    @numLose.setter
    def numLose(self, numLose: int):
        self.__numLose = numLose

    @property
    def numGames(self):
        return self.__numGames
    @numGames.setter
    def numGames(self, numGames: int):
        self.__numGames = numGames

    @property
    def rules6(self):
        return self.__rules6
    @rules6.setter
    def rules6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__rules6", None)
        self.__rules6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game7"):
                opp_val = getattr(old_value, "game7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game7"):
                opp_val = getattr(value, "game7", None)
                if opp_val is None:
                    setattr(value, "game7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def player5(self):
        return self.__player5
    @player5.setter
    def player5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__player5", None)
        self.__player5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game4"):
                opp_val = getattr(old_value, "game4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game4"):
                opp_val = getattr(value, "game4", None)
                if opp_val is None:
                    setattr(value, "game4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Player:

    def __init__(self, numMoves: int, deck2: "Deck" = None, game4: set["Game"] = None):
        self.numMoves = numMoves
        self.deck2 = deck2
        self.game4 = game4 if game4 is not None else set()
        
        pass
    @property
    def numMoves(self):
        return self.__numMoves
    @numMoves.setter
    def numMoves(self, numMoves: int):
        self.__numMoves = numMoves

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
    def game4(self):
        return self.__game4
    @game4.setter
    def game4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__game4", None)
        self.__game4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player5"):
                    opp_val = getattr(item, "player5", None)
                    
                    if opp_val == self:
                        setattr(item, "player5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player5"):
                    opp_val = getattr(item, "player5", None)
                    
                    setattr(item, "player5", self)
                    



class Card:

    def __init__(self, Enum: Face1, deck1: "Deck" = None):
        self.Enum = Enum
        self.deck1 = deck1
        
        pass
    @property
    def Enum(self):
        return self.__Enum
    @Enum.setter
    def Enum(self, Enum: Face1):
        self.__Enum = Enum

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



class Deck:

    def __init__(self, numCards: int, card0: set["Card"] = None, player3: "Player" = None):
        self.numCards = numCards
        self.card0 = card0 if card0 is not None else set()
        self.player3 = player3
        
        pass
    @property
    def numCards(self):
        return self.__numCards
    @numCards.setter
    def numCards(self, numCards: int):
        self.__numCards = numCards

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
                    

