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
Player: Enumeration = Enumeration(
    name="Player",
    literals={
            
    }
)

STATE: Enumeration = Enumeration(
    name="STATE",
    literals={
            
    }
)

# Classes
Piece = Class(name="Piece", is_abstract=True)
Pawn = Class(name="Pawn")
Rook = Class(name="Rook")
Bishop = Class(name="Bishop")
Knight = Class(name="Knight")
King = Class(name="King")
Queen = Class(name="Queen")

# Piece class attributes and methods
Piece_Name: Property = Property(name="Name", type=StringType)
Piece.attributes={Piece_Name}

# Pawn class attributes and methods

# Rook class attributes and methods

# Bishop class attributes and methods

# Knight class attributes and methods

# King class attributes and methods

# Queen class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_zfOhoKn_EeeEQN1ZyOr__g",
    types={Piece, Pawn, Rook, Bishop, Knight, King, Queen, Player, STATE},
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