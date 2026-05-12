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
Deck = Class(name="Deck")

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=IntegerType)
Card_value: Property = Property(name="value", type=IntegerType)
Card_JOKER: Property = Property(name="JOKER", type=IntegerType)
Card_CLUBS: Property = Property(name="CLUBS", type=IntegerType)
Card_DIAMONDS: Property = Property(name="DIAMONDS", type=IntegerType)
Card_HEARTS: Property = Property(name="HEARTS", type=IntegerType)
Card_SPADES: Property = Property(name="SPADES", type=IntegerType)
Card_ACE: Property = Property(name="ACE", type=IntegerType)
Card_JACK: Property = Property(name="JACK", type=IntegerType)
Card_QUEEN: Property = Property(name="QUEEN", type=IntegerType)
Card_KING: Property = Property(name="KING", type=IntegerType)
Card.attributes={Card_ACE, Card_SPADES, Card_value, Card_JOKER, Card_suit, Card_JACK, Card_QUEEN, Card_CLUBS, Card_KING, Card_HEARTS, Card_DIAMONDS}

# Deck class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_qPUdkO_9Eee2hpeWh535Sw",
    types={Card, Deck},
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