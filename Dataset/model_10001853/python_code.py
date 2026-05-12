from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Chat:

    def __init__(self, commands: str, username: str):
        self.commands = commands
        self.username = username
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def commands(self):
        return self.__commands
    @commands.setter
    def commands(self, commands: str):
        self.__commands = commands



class Position:

    def __init__(self, x: int, y: int, has_flag: bool, is_hidden: bool, mineField5: "MineField" = None):
        self.x = x
        self.y = y
        self.has_flag = has_flag
        self.is_hidden = is_hidden
        self.mineField5 = mineField5
        
        pass
    @property
    def has_flag(self):
        return self.__has_flag
    @has_flag.setter
    def has_flag(self, has_flag: bool):
        self.__has_flag = has_flag

    @property
    def is_hidden(self):
        return self.__is_hidden
    @is_hidden.setter
    def is_hidden(self, is_hidden: bool):
        self.__is_hidden = is_hidden

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def mineField5(self):
        return self.__mineField5
    @mineField5.setter
    def mineField5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Position__mineField5", None)
        self.__mineField5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "position4"):
                opp_val = getattr(old_value, "position4", None)
                if opp_val == self:
                    setattr(old_value, "position4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "position4"):
                opp_val = getattr(value, "position4", None)
                setattr(value, "position4", self)



class Class:

    pass


class MineField:

    def __init__(self, grid: str, height: int, width: int, game3: "Game" = None, position4: "Position" = None):
        self.grid = grid
        self.height = height
        self.width = width
        self.game3 = game3
        self.position4 = position4
        
        pass
    @property
    def grid(self):
        return self.__grid
    @grid.setter
    def grid(self, grid: str):
        self.__grid = grid

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def game3(self):
        return self.__game3
    @game3.setter
    def game3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MineField__game3", None)
        self.__game3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mineField2"):
                opp_val = getattr(old_value, "mineField2", None)
                if opp_val == self:
                    setattr(old_value, "mineField2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mineField2"):
                opp_val = getattr(value, "mineField2", None)
                setattr(value, "mineField2", self)

    @property
    def position4(self):
        return self.__position4
    @position4.setter
    def position4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MineField__position4", None)
        self.__position4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mineField5"):
                opp_val = getattr(old_value, "mineField5", None)
                if opp_val == self:
                    setattr(old_value, "mineField5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mineField5"):
                opp_val = getattr(value, "mineField5", None)
                setattr(value, "mineField5", self)



class Game:

    def __init__(self, time_keeper: Timer, mine_field: MineField, score: int, timer0: "Timer" = None, mineField2: "MineField" = None):
        self.time_keeper = time_keeper
        self.mine_field = mine_field
        self.score = score
        self.timer0 = timer0
        self.mineField2 = mineField2
        
        pass
    @property
    def time_keeper(self):
        return self.__time_keeper
    @time_keeper.setter
    def time_keeper(self, time_keeper: Timer):
        self.__time_keeper = time_keeper

    @property
    def mine_field(self):
        return self.__mine_field
    @mine_field.setter
    def mine_field(self, mine_field: MineField):
        self.__mine_field = mine_field

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def mineField2(self):
        return self.__mineField2
    @mineField2.setter
    def mineField2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__mineField2", None)
        self.__mineField2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game3"):
                opp_val = getattr(old_value, "game3", None)
                if opp_val == self:
                    setattr(old_value, "game3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game3"):
                opp_val = getattr(value, "game3", None)
                setattr(value, "game3", self)

    @property
    def timer0(self):
        return self.__timer0
    @timer0.setter
    def timer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__timer0", None)
        self.__timer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game1"):
                opp_val = getattr(old_value, "game1", None)
                if opp_val == self:
                    setattr(old_value, "game1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game1"):
                opp_val = getattr(value, "game1", None)
                setattr(value, "game1", self)



class Timer:

    def __init__(self, start: int, ticks: int, game1: "Game" = None):
        self.start = start
        self.ticks = ticks
        self.game1 = game1
        
        pass
    @property
    def ticks(self):
        return self.__ticks
    @ticks.setter
    def ticks(self, ticks: int):
        self.__ticks = ticks

    @property
    def start(self):
        return self.__start
    @start.setter
    def start(self, start: int):
        self.__start = start

    @property
    def game1(self):
        return self.__game1
    @game1.setter
    def game1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Timer__game1", None)
        self.__game1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timer0"):
                opp_val = getattr(old_value, "timer0", None)
                if opp_val == self:
                    setattr(old_value, "timer0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timer0"):
                opp_val = getattr(value, "timer0", None)
                setattr(value, "timer0", self)

