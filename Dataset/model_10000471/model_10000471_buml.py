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
Poker = Class(name="Poker")
Card = Class(name="Card")
Hand = Class(name="Hand")
Player = Class(name="Player", is_abstract=True)
RecordBook = Class(name="RecordBook")
Deck = Class(name="Deck")
Dealer = Class(name="Dealer")
HandStrength = Class(name="HandStrength")
Bank = Class(name="Bank")
Human = Class(name="Human")
Computer = Class(name="Computer")

# Poker class attributes and methods
Poker_player1: Property = Property(name="player1", type=Player)
Poker_player2: Property = Property(name="player2", type=Player)
Poker_dealer: Property = Property(name="dealer", type=Dealer)
Poker.attributes={Poker_player1, Poker_dealer, Poker_player2}

# Card class attributes and methods
Card_name: Property = Property(name="name", type=StringType)
Card_val: Property = Property(name="val", type=StringType)
Card_img: Property = Property(name="img", type=StringType)
Card_suit: Property = Property(name="suit", type=StringType)
Card.attributes={Card_suit, Card_name, Card_val, Card_img}

# Hand class attributes and methods
Hand_handCollection: Property = Property(name="handCollection", type=StringType)
Hand.attributes={Hand_handCollection}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player_hand: Property = Property(name="hand", type=Hand)
Player_bank: Property = Property(name="bank", type=Bank)
Player.attributes={Player_bank, Player_name, Player_hand}

# RecordBook class attributes and methods
RecordBook_recordList: Property = Property(name="recordList", type=StringType)
RecordBook.attributes={RecordBook_recordList}

# Deck class attributes and methods
Deck_cards: Property = Property(name="cards", type=StringType)
Deck.attributes={Deck_cards}

# Dealer class attributes and methods
Dealer_deck: Property = Property(name="deck", type=Deck)
Dealer_analyzeHand: Property = Property(name="analyzeHand", type=HandStrength)
Dealer.attributes={Dealer_deck, Dealer_analyzeHand}

# HandStrength class attributes and methods
HandStrength_STRAIGHT_FLUSH: Property = Property(name="STRAIGHT_FLUSH", type=IntegerType)
HandStrength.attributes={HandStrength_STRAIGHT_FLUSH}

# Bank class attributes and methods
Bank_total: Property = Property(name="total", type=StringType)
Bank.attributes={Bank_total}

# Human class attributes and methods

# Computer class attributes and methods

# Relationships
Hand_Card: BinaryAssociation = BinaryAssociation(
    name="Hand_Card",
    ends={
        Property(name="hand11", type=Hand, multiplicity=Multiplicity(1, 1)),
        Property(name="card10", type=Card, multiplicity=Multiplicity(0, 9999))
    }
)
Dealer_Deck: BinaryAssociation = BinaryAssociation(
    name="Dealer_Deck",
    ends={
        Property(name="deck212", type=Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="dealer13", type=Dealer, multiplicity=Multiplicity(1, 1))
    }
)
HandStrength_Dealer: BinaryAssociation = BinaryAssociation(
    name="HandStrength_Dealer",
    ends={
        Property(name="dealer14", type=Dealer, multiplicity=Multiplicity(1, 1)),
        Property(name="handStrength15", type=HandStrength, multiplicity=Multiplicity(1, 1))
    }
)
Bank_Player: BinaryAssociation = BinaryAssociation(
    name="Bank_Player",
    ends={
        Property(name="player16", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="bank217", type=Bank, multiplicity=Multiplicity(1, 1))
    }
)
Card_Deck: BinaryAssociation = BinaryAssociation(
    name="Card_Deck",
    ends={
        Property(name="deck0", type=Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="card1", type=Card, multiplicity=Multiplicity(0, 9999))
    }
)
TexasHoldEm_RecordBook: BinaryAssociation = BinaryAssociation(
    name="TexasHoldEm_RecordBook",
    ends={
        Property(name="recordBook2", type=RecordBook, multiplicity=Multiplicity(1, 1)),
        Property(name="texasHoldEm3", type=Poker, multiplicity=Multiplicity(1, 1))
    }
)
Dealer_TexasHoldEm: BinaryAssociation = BinaryAssociation(
    name="Dealer_TexasHoldEm",
    ends={
        Property(name="texasHoldEm4", type=Poker, multiplicity=Multiplicity(1, 1)),
        Property(name="dealer25", type=Dealer, multiplicity=Multiplicity(1, 1))
    }
)
Player_TexasHoldEm: BinaryAssociation = BinaryAssociation(
    name="Player_TexasHoldEm",
    ends={
        Property(name="texasHoldEm6", type=Poker, multiplicity=Multiplicity(1, 1)),
        Property(name="player7", type=Player, multiplicity=Multiplicity(0, 9999))
    }
)
Player_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Hand",
    ends={
        Property(name="hand28", type=Hand, multiplicity=Multiplicity(1, 1)),
        Property(name="player9", type=Player, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3a22f95c_d681_40b0_9557_55c319b6d876",
    types={Poker, Card, Hand, Player, RecordBook, Deck, Dealer, HandStrength, Bank, Human, Computer},
    associations={Hand_Card, Dealer_Deck, HandStrength_Dealer, Bank_Player, Card_Deck, TexasHoldEm_RecordBook, Dealer_TexasHoldEm, Player_TexasHoldEm, Player_Hand},
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