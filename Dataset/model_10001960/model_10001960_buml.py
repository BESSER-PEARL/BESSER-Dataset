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
CardName: Enumeration = Enumeration(
    name="CardName",
    literals={
            
    }
)

CardName1: Enumeration = Enumeration(
    name="CardName1",
    literals={
            
    }
)

Suit: Enumeration = Enumeration(
    name="Suit",
    literals={
            
    }
)

# Classes
Player = Class(name="Player")
PlayingCard = Class(name="PlayingCard")
StandCard = Class(name="StandCard")
JokerCard = Class(name="JokerCard")
StandardCard = Class(name="StandardCard")
Deck = Class(name="Deck")
BJPlayer = Class(name="BJPlayer")
HandDeck = Class(name="HandDeck")
Gambler_Interface = Class(name="Gambler_Interface")
Dealer_Interface = Class(name="Dealer_Interface")

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player_pocket: Property = Property(name="pocket", type=IntegerType)
Player.attributes={Player_name, Player_pocket}

# PlayingCard class attributes and methods
PlayingCard_jokerCard: Property = Property(name="jokerCard", type=BooleanType)
PlayingCard_standardCard: Property = Property(name="standardCard", type=BooleanType)
PlayingCard_faceUp: Property = Property(name="faceUp", type=BooleanType)
PlayingCard.attributes={PlayingCard_standardCard, PlayingCard_faceUp, PlayingCard_jokerCard}

# StandCard class attributes and methods

# JokerCard class attributes and methods
JokerCard_jokerCard: Property = Property(name="jokerCard", type=BooleanType)
JokerCard_red: Property = Property(name="red", type=BooleanType)
JokerCard.attributes={JokerCard_jokerCard, JokerCard_red}

# StandardCard class attributes and methods
StandardCard_suit: Property = Property(name="suit", type=StringType)
StandardCard_standardCard: Property = Property(name="standardCard", type=BooleanType)
StandardCard_cardName: Property = Property(name="cardName", type=CardName)
StandardCard.attributes={StandardCard_suit, StandardCard_cardName, StandardCard_standardCard}

# Deck class attributes and methods

# BJPlayer class attributes and methods
BJPlayer_bet: Property = Property(name="bet", type=IntegerType)
BJPlayer_hands: Property = Property(name="hands", type=StringType)
BJPlayer.attributes={BJPlayer_bet, BJPlayer_hands}

# HandDeck class attributes and methods
HandDeck_stand: Property = Property(name="stand", type=BooleanType)
HandDeck_naturalBlackJack: Property = Property(name="naturalBlackJack", type=BooleanType)
HandDeck_pair: Property = Property(name="pair", type=BooleanType)
HandDeck_bust: Property = Property(name="bust", type=BooleanType)
HandDeck.attributes={HandDeck_pair, HandDeck_naturalBlackJack, HandDeck_stand, HandDeck_bust}

# Gambler_Interface class attributes and methods

# Dealer_Interface class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_fr6XYN8jEemZHaiox11UDg",
    types={Player, PlayingCard, StandCard, JokerCard, StandardCard, Deck, BJPlayer, HandDeck, Gambler_Interface, Dealer_Interface, CardName, CardName1, Suit},
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