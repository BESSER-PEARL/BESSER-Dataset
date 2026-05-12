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
Pitch = Class(name="Pitch")
Card1 = Class(name="Card1")
cardType = Class(name="cardType")
Deck1 = Class(name="Deck1")
Player1 = Class(name="Player1")
Al_player = Class(name="Al_player")
Dealer_Interface = Class(name="Dealer_Interface")
Dealer_Type_Interface = Class(name="Dealer_Type_Interface")
Home = Class(name="Home")
Rank1 = Class(name="Rank1")
Pitch1 = Class(name="Pitch1")
PitchDealer = Class(name="PitchDealer")
List_Card__external = Class(name="List_Card__external")

# Card class attributes and methods
Card_rank: Property = Property(name="rank", type=Rank)
Card_suit: Property = Property(name="suit", type=Suit)
Card.attributes={Card_rank, Card_suit}

# Deck class attributes and methods
Deck_deck: Property = Property(name="deck", type=StringType)
Deck_cardsDealt: Property = Property(name="cardsDealt", type=StringType)
Deck.attributes={Deck_cardsDealt, Deck_deck}

# Player class attributes and methods
Player_bet: Property = Property(name="bet", type=IntegerType)
Player_ID: Property = Property(name="ID", type=StringType)
Player.attributes={Player_bet, Player_ID}

# Game class attributes and methods
Game_dealerCards: Property = Property(name="dealerCards", type=StringType)
Game_playerCards: Property = Property(name="playerCards", type=StringType)
Game.attributes={Game_dealerCards, Game_playerCards}

# Pitch class attributes and methods

# Card1 class attributes and methods
Card1_suit: Property = Property(name="suit", type=Suit)
Card1_Rank: Property = Property(name="Rank", type=Rank)
Card1_total_card: Property = Property(name="total_card", type=StringType)
Card1_cardsRemianing: Property = Property(name="cardsRemianing", type=IntegerType)
Card1.attributes={Card1_cardsRemianing, Card1_total_card, Card1_Rank, Card1_suit}

# cardType class attributes and methods
cardType_Heart: Property = Property(name="Heart", type=cardType)
cardType_Diamond: Property = Property(name="Diamond", type=cardType)
cardType_Spades: Property = Property(name="Spades", type=cardType)
cardType_club: Property = Property(name="club", type=cardType)
cardType.attributes={cardType_club, cardType_Diamond, cardType_Spades, cardType_Heart}

# Deck1 class attributes and methods
Deck1_Totalcards: Property = Property(name="Totalcards", type=IntegerType)
Deck1.attributes={Deck1_Totalcards}

# Player1 class attributes and methods
Player1_id: Property = Property(name="id", type=StringType)
Player1_bet: Property = Property(name="bet", type=IntegerType)
Player1_points: Property = Property(name="points", type=IntegerType)
Player1.attributes={Player1_points, Player1_bet, Player1_id}

# Al_player class attributes and methods
Al_player_bet: Property = Property(name="bet", type=IntegerType)
Al_player_points: Property = Property(name="points", type=IntegerType)
Al_player.attributes={Al_player_bet, Al_player_points}

# Dealer_Interface class attributes and methods

# Dealer_Type_Interface class attributes and methods

# Home class attributes and methods

# Rank1 class attributes and methods
Rank1_intCard_value: Property = Property(name="intCard_value", type=IntegerType)
Rank1.attributes={Rank1_intCard_value}

# Pitch1 class attributes and methods
Pitch1_TotalDealer: Property = Property(name="TotalDealer", type=Dealer_Type_Interface)
Pitch1.attributes={Pitch1_TotalDealer}

# PitchDealer class attributes and methods
PitchDealer_Randomcards: Property = Property(name="Randomcards", type=Card1)
PitchDealer_displaycard: Property = Property(name="displaycard", type=Card1)
PitchDealer_SelectDealer: Property = Property(name="SelectDealer", type=Dealer_Interface)
PitchDealer.attributes={PitchDealer_Randomcards, PitchDealer_SelectDealer, PitchDealer_displaycard}

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
        Property(name="blackJackMain8", type=Pitch, multiplicity=Multiplicity(0, 1)),
        Property(name="game9", type=Game, multiplicity=Multiplicity(0, 1))
    }
)
Player_BlackJackMain: BinaryAssociation = BinaryAssociation(
    name="Player_BlackJackMain",
    ends={
        Property(name="blackJackMain10", type=Pitch, multiplicity=Multiplicity(0, 1)),
        Property(name="player11", type=Player, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_14be3332_bb2f_4945_9c4a_5b2af5dc3977",
    types={Card, Deck, Player, Game, Pitch, Card1, cardType, Deck1, Player1, Al_player, Dealer_Interface, Dealer_Type_Interface, Home, Rank1, Pitch1, PitchDealer, List_Card__external, Suit, Rank},
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