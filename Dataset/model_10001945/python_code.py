from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Connect4_connect:

    def __init__(self, FRAME_WIDTH: int, FRAME_HEIGHT: int, rowSize: int, columnSize: int, x: int, y: int, panel: str, label1: str, label2: str, label3: str, label4: str, label5: str, circlePanel5: "Connect4_CirclePanel" = None, board7: "Connect4_Board" = None):
        self.FRAME_WIDTH = FRAME_WIDTH
        self.FRAME_HEIGHT = FRAME_HEIGHT
        self.rowSize = rowSize
        self.columnSize = columnSize
        self.x = x
        self.y = y
        self.panel = panel
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        self.label5 = label5
        self.circlePanel5 = circlePanel5
        self.board7 = board7
        
        pass
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def columnSize(self):
        return self.__columnSize
    @columnSize.setter
    def columnSize(self, columnSize: int):
        self.__columnSize = columnSize

    @property
    def label1(self):
        return self.__label1
    @label1.setter
    def label1(self, label1: str):
        self.__label1 = label1

    @property
    def label2(self):
        return self.__label2
    @label2.setter
    def label2(self, label2: str):
        self.__label2 = label2

    @property
    def FRAME_HEIGHT(self):
        return self.__FRAME_HEIGHT
    @FRAME_HEIGHT.setter
    def FRAME_HEIGHT(self, FRAME_HEIGHT: int):
        self.__FRAME_HEIGHT = FRAME_HEIGHT

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def FRAME_WIDTH(self):
        return self.__FRAME_WIDTH
    @FRAME_WIDTH.setter
    def FRAME_WIDTH(self, FRAME_WIDTH: int):
        self.__FRAME_WIDTH = FRAME_WIDTH

    @property
    def label4(self):
        return self.__label4
    @label4.setter
    def label4(self, label4: str):
        self.__label4 = label4

    @property
    def label3(self):
        return self.__label3
    @label3.setter
    def label3(self, label3: str):
        self.__label3 = label3

    @property
    def panel(self):
        return self.__panel
    @panel.setter
    def panel(self, panel: str):
        self.__panel = panel

    @property
    def rowSize(self):
        return self.__rowSize
    @rowSize.setter
    def rowSize(self, rowSize: int):
        self.__rowSize = rowSize

    @property
    def label5(self):
        return self.__label5
    @label5.setter
    def label5(self, label5: str):
        self.__label5 = label5

    @property
    def board7(self):
        return self.__board7
    @board7.setter
    def board7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4_connect__board7", None)
        self.__board7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connect6"):
                opp_val = getattr(old_value, "connect6", None)
                if opp_val == self:
                    setattr(old_value, "connect6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connect6"):
                opp_val = getattr(value, "connect6", None)
                setattr(value, "connect6", self)

    @property
    def circlePanel5(self):
        return self.__circlePanel5
    @circlePanel5.setter
    def circlePanel5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4_connect__circlePanel5", None)
        self.__circlePanel5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connect4"):
                opp_val = getattr(old_value, "connect4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connect4"):
                opp_val = getattr(value, "connect4", None)
                if opp_val is None:
                    setattr(value, "connect4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Connect4_CirclePanel:

    def __init__(self, color: str, colorIndex: int, connect4: set["Connect4_connect"] = None):
        self.color = color
        self.colorIndex = colorIndex
        self.connect4 = connect4 if connect4 is not None else set()
        
        pass
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def colorIndex(self):
        return self.__colorIndex
    @colorIndex.setter
    def colorIndex(self, colorIndex: int):
        self.__colorIndex = colorIndex

    @property
    def connect4(self):
        return self.__connect4
    @connect4.setter
    def connect4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4_CirclePanel__connect4", None)
        self.__connect4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "circlePanel5"):
                    opp_val = getattr(item, "circlePanel5", None)
                    
                    if opp_val == self:
                        setattr(item, "circlePanel5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "circlePanel5"):
                    opp_val = getattr(item, "circlePanel5", None)
                    
                    setattr(item, "circlePanel5", self)
                    



class Connect4_Board:

    def __init__(self, maxRows: int, maxColumns: int, gameBoard: str, token0: set["Connect4_Token"] = None, player2: set["Connect4_Player"] = None, connect6: "Connect4_connect" = None):
        self.maxRows = maxRows
        self.maxColumns = maxColumns
        self.gameBoard = gameBoard
        self.token0 = token0 if token0 is not None else set()
        self.player2 = player2 if player2 is not None else set()
        self.connect6 = connect6
        
        pass
    @property
    def gameBoard(self):
        return self.__gameBoard
    @gameBoard.setter
    def gameBoard(self, gameBoard: str):
        self.__gameBoard = gameBoard

    @property
    def maxColumns(self):
        return self.__maxColumns
    @maxColumns.setter
    def maxColumns(self, maxColumns: int):
        self.__maxColumns = maxColumns

    @property
    def maxRows(self):
        return self.__maxRows
    @maxRows.setter
    def maxRows(self, maxRows: int):
        self.__maxRows = maxRows

    @property
    def connect6(self):
        return self.__connect6
    @connect6.setter
    def connect6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4_Board__connect6", None)
        self.__connect6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board7"):
                opp_val = getattr(old_value, "board7", None)
                if opp_val == self:
                    setattr(old_value, "board7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board7"):
                opp_val = getattr(value, "board7", None)
                setattr(value, "board7", self)

    @property
    def token0(self):
        return self.__token0
    @token0.setter
    def token0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4_Board__token0", None)
        self.__token0 = value if value is not None else set()
        
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
        old_value = getattr(self, f"_Connect4_Board__player2", None)
        self.__player2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "board3"):
                    opp_val = getattr(item, "board3", None)
                    
                    if opp_val == self:
                        setattr(item, "board3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "board3"):
                    opp_val = getattr(item, "board3", None)
                    
                    setattr(item, "board3", self)
                    



class Connect4_Token:

    def __init__(self, color: str, xValue: int, yValue: int, isEmpty: bool, board1: "Connect4_Board" = None):
        self.color = color
        self.xValue = xValue
        self.yValue = yValue
        self.isEmpty = isEmpty
        self.board1 = board1
        
        pass
    @property
    def yValue(self):
        return self.__yValue
    @yValue.setter
    def yValue(self, yValue: int):
        self.__yValue = yValue

    @property
    def isEmpty(self):
        return self.__isEmpty
    @isEmpty.setter
    def isEmpty(self, isEmpty: bool):
        self.__isEmpty = isEmpty

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def xValue(self):
        return self.__xValue
    @xValue.setter
    def xValue(self, xValue: int):
        self.__xValue = xValue

    @property
    def board1(self):
        return self.__board1
    @board1.setter
    def board1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4_Token__board1", None)
        self.__board1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "token0"):
                opp_val = getattr(old_value, "token0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "token0"):
                opp_val = getattr(value, "token0", None)
                if opp_val is None:
                    setattr(value, "token0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Connect4_Player:

    def __init__(self, name: str, wins: int, tokenColor: str, currentPlayer: bool, roundWon: bool, board3: "Connect4_Board" = None):
        self.name = name
        self.wins = wins
        self.tokenColor = tokenColor
        self.currentPlayer = currentPlayer
        self.roundWon = roundWon
        self.board3 = board3
        
        pass
    @property
    def currentPlayer(self):
        return self.__currentPlayer
    @currentPlayer.setter
    def currentPlayer(self, currentPlayer: bool):
        self.__currentPlayer = currentPlayer

    @property
    def tokenColor(self):
        return self.__tokenColor
    @tokenColor.setter
    def tokenColor(self, tokenColor: str):
        self.__tokenColor = tokenColor

    @property
    def roundWon(self):
        return self.__roundWon
    @roundWon.setter
    def roundWon(self, roundWon: bool):
        self.__roundWon = roundWon

    @property
    def wins(self):
        return self.__wins
    @wins.setter
    def wins(self, wins: int):
        self.__wins = wins

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def board3(self):
        return self.__board3
    @board3.setter
    def board3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4_Player__board3", None)
        self.__board3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player2"):
                opp_val = getattr(old_value, "player2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player2"):
                opp_val = getattr(value, "player2", None)
                if opp_val is None:
                    setattr(value, "player2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

