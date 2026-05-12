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

Rank: Enumeration = Enumeration(
    name="Rank",
    literals={
            
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            
    }
)

# Classes
Player = Class(name="Player", is_abstract=True)
Card = Class(name="Card")
Session = Class(name="Session")

# Player class attributes and methods
Player_id: Property = Property(name="id", type=IntegerType)
Player_name: Property = Property(name="name", type=StringType)
Player_hand: Property = Property(name="hand", type=Card)
Player.attributes={Player_id, Player_name, Player_hand}

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=Suit)
Card_rank: Property = Property(name="rank", type=Rank)
Card_color: Property = Property(name="color", type=Color)
Card.attributes={Card_rank, Card_suit, Card_color}

# Session class attributes and methods
Session_id: Property = Property(name="id", type=IntegerType)
Session_players: Property = Property(name="players", type=StringType)
Session_cardDeck: Property = Property(name="cardDeck", type=StringType)
Session_discardPile: Property = Property(name="discardPile", type=StringType)
Session_humanTurn: Property = Property(name="humanTurn", type=BooleanType)
Session_humanPointer: Property = Property(name="humanPointer", type=IntegerType)
Session_currentPlayerPointer: Property = Property(name="currentPlayerPointer", type=IntegerType)
Session_gameStatus: Property = Property(name="gameStatus", type=StringType)
Session_gameStatusCode: Property = Property(name="gameStatusCode", type=IntegerType)
Session.attributes={Session_id, Session_gameStatus, Session_currentPlayerPointer, Session_discardPile, Session_cardDeck, Session_humanPointer, Session_players, Session_gameStatusCode, Session_humanTurn}

# Relationships
Player_Card: BinaryAssociation = BinaryAssociation(
    name="Player_Card",
    ends={
        Property(name="cards0", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="player1", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Session_Card: BinaryAssociation = BinaryAssociation(
    name="Session_Card",
    ends={
        Property(name="card2", type=Card, multiplicity=Multiplicity(0, 1)),
        Property(name="session3", type=Session, multiplicity=Multiplicity(0, 1))
    }
)
Session_Player: BinaryAssociation = BinaryAssociation(
    name="Session_Player",
    ends={
        Property(name="player4", type=Player, multiplicity=Multiplicity(0, 1)),
        Property(name="session5", type=Session, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9a34ca4a_2350_4ee6_84f3_4e30702f7adc",
    types={Player, Card, Session, Suit, Rank, Color},
    associations={Player_Card, Session_Card, Session_Player},
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