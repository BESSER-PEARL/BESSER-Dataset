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

List_Pieces_: Enumeration = Enumeration(
    name="List_Pieces_",
    literals={
            
    }
)

# Classes
Piece = Class(name="Piece")
Pawn = Class(name="Pawn")
Rook = Class(name="Rook")
Bishop = Class(name="Bishop")
King = Class(name="King")
Queen = Class(name="Queen")
Knight = Class(name="Knight")
Spot = Class(name="Spot")
T = Class(name="T")
Board = Class(name="Board")
Player = Class(name="Player")
List = Class(name="List")

# Piece class attributes and methods
Piece_x: Property = Property(name="x", type=IntegerType)
Piece_y: Property = Property(name="y", type=IntegerType)
Piece_color: Property = Property(name="color", type=Color)
Piece.attributes={Piece_color, Piece_y, Piece_x}

# Pawn class attributes and methods

# Rook class attributes and methods

# Bishop class attributes and methods

# King class attributes and methods

# Queen class attributes and methods

# Knight class attributes and methods

# Spot class attributes and methods
Spot_x: Property = Property(name="x", type=IntegerType)
Spot_y: Property = Property(name="y", type=IntegerType)
Spot_piece: Property = Property(name="piece", type=Piece)
Spot.attributes={Spot_x, Spot_y, Spot_piece}

# T class attributes and methods

# Board class attributes and methods
Board_whitePlayer: Property = Property(name="whitePlayer", type=Player)
Board_blackPlayer: Property = Property(name="blackPlayer", type=Player)
Board_spots: Property = Property(name="spots", type=StringType)
Board_currentPlayer: Property = Property(name="currentPlayer", type=Player)
Board_isCheck: Property = Property(name="isCheck", type=BooleanType)
Board_isCheckMate: Property = Property(name="isCheckMate", type=BooleanType)
Board_isStaleMate: Property = Property(name="isStaleMate", type=BooleanType)
Board.attributes={Board_blackPlayer, Board_whitePlayer, Board_isCheck, Board_spots, Board_currentPlayer, Board_isStaleMate, Board_isCheckMate}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player_color: Property = Property(name="color", type=Color)
Player_pieces: Property = Property(name="pieces", type=List_Pieces_)
Player.attributes={Player_name, Player_color, Player_pieces}

# List class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_MAoWwPnUEeeyruBoe7_QtQ",
    types={Piece, Pawn, Rook, Bishop, King, Queen, Knight, Spot, T, Board, Player, List, Color, List_Pieces_},
    associations={},
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