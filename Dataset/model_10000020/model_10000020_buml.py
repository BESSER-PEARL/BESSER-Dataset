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
int_Interface = Class(name="int_Interface")
Card = Class(name="Card")
Group = Class(name="Group")
Deck = Class(name="Deck")
Hand = Class(name="Hand")
HandSorter = Class(name="HandSorter")
Player = Class(name="Player")
Team = Class(name="Team")
Trick = Class(name="Trick")
StartGame = Class(name="StartGame")

# int_Interface class attributes and methods

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=IntegerType)
Card_rank: Property = Property(name="rank", type=IntegerType)
Card_isDouble: Property = Property(name="isDouble", type=BooleanType)
Card_points: Property = Property(name="points", type=IntegerType)
Card.attributes={Card_isDouble, Card_rank, Card_suit, Card_points}

# Group class attributes and methods
Group_contents: Property = Property(name="contents", type=StringType)
Group.attributes={Group_contents}

# Deck class attributes and methods

# Hand class attributes and methods

# HandSorter class attributes and methods

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player_number: Property = Property(name="number", type=IntegerType)
Player_score: Property = Property(name="score", type=IntegerType)
Player_hand: Property = Property(name="hand", type=Hand)
Player.attributes={Player_hand, Player_score, Player_number, Player_name}

# Team class attributes and methods
Team_p1: Property = Property(name="p1", type=Player)
Team_p2: Property = Property(name="p2", type=Player)
Team_score: Property = Property(name="score", type=IntegerType)
Team.attributes={Team_score, Team_p2, Team_p1}

# Trick class attributes and methods
Trick_suitLead: Property = Property(name="suitLead", type=IntegerType)
Trick.attributes={Trick_suitLead}

# StartGame class attributes and methods
StartGame_deck: Property = Property(name="deck", type=Deck)
StartGame_p1: Property = Property(name="p1", type=Player)
StartGame_p2: Property = Property(name="p2", type=Player)
StartGame_p3: Property = Property(name="p3", type=Player)
StartGame_p4: Property = Property(name="p4", type=Player)
StartGame_playerOrder: Property = Property(name="playerOrder", type=StringType)
StartGame_t1: Property = Property(name="t1", type=Team)
StartGame_t2: Property = Property(name="t2", type=Team)
StartGame_trick: Property = Property(name="trick", type=Trick)
StartGame_lead: Property = Property(name="lead", type=IntegerType)
StartGame_turn: Property = Property(name="turn", type=IntegerType)
StartGame_bidNumber: Property = Property(name="bidNumber", type=IntegerType)
StartGame.attributes={StartGame_trick, StartGame_p1, StartGame_playerOrder, StartGame_turn, StartGame_p3, StartGame_t2, StartGame_p2, StartGame_t1, StartGame_deck, StartGame_bidNumber, StartGame_p4, StartGame_lead}

# Relationships
Card_Group: BinaryAssociation = BinaryAssociation(
    name="Card_Group",
    ends={
        Property(name="group0", type=Group, multiplicity=Multiplicity(1, 1)),
        Property(name="card1", type=Card, multiplicity=Multiplicity(0, 9999))
    }
)
Team_Player: BinaryAssociation = BinaryAssociation(
    name="Team_Player",
    ends={
        Property(name="player2", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="team3", type=Team, multiplicity=Multiplicity(0, 9999))
    }
)
Player_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Hand",
    ends={
        Property(name="hand4", type=Hand, multiplicity=Multiplicity(1, 1)),
        Property(name="player5", type=Player, multiplicity=Multiplicity(1, 1))
    }
)
StartGame_Player: BinaryAssociation = BinaryAssociation(
    name="StartGame_Player",
    ends={
        Property(name="player6", type=Player, multiplicity=Multiplicity(0, 9999)),
        Property(name="startGame7", type=StartGame, multiplicity=Multiplicity(1, 1))
    }
)
StartGame_Team: BinaryAssociation = BinaryAssociation(
    name="StartGame_Team",
    ends={
        Property(name="team8", type=Team, multiplicity=Multiplicity(0, 9999)),
        Property(name="startGame9", type=StartGame, multiplicity=Multiplicity(1, 1))
    }
)
StartGame_Deck: BinaryAssociation = BinaryAssociation(
    name="StartGame_Deck",
    ends={
        Property(name="deck10", type=Deck, multiplicity=Multiplicity(0, 9999)),
        Property(name="startGame11", type=StartGame, multiplicity=Multiplicity(1, 1))
    }
)
StartGame_Trick: BinaryAssociation = BinaryAssociation(
    name="StartGame_Trick",
    ends={
        Property(name="trick12", type=Trick, multiplicity=Multiplicity(0, 9999)),
        Property(name="startGame13", type=StartGame, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_03cb9bcb_015d_4f5f_89b8_a5f758e3e4da",
    types={int_Interface, Card, Group, Deck, Hand, HandSorter, Player, Team, Trick, StartGame},
    associations={Card_Group, Team_Player, Player_Hand, StartGame_Player, StartGame_Team, StartGame_Deck, StartGame_Trick},
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