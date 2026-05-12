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
Poker_PokerRank: Enumeration = Enumeration(
    name="Poker_PokerRank",
    literals={
            
    }
)

# Classes
Poker_PokerGame = Class(name="Poker_PokerGame")
Poker_Player = Class(name="Poker_Player")
Poker_Human = Class(name="Poker_Human")
Poker_Computer = Class(name="Poker_Computer")
Poker_Iterator_Interface = Class(name="Poker_Iterator_Interface")
Poker_HandIterator = Class(name="Poker_HandIterator")
Poker_Hand = Class(name="Poker_Hand")
Cards_Card = Class(name="Cards_Card")
Cards_Deck = Class(name="Cards_Deck")

# Poker_PokerGame class attributes and methods
Poker_PokerGame_numPlayers: Property = Property(name="numPlayers", type=IntegerType)
Poker_PokerGame_Round: Property = Property(name="Round", type=IntegerType)
Poker_PokerGame.attributes={Poker_PokerGame_numPlayers, Poker_PokerGame_Round}

# Poker_Player class attributes and methods
Poker_Player_currentMoney: Property = Property(name="currentMoney", type=IntegerType)
Poker_Player_currentBet: Property = Property(name="currentBet", type=IntegerType)
Poker_Player_hand: Property = Property(name="hand", type=Poker_Hand)
Poker_Player.attributes={Poker_Player_currentBet, Poker_Player_currentMoney, Poker_Player_hand}

# Poker_Human class attributes and methods

# Poker_Computer class attributes and methods

# Poker_Iterator_Interface class attributes and methods

# Poker_HandIterator class attributes and methods

# Poker_Hand class attributes and methods
Poker_Hand_numCards: Property = Property(name="numCards", type=IntegerType)
Poker_Hand_cardsInHand: Property = Property(name="cardsInHand", type=StringType)
Poker_Hand_Fold: Property = Property(name="Fold", type=BooleanType)
Poker_Hand_handIterator: Property = Property(name="handIterator", type=Poker_HandIterator)
Poker_Hand.attributes={Poker_Hand_cardsInHand, Poker_Hand_numCards, Poker_Hand_Fold, Poker_Hand_handIterator}

# Cards_Card class attributes and methods
Cards_Card_rank: Property = Property(name="rank", type=IntegerType)
Cards_Card.attributes={Cards_Card_rank}

# Cards_Deck class attributes and methods
Cards_Deck_cardsInDeck: Property = Property(name="cardsInDeck", type=StringType)
Cards_Deck.attributes={Cards_Deck_cardsInDeck}

# Relationships
Hand_HandIterator: BinaryAssociation = BinaryAssociation(
    name="Hand_HandIterator",
    ends={
        Property(name="Hand_HandIterator_00", type=Poker_HandIterator, multiplicity=Multiplicity(1, 1)),
        Property(name="handIterator1", type=Poker_Hand, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_r2h1IBUQEeqDmNBP3mfLQg",
    types={Poker_PokerGame, Poker_Player, Poker_Human, Poker_Computer, Poker_Iterator_Interface, Poker_HandIterator, Poker_Hand, Cards_Card, Cards_Deck, Poker_PokerRank},
    associations={Hand_HandIterator},
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