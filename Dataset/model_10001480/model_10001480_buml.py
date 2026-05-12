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
color: Enumeration = Enumeration(
    name="color",
    literals={
            
    }
)

PieceType: Enumeration = Enumeration(
    name="PieceType",
    literals={
            
    }
)

# Classes
ChessBoardInterface_Interface = Class(name="ChessBoardInterface_Interface")
Square = Class(name="Square")
Position = Class(name="Position")
Piece = Class(name="Piece")
Bishop = Class(name="Bishop")
Rook = Class(name="Rook")
King = Class(name="King")
Knigh = Class(name="Knigh")
Pawn = Class(name="Pawn")
Queen = Class(name="Queen")
ChessBoard = Class(name="ChessBoard")
ChessGameController = Class(name="ChessGameController")
BoardValidator = Class(name="BoardValidator")
Player = Class(name="Player")
ChessGame = Class(name="ChessGame")
BoardValidatorInterface_Interface = Class(name="BoardValidatorInterface_Interface")
BoardViewInterface_Interface = Class(name="BoardViewInterface_Interface")
BoardView = Class(name="BoardView")

# ChessBoardInterface_Interface class attributes and methods

# Square class attributes and methods
Square_position: Property = Property(name="position", type=Position)
Square_piece: Property = Property(name="piece", type=Piece)
Square.attributes={Square_position, Square_piece}

# Position class attributes and methods
Position_x: Property = Property(name="x", type=IntegerType)
Position_y: Property = Property(name="y", type=IntegerType)
Position.attributes={Position_y, Position_x}

# Piece class attributes and methods
Piece_attribute: Property = Property(name="attribute", type=StringType)
Piece.attributes={Piece_attribute}

# Bishop class attributes and methods

# Rook class attributes and methods

# King class attributes and methods

# Knigh class attributes and methods

# Pawn class attributes and methods

# Queen class attributes and methods

# ChessBoard class attributes and methods

# ChessGameController class attributes and methods
ChessGameController_attribute: Property = Property(name="attribute", type=StringType)
ChessGameController_attribute2: Property = Property(name="attribute2", type=StringType)
ChessGameController.attributes={ChessGameController_attribute2, ChessGameController_attribute}

# BoardValidator class attributes and methods

# Player class attributes and methods

# ChessGame class attributes and methods

# BoardValidatorInterface_Interface class attributes and methods

# BoardViewInterface_Interface class attributes and methods

# BoardView class attributes and methods

# Relationships
ChessBoard_Piece: BinaryAssociation = BinaryAssociation(
    name="ChessBoard_Piece",
    ends={
        Property(name="piece0", type=Piece, multiplicity=Multiplicity(1, 9999)),
        Property(name="chessBoard1", type=ChessBoard, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9uWo0FA_EeeTnI9B59buBQ",
    types={ChessBoardInterface_Interface, Square, Position, Piece, Bishop, Rook, King, Knigh, Pawn, Queen, ChessBoard, ChessGameController, BoardValidator, Player, ChessGame, BoardValidatorInterface_Interface, BoardViewInterface_Interface, BoardView, color, PieceType},
    associations={ChessBoard_Piece},
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