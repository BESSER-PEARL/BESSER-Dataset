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
ParkingSpotType: Enumeration = Enumeration(
    name="ParkingSpotType",
    literals={
            
    }
)

PieceColor: Enumeration = Enumeration(
    name="PieceColor",
    literals={
            
    }
)

# Classes
ParkingLot = Class(name="ParkingLot")
ParkingSpot = Class(name="ParkingSpot")
Level = Class(name="Level")
Chess = Class(name="Chess")
Piece = Class(name="Piece")
Knight = Class(name="Knight")
Bishop = Class(name="Bishop")
Rook = Class(name="Rook")
Queen = Class(name="Queen")
King = Class(name="King")
Pawn = Class(name="Pawn")
Slot = Class(name="Slot")

# ParkingLot class attributes and methods
ParkingLot_levels: Property = Property(name="levels", type=StringType)
ParkingLot_spotsOccupied: Property = Property(name="spotsOccupied", type=IntegerType)
ParkingLot_hours: Property = Property(name="hours", type=StringType)
ParkingLot_numOfLevels: Property = Property(name="numOfLevels", type=IntegerType)
ParkingLot_capacity: Property = Property(name="capacity", type=IntegerType)
ParkingLot.attributes={ParkingLot_capacity, ParkingLot_levels, ParkingLot_hours, ParkingLot_spotsOccupied, ParkingLot_numOfLevels}

# ParkingSpot class attributes and methods
ParkingSpot_parkingSpotId: Property = Property(name="parkingSpotId", type=IntegerType)
ParkingSpot_spotType: Property = Property(name="spotType", type=ParkingSpotType)
ParkingSpot_occupied: Property = Property(name="occupied", type=BooleanType)
ParkingSpot.attributes={ParkingSpot_parkingSpotId, ParkingSpot_spotType, ParkingSpot_occupied}

# Level class attributes and methods
Level_parkingSpots: Property = Property(name="parkingSpots", type=StringType)
Level_levelId: Property = Property(name="levelId", type=IntegerType)
Level_numofSpots: Property = Property(name="numofSpots", type=IntegerType)
Level.attributes={Level_numofSpots, Level_parkingSpots, Level_levelId}

# Chess class attributes and methods
Chess_board: Property = Property(name="board", type=StringType)
Chess.attributes={Chess_board}

# Piece class attributes and methods
Piece_pieceColor: Property = Property(name="pieceColor", type=PieceColor)
Piece.attributes={Piece_pieceColor}

# Knight class attributes and methods
Knight_pieceColor: Property = Property(name="pieceColor", type=StringType)
Knight.attributes={Knight_pieceColor}

# Bishop class attributes and methods
Bishop_pieceColor: Property = Property(name="pieceColor", type=StringType)
Bishop.attributes={Bishop_pieceColor}

# Rook class attributes and methods
Rook_pieceColor: Property = Property(name="pieceColor", type=StringType)
Rook.attributes={Rook_pieceColor}

# Queen class attributes and methods
Queen_pieceColor: Property = Property(name="pieceColor", type=StringType)
Queen.attributes={Queen_pieceColor}

# King class attributes and methods
King_pieceColor: Property = Property(name="pieceColor", type=StringType)
King.attributes={King_pieceColor}

# Pawn class attributes and methods
Pawn_pieceColor: Property = Property(name="pieceColor", type=StringType)
Pawn.attributes={Pawn_pieceColor}

# Slot class attributes and methods
Slot_piece: Property = Property(name="piece", type=Piece)
Slot_Occupied: Property = Property(name="Occupied", type=BooleanType)
Slot.attributes={Slot_piece, Slot_Occupied}

# Relationships
ParkingLot_Level: BinaryAssociation = BinaryAssociation(
    name="ParkingLot_Level",
    ends={
        Property(name="level0", type=Level, multiplicity=Multiplicity(0, 9999)),
        Property(name="parkingLot1", type=ParkingLot, multiplicity=Multiplicity(1, 1))
    }
)
Level_ParkingSpot: BinaryAssociation = BinaryAssociation(
    name="Level_ParkingSpot",
    ends={
        Property(name="parkingSpot2", type=ParkingSpot, multiplicity=Multiplicity(0, 9999)),
        Property(name="level3", type=Level, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_rgVxgPZIEeeL5uCiN2F57w",
    types={ParkingLot, ParkingSpot, Level, Chess, Piece, Knight, Bishop, Rook, Queen, King, Pawn, Slot, ParkingSpotType, PieceColor},
    associations={ParkingLot_Level, Level_ParkingSpot},
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