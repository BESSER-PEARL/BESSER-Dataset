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
Player = Class(name="Player")
SheddingGame = Class(name="SheddingGame")
TrickGame = Class(name="TrickGame")
MatchingGame = Class(name="MatchingGame")

# Card class attributes and methods
Card_value: Property = Property(name="value", type=IntegerType)
Card_suit: Property = Property(name="suit", type=StringType)
Card.attributes={Card_suit, Card_value}

# Deck class attributes and methods
Deck_deck: Property = Property(name="deck", type=StringType)
Deck.attributes={Deck_deck}

# Game class attributes and methods
Game_players: Property = Property(name="players", type=StringType)
Game_round: Property = Property(name="round", type=IntegerType)
Game_winner: Property = Property(name="winner", type=Player)
Game.attributes={Game_round, Game_winner, Game_players}

# Player class attributes and methods
Player_hand: Property = Property(name="hand", type=StringType)
Player_score: Property = Property(name="score", type=IntegerType)
Player.attributes={Player_score, Player_hand}

# SheddingGame class attributes and methods

# TrickGame class attributes and methods

# MatchingGame class attributes and methods

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="card0", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
holds: BinaryAssociation = BinaryAssociation(
    name="holds",
    ends={
        Property(name="player2", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="card3", type=Card, multiplicity=Multiplicity(1, 9999))
    }
)
isPlayedBy: BinaryAssociation = BinaryAssociation(
    name="isPlayedBy",
    ends={
        Property(name="player4", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="game5", type=Game, multiplicity=Multiplicity(1, 1))
    }
)
drawsFrom: BinaryAssociation = BinaryAssociation(
    name="drawsFrom",
    ends={
        Property(name="deck6", type=Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="game7", type=Game, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_93ce0e84_0274_4d2a_80fc_e8bc8cb6afd6",
    types={Card, Deck, Game, Player, SheddingGame, TrickGame, MatchingGame},
    associations={contains, holds, isPlayedBy, drawsFrom},
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