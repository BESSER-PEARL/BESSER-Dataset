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
BJPlayer = Class(name="BJPlayer", is_abstract=True)
User_Actor = Class(name="User_Actor")
UseCase_UseCase = Class(name="UseCase_UseCase")
JLabel = Class(name="JLabel")
Gambler = Class(name="Gambler")
Dealer = Class(name="Dealer")
BlackjackGame = Class(name="BlackjackGame")
Deck = Class(name="Deck")
HandDeck = Class(name="HandDeck")
Card = Class(name="Card")
Strategy = Class(name="Strategy")
JButton = Class(name="JButton")
Player = Class(name="Player")

# BJPlayer class attributes and methods
BJPlayer_isBusted: Property = Property(name="isBusted", type=BooleanType)
BJPlayer.attributes={BJPlayer_isBusted}

# User_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# JLabel class attributes and methods

# Gambler class attributes and methods
Gambler_hand: Property = Property(name="hand", type=HandDeck)
Gambler_profile: Property = Property(name="profile", type=StringType)
Gambler_money: Property = Property(name="money", type=IntegerType)
Gambler.attributes={Gambler_profile, Gambler_hand, Gambler_money}

# Dealer class attributes and methods
Dealer_hand: Property = Property(name="hand", type=HandDeck)
Dealer_cardTotalLimit: Property = Property(name="cardTotalLimit", type=IntegerType)
Dealer.attributes={Dealer_hand, Dealer_cardTotalLimit}

# BlackjackGame class attributes and methods
BlackjackGame_deck: Property = Property(name="deck", type=Deck)
BlackjackGame_dealer: Property = Property(name="dealer", type=Dealer)
BlackjackGame_player: Property = Property(name="player", type=Gambler)
BlackjackGame_bet: Property = Property(name="bet", type=IntegerType)
BlackjackGame.attributes={BlackjackGame_dealer, BlackjackGame_deck, BlackjackGame_player, BlackjackGame_bet}

# Deck class attributes and methods
Deck_cards: Property = Property(name="cards", type=Card)
Deck.attributes={Deck_cards}

# HandDeck class attributes and methods
HandDeck_cards: Property = Property(name="cards", type=Card)
HandDeck_total: Property = Property(name="total", type=IntegerType)
HandDeck.attributes={HandDeck_total, HandDeck_cards}

# Card class attributes and methods
Card_name: Property = Property(name="name", type=StringType)
Card_avatar: Property = Property(name="avatar", type=StringType)
Card_valueSoft: Property = Property(name="valueSoft", type=StringType)
Card_valueHard: Property = Property(name="valueHard", type=StringType)
Card_suit: Property = Property(name="suit", type=StringType)
Card_rank: Property = Property(name="rank", type=StringType)
Card_Count: Property = Property(name="Count", type=IntegerType)
Card.attributes={Card_suit, Card_rank, Card_valueSoft, Card_name, Card_Count, Card_avatar, Card_valueHard}

# Strategy class attributes and methods
Strategy_game: Property = Property(name="game", type=BlackjackGame)
Strategy.attributes={Strategy_game}

# JButton class attributes and methods

# Player class attributes and methods

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
        Property(name="player3", type=Gambler, multiplicity=Multiplicity(0, 1))
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
        Property(name="hand8", type=HandDeck, multiplicity=Multiplicity(1, 1)),
        Property(name="dealer9", type=Dealer, multiplicity=Multiplicity(1, 1))
    }
)
Player_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Hand",
    ends={
        Property(name="hand10", type=HandDeck, multiplicity=Multiplicity(1, 9999)),
        Property(name="player11", type=Gambler, multiplicity=Multiplicity(1, 1))
    }
)
Hand_Card: BinaryAssociation = BinaryAssociation(
    name="Hand_Card",
    ends={
        Property(name="card12", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="hand13", type=HandDeck, multiplicity=Multiplicity(0, 1))
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
    name="_2xwCoN8EEemZHaiox11UDg",
    types={BJPlayer, User_Actor, UseCase_UseCase, JLabel, Gambler, Dealer, BlackjackGame, Deck, HandDeck, Card, Strategy, JButton, Player},
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