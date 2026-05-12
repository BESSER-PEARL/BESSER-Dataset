####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
Player_Interface = Class(name="Player_Interface")
ConsolePlayer = Class(name="ConsolePlayer")
AIplayer = Class(name="AIplayer")
RandomPlayer = Class(name="RandomPlayer")
Piece = Class(name="Piece")
GameboardGUI = Class(name="GameboardGUI")
Connect4GUI = Class(name="Connect4GUI")
Button = Class(name="Button")
ScoreBoardGUI = Class(name="ScoreBoardGUI")
GameBoard = Class(name="GameBoard")
MainMenuGUI = Class(name="MainMenuGUI")
Connect4 = Class(name="Connect4")

# Player_Interface class attributes and methods

# ConsolePlayer class attributes and methods
ConsolePlayer_name: Property = Property(name="name", type=StringType)
ConsolePlayer_score: Property = Property(name="score", type=StringType)
ConsolePlayer.attributes={ConsolePlayer_name, ConsolePlayer_score}

# AIplayer class attributes and methods
AIplayer_name: Property = Property(name="name", type=StringType)
AIplayer_score: Property = Property(name="score", type=StringType)
AIplayer.attributes={AIplayer_name, AIplayer_score}

# RandomPlayer class attributes and methods
RandomPlayer_name: Property = Property(name="name", type=StringType)
RandomPlayer_score: Property = Property(name="score", type=StringType)
RandomPlayer.attributes={RandomPlayer_name, RandomPlayer_score}

# Piece class attributes and methods
Piece_pieceSize: Property = Property(name="pieceSize", type=IntegerType)
Piece_pieceColor: Property = Property(name="pieceColor", type=StringType)
Piece.attributes={Piece_pieceColor, Piece_pieceSize}

# GameboardGUI class attributes and methods
GameboardGUI_rows: Property = Property(name="rows", type=IntegerType)
GameboardGUI_columns: Property = Property(name="columns", type=IntegerType)
GameboardGUI_piecesList: Property = Property(name="piecesList", type=StringType)
GameboardGUI.attributes={GameboardGUI_piecesList, GameboardGUI_columns, GameboardGUI_rows}

# Connect4GUI class attributes and methods
Connect4GUI_root: Property = Property(name="root", type=StringType)
Connect4GUI_undo: Property = Property(name="undo", type=Button)
Connect4GUI.attributes={Connect4GUI_root, Connect4GUI_undo}

# Button class attributes and methods

# ScoreBoardGUI class attributes and methods
ScoreBoardGUI_playersList: Property = Property(name="playersList", type=StringType)
ScoreBoardGUI.attributes={ScoreBoardGUI_playersList}

# GameBoard class attributes and methods
GameBoard_board: Property = Property(name="board", type=StringType)
GameBoard_whoPlay: Property = Property(name="whoPlay", type=StringType)
GameBoard_player1: Property = Property(name="player1", type=Player_Interface)
GameBoard_player2: Property = Property(name="player2", type=Player_Interface)
GameBoard.attributes={GameBoard_player2, GameBoard_board, GameBoard_whoPlay, GameBoard_player1}

# MainMenuGUI class attributes and methods

# Connect4 class attributes and methods

# Relationships
GameboardGUI_Connect4GUI: BinaryAssociation = BinaryAssociation(
    name="GameboardGUI_Connect4GUI",
    ends={
        Property(name="connect4GUI4", type=Connect4GUI, multiplicity=Multiplicity(0, 1)),
        Property(name="gameboardGUI5", type=GameboardGUI, multiplicity=Multiplicity(0, 1))
    }
)
Player_GameBoard: BinaryAssociation = BinaryAssociation(
    name="Player_GameBoard",
    ends={
        Property(name="gameBoard6", type=GameBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="player7", type=Player_Interface, multiplicity=Multiplicity(1, 9999))
    }
)
Connect4_MainMenuGUI: BinaryAssociation = BinaryAssociation(
    name="Connect4_MainMenuGUI",
    ends={
        Property(name="mainMenuGUI8", type=MainMenuGUI, multiplicity=Multiplicity(0, 1)),
        Property(name="connect49", type=Connect4, multiplicity=Multiplicity(0, 1))
    }
)
MainMenuGUI_Connect4GUI: BinaryAssociation = BinaryAssociation(
    name="MainMenuGUI_Connect4GUI",
    ends={
        Property(name="connect4GUI10", type=Connect4GUI, multiplicity=Multiplicity(1, 1)),
        Property(name="mainMenuGUI11", type=MainMenuGUI, multiplicity=Multiplicity(1, 1))
    }
)
ScoreBoardGUI_MainMenuGUI: BinaryAssociation = BinaryAssociation(
    name="ScoreBoardGUI_MainMenuGUI",
    ends={
        Property(name="mainMenuGUI12", type=MainMenuGUI, multiplicity=Multiplicity(1, 1)),
        Property(name="scoreBoardGUI13", type=ScoreBoardGUI, multiplicity=Multiplicity(1, 1))
    }
)
GameBoard_Connect4GUI: BinaryAssociation = BinaryAssociation(
    name="GameBoard_Connect4GUI",
    ends={
        Property(name="connect4GUI14", type=Connect4GUI, multiplicity=Multiplicity(1, 1)),
        Property(name="gameBoard15", type=GameBoard, multiplicity=Multiplicity(1, 1))
    }
)
GameboardGUI_Piece: BinaryAssociation = BinaryAssociation(
    name="GameboardGUI_Piece",
    ends={
        Property(name="piece0", type=Piece, multiplicity=Multiplicity(0, 9999)),
        Property(name="gameboardGUI1", type=GameboardGUI, multiplicity=Multiplicity(1, 1))
    }
)
ScoreBoardGUI_Player: BinaryAssociation = BinaryAssociation(
    name="ScoreBoardGUI_Player",
    ends={
        Property(name="player2", type=Player_Interface, multiplicity=Multiplicity(1, 9999)),
        Property(name="ScoreBoardGUI_Player_13", type=ScoreBoardGUI, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b44f6c28_daf4_41f9_97ae_beed9a121759",
    types={Player_Interface, ConsolePlayer, AIplayer, RandomPlayer, Piece, GameboardGUI, Connect4GUI, Button, ScoreBoardGUI, GameBoard, MainMenuGUI, Connect4},
    associations={GameboardGUI_Connect4GUI, Player_GameBoard, Connect4_MainMenuGUI, MainMenuGUI_Connect4GUI, ScoreBoardGUI_MainMenuGUI, GameBoard_Connect4GUI, GameboardGUI_Piece, ScoreBoardGUI_Player},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)