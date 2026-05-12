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

    def __init__(self, FRAME_HEIGHT: int, statusbar: genmymodelreverse_javax_swing_JLabel, timeBar: genmymodelreverse_javax_swing_JLabel, hexCell: genmymodelreverse_javax_swing_JMenuItem, FRAME_WIDTH: int):
        self.FRAME_HEIGHT = FRAME_HEIGHT
        self.statusbar = statusbar
        self.timeBar = timeBar
        self.hexCell = hexCell
        self.FRAME_WIDTH = FRAME_WIDTH
        
        pass
    @property
    def statusbar(self):
        return self.__statusbar
    @statusbar.setter
    def statusbar(self, statusbar: genmymodelreverse_javax_swing_JLabel):
        self.__statusbar = statusbar

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
    def FRAME_HEIGHT(self):
        return self.__FRAME_HEIGHT
    @FRAME_HEIGHT.setter
    def FRAME_HEIGHT(self, FRAME_HEIGHT: int):
        self.__FRAME_HEIGHT = FRAME_HEIGHT

    @property
    def timeBar(self):
        return self.__timeBar
    @timeBar.setter
    def timeBar(self, timeBar: genmymodelreverse_javax_swing_JLabel):
        self.__timeBar = timeBar

