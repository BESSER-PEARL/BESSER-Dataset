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
CardName: Enumeration = Enumeration(
    name="CardName",
    literals={
            
    }
)

CardName1: Enumeration = Enumeration(
    name="CardName1",
    literals={
            
    }
)

Suit: Enumeration = Enumeration(
    name="Suit",
    literals={
            
    }
)

# Classes
JokerCard = Class(name="JokerCard")
StandardCard = Class(name="StandardCard")
Deck = Class(name="Deck")
BlackJackHandDeck = Class(name="BlackJackHandDeck")
GameRole = Class(name="GameRole")
Gambler = Class(name="Gambler")
Player = Class(name="Player")
Dealer = Class(name="Dealer")
Player1 = Class(name="Player1")
HandDeck = Class(name="HandDeck")
TEHandDeck = Class(name="TEHandDeck")
Banker = Class(name="Banker")
TEGambler = Class(name="TEGambler")
PlayingCard = Class(name="PlayingCard")
StandCard = Class(name="StandCard")

# JokerCard class attributes and methods
JokerCard_isRed: Property = Property(name="isRed", type=BooleanType)
JokerCard.attributes={JokerCard_isRed}

# StandardCard class attributes and methods
StandardCard_suit: Property = Property(name="suit", type=StringType)
StandardCard_cardName: Property = Property(name="cardName", type=CardName)
StandardCard.attributes={StandardCard_cardName, StandardCard_suit}

# Deck class attributes and methods

# BlackJackHandDeck class attributes and methods
BlackJackHandDeck_stand: Property = Property(name="stand", type=BooleanType)
BlackJackHandDeck_wager: Property = Property(name="wager", type=IntegerType)
BlackJackHandDeck_MAX_SCORE: Property = Property(name="MAX_SCORE", type=IntegerType)
BlackJackHandDeck.attributes={BlackJackHandDeck_wager, BlackJackHandDeck_stand, BlackJackHandDeck_MAX_SCORE}

# GameRole class attributes and methods
GameRole_player: Property = Property(name="player", type=Player)
GameRole.attributes={GameRole_player}

# Gambler class attributes and methods
Gambler_bet: Property = Property(name="bet", type=IntegerType)
Gambler_hands: Property = Property(name="hands", type=StringType)
Gambler_hasSplit: Property = Property(name="hasSplit", type=BooleanType)
Gambler.attributes={Gambler_hasSplit, Gambler_bet, Gambler_hands}

# Player class attributes and methods

# Dealer class attributes and methods
Dealer_hand: Property = Property(name="hand", type=BlackJackHandDeck)
Dealer.attributes={Dealer_hand}

# Player1 class attributes and methods
Player1_name: Property = Property(name="name", type=StringType)
Player1_pocket: Property = Property(name="pocket", type=IntegerType)
Player1.attributes={Player1_pocket, Player1_name}

# HandDeck class attributes and methods
HandDeck_owner: Property = Property(name="owner", type=GameRole)
HandDeck.attributes={HandDeck_owner}

# TEHandDeck class attributes and methods
TEHandDeck_TE_MAX_SCORE: Property = Property(name="TE_MAX_SCORE", type=IntegerType)
TEHandDeck.attributes={TEHandDeck_TE_MAX_SCORE}

# Banker class attributes and methods

# TEGambler class attributes and methods

# PlayingCard class attributes and methods
PlayingCard_faceUp: Property = Property(name="faceUp", type=BooleanType)
PlayingCard.attributes={PlayingCard_faceUp}

# StandCard class attributes and methods

# Relationships
GameRole_Player: BinaryAssociation = BinaryAssociation(
    name="GameRole_Player",
    ends={
        Property(name="player20", type=Player1, multiplicity=Multiplicity(1, 1)),
        Property(name="gameRole1", type=GameRole, multiplicity=Multiplicity(1, 1))
    }
)
Dealer_HandDeck: BinaryAssociation = BinaryAssociation(
    name="Dealer_HandDeck",
    ends={
        Property(name="handDeck2", type=BlackJackHandDeck, multiplicity=Multiplicity(1, 1)),
        Property(name="dealer3", type=Dealer, multiplicity=Multiplicity(1, 1))
    }
)
Gambler_HandDeck: BinaryAssociation = BinaryAssociation(
    name="Gambler_HandDeck",
    ends={
        Property(name="handDeck4", type=BlackJackHandDeck, multiplicity=Multiplicity(1, 9999)),
        Property(name="gambler5", type=Gambler, multiplicity=Multiplicity(1, 1))
    }
)
Deck_PlayingCard: BinaryAssociation = BinaryAssociation(
    name="Deck_PlayingCard",
    ends={
        Property(name="playingCard6", type=PlayingCard, multiplicity=Multiplicity(0, 9999)),
        Property(name="deck7", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_gAsI0N8IEemZHaiox11UDg",
    types={JokerCard, StandardCard, Deck, BlackJackHandDeck, GameRole, Gambler, Player, Dealer, Player1, HandDeck, TEHandDeck, Banker, TEGambler, PlayingCard, StandCard, CardName, CardName1, Suit},
    associations={GameRole_Player, Dealer_HandDeck, Gambler_HandDeck, Deck_PlayingCard},
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