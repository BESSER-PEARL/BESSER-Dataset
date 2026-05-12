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

Suit2: Enumeration = Enumeration(
    name="Suit2",
    literals={
            
    }
)

Kind2: Enumeration = Enumeration(
    name="Kind2",
    literals={
            
    }
)

Suit1: Enumeration = Enumeration(
    name="Suit1",
    literals={
            
    }
)

Kind1: Enumeration = Enumeration(
    name="Kind1",
    literals={
            
    }
)

# Classes
Theme = Class(name="Theme")
Deck = Class(name="Deck")
Game = Class(name="Game", is_abstract=True)
Card = Class(name="Card")
Avatar = Class(name="Avatar")
Player = Class(name="Player", is_abstract=True)
Theme2 = Class(name="Theme2")
Deck2 = Class(name="Deck2")
Game2 = Class(name="Game2", is_abstract=True)
Card2 = Class(name="Card2")
Avatar2 = Class(name="Avatar2")
Player2 = Class(name="Player2", is_abstract=True)
Theme1 = Class(name="Theme1")
Deck1 = Class(name="Deck1")
Game1 = Class(name="Game1", is_abstract=True)
Card1 = Class(name="Card1")
Avatar1 = Class(name="Avatar1")
Player1 = Class(name="Player1", is_abstract=True)

# Theme class attributes and methods

# Deck class attributes and methods

# Game class attributes and methods
Game_name: Property = Property(name="name", type=StringType)
Game.attributes={Game_name}

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=Suit)
Card_kind: Property = Property(name="kind", type=Kind)
Card.attributes={Card_suit, Card_kind}

# Avatar class attributes and methods

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player.attributes={Player_name}

# Theme2 class attributes and methods

# Deck2 class attributes and methods

# Game2 class attributes and methods
Game2_name: Property = Property(name="name", type=StringType)
Game2.attributes={Game2_name}

# Card2 class attributes and methods
Card2_suit: Property = Property(name="suit", type=Suit2)
Card2_kind: Property = Property(name="kind", type=Kind2)
Card2.attributes={Card2_kind, Card2_suit}

# Avatar2 class attributes and methods

# Player2 class attributes and methods
Player2_name: Property = Property(name="name", type=StringType)
Player2.attributes={Player2_name}

# Theme1 class attributes and methods

# Deck1 class attributes and methods
Deck1_Card_cards_52_: Property = Property(name="Card_cards_52_", type=Card)
Deck1.attributes={Deck1_Card_cards_52_}

# Game1 class attributes and methods
Game1_name: Property = Property(name="name", type=StringType)
Game1.attributes={Game1_name}

# Card1 class attributes and methods
Card1_suit: Property = Property(name="suit", type=Suit1)
Card1_kind: Property = Property(name="kind", type=Kind1)
Card1.attributes={Card1_kind, Card1_suit}

# Avatar1 class attributes and methods

# Player1 class attributes and methods
Player1_name: Property = Property(name="name", type=StringType)
Player1_hand: Property = Property(name="hand", type=StringType)
Player1.attributes={Player1_hand, Player1_name}

# Relationships
Deck_Theme2: BinaryAssociation = BinaryAssociation(
    name="Deck_Theme2",
    ends={
        Property(name="decks13", type=Deck2, multiplicity=Multiplicity(0, 9999)),
        Property(name="theme12", type=Theme2, multiplicity=Multiplicity(1, 1))
    }
)
Deck_Card2: BinaryAssociation = BinaryAssociation(
    name="Deck_Card2",
    ends={
        Property(name="cards14", type=Card2, multiplicity=Multiplicity(1, 9999)),
        Property(name="deck15", type=Deck2, multiplicity=Multiplicity(1, 1))
    }
)
Game_Deck2: BinaryAssociation = BinaryAssociation(
    name="Game_Deck2",
    ends={
        Property(name="decks16", type=Deck2, multiplicity=Multiplicity(1, 9999)),
        Property(name="games17", type=Game2, multiplicity=Multiplicity(0, 9999))
    }
)
Game_Player2: BinaryAssociation = BinaryAssociation(
    name="Game_Player2",
    ends={
        Property(name="players18", type=Player2, multiplicity=Multiplicity(1, 9999)),
        Property(name="games19", type=Game2, multiplicity=Multiplicity(0, 9999))
    }
)
Player_Card2: BinaryAssociation = BinaryAssociation(
    name="Player_Card2",
    ends={
        Property(name="cards20", type=Card2, multiplicity=Multiplicity(1, 9999)),
        Property(name="player21", type=Player2, multiplicity=Multiplicity(0, 1))
    }
)
Player_Avatar2: BinaryAssociation = BinaryAssociation(
    name="Player_Avatar2",
    ends={
        Property(name="avatar22", type=Avatar2, multiplicity=Multiplicity(0, 1)),
        Property(name="players23", type=Player2, multiplicity=Multiplicity(0, 9999))
    }
)
Deck_Theme3: BinaryAssociation = BinaryAssociation(
    name="Deck_Theme3",
    ends={
        Property(name="theme24", type=Theme1, multiplicity=Multiplicity(1, 1)),
        Property(name="decks25", type=Deck1, multiplicity=Multiplicity(0, 9999))
    }
)
Deck_Theme: BinaryAssociation = BinaryAssociation(
    name="Deck_Theme",
    ends={
        Property(name="theme0", type=Theme, multiplicity=Multiplicity(1, 1)),
        Property(name="decks1", type=Deck, multiplicity=Multiplicity(0, 9999))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="cards2", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="deck3", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
Game_Deck: BinaryAssociation = BinaryAssociation(
    name="Game_Deck",
    ends={
        Property(name="decks4", type=Deck, multiplicity=Multiplicity(1, 9999)),
        Property(name="games5", type=Game, multiplicity=Multiplicity(0, 9999))
    }
)
Game_Player: BinaryAssociation = BinaryAssociation(
    name="Game_Player",
    ends={
        Property(name="players6", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="games7", type=Game, multiplicity=Multiplicity(0, 9999))
    }
)
Player_Card: BinaryAssociation = BinaryAssociation(
    name="Player_Card",
    ends={
        Property(name="cards8", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="player9", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Player_Avatar: BinaryAssociation = BinaryAssociation(
    name="Player_Avatar",
    ends={
        Property(name="avatar10", type=Avatar, multiplicity=Multiplicity(0, 1)),
        Property(name="players11", type=Player, multiplicity=Multiplicity(0, 9999))
    }
)
Deck_Card3: BinaryAssociation = BinaryAssociation(
    name="Deck_Card3",
    ends={
        Property(name="cards26", type=Card1, multiplicity=Multiplicity(1, 9999)),
        Property(name="deck27", type=Deck1, multiplicity=Multiplicity(1, 1))
    }
)
Game_Deck3: BinaryAssociation = BinaryAssociation(
    name="Game_Deck3",
    ends={
        Property(name="decks28", type=Deck1, multiplicity=Multiplicity(1, 9999)),
        Property(name="games29", type=Game1, multiplicity=Multiplicity(0, 9999))
    }
)
Game_Player3: BinaryAssociation = BinaryAssociation(
    name="Game_Player3",
    ends={
        Property(name="players30", type=Player1, multiplicity=Multiplicity(1, 9999)),
        Property(name="games31", type=Game1, multiplicity=Multiplicity(0, 9999))
    }
)
Player_Card3: BinaryAssociation = BinaryAssociation(
    name="Player_Card3",
    ends={
        Property(name="cards32", type=Card1, multiplicity=Multiplicity(1, 9999)),
        Property(name="player33", type=Player1, multiplicity=Multiplicity(0, 1))
    }
)
Player_Avatar3: BinaryAssociation = BinaryAssociation(
    name="Player_Avatar3",
    ends={
        Property(name="avatar34", type=Avatar1, multiplicity=Multiplicity(0, 1)),
        Property(name="players35", type=Player1, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b62c23a3_40c0_4eac_8f31_e43b5556d506",
    types={Theme, Deck, Game, Card, Avatar, Player, Theme2, Deck2, Game2, Card2, Avatar2, Player2, Theme1, Deck1, Game1, Card1, Avatar1, Player1, Suit, Kind, Suit2, Kind2, Suit1, Kind1},
    associations={Deck_Theme2, Deck_Card2, Game_Deck2, Game_Player2, Player_Card2, Player_Avatar2, Deck_Theme3, Deck_Theme, Deck_Card, Game_Deck, Game_Player, Player_Card, Player_Avatar, Deck_Card3, Game_Deck3, Game_Player3, Player_Card3, Player_Avatar3},
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