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
en: Enumeration = Enumeration(
    name="en",
    literals={
            
    }
)

en2: Enumeration = Enumeration(
    name="en2",
    literals={
            
    }
)

Rank: Enumeration = Enumeration(
    name="Rank",
    literals={
            
    }
)

Suit: Enumeration = Enumeration(
    name="Suit",
    literals={
            
    }
)

# Classes
Player1_Actor = Class(name="Player1_Actor")
Player2_Actor = Class(name="Player2_Actor")
Play_UseCase = Class(name="Play_UseCase")
War_UseCase = Class(name="War_UseCase")
Winner_UseCase = Class(name="Winner_UseCase")
War_UseCase1 = Class(name="War_UseCase1")
Play_UseCase1 = Class(name="Play_UseCase1")
playerTwo_external = Class(name="playerTwo_external")
playerOne_external = Class(name="playerOne_external")
WAR = Class(name="WAR")
Deck = Class(name="Deck")
Card_Interface = Class(name="Card_Interface")
Players = Class(name="Players")
Play = Class(name="Play")

# Player1_Actor class attributes and methods

# Player2_Actor class attributes and methods

# Play_UseCase class attributes and methods

# War_UseCase class attributes and methods

# Winner_UseCase class attributes and methods

# War_UseCase1 class attributes and methods

# Play_UseCase1 class attributes and methods

# playerTwo_external class attributes and methods

# playerOne_external class attributes and methods

# WAR class attributes and methods

# Deck class attributes and methods
Deck_topcard: Property = Property(name="topcard", type=IntegerType)
Deck_draw__: Property = Property(name="draw__", type=StringType)
Deck_shuffle__: Property = Property(name="shuffle__", type=StringType)
Deck_deck__: Property = Property(name="deck__", type=Deck)
Deck_isEmpty__: Property = Property(name="isEmpty__", type=BooleanType)
Deck.attributes={Deck_shuffle__, Deck_topcard, Deck_deck__, Deck_draw__, Deck_isEmpty__}

# Card_Interface class attributes and methods

# Players class attributes and methods
Players_Player1: Property = Property(name="Player1", type=Card_Interface)
Players_Player2: Property = Property(name="Player2", type=Card_Interface)
Players.attributes={Players_Player2, Players_Player1}

# Play class attributes and methods
Play_Score: Property = Property(name="Score", type=IntegerType)
Play_removedCard: Property = Property(name="removedCard", type=IntegerType)
Play.attributes={Play_removedCard, Play_Score}

# Relationships
Deck_WAR: BinaryAssociation = BinaryAssociation(
    name="Deck_WAR",
    ends={
        Property(name="wAR0", type=WAR, multiplicity=Multiplicity(0, 1)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card2", type=Card_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="deck3", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
WAR_Players: BinaryAssociation = BinaryAssociation(
    name="WAR_Players",
    ends={
        Property(name="players4", type=Players, multiplicity=Multiplicity(0, 1)),
        Property(name="wAR5", type=WAR, multiplicity=Multiplicity(0, 1))
    }
)
Players_WAR: BinaryAssociation = BinaryAssociation(
    name="Players_WAR",
    ends={
        Property(name="wAR6", type=WAR, multiplicity=Multiplicity(0, 1)),
        Property(name="players7", type=Players, multiplicity=Multiplicity(0, 1))
    }
)
Function_Players: BinaryAssociation = BinaryAssociation(
    name="Function_Players",
    ends={
        Property(name="players28", type=Players, multiplicity=Multiplicity(0, 1)),
        Property(name="play9", type=Play, multiplicity=Multiplicity(0, 1))
    }
)
Function_PlayerCPU: BinaryAssociation = BinaryAssociation(
    name="Function_PlayerCPU",
    ends={
        Property(name="playerTwo10", type=playerTwo_external, multiplicity=Multiplicity(0, 1)),
        Property(name="play11", type=Play, multiplicity=Multiplicity(0, 1))
    }
)
Function_PlayerUser: BinaryAssociation = BinaryAssociation(
    name="Function_PlayerUser",
    ends={
        Property(name="playerOne12", type=playerOne_external, multiplicity=Multiplicity(0, 1)),
        Property(name="play13", type=Play, multiplicity=Multiplicity(0, 1))
    }
)
Function_Card: BinaryAssociation = BinaryAssociation(
    name="Function_Card",
    ends={
        Property(name="card14", type=Card_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="play15", type=Play, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Function: BinaryAssociation = BinaryAssociation(
    name="Deck_Function",
    ends={
        Property(name="play16", type=Play, multiplicity=Multiplicity(0, 1)),
        Property(name="deck17", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
Player2_Play: BinaryAssociation = BinaryAssociation(
    name="Player2_Play",
    ends={
        Property(name="play18", type=Play_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player219", type=Player2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player1_Play: BinaryAssociation = BinaryAssociation(
    name="Player1_Play",
    ends={
        Property(name="play20", type=Play_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player121", type=Player1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Play_Winner: BinaryAssociation = BinaryAssociation(
    name="Play_Winner",
    ends={
        Property(name="winner22", type=War_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="play23", type=Play_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Winner_Play: BinaryAssociation = BinaryAssociation(
    name="Winner_Play",
    ends={
        Property(name="play24", type=Winner_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="winner25", type=War_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Play_Winner2: BinaryAssociation = BinaryAssociation(
    name="Play_Winner2",
    ends={
        Property(name="winner26", type=War_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="play27", type=War_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Play_Winner3: BinaryAssociation = BinaryAssociation(
    name="Play_Winner3",
    ends={
        Property(name="winner28", type=Winner_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="play29", type=Play_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0426b845_7afa_40ba_ae6a_6c5af4257b73",
    types={Player1_Actor, Player2_Actor, Play_UseCase, War_UseCase, Winner_UseCase, War_UseCase1, Play_UseCase1, playerTwo_external, playerOne_external, WAR, Deck, Card_Interface, Players, Play, en, en2, Rank, Suit},
    associations={Deck_WAR, Deck_Card, WAR_Players, Players_WAR, Function_Players, Function_PlayerCPU, Function_PlayerUser, Function_Card, Deck_Function, Player2_Play, Player1_Play, Play_Winner, Winner_Play, Play_Winner2, Play_Winner3},
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