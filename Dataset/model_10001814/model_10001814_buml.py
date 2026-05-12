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

Kind: Enumeration = Enumeration(
    name="Kind",
    literals={
            
    }
)

# Classes
Deck = Class(name="Deck")
Theme = Class(name="Theme")
Avatar = Class(name="Avatar")
Game = Class(name="Game", is_abstract=True)
Player = Class(name="Player", is_abstract=True)
Card = Class(name="Card")
_unnamed = Class(name="_unnamed")

# Deck class attributes and methods

# Theme class attributes and methods

# Avatar class attributes and methods

# Game class attributes and methods
Game_name: Property = Property(name="name", type=StringType)
Game.attributes={Game_name}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player.attributes={Player_name}

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=Suit)
Card_kind: Property = Property(name="kind", type=Kind)
Card.attributes={Card_suit, Card_kind}

# _unnamed class attributes and methods

# Relationships
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="cards0", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
Deck_Theme: BinaryAssociation = BinaryAssociation(
    name="Deck_Theme",
    ends={
        Property(name="theme2", type=Theme, multiplicity=Multiplicity(1, 1)),
        Property(name="decks3", type=Deck, multiplicity=Multiplicity(0, 9999))
    }
)
Player_Avatar: BinaryAssociation = BinaryAssociation(
    name="Player_Avatar",
    ends={
        Property(name="avatar4", type=Avatar, multiplicity=Multiplicity(0, 1)),
        Property(name="players5", type=Player, multiplicity=Multiplicity(0, 9999))
    }
)
Game_Player: BinaryAssociation = BinaryAssociation(
    name="Game_Player",
    ends={
        Property(name="players6", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="games7", type=Game, multiplicity=Multiplicity(0, 9999))
    }
)
Game_Deck: BinaryAssociation = BinaryAssociation(
    name="Game_Deck",
    ends={
        Property(name="decks8", type=Deck, multiplicity=Multiplicity(1, 9999)),
        Property(name="games9", type=Game, multiplicity=Multiplicity(0, 9999))
    }
)
Player_Card: BinaryAssociation = BinaryAssociation(
    name="Player_Card",
    ends={
        Property(name="cards10", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="player11", type=Player, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Xh9KcPXcEemEXt2Xl4w_3Q",
    types={Deck, Theme, Avatar, Game, Player, Card, _unnamed, Suit, Kind},
    associations={Deck_Card, Deck_Theme, Player_Avatar, Game_Player, Game_Deck, Player_Card},
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