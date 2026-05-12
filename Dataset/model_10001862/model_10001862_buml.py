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
poker_Game = Class(name="poker_Game")
poker_GameRun = Class(name="poker_GameRun")
card_Card = Class(name="card_Card")
Comparable_Interface = Class(name="Comparable_Interface")
Card = Class(name="Card")
player_Player = Class(name="player_Player")
player_Deck = Class(name="player_Deck")
Board = Class(name="Board")
JFrame = Class(name="JFrame")

# poker_Game class attributes and methods
poker_Game_hand_size: Property = Property(name="hand_size", type=IntegerType)
poker_Game_tryagain: Property = Property(name="tryagain", type=IntegerType)
poker_Game.attributes={poker_Game_hand_size, poker_Game_tryagain}

# poker_GameRun class attributes and methods

# card_Card class attributes and methods
card_Card_suit: Property = Property(name="suit", type=IntegerType)
card_Card_rank: Property = Property(name="rank", type=IntegerType)
card_Card.attributes={card_Card_suit, card_Card_rank}

# Comparable_Interface class attributes and methods

# Card class attributes and methods

# player_Player class attributes and methods

# player_Deck class attributes and methods
player_Deck_deck_size: Property = Property(name="deck_size", type=IntegerType)
player_Deck_hand_size: Property = Property(name="hand_size", type=IntegerType)
player_Deck_numberofShuffles: Property = Property(name="numberofShuffles", type=IntegerType)
player_Deck_remainofDeck: Property = Property(name="remainofDeck", type=IntegerType)
player_Deck.attributes={player_Deck_remainofDeck, player_Deck_deck_size, player_Deck_hand_size, player_Deck_numberofShuffles}

# Board class attributes and methods
Board_cardArea: Property = Property(name="cardArea", type=StringType)
Board_playAagain: Property = Property(name="playAagain", type=StringType)
Board.attributes={Board_cardArea, Board_playAagain}

# JFrame class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_a3NhYAqnEeihOuC11hdjgA",
    types={poker_Game, poker_GameRun, card_Card, Comparable_Interface, Card, player_Player, player_Deck, Board, JFrame},
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