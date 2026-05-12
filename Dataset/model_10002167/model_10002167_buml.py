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
Deck = Class(name="Deck")
Card = Class(name="Card")
Stack = Class(name="Stack")

# Deck class attributes and methods
Deck_numOfCards: Property = Property(name="numOfCards", type=IntegerType)
Deck_Card__: Property = Property(name="Card__", type=Card)
Deck.attributes={Deck_Card__, Deck_numOfCards}

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=IntegerType)
Card_value: Property = Property(name="value", type=IntegerType)
Card.attributes={Card_suit, Card_value}

# Stack class attributes and methods
Stack_cards__: Property = Property(name="cards__", type=Card)
Stack_numOfCards: Property = Property(name="numOfCards", type=IntegerType)
Stack.attributes={Stack_numOfCards, Stack_cards__}

# Relationships
Card_Deck: BinaryAssociation = BinaryAssociation(
    name="Card_Deck",
    ends={
        Property(name="Contains0", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="card1", type=Card, multiplicity=Multiplicity(0, 1))
    }
)
Card_Stack: BinaryAssociation = BinaryAssociation(
    name="Card_Stack",
    ends={
        Property(name="Conatins2", type=Stack, multiplicity=Multiplicity(0, 1)),
        Property(name="card3", type=Card, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Stack: BinaryAssociation = BinaryAssociation(
    name="Deck_Stack",
    ends={
        Property(name="stack4", type=Stack, multiplicity=Multiplicity(0, 1)),
        Property(name="deals5", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
Stack_Stack: BinaryAssociation = BinaryAssociation(
    name="Stack_Stack",
    ends={
        Property(name="stack6", type=Stack, multiplicity=Multiplicity(0, 1)),
        Property(name="moves7", type=Stack, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_tuFa4MKUEeeEXb8Dudo6PQ",
    types={Deck, Card, Stack},
    associations={Card_Deck, Card_Stack, Deck_Stack, Stack_Stack},
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