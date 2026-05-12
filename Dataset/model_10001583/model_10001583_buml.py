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
b = Class(name="b")
Computer = Class(name="Computer")
Game = Class(name="Game")
Rules = Class(name="Rules")
GoFish = Class(name="GoFish")
Class_ = Class(name="Class")

# Card class attributes and methods
Card_color: Property = Property(name="color", type=StringType)
Card_suit: Property = Property(name="suit", type=StringType)
Card_number: Property = Property(name="number", type=IntegerType)
Card.attributes={Card_number, Card_suit, Card_color}

# Deck class attributes and methods
Deck_deck: Property = Property(name="deck", type=StringType)
Deck.attributes={Deck_deck}

# Player class attributes and methods
Player_hand: Property = Property(name="hand", type=StringType)
Player_name: Property = Property(name="name", type=StringType)
Player.attributes={Player_name, Player_hand}

# b class attributes and methods

# Computer class attributes and methods

# Game class attributes and methods

# Rules class attributes and methods
Rules_attribute: Property = Property(name="attribute", type=StringType)
Rules_currentRules: Property = Property(name="currentRules", type=BooleanType)
Rules.attributes={Rules_currentRules, Rules_attribute}

# GoFish class attributes and methods

# Class class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_H658wFr_Eemi7vOoM7alqA",
    types={Card, Deck, Player, b, Computer, Game, Rules, GoFish, Class_},
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