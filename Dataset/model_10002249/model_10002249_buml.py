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
BasePlayer = Class(name="BasePlayer", is_abstract=True)
User_Actor = Class(name="User_Actor")
UseCase_UseCase = Class(name="UseCase_UseCase")
JLabel = Class(name="JLabel")
Player = Class(name="Player")
Dealer = Class(name="Dealer")
BlackjackGame = Class(name="BlackjackGame")
Deck = Class(name="Deck")
Hand = Class(name="Hand")
Card = Class(name="Card")
Strategy = Class(name="Strategy")
JButton = Class(name="JButton")

# BasePlayer class attributes and methods
BasePlayer_isBusted: Property = Property(name="isBusted", type=BooleanType)
BasePlayer.attributes={BasePlayer_isBusted}

# User_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# JLabel class attributes and methods

# Player class attributes and methods
Player_hand: Property = Property(name="hand", type=Hand)
Player_profile: Property = Property(name="profile", type=StringType)
Player_money: Property = Property(name="money", type=IntegerType)
Player.attributes={Player_hand, Player_profile, Player_money}

# Dealer class attributes and methods
Dealer_cardTotalLimit: Property = Property(name="cardTotalLimit", type=IntegerType)
Dealer_hand: Property = Property(name="hand", type=Hand)
Dealer.attributes={Dealer_cardTotalLimit, Dealer_hand}

# BlackjackGame class attributes and methods
BlackjackGame_deck: Property = Property(name="deck", type=Deck)
BlackjackGame_dealer: Property = Property(name="dealer", type=Dealer)
BlackjackGame_player: Property = Property(name="player", type=Player)
BlackjackGame_bet: Property = Property(name="bet", type=IntegerType)
BlackjackGame.attributes={BlackjackGame_player, BlackjackGame_dealer, BlackjackGame_deck, BlackjackGame_bet}

# Deck class attributes and methods
Deck_cards: Property = Property(name="cards", type=Card)
Deck.attributes={Deck_cards}

# Hand class attributes and methods
Hand_cards: Property = Property(name="cards", type=Card)
Hand_total: Property = Property(name="total", type=IntegerType)
Hand.attributes={Hand_total, Hand_cards}

# Card class attributes and methods
Card_name: Property = Property(name="name", type=StringType)
Card_avatar: Property = Property(name="avatar", type=StringType)
Card_valueSoft: Property = Property(name="valueSoft", type=StringType)
Card_valueHard: Property = Property(name="valueHard", type=StringType)
Card_suit: Property = Property(name="suit", type=StringType)
Card_rank: Property = Property(name="rank", type=StringType)
Card_Count: Property = Property(name="Count", type=IntegerType)
Card.attributes={Card_avatar, Card_Count, Card_name, Card_valueSoft, Card_rank, Card_suit, Card_valueHard}

# Strategy class attributes and methods
Strategy_game: Property = Property(name="game", type=BlackjackGame)
Strategy.attributes={Strategy_game}

# JButton class attributes and methods

# Relationships
Blackjack_Strategy: BinaryAssociation = BinaryAssociation(
    name="Blackjack_Strategy",
    ends={
        Property(name="strategy0", type=Strategy, multiplicity=Multiplicity(0, 1)),
        Property(name="blackjack1", type=BlackjackGame, multiplicity=Multiplicity(0, 1))
    }
)
Player_Blackjack: BinaryAssociation = BinaryAssociation(
    name="Player_Blackjack",
    ends={
        Property(name="blackjack2", type=BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="player3", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Blackjack: BinaryAssociation = BinaryAssociation(
    name="Dealer_Blackjack",
    ends={
        Property(name="blackjack4", type=BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer5", type=Dealer, multiplicity=Multiplicity(0, 1))
    }
)
Blackjack_Deck: BinaryAssociation = BinaryAssociation(
    name="Blackjack_Deck",
    ends={
        Property(name="deck26", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="blackjack7", type=BlackjackGame, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Hand: BinaryAssociation = BinaryAssociation(
    name="Dealer_Hand",
    ends={
        Property(name="hand8", type=Hand, multiplicity=Multiplicity(1, 1)),
        Property(name="dealer9", type=Dealer, multiplicity=Multiplicity(1, 1))
    }
)
Player_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Hand",
    ends={
        Property(name="hand10", type=Hand, multiplicity=Multiplicity(1, 9999)),
        Property(name="player11", type=Player, multiplicity=Multiplicity(1, 1))
    }
)
Hand_Card: BinaryAssociation = BinaryAssociation(
    name="Hand_Card",
    ends={
        Property(name="card12", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="hand13", type=Hand, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card14", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="deck15", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_zR_JsNAJEemalJMtXLKA2A",
    types={BasePlayer, User_Actor, UseCase_UseCase, JLabel, Player, Dealer, BlackjackGame, Deck, Hand, Card, Strategy, JButton},
    associations={Blackjack_Strategy, Player_Blackjack, Dealer_Blackjack, Blackjack_Deck, Dealer_Hand, Player_Hand, Hand_Card, Deck_Card},
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