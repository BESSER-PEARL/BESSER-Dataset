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
connect_four_gui_GamePanel = Class(name="connect_four_gui_GamePanel")
connect_four_gui_Connect4GUI = Class(name="connect_four_gui_Connect4GUI")
connect_four_gui_Token = Class(name="connect_four_gui_Token")
connect_four_gui_red = Class(name="connect_four_gui_red")
connect_four_gui_GUIPlayer = Class(name="connect_four_gui_GUIPlayer")
connect_four_gui_StartMenu = Class(name="connect_four_gui_StartMenu")
connect_four_gui_stage = Class(name="connect_four_gui_stage")
connect_four_gui_GameOverPanel = Class(name="connect_four_gui_GameOverPanel")
connect_four_gui_Connect4Constant_Interface = Class(name="connect_four_gui_Connect4Constant_Interface")
connect_four_gui_Circle = Class(name="connect_four_gui_Circle")
Player = Class(name="Player")
Listener_Interface = Class(name="Listener_Interface")
ImageIcon = Class(name="ImageIcon")
javax_swing_JButton = Class(name="javax_swing_JButton")
javax_swing_JTextField = Class(name="javax_swing_JTextField")
Player_1_Actor = Class(name="Player_1_Actor")
Computer_AI_Actor = Class(name="Computer_AI_Actor")
Player_2_Actor = Class(name="Player_2_Actor")
Connect_Four_Component = Class(name="Connect_Four_Component")
List_Token_ = Class(name="List_Token_")
Label = Class(name="Label")
Button = Class(name="Button")
HBox = Class(name="HBox")
VBox = Class(name="VBox")
BorderPane = Class(name="BorderPane")
Choose_how_many_Players_external = Class(name="Choose_how_many_Players_external")
Enter_Name_external = Class(name="Enter_Name_external")
Select_Column_external = Class(name="Select_Column_external")
Compute_Column_external = Class(name="Compute_Column_external")

# connect_four_gui_GamePanel class attributes and methods
connect_four_gui_GamePanel_Connect4_GUI: Property = Property(name="Connect4_GUI", type=connect_four_gui_Connect4GUI)
connect_four_gui_GamePanel_startUp: Property = Property(name="startUp", type=StringType)
connect_four_gui_GamePanel_windows: Property = Property(name="windows", type=StringType)
connect_four_gui_GamePanel_columnNum: Property = Property(name="columnNum", type=IntegerType)
connect_four_gui_GamePanel_turnNum: Property = Property(name="turnNum", type=IntegerType)
connect_four_gui_GamePanel_whoPlayed: Property = Property(name="whoPlayed", type=IntegerType)
connect_four_gui_GamePanel_newDrawPos: Property = Property(name="newDrawPos", type=IntegerType)
connect_four_gui_GamePanel_newColumnNum: Property = Property(name="newColumnNum", type=IntegerType)
connect_four_gui_GamePanel_players: Property = Property(name="players", type=StringType)
connect_four_gui_GamePanel_game: Property = Property(name="game", type=StringType)
connect_four_gui_GamePanel_pieces: Property = Property(name="pieces", type=StringType)
connect_four_gui_GamePanel_board: Property = Property(name="board", type=StringType)
connect_four_gui_GamePanel_isComputerEnabled: Property = Property(name="isComputerEnabled", type=BooleanType)
connect_four_gui_GamePanel_justWon: Property = Property(name="justWon", type=BooleanType)
connect_four_gui_GamePanel.attributes={connect_four_gui_GamePanel_newDrawPos, connect_four_gui_GamePanel_isComputerEnabled, connect_four_gui_GamePanel_justWon, connect_four_gui_GamePanel_startUp, connect_four_gui_GamePanel_whoPlayed, connect_four_gui_GamePanel_columnNum, connect_four_gui_GamePanel_newColumnNum, connect_four_gui_GamePanel_turnNum, connect_four_gui_GamePanel_players, connect_four_gui_GamePanel_board, connect_four_gui_GamePanel_game, connect_four_gui_GamePanel_Connect4_GUI, connect_four_gui_GamePanel_windows, connect_four_gui_GamePanel_pieces}

# connect_four_gui_Connect4GUI class attributes and methods
connect_four_gui_Connect4GUI_window: Property = Property(name="window", type=StringType)
connect_four_gui_Connect4GUI_startUp: Property = Property(name="startUp", type=StringType)
connect_four_gui_Connect4GUI_tokenRoot: Property = Property(name="tokenRoot", type=StringType)
connect_four_gui_Connect4GUI_gridBoard: Property = Property(name="gridBoard", type=StringType)
connect_four_gui_Connect4GUI_redToken: Property = Property(name="redToken", type=BooleanType)
connect_four_gui_Connect4GUI_comp: Property = Property(name="comp", type=BooleanType)
connect_four_gui_Connect4GUI_cpList: Property = Property(name="cpList", type=List_Token_)
connect_four_gui_Connect4GUI.attributes={connect_four_gui_Connect4GUI_gridBoard, connect_four_gui_Connect4GUI_window, connect_four_gui_Connect4GUI_startUp, connect_four_gui_Connect4GUI_tokenRoot, connect_four_gui_Connect4GUI_redToken, connect_four_gui_Connect4GUI_cpList, connect_four_gui_Connect4GUI_comp}

# connect_four_gui_Token class attributes and methods
connect_four_gui_Token_red: Property = Property(name="red", type=BooleanType)
connect_four_gui_Token_X: Property = Property(name="X", type=StringType)
connect_four_gui_Token_Y: Property = Property(name="Y", type=StringType)
connect_four_gui_Token.attributes={connect_four_gui_Token_Y, connect_four_gui_Token_X, connect_four_gui_Token_red}

# connect_four_gui_red class attributes and methods

# connect_four_gui_GUIPlayer class attributes and methods
connect_four_gui_GUIPlayer_m_name: Property = Property(name="m_name", type=StringType)
connect_four_gui_GUIPlayer_gpGUI: Property = Property(name="gpGUI", type=connect_four_gui_GamePanel)
connect_four_gui_GUIPlayer_board: Property = Property(name="board", type=StringType)
connect_four_gui_GUIPlayer.attributes={connect_four_gui_GUIPlayer_m_name, connect_four_gui_GUIPlayer_gpGUI, connect_four_gui_GUIPlayer_board}

# connect_four_gui_StartMenu class attributes and methods
connect_four_gui_StartMenu_window: Property = Property(name="window", type=StringType)
connect_four_gui_StartMenu_startLabel: Property = Property(name="startLabel", type=Label)
connect_four_gui_StartMenu_bPlay: Property = Property(name="bPlay", type=Button)
connect_four_gui_StartMenu_label: Property = Property(name="label", type=HBox)
connect_four_gui_StartMenu_bStart: Property = Property(name="bStart", type=VBox)
connect_four_gui_StartMenu_bp: Property = Property(name="bp", type=BorderPane)
connect_four_gui_StartMenu.attributes={connect_four_gui_StartMenu_bStart, connect_four_gui_StartMenu_startLabel, connect_four_gui_StartMenu_bPlay, connect_four_gui_StartMenu_window, connect_four_gui_StartMenu_bp, connect_four_gui_StartMenu_label}

# connect_four_gui_stage class attributes and methods

# connect_four_gui_GameOverPanel class attributes and methods
connect_four_gui_GameOverPanel_gui: Property = Property(name="gui", type=connect_four_gui_Connect4GUI)
connect_four_gui_GameOverPanel_butMainMenu: Property = Property(name="butMainMenu", type=javax_swing_JButton)
connect_four_gui_GameOverPanel_butPlayAgain: Property = Property(name="butPlayAgain", type=javax_swing_JButton)
connect_four_gui_GameOverPanel_labelGameOVer: Property = Property(name="labelGameOVer", type=StringType)
connect_four_gui_GameOverPanel_winner: Property = Property(name="winner", type=StringType)
connect_four_gui_GameOverPanel_winnerDisplay: Property = Property(name="winnerDisplay", type=StringType)
connect_four_gui_GameOverPanel.attributes={connect_four_gui_GameOverPanel_winnerDisplay, connect_four_gui_GameOverPanel_labelGameOVer, connect_four_gui_GameOverPanel_gui, connect_four_gui_GameOverPanel_winner, connect_four_gui_GameOverPanel_butMainMenu, connect_four_gui_GameOverPanel_butPlayAgain}

# connect_four_gui_Connect4Constant_Interface class attributes and methods

# connect_four_gui_Circle class attributes and methods

# Player class attributes and methods

# Listener_Interface class attributes and methods

# ImageIcon class attributes and methods

# javax_swing_JButton class attributes and methods

# javax_swing_JTextField class attributes and methods

# Player_1_Actor class attributes and methods

# Computer_AI_Actor class attributes and methods

# Player_2_Actor class attributes and methods

# Connect_Four_Component class attributes and methods

# List_Token_ class attributes and methods

# Label class attributes and methods

# Button class attributes and methods

# HBox class attributes and methods

# VBox class attributes and methods

# BorderPane class attributes and methods

# Choose_how_many_Players_external class attributes and methods

# Enter_Name_external class attributes and methods

# Select_Column_external class attributes and methods

# Compute_Column_external class attributes and methods

# Relationships
GUI_GamePanel: BinaryAssociation = BinaryAssociation(
    name="GUI_GamePanel",
    ends={
        Property(name="gamePanel20", type=connect_four_gui_GamePanel, multiplicity=Multiplicity(1, 1)),
        Property(name="gUI1", type=connect_four_gui_Connect4GUI, multiplicity=Multiplicity(1, 1))
    }
)
GameOverPanel_GUI: BinaryAssociation = BinaryAssociation(
    name="GameOverPanel_GUI",
    ends={
        Property(name="gUI2", type=connect_four_gui_Connect4GUI, multiplicity=Multiplicity(1, 1)),
        Property(name="gameOverPanel23", type=connect_four_gui_GameOverPanel, multiplicity=Multiplicity(1, 1))
    }
)
Player_1_Choose_how_many_Players: BinaryAssociation = BinaryAssociation(
    name="Player_1_Choose_how_many_Players",
    ends={
        Property(name="choose_how_many_Players4", type=Choose_how_many_Players_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player_15", type=Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Enter_Name_Player_1: BinaryAssociation = BinaryAssociation(
    name="Enter_Name_Player_1",
    ends={
        Property(name="player_16", type=Player_1_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="enter_Name7", type=Enter_Name_external, multiplicity=Multiplicity(0, 1))
    }
)
Player_1_Select_Column: BinaryAssociation = BinaryAssociation(
    name="Player_1_Select_Column",
    ends={
        Property(name="select_Column8", type=Select_Column_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player_19", type=Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Select_Column_Player_2: BinaryAssociation = BinaryAssociation(
    name="Select_Column_Player_2",
    ends={
        Property(name="player_210", type=Player_2_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="select_Column11", type=Select_Column_external, multiplicity=Multiplicity(0, 1))
    }
)
Player_2_Enter_Name: BinaryAssociation = BinaryAssociation(
    name="Player_2_Enter_Name",
    ends={
        Property(name="enter_Name12", type=Enter_Name_external, multiplicity=Multiplicity(0, 1)),
        Property(name="player_213", type=Player_2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Computer_AI_Compute_Column: BinaryAssociation = BinaryAssociation(
    name="Computer_AI_Compute_Column",
    ends={
        Property(name="compute_Column14", type=Compute_Column_external, multiplicity=Multiplicity(0, 1)),
        Property(name="computer_AI15", type=Computer_AI_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_rB3WYA5fEeqFuqcFjV_c2A",
    types={connect_four_gui_GamePanel, connect_four_gui_Connect4GUI, connect_four_gui_Token, connect_four_gui_red, connect_four_gui_GUIPlayer, connect_four_gui_StartMenu, connect_four_gui_stage, connect_four_gui_GameOverPanel, connect_four_gui_Connect4Constant_Interface, connect_four_gui_Circle, Player, Listener_Interface, ImageIcon, javax_swing_JButton, javax_swing_JTextField, Player_1_Actor, Computer_AI_Actor, Player_2_Actor, Connect_Four_Component, List_Token_, Label, Button, HBox, VBox, BorderPane, Choose_how_many_Players_external, Enter_Name_external, Select_Column_external, Compute_Column_external},
    associations={GUI_GamePanel, GameOverPanel_GUI, Player_1_Choose_how_many_Players, Enter_Name_Player_1, Player_1_Select_Column, Select_Column_Player_2, Player_2_Enter_Name, Computer_AI_Compute_Column},
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