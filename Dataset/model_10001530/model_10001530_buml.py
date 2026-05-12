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
Game = Class(name="Game")

# Card class attributes and methods
Card_value: Property = Property(name="value", type=IntegerType)
Card.attributes={Card_value}

# Deck class attributes and methods
Deck_cards: Property = Property(name="cards", type=Card)
Deck.attributes={Deck_cards}

# Game class attributes and methods
Game_mainDeck: Property = Property(name="mainDeck", type=Deck)
Game_completedCards: Property = Property(name="completedCards", type=Deck)
Game_cardsOnTable: Property = Property(name="cardsOnTable", type=Card)
Game.attributes={Game_mainDeck, Game_cardsOnTable, Game_completedCards}

# Domain Model
domain_model = DomainModel(
    name="_DxezcEmfEemcCbHu8oEdZw",
    types={Card, Deck, Game},
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