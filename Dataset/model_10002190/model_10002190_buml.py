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
Player = Class(name="Player")

# Card class attributes and methods
Card_faceUp: Property = Property(name="faceUp", type=BooleanType)
Card_value: Property = Property(name="value", type=IntegerType)
Card_display: Property = Property(name="display", type=StringType)
Card_suit: Property = Property(name="suit", type=IntegerType)
Card.attributes={Card_faceUp, Card_display, Card_value, Card_suit}

# Deck class attributes and methods
Deck_deck: Property = Property(name="deck", type=StringType)
Deck_usedCards: Property = Property(name="usedCards", type=StringType)
Deck.attributes={Deck_deck, Deck_usedCards}

# Player class attributes and methods
Player_type: Property = Property(name="type", type=StringType)
Player_value: Property = Property(name="value", type=StringType)
Player_cards: Property = Property(name="cards", type=StringType)
Player.attributes={Player_type, Player_cards, Player_value}

# Relationships
Card_Deck: BinaryAssociation = BinaryAssociation(
    name="Card_Deck",
    ends={
        Property(name="deck0", type=Deck, multiplicity=Multiplicity(0, 9999)),
        Property(name="card1", type=Card, multiplicity=Multiplicity(0, 9999))
    }
)
Player_Card: BinaryAssociation = BinaryAssociation(
    name="Player_Card",
    ends={
        Property(name="card2", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="player3", type=Player, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vLkzsJUmEeiilJ4tAEXZQQ",
    types={Card, Deck, Player},
    associations={Card_Deck, Player_Card},
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