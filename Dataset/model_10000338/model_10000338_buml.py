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

# Enumerations
candyCrushPackage_SwapDirection: Enumeration = Enumeration(
    name="candyCrushPackage_SwapDirection",
    literals={
            
    }
)

# Classes
ImageIcon_external = Class(name="ImageIcon_external")
JButton_external = Class(name="JButton_external")
candyCrushPackage_Candy = Class(name="candyCrushPackage_Candy", is_abstract=True)
candyCrushPackage_Visitor_Interface = Class(name="candyCrushPackage_Visitor_Interface")
candyCrushPackage_Visited_Interface = Class(name="candyCrushPackage_Visited_Interface")
candyCrushPackage_RegularCandy = Class(name="candyCrushPackage_RegularCandy")
candyCrushPackage_Game = Class(name="candyCrushPackage_Game")
candyCrushPackage_Menu = Class(name="candyCrushPackage_Menu")
candyCrushPackage_Board = Class(name="candyCrushPackage_Board")
candyCrushPackage_StrippedCandy = Class(name="candyCrushPackage_StrippedCandy")
candyCrushPackage_WrappedCandy = Class(name="candyCrushPackage_WrappedCandy")
candyCrushPackage_ColorBombCandy = Class(name="candyCrushPackage_ColorBombCandy")
candyCrushPackage_CandyButton = Class(name="candyCrushPackage_CandyButton")
candyCrushPackage_JFrame = Class(name="candyCrushPackage_JFrame")
candyCrushPackage_JPanel = Class(name="candyCrushPackage_JPanel")
candyCrushPackage_ActionListener_Interface = Class(name="candyCrushPackage_ActionListener_Interface")
Color_external = Class(name="Color_external")

# ImageIcon_external class attributes and methods

# JButton_external class attributes and methods

# candyCrushPackage_Candy class attributes and methods
candyCrushPackage_Candy_color: Property = Property(name="color", type=IntegerType)
candyCrushPackage_Candy_row: Property = Property(name="row", type=IntegerType)
candyCrushPackage_Candy_col: Property = Property(name="col", type=IntegerType)
candyCrushPackage_Candy.attributes={candyCrushPackage_Candy_color, candyCrushPackage_Candy_col, candyCrushPackage_Candy_row}

# candyCrushPackage_Visitor_Interface class attributes and methods

# candyCrushPackage_Visited_Interface class attributes and methods

# candyCrushPackage_RegularCandy class attributes and methods
candyCrushPackage_RegularCandy_selfCrush: Property = Property(name="selfCrush", type=BooleanType)
candyCrushPackage_RegularCandy_selfCrushRange: Property = Property(name="selfCrushRange", type=IntegerType)
candyCrushPackage_RegularCandy.attributes={candyCrushPackage_RegularCandy_selfCrush, candyCrushPackage_RegularCandy_selfCrushRange}

# candyCrushPackage_Game class attributes and methods
candyCrushPackage_Game_SEP: Property = Property(name="SEP", type=StringType)
candyCrushPackage_Game_IMAGES_PATH: Property = Property(name="IMAGES_PATH", type=StringType)
candyCrushPackage_Game_SOUNDS_PATH: Property = Property(name="SOUNDS_PATH", type=StringType)
candyCrushPackage_Game_WINDOW_WIDTH: Property = Property(name="WINDOW_WIDTH", type=IntegerType)
candyCrushPackage_Game_WINDOW_HEIGHT: Property = Property(name="WINDOW_HEIGHT", type=IntegerType)
candyCrushPackage_Game_playerName: Property = Property(name="playerName", type=StringType)
candyCrushPackage_Game_score: Property = Property(name="score", type=IntegerType)
candyCrushPackage_Game.attributes={candyCrushPackage_Game_SEP, candyCrushPackage_Game_SOUNDS_PATH, candyCrushPackage_Game_WINDOW_WIDTH, candyCrushPackage_Game_IMAGES_PATH, candyCrushPackage_Game_score, candyCrushPackage_Game_playerName, candyCrushPackage_Game_WINDOW_HEIGHT}

# candyCrushPackage_Menu class attributes and methods
candyCrushPackage_Menu_menuBGColor: Property = Property(name="menuBGColor", type=StringType)
candyCrushPackage_Menu_buttonBGColor: Property = Property(name="buttonBGColor", type=StringType)
candyCrushPackage_Menu_highScoreLabel: Property = Property(name="highScoreLabel", type=StringType)
candyCrushPackage_Menu_movesLabel: Property = Property(name="movesLabel", type=StringType)
candyCrushPackage_Menu.attributes={candyCrushPackage_Menu_menuBGColor, candyCrushPackage_Menu_movesLabel, candyCrushPackage_Menu_buttonBGColor, candyCrushPackage_Menu_highScoreLabel}

# candyCrushPackage_Board class attributes and methods
candyCrushPackage_Board_BOARD_HEIGHT: Property = Property(name="BOARD_HEIGHT", type=IntegerType)
candyCrushPackage_Board_SIZE: Property = Property(name="SIZE", type=IntegerType)
candyCrushPackage_Board_candyWidth: Property = Property(name="candyWidth", type=IntegerType)
candyCrushPackage_Board_candyHeight: Property = Property(name="candyHeight", type=IntegerType)
candyCrushPackage_Board_delay: Property = Property(name="delay", type=IntegerType)
candyCrushPackage_Board_moveDistance: Property = Property(name="moveDistance", type=IntegerType)
candyCrushPackage_Board_baseScorePerCandy: Property = Property(name="baseScorePerCandy", type=IntegerType)
candyCrushPackage_Board_movesPerGame: Property = Property(name="movesPerGame", type=IntegerType)
candyCrushPackage_Board_gameScore: Property = Property(name="gameScore", type=IntegerType)
candyCrushPackage_Board_scorePerCandy: Property = Property(name="scorePerCandy", type=StringType)
candyCrushPackage_Board_dropTimer: Property = Property(name="dropTimer", type=StringType)
candyCrushPackage_Board_swapTimer: Property = Property(name="swapTimer", type=StringType)
candyCrushPackage_Board_crushTimer: Property = Property(name="crushTimer", type=StringType)
candyCrushPackage_Board_selfCrushTimer: Property = Property(name="selfCrushTimer", type=StringType)
candyCrushPackage_Board_cascadeTimer: Property = Property(name="cascadeTimer", type=StringType)
candyCrushPackage_Board_dropTimerCount: Property = Property(name="dropTimerCount", type=IntegerType)
candyCrushPackage_Board_swapTimerCount: Property = Property(name="swapTimerCount", type=IntegerType)
candyCrushPackage_Board_crushTimerCount: Property = Property(name="crushTimerCount", type=IntegerType)
candyCrushPackage_Board_selfCrushTimerCount: Property = Property(name="selfCrushTimerCount", type=IntegerType)
candyCrushPackage_Board_isFirstPressed: Property = Property(name="isFirstPressed", type=BooleanType)
candyCrushPackage_Board_isSwapBack: Property = Property(name="isSwapBack", type=BooleanType)
candyCrushPackage_Board_movesLeft: Property = Property(name="movesLeft", type=IntegerType)
candyCrushPackage_Board_firstPressedCandy: Property = Property(name="firstPressedCandy", type=candyCrushPackage_Candy)
candyCrushPackage_Board_secondPressedCandy: Property = Property(name="secondPressedCandy", type=candyCrushPackage_Candy)
candyCrushPackage_Board_selfCrushCandy: Property = Property(name="selfCrushCandy", type=candyCrushPackage_Candy)
candyCrushPackage_Board_swapDirection: Property = Property(name="swapDirection", type=candyCrushPackage_SwapDirection)
candyCrushPackage_Board_HORIZONTAL_GAP: Property = Property(name="HORIZONTAL_GAP", type=IntegerType)
candyCrushPackage_Board_VERTICAL_GAP: Property = Property(name="VERTICAL_GAP", type=IntegerType)
candyCrushPackage_Board_BOARD_WIDTH: Property = Property(name="BOARD_WIDTH", type=IntegerType)
candyCrushPackage_Board.attributes={candyCrushPackage_Board_moveDistance, candyCrushPackage_Board_swapDirection, candyCrushPackage_Board_movesLeft, candyCrushPackage_Board_movesPerGame, candyCrushPackage_Board_delay, candyCrushPackage_Board_selfCrushTimer, candyCrushPackage_Board_swapTimerCount, candyCrushPackage_Board_cascadeTimer, candyCrushPackage_Board_selfCrushCandy, candyCrushPackage_Board_SIZE, candyCrushPackage_Board_swapTimer, candyCrushPackage_Board_BOARD_WIDTH, candyCrushPackage_Board_crushTimer, candyCrushPackage_Board_scorePerCandy, candyCrushPackage_Board_dropTimer, candyCrushPackage_Board_dropTimerCount, candyCrushPackage_Board_gameScore, candyCrushPackage_Board_isSwapBack, candyCrushPackage_Board_BOARD_HEIGHT, candyCrushPackage_Board_crushTimerCount, candyCrushPackage_Board_secondPressedCandy, candyCrushPackage_Board_VERTICAL_GAP, candyCrushPackage_Board_HORIZONTAL_GAP, candyCrushPackage_Board_candyHeight, candyCrushPackage_Board_baseScorePerCandy, candyCrushPackage_Board_isFirstPressed, candyCrushPackage_Board_firstPressedCandy, candyCrushPackage_Board_selfCrushTimerCount, candyCrushPackage_Board_candyWidth}

# candyCrushPackage_StrippedCandy class attributes and methods
candyCrushPackage_StrippedCandy_isHorizontal: Property = Property(name="isHorizontal", type=BooleanType)
candyCrushPackage_StrippedCandy.attributes={candyCrushPackage_StrippedCandy_isHorizontal}

# candyCrushPackage_WrappedCandy class attributes and methods
candyCrushPackage_WrappedCandy_selfCrushRange: Property = Property(name="selfCrushRange", type=IntegerType)
candyCrushPackage_WrappedCandy.attributes={candyCrushPackage_WrappedCandy_selfCrushRange}

# candyCrushPackage_ColorBombCandy class attributes and methods

# candyCrushPackage_CandyButton class attributes and methods
candyCrushPackage_CandyButton_button: Property = Property(name="button", type=StringType)
candyCrushPackage_CandyButton_image: Property = Property(name="image", type=StringType)
candyCrushPackage_CandyButton_x: Property = Property(name="x", type=IntegerType)
candyCrushPackage_CandyButton_y: Property = Property(name="y", type=IntegerType)
candyCrushPackage_CandyButton.attributes={candyCrushPackage_CandyButton_image, candyCrushPackage_CandyButton_y, candyCrushPackage_CandyButton_x, candyCrushPackage_CandyButton_button}

# candyCrushPackage_JFrame class attributes and methods

# candyCrushPackage_JPanel class attributes and methods

# candyCrushPackage_ActionListener_Interface class attributes and methods

# Color_external class attributes and methods

# Relationships
Game_Menu: BinaryAssociation = BinaryAssociation(
    name="Game_Menu",
    ends={
        Property(name="menu0", type=candyCrushPackage_Menu, multiplicity=Multiplicity(0, 1)),
        Property(name="game1", type=candyCrushPackage_Game, multiplicity=Multiplicity(0, 1))
    }
)
Game_Board: BinaryAssociation = BinaryAssociation(
    name="Game_Board",
    ends={
        Property(name="board2", type=candyCrushPackage_Board, multiplicity=Multiplicity(0, 1)),
        Property(name="game3", type=candyCrushPackage_Game, multiplicity=Multiplicity(0, 1))
    }
)
CandyButton_ImageIcon: BinaryAssociation = BinaryAssociation(
    name="CandyButton_ImageIcon",
    ends={
        Property(name="image4", type=ImageIcon_external, multiplicity=Multiplicity(0, 1)),
        Property(name="candyButton5", type=candyCrushPackage_CandyButton, multiplicity=Multiplicity(0, 1))
    }
)
CandyButton_JButton: BinaryAssociation = BinaryAssociation(
    name="CandyButton_JButton",
    ends={
        Property(name="button6", type=JButton_external, multiplicity=Multiplicity(0, 1)),
        Property(name="candyButton7", type=candyCrushPackage_CandyButton, multiplicity=Multiplicity(0, 1))
    }
)
Candy_Candy: BinaryAssociation = BinaryAssociation(
    name="Candy_Candy",
    ends={
        Property(name="board8", type=candyCrushPackage_Candy, multiplicity=Multiplicity(1, 9999)),
        Property(name="candy9", type=candyCrushPackage_Candy, multiplicity=Multiplicity(0, 1))
    }
)
Board_Candy: BinaryAssociation = BinaryAssociation(
    name="Board_Candy",
    ends={
        Property(name="candies10", type=candyCrushPackage_Candy, multiplicity=Multiplicity(1, 9999)),
        Property(name="board11", type=candyCrushPackage_Board, multiplicity=Multiplicity(0, 1))
    }
)
Board_CandyButton: BinaryAssociation = BinaryAssociation(
    name="Board_CandyButton",
    ends={
        Property(name="candiesButtons12", type=candyCrushPackage_CandyButton, multiplicity=Multiplicity(1, 9999)),
        Property(name="board13", type=candyCrushPackage_Board, multiplicity=Multiplicity(0, 1))
    }
)
Menu_Color: BinaryAssociation = BinaryAssociation(
    name="Menu_Color",
    ends={
        Property(name="color14", type=Color_external, multiplicity=Multiplicity(0, 1)),
        Property(name="menu15", type=candyCrushPackage_Menu, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2a80b1de_3868_4066_887d_e9d3489d525f",
    types={ImageIcon_external, JButton_external, candyCrushPackage_Candy, candyCrushPackage_Visitor_Interface, candyCrushPackage_Visited_Interface, candyCrushPackage_RegularCandy, candyCrushPackage_Game, candyCrushPackage_Menu, candyCrushPackage_Board, candyCrushPackage_StrippedCandy, candyCrushPackage_WrappedCandy, candyCrushPackage_ColorBombCandy, candyCrushPackage_CandyButton, candyCrushPackage_JFrame, candyCrushPackage_JPanel, candyCrushPackage_ActionListener_Interface, Color_external, candyCrushPackage_SwapDirection},
    associations={Game_Menu, Game_Board, CandyButton_ImageIcon, CandyButton_JButton, Candy_Candy, Board_Candy, Board_CandyButton, Menu_Color},
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