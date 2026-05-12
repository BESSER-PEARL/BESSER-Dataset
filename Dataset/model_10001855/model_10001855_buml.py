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
Card = Class(name="Card")
Class_ = Class(name="Class")
CardDeckInterface = Class(name="CardDeckInterface")

# Card class attributes and methods
Card_Clubs: Property = Property(name="Clubs", type=StringType)
Card_Hearts: Property = Property(name="Hearts", type=StringType)
Card_Spades: Property = Property(name="Spades", type=StringType)
Card_Diamonds: Property = Property(name="Diamonds", type=StringType)
Card_Ace___14: Property = Property(name="Ace___14", type=IntegerType)
Card_King_13: Property = Property(name="King_13", type=IntegerType)
Card_Queen_12: Property = Property(name="Queen_12", type=IntegerType)
Card_Jack_11: Property = Property(name="Jack_11", type=IntegerType)
Card_suit: Property = Property(name="suit", type=StringType)
Card_face: Property = Property(name="face", type=IntegerType)
Card.attributes={Card_Ace___14, Card_Jack_11, Card_Clubs, Card_Diamonds, Card_face, Card_Hearts, Card_Spades, Card_Queen_12, Card_suit, Card_King_13}

# Class class attributes and methods

# CardDeckInterface class attributes and methods
CardDeckInterface_draw: Property = Property(name="draw", type=Card)
CardDeckInterface_shuffle: Property = Property(name="shuffle", type=StringType)
CardDeckInterface_size: Property = Property(name="size", type=IntegerType)
CardDeckInterface.attributes={CardDeckInterface_size, CardDeckInterface_shuffle, CardDeckInterface_draw}

# Relationships
Card_CardDeckInterface: BinaryAssociation = BinaryAssociation(
    name="Card_CardDeckInterface",
    ends={
        Property(name="cardDeckInterface0", type=CardDeckInterface, multiplicity=Multiplicity(0, 1)),
        Property(name="card1", type=Card, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__Z_g8DNTEemjcq_iJCnVjQ",
    types={Card, Class_, CardDeckInterface},
    associations={Card_CardDeckInterface},
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