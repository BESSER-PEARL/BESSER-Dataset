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
CoordState: Enumeration = Enumeration(
    name="CoordState",
    literals={
            
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            
    }
)

# Classes
Coordinate = Class(name="Coordinate")
Boat = Class(name="Boat")
Board = Class(name="Board")
Player = Class(name="Player")
Game = Class(name="Game")

# Coordinate class attributes and methods
Coordinate_x: Property = Property(name="x", type=IntegerType)
Coordinate_y: Property = Property(name="y", type=IntegerType)
Coordinate_state: Property = Property(name="state", type=CoordState)
Coordinate.attributes={Coordinate_x, Coordinate_y, Coordinate_state}

# Boat class attributes and methods
Boat_startCoord: Property = Property(name="startCoord", type=Coordinate)
Boat_length: Property = Property(name="length", type=IntegerType)
Boat_direction: Property = Property(name="direction", type=Direction)
Boat_MAX_LENGTH: Property = Property(name="MAX_LENGTH", type=IntegerType)
Boat.attributes={Boat_direction, Boat_startCoord, Boat_length, Boat_MAX_LENGTH}

# Board class attributes and methods
Board_aircraftCarrier: Property = Property(name="aircraftCarrier", type=BooleanType)
Board_battleship: Property = Property(name="battleship", type=BooleanType)
Board_submarine: Property = Property(name="submarine", type=BooleanType)
Board_destroyer: Property = Property(name="destroyer", type=BooleanType)
Board_patrolBoat: Property = Property(name="patrolBoat", type=BooleanType)
Board.attributes={Board_destroyer, Board_submarine, Board_battleship, Board_aircraftCarrier, Board_patrolBoat}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player_won: Property = Property(name="won", type=BooleanType)
Player_turn: Property = Property(name="turn", type=BooleanType)
Player.attributes={Player_turn, Player_won, Player_name}

# Game class attributes and methods
Game_done: Property = Property(name="done", type=BooleanType)
Game_p1: Property = Property(name="p1", type=Player)
Game_p2: Property = Property(name="p2", type=Player)
Game.attributes={Game_p2, Game_done, Game_p1}

# Relationships
Board_Coordinate: BinaryAssociation = BinaryAssociation(
    name="Board_Coordinate",
    ends={
        Property(name="coordinates0", type=Coordinate, multiplicity=Multiplicity(1, 9999)),
        Property(name="board1", type=Board, multiplicity=Multiplicity(1, 1))
    }
)
Board_Player: BinaryAssociation = BinaryAssociation(
    name="Board_Player",
    ends={
        Property(name="player2", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="board3", type=Board, multiplicity=Multiplicity(1, 1))
    }
)
Game_Player: BinaryAssociation = BinaryAssociation(
    name="Game_Player",
    ends={
        Property(name="player4", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="game5", type=Game, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_nJGVAP_LEeeLEbIzy5aHfg",
    types={Coordinate, Boat, Board, Player, Game, CoordState, Direction},
    associations={Board_Coordinate, Board_Player, Game_Player},
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