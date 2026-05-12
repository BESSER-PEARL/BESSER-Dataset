from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class window:

    def __init__(self, _main: str, current: cursor, x: int, y: int, columns: int, lines: int):
        self._main = _main
        self.current = current
        self.x = x
        self.y = y
        self.columns = columns
        self.lines = lines
        
        pass
    @property
    def current(self):
        return self.__current
    @current.setter
    def current(self, current: cursor):
        self.__current = current

    @property
    def columns(self):
        return self.__columns
    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

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
    def lines(self):
        return self.__lines
    @lines.setter
    def lines(self, lines: int):
        self.__lines = lines

    @property
    def _main(self):
        return self.___main
    @_main.setter
    def _main(self, _main: str):
        self.___main = _main



class cursor1:

    def __init__(self, pos_x: int, pos_y: int, limit_y: str, limit_x: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.limit_y = limit_y
        self.limit_x = limit_x
        
        pass
    @property
    def pos_y(self):
        return self.__pos_y
    @pos_y.setter
    def pos_y(self, pos_y: int):
        self.__pos_y = pos_y

    @property
    def limit_y(self):
        return self.__limit_y
    @limit_y.setter
    def limit_y(self, limit_y: str):
        self.__limit_y = limit_y

    @property
    def pos_x(self):
        return self.__pos_x
    @pos_x.setter
    def pos_x(self, pos_x: int):
        self.__pos_x = pos_x

    @property
    def limit_x(self):
        return self.__limit_x
    @limit_x.setter
    def limit_x(self, limit_x: int):
        self.__limit_x = limit_x



class sudoku_validator:

    pass


class sudoku_board1:

    def __init__(self, board_9__9_: int, fixed_9__9_: int):
        self.board_9__9_ = board_9__9_
        self.fixed_9__9_ = fixed_9__9_
        
        pass
    @property
    def fixed_9__9_(self):
        return self.__fixed_9__9_
    @fixed_9__9_.setter
    def fixed_9__9_(self, fixed_9__9_: int):
        self.__fixed_9__9_ = fixed_9__9_

    @property
    def board_9__9_(self):
        return self.__board_9__9_
    @board_9__9_.setter
    def board_9__9_(self, board_9__9_: int):
        self.__board_9__9_ = board_9__9_



class load:

    def __init__(self, file_name: str):
        self.file_name = file_name
        
        pass
    @property
    def file_name(self):
        return self.__file_name
    @file_name.setter
    def file_name(self, file_name: str):
        self.__file_name = file_name



class save:

    def __init__(self, file_name: str):
        self.file_name = file_name
        
        pass
    @property
    def file_name(self):
        return self.__file_name
    @file_name.setter
    def file_name(self, file_name: str):
        self.__file_name = file_name



class sudoku_board:

    pass


class game_board1:

    def __init__(self, board: sudoku_board):
        self.board = board
        
        pass
    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: sudoku_board):
        self.__board = board



class game_board:

    pass


class choice_window:

    def __init__(self, names_3_: str, prompt_3_: cursor, response_3_: str):
        self.names_3_ = names_3_
        self.prompt_3_ = prompt_3_
        self.response_3_ = response_3_
        
        pass
    @property
    def names_3_(self):
        return self.__names_3_
    @names_3_.setter
    def names_3_(self, names_3_: str):
        self.__names_3_ = names_3_

    @property
    def response_3_(self):
        return self.__response_3_
    @response_3_.setter
    def response_3_(self, response_3_: str):
        self.__response_3_ = response_3_

    @property
    def prompt_3_(self):
        return self.__prompt_3_
    @prompt_3_.setter
    def prompt_3_(self, prompt_3_: cursor):
        self.__prompt_3_ = prompt_3_



class cursor:

    pass
