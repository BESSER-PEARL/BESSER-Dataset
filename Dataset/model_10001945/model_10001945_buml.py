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
Connect4_Player = Class(name="Connect4_Player")
Connect4_Token = Class(name="Connect4_Token")
Connect4_Board = Class(name="Connect4_Board")
Connect4_CirclePanel = Class(name="Connect4_CirclePanel")
Connect4_connect = Class(name="Connect4_connect")

# Connect4_Player class attributes and methods
Connect4_Player_name: Property = Property(name="name", type=StringType)
Connect4_Player_wins: Property = Property(name="wins", type=IntegerType)
Connect4_Player_tokenColor: Property = Property(name="tokenColor", type=StringType)
Connect4_Player_currentPlayer: Property = Property(name="currentPlayer", type=BooleanType)
Connect4_Player_roundWon: Property = Property(name="roundWon", type=BooleanType)
Connect4_Player.attributes={Connect4_Player_roundWon, Connect4_Player_wins, Connect4_Player_name, Connect4_Player_tokenColor, Connect4_Player_currentPlayer}

# Connect4_Token class attributes and methods
Connect4_Token_color: Property = Property(name="color", type=StringType)
Connect4_Token_xValue: Property = Property(name="xValue", type=IntegerType)
Connect4_Token_yValue: Property = Property(name="yValue", type=IntegerType)
Connect4_Token_isEmpty: Property = Property(name="isEmpty", type=BooleanType)
Connect4_Token.attributes={Connect4_Token_color, Connect4_Token_yValue, Connect4_Token_xValue, Connect4_Token_isEmpty}

# Connect4_Board class attributes and methods
Connect4_Board_maxRows: Property = Property(name="maxRows", type=IntegerType)
Connect4_Board_maxColumns: Property = Property(name="maxColumns", type=IntegerType)
Connect4_Board_gameBoard: Property = Property(name="gameBoard", type=StringType)
Connect4_Board.attributes={Connect4_Board_maxColumns, Connect4_Board_gameBoard, Connect4_Board_maxRows}

# Connect4_CirclePanel class attributes and methods
Connect4_CirclePanel_color: Property = Property(name="color", type=StringType)
Connect4_CirclePanel_colorIndex: Property = Property(name="colorIndex", type=IntegerType)
Connect4_CirclePanel.attributes={Connect4_CirclePanel_colorIndex, Connect4_CirclePanel_color}

# Connect4_connect class attributes and methods
Connect4_connect_FRAME_WIDTH: Property = Property(name="FRAME_WIDTH", type=IntegerType)
Connect4_connect_FRAME_HEIGHT: Property = Property(name="FRAME_HEIGHT", type=IntegerType)
Connect4_connect_rowSize: Property = Property(name="rowSize", type=IntegerType)
Connect4_connect_columnSize: Property = Property(name="columnSize", type=IntegerType)
Connect4_connect_x: Property = Property(name="x", type=IntegerType)
Connect4_connect_y: Property = Property(name="y", type=IntegerType)
Connect4_connect_panel: Property = Property(name="panel", type=StringType)
Connect4_connect_label1: Property = Property(name="label1", type=StringType)
Connect4_connect_label2: Property = Property(name="label2", type=StringType)
Connect4_connect_label3: Property = Property(name="label3", type=StringType)
Connect4_connect_label4: Property = Property(name="label4", type=StringType)
Connect4_connect_label5: Property = Property(name="label5", type=StringType)
Connect4_connect.attributes={Connect4_connect_label5, Connect4_connect_y, Connect4_connect_label3, Connect4_connect_label2, Connect4_connect_label4, Connect4_connect_x, Connect4_connect_panel, Connect4_connect_columnSize, Connect4_connect_FRAME_WIDTH, Connect4_connect_FRAME_HEIGHT, Connect4_connect_label1, Connect4_connect_rowSize}

# Relationships
Board_Token: BinaryAssociation = BinaryAssociation(
    name="Board_Token",
    ends={
        Property(name="token0", type=Connect4_Token, multiplicity=Multiplicity(1, 9999)),
        Property(name="board1", type=Connect4_Board, multiplicity=Multiplicity(1, 1))
    }
)
Board_Player: BinaryAssociation = BinaryAssociation(
    name="Board_Player",
    ends={
        Property(name="player2", type=Connect4_Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="board3", type=Connect4_Board, multiplicity=Multiplicity(1, 1))
    }
)
CirclePanel_connect: BinaryAssociation = BinaryAssociation(
    name="CirclePanel_connect",
    ends={
        Property(name="connect4", type=Connect4_connect, multiplicity=Multiplicity(1, 9999)),
        Property(name="circlePanel5", type=Connect4_CirclePanel, multiplicity=Multiplicity(1, 1))
    }
)
Board_connect: BinaryAssociation = BinaryAssociation(
    name="Board_connect",
    ends={
        Property(name="connect6", type=Connect4_connect, multiplicity=Multiplicity(0, 1)),
        Property(name="board7", type=Connect4_Board, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_fA1PoNMkEeehRMl7r1_c5g",
    types={Connect4_Player, Connect4_Token, Connect4_Board, Connect4_CirclePanel, Connect4_connect},
    associations={Board_Token, Board_Player, CirclePanel_connect, Board_connect},
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