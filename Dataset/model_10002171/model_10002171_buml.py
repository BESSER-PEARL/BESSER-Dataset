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
Suit: Enumeration = Enumeration(
    name="Suit",
    literals={
            
    }
)

CardSuit: Enumeration = Enumeration(
    name="CardSuit",
    literals={
            
    }
)

Value: Enumeration = Enumeration(
    name="Value",
    literals={
            
    }
)

# Classes
BlackjackGameSimulator = Class(name="BlackjackGameSimulator")
Deck = Class(name="Deck")
Card = Class(name="Card")

# BlackjackGameSimulator class attributes and methods

# Deck class attributes and methods
Deck_ArrayList: Property = Property(name="ArrayList", type=StringType)
Deck.attributes={Deck_ArrayList}

# Card class attributes and methods
Card__CardSuit: Property = Property(name="_CardSuit", type=IntegerType)
Card_toString: Property = Property(name="toString", type=StringType)
Card_Value: Property = Property(name="Value", type=IntegerType)
Card.attributes={Card__CardSuit, Card_Value, Card_toString}

# Domain Model
domain_model = DomainModel(
    name="_u8AE0P61EemrrdzmwAEMcA",
    types={BlackjackGameSimulator, Deck, Card, Suit, CardSuit, Value},
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