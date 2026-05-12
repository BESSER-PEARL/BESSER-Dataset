from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class StartGame:

    def __init__(self, deck: Deck, p1: Player, p2: Player, p3: Player, p4: Player, playerOrder: str, t1: Team, t2: Team, trick: Trick, lead: int, turn: int, bidNumber: int, player6: set["Player"] = None, team8: set["Team"] = None, deck10: set["Deck"] = None, trick12: set["Trick"] = None):
        self.deck = deck
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.playerOrder = playerOrder
        self.t1 = t1
        self.t2 = t2
        self.trick = trick
        self.lead = lead
        self.turn = turn
        self.bidNumber = bidNumber
        self.player6 = player6 if player6 is not None else set()
        self.team8 = team8 if team8 is not None else set()
        self.deck10 = deck10 if deck10 is not None else set()
        self.trick12 = trick12 if trick12 is not None else set()
        
        pass
    @property
    def p2(self):
        return self.__p2
    @p2.setter
    def p2(self, p2: Player):
        self.__p2 = p2

    @property
    def p3(self):
        return self.__p3
    @p3.setter
    def p3(self, p3: Player):
        self.__p3 = p3

    @property
    def playerOrder(self):
        return self.__playerOrder
    @playerOrder.setter
    def playerOrder(self, playerOrder: str):
        self.__playerOrder = playerOrder

    @property
    def bidNumber(self):
        return self.__bidNumber
    @bidNumber.setter
    def bidNumber(self, bidNumber: int):
        self.__bidNumber = bidNumber

    @property
    def p4(self):
        return self.__p4
    @p4.setter
    def p4(self, p4: Player):
        self.__p4 = p4

    @property
    def trick(self):
        return self.__trick
    @trick.setter
    def trick(self, trick: Trick):
        self.__trick = trick

    @property
    def turn(self):
        return self.__turn
    @turn.setter
    def turn(self, turn: int):
        self.__turn = turn

    @property
    def lead(self):
        return self.__lead
    @lead.setter
    def lead(self, lead: int):
        self.__lead = lead

    @property
    def t2(self):
        return self.__t2
    @t2.setter
    def t2(self, t2: Team):
        self.__t2 = t2

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

    @property
    def t1(self):
        return self.__t1
    @t1.setter
    def t1(self, t1: Team):
        self.__t1 = t1

    @property
    def p1(self):
        return self.__p1
    @p1.setter
    def p1(self, p1: Player):
        self.__p1 = p1

    @property
    def trick12(self):
        return self.__trick12
    @trick12.setter
    def trick12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StartGame__trick12", None)
        self.__trick12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "startGame13"):
                    opp_val = getattr(item, "startGame13", None)
                    
                    if opp_val == self:
                        setattr(item, "startGame13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "startGame13"):
                    opp_val = getattr(item, "startGame13", None)
                    
                    setattr(item, "startGame13", self)
                    

    @property
    def team8(self):
        return self.__team8
    @team8.setter
    def team8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StartGame__team8", None)
        self.__team8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "startGame9"):
                    opp_val = getattr(item, "startGame9", None)
                    
                    if opp_val == self:
                        setattr(item, "startGame9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "startGame9"):
                    opp_val = getattr(item, "startGame9", None)
                    
                    setattr(item, "startGame9", self)
                    

    @property
    def player6(self):
        return self.__player6
    @player6.setter
    def player6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StartGame__player6", None)
        self.__player6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "startGame7"):
                    opp_val = getattr(item, "startGame7", None)
                    
                    if opp_val == self:
                        setattr(item, "startGame7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "startGame7"):
                    opp_val = getattr(item, "startGame7", None)
                    
                    setattr(item, "startGame7", self)
                    

    @property
    def deck10(self):
        return self.__deck10
    @deck10.setter
    def deck10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StartGame__deck10", None)
        self.__deck10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "startGame11"):
                    opp_val = getattr(item, "startGame11", None)
                    
                    if opp_val == self:
                        setattr(item, "startGame11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "startGame11"):
                    opp_val = getattr(item, "startGame11", None)
                    
                    setattr(item, "startGame11", self)
                    



class Trick:

    def __init__(self, suitLead: int, startGame13: "StartGame" = None):
        self.suitLead = suitLead
        self.startGame13 = startGame13
        
        pass
    @property
    def suitLead(self):
        return self.__suitLead
    @suitLead.setter
    def suitLead(self, suitLead: int):
        self.__suitLead = suitLead

    @property
    def startGame13(self):
        return self.__startGame13
    @startGame13.setter
    def startGame13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trick__startGame13", None)
        self.__startGame13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trick12"):
                opp_val = getattr(old_value, "trick12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trick12"):
                opp_val = getattr(value, "trick12", None)
                if opp_val is None:
                    setattr(value, "trick12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Team:

    def __init__(self, p1: Player, p2: Player, score: int, player2: "Player" = None, startGame9: "StartGame" = None):
        self.p1 = p1
        self.p2 = p2
        self.score = score
        self.player2 = player2
        self.startGame9 = startGame9
        
        pass
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def p2(self):
        return self.__p2
    @p2.setter
    def p2(self, p2: Player):
        self.__p2 = p2

    @property
    def p1(self):
        return self.__p1
    @p1.setter
    def p1(self, p1: Player):
        self.__p1 = p1

    @property
    def startGame9(self):
        return self.__startGame9
    @startGame9.setter
    def startGame9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Team__startGame9", None)
        self.__startGame9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "team8"):
                opp_val = getattr(old_value, "team8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "team8"):
                opp_val = getattr(value, "team8", None)
                if opp_val is None:
                    setattr(value, "team8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Team__player2", None)
        self.__player2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "team3"):
                opp_val = getattr(old_value, "team3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "team3"):
                opp_val = getattr(value, "team3", None)
                if opp_val is None:
                    setattr(value, "team3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Player:

    def __init__(self, name: str, number: int, score: int, hand: Hand, team3: set["Team"] = None, hand4: "Hand" = None, startGame7: "StartGame" = None):
        self.name = name
        self.number = number
        self.score = score
        self.hand = hand
        self.team3 = team3 if team3 is not None else set()
        self.hand4 = hand4
        self.startGame7 = startGame7
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def hand(self, hand: Hand):
        self.__hand = hand

    @property
    def startGame7(self):
        return self.__startGame7
    @startGame7.setter
    def startGame7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__startGame7", None)
        self.__startGame7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player6"):
                opp_val = getattr(old_value, "player6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player6"):
                opp_val = getattr(value, "player6", None)
                if opp_val is None:
                    setattr(value, "player6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def team3(self):
        return self.__team3
    @team3.setter
    def team3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__team3", None)
        self.__team3 = value if value is not None else set()
        
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
                    

    @property
    def hand4(self):
        return self.__hand4
    @hand4.setter
    def hand4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__hand4", None)
        self.__hand4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player5"):
                opp_val = getattr(old_value, "player5", None)
                if opp_val == self:
                    setattr(old_value, "player5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player5"):
                opp_val = getattr(value, "player5", None)
                setattr(value, "player5", self)



class HandSorter:

    pass


class Hand:

    pass


class Deck:

    pass


class Group:

    def __init__(self, contents: str, card1: set["Card"] = None):
        self.contents = contents
        self.card1 = card1 if card1 is not None else set()
        
        pass
    @property
    def contents(self):
        return self.__contents
    @contents.setter
    def contents(self, contents: str):
        self.__contents = contents

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Group__card1", None)
        self.__card1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "group0"):
                    opp_val = getattr(item, "group0", None)
                    
                    if opp_val == self:
                        setattr(item, "group0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "group0"):
                    opp_val = getattr(item, "group0", None)
                    
                    setattr(item, "group0", self)
                    



class Card:

    def __init__(self, suit: int, rank: int, isDouble: bool, points: int, group0: "Group" = None):
        self.suit = suit
        self.rank = rank
        self.isDouble = isDouble
        self.points = points
        self.group0 = group0
        
        pass
    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def isDouble(self):
        return self.__isDouble
    @isDouble.setter
    def isDouble(self, isDouble: bool):
        self.__isDouble = isDouble

    @property
    def group0(self):
        return self.__group0
    @group0.setter
    def group0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__group0", None)
        self.__group0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card1"):
                opp_val = getattr(old_value, "card1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card1"):
                opp_val = getattr(value, "card1", None)
                if opp_val is None:
                    setattr(value, "card1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class int_Interface:

    pass
