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
Cards_CardRank: Enumeration = Enumeration(
    name="Cards_CardRank",
    literals={
            
    }
)

Cards_Suit: Enumeration = Enumeration(
    name="Cards_Suit",
    literals={
            
    }
)

Chips_ChipDeductResult: Enumeration = Enumeration(
    name="Chips_ChipDeductResult",
    literals={
            
    }
)

Ranker_Ranking: Enumeration = Enumeration(
    name="Ranker_Ranking",
    literals={
            
    }
)

Player_PlayerStatus: Enumeration = Enumeration(
    name="Player_PlayerStatus",
    literals={
            
    }
)

# Classes
Cards_Card = Class(name="Cards_Card")
Chips_Chip = Class(name="Chips_Chip")
Chips_ChipStash = Class(name="Chips_ChipStash")
Chips_Pot = Class(name="Chips_Pot")
Gameplay_Game = Class(name="Gameplay_Game")
Gameplay_GameInitializer = Class(name="Gameplay_GameInitializer")
Ranker_Rank = Class(name="Ranker_Rank")
Player_Player = Class(name="Player_Player")
DiscardableArray_DiscardableArray_Interface = Class(name="DiscardableArray_DiscardableArray_Interface")
DiscardableArray_DealableArray = Class(name="DiscardableArray_DealableArray")

# Cards_Card class attributes and methods
Cards_Card_rank: Property = Property(name="rank", type=Cards_CardRank)
Cards_Card_suit: Property = Property(name="suit", type=Cards_Suit)
Cards_Card.attributes={Cards_Card_rank, Cards_Card_suit}

# Chips_Chip class attributes and methods
Chips_Chip_value: Property = Property(name="value", type=IntegerType)
Chips_Chip.attributes={Chips_Chip_value}

# Chips_ChipStash class attributes and methods

# Chips_Pot class attributes and methods

# Gameplay_Game class attributes and methods
Gameplay_Game_players: Property = Property(name="players", type=Player_Player)
Gameplay_Game_pot: Property = Property(name="pot", type=Chips_Pot)
Gameplay_Game_deck: Property = Property(name="deck", type=StringType)
Gameplay_Game_round: Property = Property(name="round", type=IntegerType)
Gameplay_Game.attributes={Gameplay_Game_players, Gameplay_Game_deck, Gameplay_Game_round, Gameplay_Game_pot}

# Gameplay_GameInitializer class attributes and methods

# Ranker_Rank class attributes and methods

# Player_Player class attributes and methods
Player_Player_chips: Property = Property(name="chips", type=Chips_ChipStash)
Player_Player_status: Property = Property(name="status", type=Player_PlayerStatus)
Player_Player.attributes={Player_Player_chips, Player_Player_status}

# DiscardableArray_DiscardableArray_Interface class attributes and methods

# DiscardableArray_DealableArray class attributes and methods

# Relationships
Card_Player: BinaryAssociation = BinaryAssociation(
    name="Card_Player",
    ends={
        Property(name="player0", type=Player_Player, multiplicity=Multiplicity(0, 1)),
        Property(name="card1", type=Cards_Card, multiplicity=Multiplicity(0, 5))
    }
)
Chip_ChipStash: BinaryAssociation = BinaryAssociation(
    name="Chip_ChipStash",
    ends={
        Property(name="chipStash2", type=Chips_ChipStash, multiplicity=Multiplicity(0, 9999)),
        Property(name="chip3", type=Chips_Chip, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_eUm1sAiAEeiTXI7G38ZLFQ",
    types={Cards_Card, Chips_Chip, Chips_ChipStash, Chips_Pot, Gameplay_Game, Gameplay_GameInitializer, Ranker_Rank, Player_Player, DiscardableArray_DiscardableArray_Interface, DiscardableArray_DealableArray, Cards_CardRank, Cards_Suit, Chips_ChipDeductResult, Ranker_Ranking, Player_PlayerStatus},
    associations={Card_Player, Chip_ChipStash},
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