from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Connect4:

    pass


class MainMenuGUI:

    pass


class GameBoard:

    def __init__(self, board: str, whoPlay: str, player1: Player_Interface, player2: Player_Interface, player7: set["Player_Interface"] = None, connect4GUI14: "Connect4GUI" = None):
        self.board = board
        self.whoPlay = whoPlay
        self.player1 = player1
        self.player2 = player2
        self.player7 = player7 if player7 is not None else set()
        self.connect4GUI14 = connect4GUI14
        
        pass
    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, player2: Player_Interface):
        self.__player2 = player2

    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: str):
        self.__board = board

    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self, player1: Player_Interface):
        self.__player1 = player1

    @property
    def whoPlay(self):
        return self.__whoPlay
    @whoPlay.setter
    def whoPlay(self, whoPlay: str):
        self.__whoPlay = whoPlay

    @property
    def player7(self):
        return self.__player7
    @player7.setter
    def player7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameBoard__player7", None)
        self.__player7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gameBoard6"):
                    opp_val = getattr(item, "gameBoard6", None)
                    
                    if opp_val == self:
                        setattr(item, "gameBoard6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gameBoard6"):
                    opp_val = getattr(item, "gameBoard6", None)
                    
                    setattr(item, "gameBoard6", self)
                    

    @property
    def connect4GUI14(self):
        return self.__connect4GUI14
    @connect4GUI14.setter
    def connect4GUI14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameBoard__connect4GUI14", None)
        self.__connect4GUI14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameBoard15"):
                opp_val = getattr(old_value, "gameBoard15", None)
                if opp_val == self:
                    setattr(old_value, "gameBoard15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameBoard15"):
                opp_val = getattr(value, "gameBoard15", None)
                setattr(value, "gameBoard15", self)



class ScoreBoardGUI:

    def __init__(self, playersList: str, player2: set["Player_Interface"] = None, mainMenuGUI12: "MainMenuGUI" = None):
        self.playersList = playersList
        self.player2 = player2 if player2 is not None else set()
        self.mainMenuGUI12 = mainMenuGUI12
        
        pass
    @property
    def playersList(self):
        return self.__playersList
    @playersList.setter
    def playersList(self, playersList: str):
        self.__playersList = playersList

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScoreBoardGUI__player2", None)
        self.__player2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ScoreBoardGUI_Player_13"):
                    opp_val = getattr(item, "ScoreBoardGUI_Player_13", None)
                    
                    if opp_val == self:
                        setattr(item, "ScoreBoardGUI_Player_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ScoreBoardGUI_Player_13"):
                    opp_val = getattr(item, "ScoreBoardGUI_Player_13", None)
                    
                    setattr(item, "ScoreBoardGUI_Player_13", self)
                    

    @property
    def mainMenuGUI12(self):
        return self.__mainMenuGUI12
    @mainMenuGUI12.setter
    def mainMenuGUI12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScoreBoardGUI__mainMenuGUI12", None)
        self.__mainMenuGUI12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scoreBoardGUI13"):
                opp_val = getattr(old_value, "scoreBoardGUI13", None)
                if opp_val == self:
                    setattr(old_value, "scoreBoardGUI13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scoreBoardGUI13"):
                opp_val = getattr(value, "scoreBoardGUI13", None)
                setattr(value, "scoreBoardGUI13", self)



class Button:

    pass


class Connect4GUI:

    def __init__(self, root: str, undo: Button, gameboardGUI5: "GameboardGUI" = None, mainMenuGUI11: "MainMenuGUI" = None, gameBoard15: "GameBoard" = None):
        self.root = root
        self.undo = undo
        self.gameboardGUI5 = gameboardGUI5
        self.mainMenuGUI11 = mainMenuGUI11
        self.gameBoard15 = gameBoard15
        
        pass
    @property
    def root(self):
        return self.__root
    @root.setter
    def root(self, root: str):
        self.__root = root

    @property
    def undo(self):
        return self.__undo
    @undo.setter
    def undo(self, undo: Button):
        self.__undo = undo

    @property
    def gameBoard15(self):
        return self.__gameBoard15
    @gameBoard15.setter
    def gameBoard15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4GUI__gameBoard15", None)
        self.__gameBoard15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connect4GUI14"):
                opp_val = getattr(old_value, "connect4GUI14", None)
                if opp_val == self:
                    setattr(old_value, "connect4GUI14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connect4GUI14"):
                opp_val = getattr(value, "connect4GUI14", None)
                setattr(value, "connect4GUI14", self)

    @property
    def mainMenuGUI11(self):
        return self.__mainMenuGUI11
    @mainMenuGUI11.setter
    def mainMenuGUI11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4GUI__mainMenuGUI11", None)
        self.__mainMenuGUI11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connect4GUI10"):
                opp_val = getattr(old_value, "connect4GUI10", None)
                if opp_val == self:
                    setattr(old_value, "connect4GUI10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connect4GUI10"):
                opp_val = getattr(value, "connect4GUI10", None)
                setattr(value, "connect4GUI10", self)

    @property
    def gameboardGUI5(self):
        return self.__gameboardGUI5
    @gameboardGUI5.setter
    def gameboardGUI5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Connect4GUI__gameboardGUI5", None)
        self.__gameboardGUI5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connect4GUI4"):
                opp_val = getattr(old_value, "connect4GUI4", None)
                if opp_val == self:
                    setattr(old_value, "connect4GUI4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connect4GUI4"):
                opp_val = getattr(value, "connect4GUI4", None)
                setattr(value, "connect4GUI4", self)



class GameboardGUI:

    def __init__(self, rows: int, columns: int, piecesList: str, piece0: set["Piece"] = None, connect4GUI4: "Connect4GUI" = None):
        self.rows = rows
        self.columns = columns
        self.piecesList = piecesList
        self.piece0 = piece0 if piece0 is not None else set()
        self.connect4GUI4 = connect4GUI4
        
        pass
    @property
    def rows(self):
        return self.__rows
    @rows.setter
    def rows(self, rows: int):
        self.__rows = rows

    @property
    def columns(self):
        return self.__columns
    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

    @property
    def piecesList(self):
        return self.__piecesList
    @piecesList.setter
    def piecesList(self, piecesList: str):
        self.__piecesList = piecesList

    @property
    def connect4GUI4(self):
        return self.__connect4GUI4
    @connect4GUI4.setter
    def connect4GUI4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameboardGUI__connect4GUI4", None)
        self.__connect4GUI4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameboardGUI5"):
                opp_val = getattr(old_value, "gameboardGUI5", None)
                if opp_val == self:
                    setattr(old_value, "gameboardGUI5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameboardGUI5"):
                opp_val = getattr(value, "gameboardGUI5", None)
                setattr(value, "gameboardGUI5", self)

    @property
    def piece0(self):
        return self.__piece0
    @piece0.setter
    def piece0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameboardGUI__piece0", None)
        self.__piece0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gameboardGUI1"):
                    opp_val = getattr(item, "gameboardGUI1", None)
                    
                    if opp_val == self:
                        setattr(item, "gameboardGUI1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gameboardGUI1"):
                    opp_val = getattr(item, "gameboardGUI1", None)
                    
                    setattr(item, "gameboardGUI1", self)
                    



class Piece:

    def __init__(self, pieceSize: int, pieceColor: str, gameboardGUI1: "GameboardGUI" = None):
        self.pieceSize = pieceSize
        self.pieceColor = pieceColor
        self.gameboardGUI1 = gameboardGUI1
        
        pass
    @property
    def pieceColor(self):
        return self.__pieceColor
    @pieceColor.setter
    def pieceColor(self, pieceColor: str):
        self.__pieceColor = pieceColor

    @property
    def pieceSize(self):
        return self.__pieceSize
    @pieceSize.setter
    def pieceSize(self, pieceSize: int):
        self.__pieceSize = pieceSize

    @property
    def gameboardGUI1(self):
        return self.__gameboardGUI1
    @gameboardGUI1.setter
    def gameboardGUI1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Piece__gameboardGUI1", None)
        self.__gameboardGUI1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "piece0"):
                opp_val = getattr(old_value, "piece0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "piece0"):
                opp_val = getattr(value, "piece0", None)
                if opp_val is None:
                    setattr(value, "piece0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class RandomPlayer:

    def __init__(self, name: str, score: str):
        self.name = name
        self.score = score
        
        pass
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
    def score(self, score: str):
        self.__score = score



class AIplayer:

    def __init__(self, name: str, score: str):
        self.name = name
        self.score = score
        
        pass
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: str):
        self.__score = score

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class ConsolePlayer:

    def __init__(self, name: str, score: str):
        self.name = name
        self.score = score
        
        pass
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: str):
        self.__score = score

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Player_Interface:

    pass
