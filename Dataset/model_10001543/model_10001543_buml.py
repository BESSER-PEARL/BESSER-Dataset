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
card = Class(name="card")
cardFace = Class(name="cardFace")
cardValue = Class(name="cardValue")
Player = Class(name="Player")
Deck = Class(name="Deck")
ElevensGame = Class(name="ElevensGame")

# card class attributes and methods
card_has_a: Property = Property(name="has_a", type=cardFace)
card_has_a1: Property = Property(name="has_a1", type=cardValue)
card.attributes={card_has_a1, card_has_a}

# cardFace class attributes and methods
cardFace_Club: Property = Property(name="Club", type=cardFace)
cardFace_has_a: Property = Property(name="has_a", type=cardValue)
cardFace.attributes={cardFace_Club, cardFace_has_a}

# cardValue class attributes and methods
cardValue_Ace: Property = Property(name="Ace", type=cardValue)
cardValue_King: Property = Property(name="King", type=cardValue)
cardValue_Queen: Property = Property(name="Queen", type=cardValue)
cardValue_Jack: Property = Property(name="Jack", type=cardValue)
cardValue.attributes={cardValue_King, cardValue_Queen, cardValue_Ace, cardValue_Jack}

# Player class attributes and methods
Player_has_a: Property = Property(name="has_a", type=card)
Player.attributes={Player_has_a}

# Deck class attributes and methods
Deck_creates_and_shuffles: Property = Property(name="creates_and_shuffles", type=card)
Deck.attributes={Deck_creates_and_shuffles}

# ElevensGame class attributes and methods
ElevensGame_creates_Play_and_Deck: Property = Property(name="creates_Play_and_Deck", type=Deck)
ElevensGame.attributes={ElevensGame_creates_Play_and_Deck}

# Domain Model
domain_model = DomainModel(
    name="_EeRNgEv7EemIEMlOKLl_tQ",
    types={card, cardFace, cardValue, Player, Deck, ElevensGame},
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