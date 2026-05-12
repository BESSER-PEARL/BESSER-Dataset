from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class genmymodelreverse_javax_swing_JMenuItem:

    pass


class genmymodelreverse_javax_swing_JFrame:

    pass


class genmymodelreverse_javax_swing_JPanel:

    pass


class genmymodelreverse_javax_swing_JLabel:

    pass


class genmymodelreverse_java_awt_event_MouseEvent:

    pass


class genmymodelreverse_java_awt_event_MouseAdapter(ABC):

    pass


class genmymodelreverse_java_awt_Graphics(ABC):

    pass


class Mines:

    def __init__(self, FRAME_WIDTH: int, FRAME_HEIGHT: int, statusbar: genmymodelreverse_javax_swing_JLabel, timeBar: genmymodelreverse_javax_swing_JLabel, hexCell: genmymodelreverse_javax_swing_JMenuItem, game1: "Board" = None):
        self.FRAME_WIDTH = FRAME_WIDTH
        self.FRAME_HEIGHT = FRAME_HEIGHT
        self.statusbar = statusbar
        self.timeBar = timeBar
        self.hexCell = hexCell
        self.game1 = game1
        
        pass
    @property
    def hexCell(self):
        return self.__hexCell
    @hexCell.setter
    def hexCell(self, hexCell: genmymodelreverse_javax_swing_JMenuItem):
        self.__hexCell = hexCell

    @property
    def FRAME_WIDTH(self):
        return self.__FRAME_WIDTH
    @FRAME_WIDTH.setter
    def FRAME_WIDTH(self, FRAME_WIDTH: int):
        self.__FRAME_WIDTH = FRAME_WIDTH

    @property
    def timeBar(self):
        return self.__timeBar
    @timeBar.setter
    def timeBar(self, timeBar: genmymodelreverse_javax_swing_JLabel):
        self.__timeBar = timeBar

    @property
    def statusbar(self):
        return self.__statusbar
    @statusbar.setter
    def statusbar(self, statusbar: genmymodelreverse_javax_swing_JLabel):
        self.__statusbar = statusbar

    @property
    def FRAME_HEIGHT(self):
        return self.__FRAME_HEIGHT
    @FRAME_HEIGHT.setter
    def FRAME_HEIGHT(self, FRAME_HEIGHT: int):
        self.__FRAME_HEIGHT = FRAME_HEIGHT

    @property
    def game1(self):
        return self.__game1
    @game1.setter
    def game1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mines__game1", None)
        self.__game1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mines0"):
                opp_val = getattr(old_value, "mines0", None)
                if opp_val == self:
                    setattr(old_value, "mines0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mines0"):
                opp_val = getattr(value, "mines0", None)
                setattr(value, "mines0", self)



class MinesAdapter:

    pass


class Board:

    def __init__(self, NUM_IMAGES: int, CELL_SIZE: int, COVER_FOR_CELL: int, MARK_FOR_CELL: int, EMPTY_CELL: int, MINE_CELL: int, COVERED_MINE_CELL: int, MARKED_MINE_CELL: int, DRAW_MINE: int, DRAW_COVER: int, DRAW_MARK: int, DRAW_WRONG_MARK: int, N_MINES: int, N_ROWS: int, N_COLS: int, field: str, inGame: bool, mines_left: int, img: str, all_cells: int, statusbar: genmymodelreverse_javax_swing_JLabel, timeBar: genmymodelreverse_javax_swing_JLabel, mines0: "Mines" = None):
        self.NUM_IMAGES = NUM_IMAGES
        self.CELL_SIZE = CELL_SIZE
        self.COVER_FOR_CELL = COVER_FOR_CELL
        self.MARK_FOR_CELL = MARK_FOR_CELL
        self.EMPTY_CELL = EMPTY_CELL
        self.MINE_CELL = MINE_CELL
        self.COVERED_MINE_CELL = COVERED_MINE_CELL
        self.MARKED_MINE_CELL = MARKED_MINE_CELL
        self.DRAW_MINE = DRAW_MINE
        self.DRAW_COVER = DRAW_COVER
        self.DRAW_MARK = DRAW_MARK
        self.DRAW_WRONG_MARK = DRAW_WRONG_MARK
        self.N_MINES = N_MINES
        self.N_ROWS = N_ROWS
        self.N_COLS = N_COLS
        self.field = field
        self.inGame = inGame
        self.mines_left = mines_left
        self.img = img
        self.all_cells = all_cells
        self.statusbar = statusbar
        self.timeBar = timeBar
        self.mines0 = mines0
        
        pass
    @property
    def DRAW_MARK(self):
        return self.__DRAW_MARK
    @DRAW_MARK.setter
    def DRAW_MARK(self, DRAW_MARK: int):
        self.__DRAW_MARK = DRAW_MARK

    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, img: str):
        self.__img = img

    @property
    def EMPTY_CELL(self):
        return self.__EMPTY_CELL
    @EMPTY_CELL.setter
    def EMPTY_CELL(self, EMPTY_CELL: int):
        self.__EMPTY_CELL = EMPTY_CELL

    @property
    def COVERED_MINE_CELL(self):
        return self.__COVERED_MINE_CELL
    @COVERED_MINE_CELL.setter
    def COVERED_MINE_CELL(self, COVERED_MINE_CELL: int):
        self.__COVERED_MINE_CELL = COVERED_MINE_CELL

    @property
    def N_ROWS(self):
        return self.__N_ROWS
    @N_ROWS.setter
    def N_ROWS(self, N_ROWS: int):
        self.__N_ROWS = N_ROWS

    @property
    def all_cells(self):
        return self.__all_cells
    @all_cells.setter
    def all_cells(self, all_cells: int):
        self.__all_cells = all_cells

    @property
    def MINE_CELL(self):
        return self.__MINE_CELL
    @MINE_CELL.setter
    def MINE_CELL(self, MINE_CELL: int):
        self.__MINE_CELL = MINE_CELL

    @property
    def N_COLS(self):
        return self.__N_COLS
    @N_COLS.setter
    def N_COLS(self, N_COLS: int):
        self.__N_COLS = N_COLS

    @property
    def DRAW_WRONG_MARK(self):
        return self.__DRAW_WRONG_MARK
    @DRAW_WRONG_MARK.setter
    def DRAW_WRONG_MARK(self, DRAW_WRONG_MARK: int):
        self.__DRAW_WRONG_MARK = DRAW_WRONG_MARK

    @property
    def mines_left(self):
        return self.__mines_left
    @mines_left.setter
    def mines_left(self, mines_left: int):
        self.__mines_left = mines_left

    @property
    def statusbar(self):
        return self.__statusbar
    @statusbar.setter
    def statusbar(self, statusbar: genmymodelreverse_javax_swing_JLabel):
        self.__statusbar = statusbar

    @property
    def MARK_FOR_CELL(self):
        return self.__MARK_FOR_CELL
    @MARK_FOR_CELL.setter
    def MARK_FOR_CELL(self, MARK_FOR_CELL: int):
        self.__MARK_FOR_CELL = MARK_FOR_CELL

    @property
    def field(self):
        return self.__field
    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def DRAW_COVER(self):
        return self.__DRAW_COVER
    @DRAW_COVER.setter
    def DRAW_COVER(self, DRAW_COVER: int):
        self.__DRAW_COVER = DRAW_COVER

    @property
    def inGame(self):
        return self.__inGame
    @inGame.setter
    def inGame(self, inGame: bool):
        self.__inGame = inGame

    @property
    def NUM_IMAGES(self):
        return self.__NUM_IMAGES
    @NUM_IMAGES.setter
    def NUM_IMAGES(self, NUM_IMAGES: int):
        self.__NUM_IMAGES = NUM_IMAGES

    @property
    def CELL_SIZE(self):
        return self.__CELL_SIZE
    @CELL_SIZE.setter
    def CELL_SIZE(self, CELL_SIZE: int):
        self.__CELL_SIZE = CELL_SIZE

    @property
    def COVER_FOR_CELL(self):
        return self.__COVER_FOR_CELL
    @COVER_FOR_CELL.setter
    def COVER_FOR_CELL(self, COVER_FOR_CELL: int):
        self.__COVER_FOR_CELL = COVER_FOR_CELL

    @property
    def N_MINES(self):
        return self.__N_MINES
    @N_MINES.setter
    def N_MINES(self, N_MINES: int):
        self.__N_MINES = N_MINES

    @property
    def DRAW_MINE(self):
        return self.__DRAW_MINE
    @DRAW_MINE.setter
    def DRAW_MINE(self, DRAW_MINE: int):
        self.__DRAW_MINE = DRAW_MINE

    @property
    def MARKED_MINE_CELL(self):
        return self.__MARKED_MINE_CELL
    @MARKED_MINE_CELL.setter
    def MARKED_MINE_CELL(self, MARKED_MINE_CELL: int):
        self.__MARKED_MINE_CELL = MARKED_MINE_CELL

    @property
    def timeBar(self):
        return self.__timeBar
    @timeBar.setter
    def timeBar(self, timeBar: genmymodelreverse_javax_swing_JLabel):
        self.__timeBar = timeBar

    @property
    def mines0(self):
        return self.__mines0
    @mines0.setter
    def mines0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board__mines0", None)
        self.__mines0 = value
        
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

