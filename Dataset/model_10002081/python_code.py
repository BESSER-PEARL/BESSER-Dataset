from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    pass
class CoordState(Enum):
    pass

############################################
# Definition of Classes
############################################










class Game:

    def __init__(self, done: bool, p1: Player, p2: Player, player4: set["Player"] = None):
        self.done = done
        self.p1 = p1
        self.p2 = p2
        self.player4 = player4 if player4 is not None else set()
        
        pass
    @property
    def done(self):
        return self.__done
    @done.setter
    def done(self, done: bool):
        self.__done = done

    @property
    def p1(self):
        return self.__p1
    @p1.setter
    def p1(self, p1: Player):
        self.__p1 = p1

    @property
    def p2(self):
        return self.__p2
    @p2.setter
    def p2(self, p2: Player):
        self.__p2 = p2

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
                    



class Player:

    def __init__(self, name: str, won: bool, turn: bool, board3: "Board" = None, game5: "Game" = None):
        self.name = name
        self.won = won
        self.turn = turn
        self.board3 = board3
        self.game5 = game5
        
        pass
    @property
    def won(self):
        return self.__won
    @won.setter
    def won(self, won: bool):
        self.__won = won

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def turn(self):
        return self.__turn
    @turn.setter
    def turn(self, turn: bool):
        self.__turn = turn

    @property
    def board3(self):
        return self.__board3
    @board3.setter
    def board3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__board3", None)
        self.__board3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player2"):
                opp_val = getattr(old_value, "player2", None)
                if opp_val == self:
                    setattr(old_value, "player2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player2"):
                opp_val = getattr(value, "player2", None)
                setattr(value, "player2", self)

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



class Board:

    def __init__(self, aircraftCarrier: bool, battleship: bool, submarine: bool, destroyer: bool, patrolBoat: bool, coordinates0: set["Coordinate"] = None, player2: "Player" = None):
        self.aircraftCarrier = aircraftCarrier
        self.battleship = battleship
        self.submarine = submarine
        self.destroyer = destroyer
        self.patrolBoat = patrolBoat
        self.coordinates0 = coordinates0 if coordinates0 is not None else set()
        self.player2 = player2
        
        pass
    @property
    def destroyer(self):
        return self.__destroyer
    @destroyer.setter
    def destroyer(self, destroyer: bool):
        self.__destroyer = destroyer

    @property
    def aircraftCarrier(self):
        return self.__aircraftCarrier
    @aircraftCarrier.setter
    def aircraftCarrier(self, aircraftCarrier: bool):
        self.__aircraftCarrier = aircraftCarrier

    @property
    def patrolBoat(self):
        return self.__patrolBoat
    @patrolBoat.setter
    def patrolBoat(self, patrolBoat: bool):
        self.__patrolBoat = patrolBoat

    @property
    def submarine(self):
        return self.__submarine
    @submarine.setter
    def submarine(self, submarine: bool):
        self.__submarine = submarine

    @property
    def battleship(self):
        return self.__battleship
    @battleship.setter
    def battleship(self, battleship: bool):
        self.__battleship = battleship

    @property
    def coordinates0(self):
        return self.__coordinates0
    @coordinates0.setter
    def coordinates0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board__coordinates0", None)
        self.__coordinates0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "board1"):
                    opp_val = getattr(item, "board1", None)
                    
                    if opp_val == self:
                        setattr(item, "board1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "board1"):
                    opp_val = getattr(item, "board1", None)
                    
                    setattr(item, "board1", self)
                    

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board__player2", None)
        self.__player2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board3"):
                opp_val = getattr(old_value, "board3", None)
                if opp_val == self:
                    setattr(old_value, "board3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board3"):
                opp_val = getattr(value, "board3", None)
                setattr(value, "board3", self)



class Boat:

    def __init__(self, startCoord: Coordinate, length: int, direction: Direction, MAX_LENGTH: int):
        self.startCoord = startCoord
        self.length = length
        self.direction = direction
        self.MAX_LENGTH = MAX_LENGTH
        
        pass
    @property
    def MAX_LENGTH(self):
        return self.__MAX_LENGTH
    @MAX_LENGTH.setter
    def MAX_LENGTH(self, MAX_LENGTH: int):
        self.__MAX_LENGTH = MAX_LENGTH

    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def startCoord(self):
        return self.__startCoord
    @startCoord.setter
    def startCoord(self, startCoord: Coordinate):
        self.__startCoord = startCoord

    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, direction: Direction):
        self.__direction = direction



class Coordinate:

    def __init__(self, x: int, y: int, state: CoordState, board1: "Board" = None):
        self.x = x
        self.y = y
        self.state = state
        self.board1 = board1
        
        pass
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: CoordState):
        self.__state = state

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def board1(self):
        return self.__board1
    @board1.setter
    def board1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Coordinate__board1", None)
        self.__board1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coordinates0"):
                opp_val = getattr(old_value, "coordinates0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coordinates0"):
                opp_val = getattr(value, "coordinates0", None)
                if opp_val is None:
                    setattr(value, "coordinates0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

