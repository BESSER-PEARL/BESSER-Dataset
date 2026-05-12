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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            
    }
)

PlayerType: Enumeration = Enumeration(
    name="PlayerType",
    literals={
            
    }
)

# Classes
Board = Class(name="Board")
Dice = Class(name="Dice")
Field = Class(name="Field")
GameEngine = Class(name="GameEngine")
GameState = Class(name="GameState")
IOFilesManagement = Class(name="IOFilesManagement")
GraphicsGenerator = Class(name="GraphicsGenerator")
Pawn = Class(name="Pawn")
Player = Class(name="Player")
Window = Class(name="Window")
AI = Class(name="AI")
EventHandler = Class(name="EventHandler")
Menu = Class(name="Menu")

# Board class attributes and methods
Board_board: Property = Property(name="board", type=StringType)
Board.attributes={Board_board}

# Dice class attributes and methods

# Field class attributes and methods
Field_color: Property = Property(name="color", type=Color)
Field_x: Property = Property(name="x", type=IntegerType)
Field_y: Property = Property(name="y", type=IntegerType)
Field.attributes={Field_y, Field_x, Field_color}

# GameEngine class attributes and methods

# GameState class attributes and methods

# IOFilesManagement class attributes and methods

# GraphicsGenerator class attributes and methods

# Pawn class attributes and methods

# Player class attributes and methods
Player_type: Property = Property(name="type", type=PlayerType)
Player_color: Property = Property(name="color", type=Color)
Player.attributes={Player_type, Player_color}

# Window class attributes and methods

# AI class attributes and methods

# EventHandler class attributes and methods

# Menu class attributes and methods

# Relationships
IOFilesManagement_GameState: BinaryAssociation = BinaryAssociation(
    name="IOFilesManagement_GameState",
    ends={
        Property(name="IOFilesManagement_GameState_00", type=GameState, multiplicity=Multiplicity(1, 1)),
        Property(name="iOFilesManagement1", type=IOFilesManagement, multiplicity=Multiplicity(1, 1))
    }
)
Player_Dice: BinaryAssociation = BinaryAssociation(
    name="Player_Dice",
    ends={
        Property(name="dice2", type=Dice, multiplicity=Multiplicity(1, 1)),
        Property(name="player3", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Window_GraphicsGenerator: BinaryAssociation = BinaryAssociation(
    name="Window_GraphicsGenerator",
    ends={
        Property(name="graphicsGenerator4", type=GraphicsGenerator, multiplicity=Multiplicity(0, 1)),
        Property(name="window5", type=Window, multiplicity=Multiplicity(0, 1))
    }
)
Board_GraphicsGenerator: BinaryAssociation = BinaryAssociation(
    name="Board_GraphicsGenerator",
    ends={
        Property(name="graphicsGenerator6", type=GraphicsGenerator, multiplicity=Multiplicity(0, 1)),
        Property(name="board7", type=Board, multiplicity=Multiplicity(0, 1))
    }
)
Field_GraphicsGenerator: BinaryAssociation = BinaryAssociation(
    name="Field_GraphicsGenerator",
    ends={
        Property(name="graphicsGenerator8", type=GraphicsGenerator, multiplicity=Multiplicity(0, 1)),
        Property(name="field9", type=Field, multiplicity=Multiplicity(0, 1))
    }
)
GameEngine_Board: BinaryAssociation = BinaryAssociation(
    name="GameEngine_Board",
    ends={
        Property(name="board10", type=Board, multiplicity=Multiplicity(0, 1)),
        Property(name="gameEngine11", type=GameEngine, multiplicity=Multiplicity(0, 1))
    }
)
GameEngine_GameState: BinaryAssociation = BinaryAssociation(
    name="GameEngine_GameState",
    ends={
        Property(name="gameState12", type=GameState, multiplicity=Multiplicity(0, 1)),
        Property(name="gameEngine13", type=GameEngine, multiplicity=Multiplicity(0, 1))
    }
)
GameState_Player: BinaryAssociation = BinaryAssociation(
    name="GameState_Player",
    ends={
        Property(name="player14", type=Player, multiplicity=Multiplicity(0, 1)),
        Property(name="gameState15", type=GameState, multiplicity=Multiplicity(0, 1))
    }
)
Board_Window: BinaryAssociation = BinaryAssociation(
    name="Board_Window",
    ends={
        Property(name="window16", type=Window, multiplicity=Multiplicity(0, 1)),
        Property(name="board17", type=Board, multiplicity=Multiplicity(0, 1))
    }
)
Player_AI: BinaryAssociation = BinaryAssociation(
    name="Player_AI",
    ends={
        Property(name="aI18", type=AI, multiplicity=Multiplicity(0, 1)),
        Property(name="player19", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
GameEngine_EventHandler: BinaryAssociation = BinaryAssociation(
    name="GameEngine_EventHandler",
    ends={
        Property(name="eventHandler20", type=EventHandler, multiplicity=Multiplicity(0, 1)),
        Property(name="gameEngine21", type=GameEngine, multiplicity=Multiplicity(0, 1))
    }
)
GameState_Menu: BinaryAssociation = BinaryAssociation(
    name="GameState_Menu",
    ends={
        Property(name="menu22", type=Menu, multiplicity=Multiplicity(0, 1)),
        Property(name="gameState23", type=GameState, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5ZcHoFeXEeqK2M3E1LfZ7Q",
    types={Board, Dice, Field, GameEngine, GameState, IOFilesManagement, GraphicsGenerator, Pawn, Player, Window, AI, EventHandler, Menu, Color, PlayerType},
    associations={IOFilesManagement_GameState, Player_Dice, Window_GraphicsGenerator, Board_GraphicsGenerator, Field_GraphicsGenerator, GameEngine_Board, GameEngine_GameState, GameState_Player, Board_Window, Player_AI, GameEngine_EventHandler, GameState_Menu},
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