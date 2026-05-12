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
Game = Class(name="Game")
Player = Class(name="Player")
Hand = Class(name="Hand")
Deck = Class(name="Deck")
Card = Class(name="Card")

# Game class attributes and methods
Game_id: Property = Property(name="id", type=StringType)
Game_name: Property = Property(name="name", type=StringType)
Game_players: Property = Property(name="players", type=StringType)
Game_status: Property = Property(name="status", type=StringType)
Game_deck: Property = Property(name="deck", type=Deck)
Game.attributes={Game_status, Game_players, Game_deck, Game_id, Game_name}

# Player class attributes and methods
Player_id: Property = Property(name="id", type=IntegerType)
Player_name: Property = Property(name="name", type=StringType)
Player_hand: Property = Property(name="hand", type=Hand)
Player_game: Property = Property(name="game", type=Game)
Player_cards: Property = Property(name="cards", type=StringType)
Player.attributes={Player_name, Player_hand, Player_id, Player_game, Player_cards}

# Hand class attributes and methods
Hand_id: Property = Property(name="id", type=IntegerType)
Hand_player: Property = Property(name="player", type=Player)
Hand_game: Property = Property(name="game", type=Game)
Hand_cards: Property = Property(name="cards", type=StringType)
Hand.attributes={Hand_player, Hand_game, Hand_cards, Hand_id}

# Deck class attributes and methods
Deck_id: Property = Property(name="id", type=IntegerType)
Deck_cards: Property = Property(name="cards", type=StringType)
Deck_players: Property = Property(name="players", type=StringType)
Deck_attribute: Property = Property(name="attribute", type=StringType)
Deck_attribute2: Property = Property(name="attribute2", type=StringType)
Deck.attributes={Deck_attribute2, Deck_attribute, Deck_players, Deck_id, Deck_cards}

# Card class attributes and methods
Card_id: Property = Property(name="id", type=IntegerType)
Card_name: Property = Property(name="name", type=StringType)
Card_strength: Property = Property(name="strength", type=StringType)
Card.attributes={Card_strength, Card_id, Card_name}

# Relationships
Game_Player: BinaryAssociation = BinaryAssociation(
    name="Game_Player",
    ends={
        Property(name="player0", type=Player, multiplicity=Multiplicity(0, 9999)),
        Property(name="game1", type=Game, multiplicity=Multiplicity(1, 1))
    }
)
Player_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Hand",
    ends={
        Property(name="hand2", type=Hand, multiplicity=Multiplicity(1, 1)),
        Property(name="player3", type=Player, multiplicity=Multiplicity(1, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card4", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="deck5", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
Hand_Deck: BinaryAssociation = BinaryAssociation(
    name="Hand_Deck",
    ends={
        Property(name="deck6", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="hand7", type=Hand, multiplicity=Multiplicity(0, 9999))
    }
)
Game_Deck: BinaryAssociation = BinaryAssociation(
    name="Game_Deck",
    ends={
        Property(name="deck28", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="game9", type=Game, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_bDIjkH8qEemjx_6_EV_iyQ",
    types={Game, Player, Hand, Deck, Card},
    associations={Game_Player, Player_Hand, Deck_Card, Hand_Deck, Game_Deck},
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