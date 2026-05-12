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
Deck = Class(name="Deck")
Card = Class(name="Card")
Player = Class(name="Player")
CommunityCards = Class(name="CommunityCards")
Game = Class(name="Game")
makeNewPlayer = Class(name="makeNewPlayer")
AI = Class(name="AI")

# Deck class attributes and methods
Deck_cards: Property = Property(name="cards", type=StringType)
Deck_positionInDeck: Property = Property(name="positionInDeck", type=IntegerType)
Deck.attributes={Deck_positionInDeck, Deck_cards}

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=StringType)
Card_value: Property = Property(name="value", type=IntegerType)
Card.attributes={Card_value, Card_suit}

# Player class attributes and methods
Player_hand: Property = Property(name="hand", type=StringType)
Player_isBigBlind: Property = Property(name="isBigBlind", type=BooleanType)
Player_isSmallBlind: Property = Property(name="isSmallBlind", type=BooleanType)
Player_playerNumber: Property = Property(name="playerNumber", type=IntegerType)
Player_chips: Property = Property(name="chips", type=IntegerType)
Player_isFolded: Property = Property(name="isFolded", type=BooleanType)
Player_handValue: Property = Property(name="handValue", type=IntegerType)
Player_name: Property = Property(name="name", type=StringType)
Player_isAllIn: Property = Property(name="isAllIn", type=BooleanType)
Player_isAI: Property = Property(name="isAI", type=BooleanType)
Player.attributes={Player_chips, Player_isSmallBlind, Player_isFolded, Player_isAllIn, Player_name, Player_hand, Player_handValue, Player_isAI, Player_isBigBlind, Player_playerNumber}

# CommunityCards class attributes and methods
CommunityCards_cards: Property = Property(name="cards", type=StringType)
CommunityCards.attributes={CommunityCards_cards}

# Game class attributes and methods
Game_players: Property = Property(name="players", type=StringType)
Game_pot: Property = Property(name="pot", type=IntegerType)
Game_bigBlindValue: Property = Property(name="bigBlindValue", type=IntegerType)
Game_currentDeck: Property = Property(name="currentDeck", type=Deck)
Game_currentCommunityCards: Property = Property(name="currentCommunityCards", type=CommunityCards)
Game_currentBigBlind: Property = Property(name="currentBigBlind", type=IntegerType)
Game.attributes={Game_currentCommunityCards, Game_currentBigBlind, Game_players, Game_pot, Game_currentDeck, Game_bigBlindValue}

# makeNewPlayer class attributes and methods

# AI class attributes and methods

# Relationships
DeckOfCards_Card: BinaryAssociation = BinaryAssociation(
    name="DeckOfCards_Card",
    ends={
        Property(name="card0", type=Card, multiplicity=Multiplicity(1, 1)),
        Property(name="DeckOfCards1", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
Player_Game: BinaryAssociation = BinaryAssociation(
    name="Player_Game",
    ends={
        Property(name="game2", type=Game, multiplicity=Multiplicity(1, 1)),
        Property(name="player3", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
DeckOfCards_Game: BinaryAssociation = BinaryAssociation(
    name="DeckOfCards_Game",
    ends={
        Property(name="game4", type=Game, multiplicity=Multiplicity(1, 1)),
        Property(name="deckOfCards5", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
Community_Cards_Card: BinaryAssociation = BinaryAssociation(
    name="Community_Cards_Card",
    ends={
        Property(name="card6", type=Card, multiplicity=Multiplicity(1, 1)),
        Property(name="communityCards7", type=CommunityCards, multiplicity=Multiplicity(1, 1))
    }
)
Game_Community_Cards: BinaryAssociation = BinaryAssociation(
    name="Game_Community_Cards",
    ends={
        Property(name="communityCards8", type=CommunityCards, multiplicity=Multiplicity(1, 1)),
        Property(name="game9", type=Game, multiplicity=Multiplicity(1, 1))
    }
)
Player_Card: BinaryAssociation = BinaryAssociation(
    name="Player_Card",
    ends={
        Property(name="card10", type=Card, multiplicity=Multiplicity(1, 1)),
        Property(name="player11", type=Player, multiplicity=Multiplicity(1, 1))
    }
)
Game_makeNewPlayer: BinaryAssociation = BinaryAssociation(
    name="Game_makeNewPlayer",
    ends={
        Property(name="makeNewPlayer12", type=makeNewPlayer, multiplicity=Multiplicity(1, 9999)),
        Property(name="game13", type=Game, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9898d915_6ad1_4180_927f_e80f62f462ab",
    types={Deck, Card, Player, CommunityCards, Game, makeNewPlayer, AI},
    associations={DeckOfCards_Card, Player_Game, DeckOfCards_Game, Community_Cards_Card, Game_Community_Cards, Player_Card, Game_makeNewPlayer},
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