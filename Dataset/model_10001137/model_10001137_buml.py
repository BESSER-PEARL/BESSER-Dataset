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

CardNumber: Enumeration = Enumeration(
    name="CardNumber",
    literals={
            
    }
)

Suit1: Enumeration = Enumeration(
    name="Suit1",
    literals={
            
    }
)

# Classes
Card = Class(name="Card")
Deck = Class(name="Deck")
Player = Class(name="Player")
Dealer = Class(name="Dealer")
GameManager = Class(name="GameManager")
Program = Class(name="Program")

# Card class attributes and methods
Card__CardNumber: Property = Property(name="_CardNumber", type=IntegerType)
Card__CardValue: Property = Property(name="_CardValue", type=IntegerType)
Card__Suit: Property = Property(name="_Suit", type=IntegerType)
Card.attributes={Card__Suit, Card__CardNumber, Card__CardValue}

# Deck class attributes and methods
Deck_List_card_: Property = Property(name="List_card_", type=Card)
Deck.attributes={Deck_List_card_}

# Player class attributes and methods
Player_CardsInHand: Property = Property(name="CardsInHand", type=Card)
Player_isSoft: Property = Property(name="isSoft", type=BooleanType)
Player.attributes={Player_isSoft, Player_CardsInHand}

# Dealer class attributes and methods
Dealer_cardDeck: Property = Property(name="cardDeck", type=Deck)
Dealer.attributes={Dealer_cardDeck}

# GameManager class attributes and methods

# Program class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_8a0743e2_3ae7_4bde_b9be_3e6ee6bdbe39",
    types={Card, Deck, Player, Dealer, GameManager, Program, Suit, CardNumber, Suit1},
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