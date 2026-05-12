from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Player_2_Actor:

    pass


class Computer_AI_Actor:

    pass


class Player_1_Actor:

    pass





class Compute_Column_external:

    pass


class Select_Column_external:

    pass


class Enter_Name_external:

    pass


class Choose_how_many_Players_external:

    pass


class BorderPane:

    pass


class VBox:

    pass


class HBox:

    pass


class Button:

    pass


class Label:

    pass


class List_Token_:

    pass


class Connect_Four_Component:

    pass


class javax_swing_JTextField:

    pass


class javax_swing_JButton:

    pass


class ImageIcon:

    pass


class Listener_Interface:

    pass


class Player:

    pass


class connect_four_gui_Circle:

    pass


class connect_four_gui_Connect4Constant_Interface:

    pass


class connect_four_gui_GameOverPanel:

    def __init__(self, winner: str, winnerDisplay: str, gui: connect_four_gui_Connect4GUI, butMainMenu: javax_swing_JButton, butPlayAgain: javax_swing_JButton, labelGameOVer: str, gUI2: "connect_four_gui_Connect4GUI" = None):
        self.winner = winner
        self.winnerDisplay = winnerDisplay
        self.gui = gui
        self.butMainMenu = butMainMenu
        self.butPlayAgain = butPlayAgain
        self.labelGameOVer = labelGameOVer
        self.gUI2 = gUI2
        
        pass
    @property
    def butPlayAgain(self):
        return self.__butPlayAgain
    @butPlayAgain.setter
    def butPlayAgain(self, butPlayAgain: javax_swing_JButton):
        self.__butPlayAgain = butPlayAgain

    @property
    def gui(self):
        return self.__gui
    @gui.setter
    def gui(self, gui: connect_four_gui_Connect4GUI):
        self.__gui = gui

    @property
    def winnerDisplay(self):
        return self.__winnerDisplay
    @winnerDisplay.setter
    def winnerDisplay(self, winnerDisplay: str):
        self.__winnerDisplay = winnerDisplay

    @property
    def butMainMenu(self):
        return self.__butMainMenu
    @butMainMenu.setter
    def butMainMenu(self, butMainMenu: javax_swing_JButton):
        self.__butMainMenu = butMainMenu

    @property
    def labelGameOVer(self):
        return self.__labelGameOVer
    @labelGameOVer.setter
    def labelGameOVer(self, labelGameOVer: str):
        self.__labelGameOVer = labelGameOVer

    @property
    def winner(self):
        return self.__winner
    @winner.setter
    def winner(self, winner: str):
        self.__winner = winner

    @property
    def gUI2(self):
        return self.__gUI2
    @gUI2.setter
    def gUI2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connect_four_gui_GameOverPanel__gUI2", None)
        self.__gUI2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameOverPanel23"):
                opp_val = getattr(old_value, "gameOverPanel23", None)
                if opp_val == self:
                    setattr(old_value, "gameOverPanel23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameOverPanel23"):
                opp_val = getattr(value, "gameOverPanel23", None)
                setattr(value, "gameOverPanel23", self)



class connect_four_gui_stage:

    pass


class connect_four_gui_StartMenu:

    def __init__(self, window: str, startLabel: Label, bPlay: Button, label: HBox, bStart: VBox, bp: BorderPane):
        self.window = window
        self.startLabel = startLabel
        self.bPlay = bPlay
        self.label = label
        self.bStart = bStart
        self.bp = bp
        
        pass
    @property
    def label(self):
        return self.__label
    @label.setter
    def label(self, label: HBox):
        self.__label = label

    @property
    def startLabel(self):
        return self.__startLabel
    @startLabel.setter
    def startLabel(self, startLabel: Label):
        self.__startLabel = startLabel

    @property
    def window(self):
        return self.__window
    @window.setter
    def window(self, window: str):
        self.__window = window

    @property
    def bStart(self):
        return self.__bStart
    @bStart.setter
    def bStart(self, bStart: VBox):
        self.__bStart = bStart

    @property
    def bPlay(self):
        return self.__bPlay
    @bPlay.setter
    def bPlay(self, bPlay: Button):
        self.__bPlay = bPlay

    @property
    def bp(self):
        return self.__bp
    @bp.setter
    def bp(self, bp: BorderPane):
        self.__bp = bp



class connect_four_gui_GUIPlayer:

    def __init__(self, m_name: str, gpGUI: connect_four_gui_GamePanel, board: str):
        self.m_name = m_name
        self.gpGUI = gpGUI
        self.board = board
        
        pass
    @property
    def gpGUI(self):
        return self.__gpGUI
    @gpGUI.setter
    def gpGUI(self, gpGUI: connect_four_gui_GamePanel):
        self.__gpGUI = gpGUI

    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: str):
        self.__board = board

    @property
    def m_name(self):
        return self.__m_name
    @m_name.setter
    def m_name(self, m_name: str):
        self.__m_name = m_name



class connect_four_gui_red:

    pass


class connect_four_gui_Token:

    def __init__(self, red: bool, X: str, Y: str):
        self.red = red
        self.X = X
        self.Y = Y
        
        pass
    @property
    def Y(self):
        return self.__Y
    @Y.setter
    def Y(self, Y: str):
        self.__Y = Y

    @property
    def red(self):
        return self.__red
    @red.setter
    def red(self, red: bool):
        self.__red = red

    @property
    def X(self):
        return self.__X
    @X.setter
    def X(self, X: str):
        self.__X = X



class connect_four_gui_Connect4GUI:

    def __init__(self, window: str, startUp: str, tokenRoot: str, gridBoard: str, redToken: bool, comp: bool, cpList: List_Token_, gamePanel20: "connect_four_gui_GamePanel" = None, gameOverPanel23: "connect_four_gui_GameOverPanel" = None):
        self.window = window
        self.startUp = startUp
        self.tokenRoot = tokenRoot
        self.gridBoard = gridBoard
        self.redToken = redToken
        self.comp = comp
        self.cpList = cpList
        self.gamePanel20 = gamePanel20
        self.gameOverPanel23 = gameOverPanel23
        
        pass
    @property
    def redToken(self):
        return self.__redToken
    @redToken.setter
    def redToken(self, redToken: bool):
        self.__redToken = redToken

    @property
    def comp(self):
        return self.__comp
    @comp.setter
    def comp(self, comp: bool):
        self.__comp = comp

    @property
    def cpList(self):
        return self.__cpList
    @cpList.setter
    def cpList(self, cpList: List_Token_):
        self.__cpList = cpList

    @property
    def window(self):
        return self.__window
    @window.setter
    def window(self, window: str):
        self.__window = window

    @property
    def startUp(self):
        return self.__startUp
    @startUp.setter
    def startUp(self, startUp: str):
        self.__startUp = startUp

    @property
    def gridBoard(self):
        return self.__gridBoard
    @gridBoard.setter
    def gridBoard(self, gridBoard: str):
        self.__gridBoard = gridBoard

    @property
    def tokenRoot(self):
        return self.__tokenRoot
    @tokenRoot.setter
    def tokenRoot(self, tokenRoot: str):
        self.__tokenRoot = tokenRoot

    @property
    def gamePanel20(self):
        return self.__gamePanel20
    @gamePanel20.setter
    def gamePanel20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connect_four_gui_Connect4GUI__gamePanel20", None)
        self.__gamePanel20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI1"):
                opp_val = getattr(old_value, "gUI1", None)
                if opp_val == self:
                    setattr(old_value, "gUI1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI1"):
                opp_val = getattr(value, "gUI1", None)
                setattr(value, "gUI1", self)

    @property
    def gameOverPanel23(self):
        return self.__gameOverPanel23
    @gameOverPanel23.setter
    def gameOverPanel23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connect_four_gui_Connect4GUI__gameOverPanel23", None)
        self.__gameOverPanel23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI2"):
                opp_val = getattr(old_value, "gUI2", None)
                if opp_val == self:
                    setattr(old_value, "gUI2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI2"):
                opp_val = getattr(value, "gUI2", None)
                setattr(value, "gUI2", self)



class connect_four_gui_GamePanel:

    def __init__(self, Connect4_GUI: connect_four_gui_Connect4GUI, startUp: str, windows: str, columnNum: int, turnNum: int, whoPlayed: int, newDrawPos: int, newColumnNum: int, players: str, game: str, pieces: str, board: str, isComputerEnabled: bool, justWon: bool, gUI1: "connect_four_gui_Connect4GUI" = None):
        self.Connect4_GUI = Connect4_GUI
        self.startUp = startUp
        self.windows = windows
        self.columnNum = columnNum
        self.turnNum = turnNum
        self.whoPlayed = whoPlayed
        self.newDrawPos = newDrawPos
        self.newColumnNum = newColumnNum
        self.players = players
        self.game = game
        self.pieces = pieces
        self.board = board
        self.isComputerEnabled = isComputerEnabled
        self.justWon = justWon
        self.gUI1 = gUI1
        
        pass
    @property
    def startUp(self):
        return self.__startUp
    @startUp.setter
    def startUp(self, startUp: str):
        self.__startUp = startUp

    @property
    def whoPlayed(self):
        return self.__whoPlayed
    @whoPlayed.setter
    def whoPlayed(self, whoPlayed: int):
        self.__whoPlayed = whoPlayed

    @property
    def isComputerEnabled(self):
        return self.__isComputerEnabled
    @isComputerEnabled.setter
    def isComputerEnabled(self, isComputerEnabled: bool):
        self.__isComputerEnabled = isComputerEnabled

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

    @property
    def newDrawPos(self):
        return self.__newDrawPos
    @newDrawPos.setter
    def newDrawPos(self, newDrawPos: int):
        self.__newDrawPos = newDrawPos

    @property
    def justWon(self):
        return self.__justWon
    @justWon.setter
    def justWon(self, justWon: bool):
        self.__justWon = justWon

    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: str):
        self.__board = board

    @property
    def Connect4_GUI(self):
        return self.__Connect4_GUI
    @Connect4_GUI.setter
    def Connect4_GUI(self, Connect4_GUI: connect_four_gui_Connect4GUI):
        self.__Connect4_GUI = Connect4_GUI

    @property
    def pieces(self):
        return self.__pieces
    @pieces.setter
    def pieces(self, pieces: str):
        self.__pieces = pieces

    @property
    def columnNum(self):
        return self.__columnNum
    @columnNum.setter
    def columnNum(self, columnNum: int):
        self.__columnNum = columnNum

    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: str):
        self.__game = game

    @property
    def newColumnNum(self):
        return self.__newColumnNum
    @newColumnNum.setter
    def newColumnNum(self, newColumnNum: int):
        self.__newColumnNum = newColumnNum

    @property
    def turnNum(self):
        return self.__turnNum
    @turnNum.setter
    def turnNum(self, turnNum: int):
        self.__turnNum = turnNum

    @property
    def windows(self):
        return self.__windows
    @windows.setter
    def windows(self, windows: str):
        self.__windows = windows

    @property
    def gUI1(self):
        return self.__gUI1
    @gUI1.setter
    def gUI1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connect_four_gui_GamePanel__gUI1", None)
        self.__gUI1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gamePanel20"):
                opp_val = getattr(old_value, "gamePanel20", None)
                if opp_val == self:
                    setattr(old_value, "gamePanel20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gamePanel20"):
                opp_val = getattr(value, "gamePanel20", None)
                setattr(value, "gamePanel20", self)

