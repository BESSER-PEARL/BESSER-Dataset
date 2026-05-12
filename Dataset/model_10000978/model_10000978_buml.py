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

# Classes
Card = Class(name="Card")
Deck = Class(name="Deck")
Player = Class(name="Player")
Game = Class(name="Game")
BlackJackMain = Class(name="BlackJackMain")
List_Card__external = Class(name="List_Card__external")

# Card class attributes and methods
Card_rank: Property = Property(name="rank", type=Rank)
Card_suit: Property = Property(name="suit", type=Suit)
Card.attributes={Card_suit, Card_rank}

# Deck class attributes and methods
Deck_deck: Property = Property(name="deck", type=StringType)
Deck_cardsDealt: Property = Property(name="cardsDealt", type=StringType)
Deck.attributes={Deck_cardsDealt, Deck_deck}

# Player class attributes and methods
Player_money: Property = Property(name="money", type=IntegerType)
Player_name: Property = Property(name="name", type=StringType)
Player.attributes={Player_money, Player_name}

# Game class attributes and methods
Game_dealerCards: Property = Property(name="dealerCards", type=StringType)
Game_playerCards: Property = Property(name="playerCards", type=StringType)
Game.attributes={Game_dealerCards, Game_playerCards}

# BlackJackMain class attributes and methods

# List_Card__external class attributes and methods

# Relationships
Card_Deck: BinaryAssociation = BinaryAssociation(
    name="Card_Deck",
    ends={
        Property(name="deck0", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="card1", type=Card, multiplicity=Multiplicity(0, 1))
    }
)
Player_Deck: BinaryAssociation = BinaryAssociation(
    name="Player_Deck",
    ends={
        Property(name="deck2", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="player3", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
List_Card__Deck: BinaryAssociation = BinaryAssociation(
    name="List_Card__Deck",
    ends={
        Property(name="deck4", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="list_Card_5", type=List_Card__external, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Game: BinaryAssociation = BinaryAssociation(
    name="Deck_Game",
    ends={
        Property(name="game6", type=Game, multiplicity=Multiplicity(0, 1)),
        Property(name="deck7", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
Game_BlackJackMain: BinaryAssociation = BinaryAssociation(
    name="Game_BlackJackMain",
    ends={
        Property(name="blackJackMain8", type=BlackJackMain, multiplicity=Multiplicity(0, 1)),
        Property(name="game9", type=Game, multiplicity=Multiplicity(0, 1))
    }
)
Player_BlackJackMain: BinaryAssociation = BinaryAssociation(
    name="Player_BlackJackMain",
    ends={
        Property(name="blackJackMain10", type=BlackJackMain, multiplicity=Multiplicity(0, 1)),
        Property(name="player11", type=Player, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_770c3ccb_c19c_4458_a145_80844c55f96a",
    types={Card, Deck, Player, Game, BlackJackMain, List_Card__external, Suit, Rank},
    associations={Card_Deck, Player_Deck, List_Card__Deck, Deck_Game, Game_BlackJackMain, Player_BlackJackMain},
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