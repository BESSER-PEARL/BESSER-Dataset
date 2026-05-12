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
Player = Class(name="Player")
PlayCard = Class(name="PlayCard")
PokerTable = Class(name="PokerTable")
__abstract___BaseDeck = Class(name="__abstract___BaseDeck", is_abstract=True)
GameRound = Class(name="GameRound")
T = Class(name="T")
StandardDeck = Class(name="StandardDeck")
PokerTableView = Class(name="PokerTableView")
PlayerView = Class(name="PlayerView")
Role_external = Class(name="Role_external")
RANK_external = Class(name="RANK_external")
SUIT_external = Class(name="SUIT_external")

# Player class attributes and methods
Player_stack: Property = Property(name="stack", type=IntegerType)
Player_bid: Property = Property(name="bid", type=IntegerType)
Player.attributes={Player_stack, Player_bid}

# PlayCard class attributes and methods

# PokerTable class attributes and methods

# __abstract___BaseDeck class attributes and methods

# GameRound class attributes and methods

# T class attributes and methods

# StandardDeck class attributes and methods

# PokerTableView class attributes and methods

# PlayerView class attributes and methods

# Role_external class attributes and methods

# RANK_external class attributes and methods

# SUIT_external class attributes and methods

# Relationships
Pelaaja_Kortti: BinaryAssociation = BinaryAssociation(
    name="Pelaaja_Kortti",
    ends={
        Property(name="kortti0", type=PlayCard, multiplicity=Multiplicity(2, 2)),
        Property(name="pelaaja1", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
PeliPoyta_Pelaaja: BinaryAssociation = BinaryAssociation(
    name="PeliPoyta_Pelaaja",
    ends={
        Property(name="pelaaja2", type=Player, multiplicity=Multiplicity(2, 9999)),
        Property(name="Table3", type=PokerTable, multiplicity=Multiplicity(1, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card4", type=PlayCard, multiplicity=Multiplicity(52, 52)),
        Property(name="deck5", type=__abstract___BaseDeck, multiplicity=Multiplicity(1, 1))
    }
)
Has_had: BinaryAssociation = BinaryAssociation(
    name="Has_had",
    ends={
        Property(name="Has_had_06", type=GameRound, multiplicity=Multiplicity(0, 9999)),
        Property(name="Previous7", type=PokerTable, multiplicity=Multiplicity(1, 1))
    }
)
Table_Card: BinaryAssociation = BinaryAssociation(
    name="Table_Card",
    ends={
        Property(name="card8", type=PlayCard, multiplicity=Multiplicity(0, 5)),
        Property(name="table9", type=PokerTable, multiplicity=Multiplicity(0, 1))
    }
)
Table_Deck: BinaryAssociation = BinaryAssociation(
    name="Table_Deck",
    ends={
        Property(name="deck10", type=__abstract___BaseDeck, multiplicity=Multiplicity(1, 1)),
        Property(name="table11", type=PokerTable, multiplicity=Multiplicity(1, 1))
    }
)
Player_Role: BinaryAssociation = BinaryAssociation(
    name="Player_Role",
    ends={
        Property(name="role12", type=Role_external, multiplicity=Multiplicity(1, 2)),
        Property(name="player13", type=Player, multiplicity=Multiplicity(1, 1))
    }
)
PlayCard_RANK: BinaryAssociation = BinaryAssociation(
    name="PlayCard_RANK",
    ends={
        Property(name="rANK14", type=RANK_external, multiplicity=Multiplicity(1, 1)),
        Property(name="playCard15", type=PlayCard, multiplicity=Multiplicity(1, 1))
    }
)
PlayCard_SUIT: BinaryAssociation = BinaryAssociation(
    name="PlayCard_SUIT",
    ends={
        Property(name="sUIT16", type=SUIT_external, multiplicity=Multiplicity(1, 1)),
        Property(name="playCard17", type=PlayCard, multiplicity=Multiplicity(1, 1))
    }
)
PokerTable_Player: BinaryAssociation = BinaryAssociation(
    name="PokerTable_Player",
    ends={
        Property(name="Active18", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="pokerTable19", type=PokerTable, multiplicity=Multiplicity(1, 1))
    }
)
PokerTableView_PokerTable: BinaryAssociation = BinaryAssociation(
    name="PokerTableView_PokerTable",
    ends={
        Property(name="pokerTable20", type=PokerTable, multiplicity=Multiplicity(1, 1)),
        Property(name="pokerTableView21", type=PokerTableView, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="afbc058c_d4eb_4c7d_bdaa_cc51eba433e2",
    types={Player, PlayCard, PokerTable, __abstract___BaseDeck, GameRound, T, StandardDeck, PokerTableView, PlayerView, Role_external, RANK_external, SUIT_external},
    associations={Pelaaja_Kortti, PeliPoyta_Pelaaja, Deck_Card, Has_had, Table_Card, Table_Deck, Player_Role, PlayCard_RANK, PlayCard_SUIT, PokerTable_Player, PokerTableView_PokerTable},
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