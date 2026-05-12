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
Game = Class(name="Game")
Grid = Class(name="Grid")
Square = Class(name="Square")
Piece = Class(name="Piece")
Checker = Class(name="Checker")
King = Class(name="King")
Spectator = Class(name="Spectator")
Player = Class(name="Player")

# Game class attributes and methods

# Grid class attributes and methods

# Square class attributes and methods

# Piece class attributes and methods

# Checker class attributes and methods

# King class attributes and methods

# Spectator class attributes and methods

# Player class attributes and methods

# Relationships
Player_Game: BinaryAssociation = BinaryAssociation(
    name="Player_Game",
    ends={
        Property(name="game0", type=Game, multiplicity=Multiplicity(0, 9999)),
        Property(name="player1", type=Player, multiplicity=Multiplicity(0, 2))
    }
)
Game_Grid: BinaryAssociation = BinaryAssociation(
    name="Game_Grid",
    ends={
        Property(name="grid2", type=Grid, multiplicity=Multiplicity(1, 1)),
        Property(name="game3", type=Game, multiplicity=Multiplicity(1, 1))
    }
)
Grid_Square: BinaryAssociation = BinaryAssociation(
    name="Grid_Square",
    ends={
        Property(name="square4", type=Square, multiplicity=Multiplicity(0, 9999)),
        Property(name="grid5", type=Grid, multiplicity=Multiplicity(1, 1))
    }
)
Square_Piece: BinaryAssociation = BinaryAssociation(
    name="Square_Piece",
    ends={
        Property(name="piece6", type=Piece, multiplicity=Multiplicity(1, 1)),
        Property(name="square7", type=Square, multiplicity=Multiplicity(1, 1))
    }
)
Player_Piece: BinaryAssociation = BinaryAssociation(
    name="Player_Piece",
    ends={
        Property(name="piece8", type=Piece, multiplicity=Multiplicity(0, 1)),
        Property(name="player9", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Spectator_Game: BinaryAssociation = BinaryAssociation(
    name="Spectator_Game",
    ends={
        Property(name="game10", type=Game, multiplicity=Multiplicity(0, 1)),
        Property(name="spectator11", type=Spectator, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_1oIk0CMrEemOV5tdt4HL0w",
    types={Game, Grid, Square, Piece, Checker, King, Spectator, Player},
    associations={Player_Game, Game_Grid, Grid_Square, Square_Piece, Player_Piece, Spectator_Game},
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