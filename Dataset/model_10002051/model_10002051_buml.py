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
BlackJack_Hand = Class(name="BlackJack_Hand")
BlackJack_Generic_Player = Class(name="BlackJack_Generic_Player")
BlackJack_Deck = Class(name="BlackJack_Deck")
BlackJack_Player = Class(name="BlackJack_Player")
BlackJack_House = Class(name="BlackJack_House")
BlackJack_Game = Class(name="BlackJack_Game")
BlackJack_Card = Class(name="BlackJack_Card")

# BlackJack_Hand class attributes and methods
BlackJack_Hand_ArrayList: Property = Property(name="ArrayList", type=BlackJack_Card)
BlackJack_Hand.attributes={BlackJack_Hand_ArrayList}

# BlackJack_Generic_Player class attributes and methods
BlackJack_Generic_Player_valueOfHand: Property = Property(name="valueOfHand", type=IntegerType)
BlackJack_Generic_Player.attributes={BlackJack_Generic_Player_valueOfHand}

# BlackJack_Deck class attributes and methods
BlackJack_Deck_nextItem: Property = Property(name="nextItem", type=IntegerType)
BlackJack_Deck.attributes={BlackJack_Deck_nextItem}

# BlackJack_Player class attributes and methods
BlackJack_Player_limit: Property = Property(name="limit", type=IntegerType)
BlackJack_Player.attributes={BlackJack_Player_limit}

# BlackJack_House class attributes and methods

# BlackJack_Game class attributes and methods
BlackJack_Game_win_loose: Property = Property(name="win_loose", type=BooleanType)
BlackJack_Game.attributes={BlackJack_Game_win_loose}

# BlackJack_Card class attributes and methods
BlackJack_Card_value: Property = Property(name="value", type=IntegerType)
BlackJack_Card_color: Property = Property(name="color", type=StringType)
BlackJack_Card_rank: Property = Property(name="rank", type=IntegerType)
BlackJack_Card.attributes={BlackJack_Card_color, BlackJack_Card_value, BlackJack_Card_rank}

# Relationships
Game_House: BinaryAssociation = BinaryAssociation(
    name="Game_House",
    ends={
        Property(name="house0", type=BlackJack_House, multiplicity=Multiplicity(1, 1)),
        Property(name="game1", type=BlackJack_Game, multiplicity=Multiplicity(1, 1))
    }
)
Game_Player: BinaryAssociation = BinaryAssociation(
    name="Game_Player",
    ends={
        Property(name="player2", type=BlackJack_Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="Game_Player_13", type=BlackJack_Game, multiplicity=Multiplicity(1, 1))
    }
)
Deck_Game: BinaryAssociation = BinaryAssociation(
    name="Deck_Game",
    ends={
        Property(name="game4", type=BlackJack_House, multiplicity=Multiplicity(0, 1)),
        Property(name="deck5", type=BlackJack_Deck, multiplicity=Multiplicity(1, 1))
    }
)
Card_Hand: BinaryAssociation = BinaryAssociation(
    name="Card_Hand",
    ends={
        Property(name="hand6", type=BlackJack_Hand, multiplicity=Multiplicity(1, 9999)),
        Property(name="card7", type=BlackJack_Card, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_lPwVoNAnEeeLcIicqHdTUQ",
    types={BlackJack_Hand, BlackJack_Generic_Player, BlackJack_Deck, BlackJack_Player, BlackJack_House, BlackJack_Game, BlackJack_Card},
    associations={Game_House, Game_Player, Deck_Game, Card_Hand},
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