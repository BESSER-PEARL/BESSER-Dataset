from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration2(Enum):
    pass
class Enumeration(Enum):
    pass
class State(Enum):
    pass
class Role(Enum):
    pass
class NightAction(Enum):
    pass

############################################
# Definition of Classes
############################################










class SysMessage:

    pass


class ChatMessage:

    pass


class Room:

    pass


class Game:

    def __init__(self, turn_state: State, player0: "Player" = None):
        self.turn_state = turn_state
        self.player0 = player0
        
        pass
    @property
    def turn_state(self):
        return self.__turn_state
    @turn_state.setter
    def turn_state(self, turn_state: State):
        self.__turn_state = turn_state

    @property
    def player0(self):
        return self.__player0
    @player0.setter
    def player0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__player0", None)
        self.__player0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game1"):
                opp_val = getattr(old_value, "game1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game1"):
                opp_val = getattr(value, "game1", None)
                if opp_val is None:
                    setattr(value, "game1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Player:

    def __init__(self, role: str, isAlive: bool, votes: int, vote_for: Player, night_target: Player, game1: set["Game"] = None):
        self.role = role
        self.isAlive = isAlive
        self.votes = votes
        self.vote_for = vote_for
        self.night_target = night_target
        self.game1 = game1 if game1 is not None else set()
        
        pass
    @property
    def votes(self):
        return self.__votes
    @votes.setter
    def votes(self, votes: int):
        self.__votes = votes

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def night_target(self):
        return self.__night_target
    @night_target.setter
    def night_target(self, night_target: Player):
        self.__night_target = night_target

    @property
    def isAlive(self):
        return self.__isAlive
    @isAlive.setter
    def isAlive(self, isAlive: bool):
        self.__isAlive = isAlive

    @property
    def vote_for(self):
        return self.__vote_for
    @vote_for.setter
    def vote_for(self, vote_for: Player):
        self.__vote_for = vote_for

    @property
    def game1(self):
        return self.__game1
    @game1.setter
    def game1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__game1", None)
        self.__game1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player0"):
                    opp_val = getattr(item, "player0", None)
                    
                    if opp_val == self:
                        setattr(item, "player0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player0"):
                    opp_val = getattr(item, "player0", None)
                    
                    setattr(item, "player0", self)
                    



class Guardian:

    pass


class Seer:

    pass


class Wolf:

    pass


class Villager:

    pass


class BaseRole:

    def __init__(self, role: Role, appear_as: Role, night_action: NightAction, wins_with: Role):
        self.role = role
        self.appear_as = appear_as
        self.night_action = night_action
        self.wins_with = wins_with
        
        pass
    @property
    def wins_with(self):
        return self.__wins_with
    @wins_with.setter
    def wins_with(self, wins_with: Role):
        self.__wins_with = wins_with

    @property
    def night_action(self):
        return self.__night_action
    @night_action.setter
    def night_action(self, night_action: NightAction):
        self.__night_action = night_action

    @property
    def appear_as(self):
        return self.__appear_as
    @appear_as.setter
    def appear_as(self, appear_as: Role):
        self.__appear_as = appear_as

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role: Role):
        self.__role = role

