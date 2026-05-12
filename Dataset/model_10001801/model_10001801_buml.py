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
Player = Class(name="Player")
Card = Class(name="Card")
Deck = Class(name="Deck")

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player_points: Property = Property(name="points", type=StringType)
Player.attributes={Player_name, Player_points}

# Card class attributes and methods
Card_front: Property = Property(name="front", type=StringType)
Card_suit: Property = Property(name="suit", type=StringType)
Card_value: Property = Property(name="value", type=StringType)
Card.attributes={Card_suit, Card_front, Card_value}

# Deck class attributes and methods
Deck_deck_of_cards: Property = Property(name="deck_of_cards", type=StringType)
Deck_deck_position: Property = Property(name="deck_position", type=IntegerType)
Deck.attributes={Deck_deck_position, Deck_deck_of_cards}

# Relationships
Card_Deck: BinaryAssociation = BinaryAssociation(
    name="Card_Deck",
    ends={
        Property(name="deck0", type=Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="card1", type=Card, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_WT5D8E1SEeict5GQq2fjkw",
    types={Player, Card, Deck},
    associations={Card_Deck},
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