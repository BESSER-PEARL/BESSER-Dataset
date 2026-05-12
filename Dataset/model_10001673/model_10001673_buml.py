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
Face: Enumeration = Enumeration(
    name="Face",
    literals={
            
    }
)

Face1: Enumeration = Enumeration(
    name="Face1",
    literals={
            
    }
)

# Classes
Deck = Class(name="Deck")
Card = Class(name="Card")
Player = Class(name="Player")
Game = Class(name="Game")
Rules = Class(name="Rules")

# Deck class attributes and methods
Deck_numCards: Property = Property(name="numCards", type=IntegerType)
Deck.attributes={Deck_numCards}

# Card class attributes and methods
Card_Enum: Property = Property(name="Enum", type=Face1)
Card.attributes={Card_Enum}

# Player class attributes and methods
Player_numMoves: Property = Property(name="numMoves", type=IntegerType)
Player.attributes={Player_numMoves}

# Game class attributes and methods
Game_numGames: Property = Property(name="numGames", type=IntegerType)
Game_numWins: Property = Property(name="numWins", type=IntegerType)
Game_numLose: Property = Property(name="numLose", type=IntegerType)
Game.attributes={Game_numWins, Game_numLose, Game_numGames}

# Rules class attributes and methods
Rules_card1: Property = Property(name="card1", type=Face1)
Rules_card2: Property = Property(name="card2", type=Face1)
Rules_card3: Property = Property(name="card3", type=Face1)
Rules.attributes={Rules_card3, Rules_card2, Rules_card1}

# Relationships
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card0", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
Player_Deck: BinaryAssociation = BinaryAssociation(
    name="Player_Deck",
    ends={
        Property(name="deck2", type=Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="player3", type=Player, multiplicity=Multiplicity(1, 1))
    }
)
Player_Game: BinaryAssociation = BinaryAssociation(
    name="Player_Game",
    ends={
        Property(name="game4", type=Game, multiplicity=Multiplicity(1, 9999)),
        Property(name="player5", type=Player, multiplicity=Multiplicity(1, 1))
    }
)
Game_Rules: BinaryAssociation = BinaryAssociation(
    name="Game_Rules",
    ends={
        Property(name="rules6", type=Rules, multiplicity=Multiplicity(1, 1)),
        Property(name="game7", type=Game, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Ntj_EEdPEemB7r6RYSs12w",
    types={Deck, Card, Player, Game, Rules, Face, Face1},
    associations={Deck_Card, Player_Deck, Player_Game, Game_Rules},
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