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
_Interface = Class(name="_Interface")
Deck = Class(name="Deck")
Cards = Class(name="Cards")
Dealer = Class(name="Dealer")
Hand = Class(name="Hand")
Player = Class(name="Player")
BlackjackGame = Class(name="BlackjackGame")
Integer_external = Class(name="Integer_external")

# _Interface class attributes and methods

# Deck class attributes and methods
Deck_size: Property = Property(name="size", type=IntegerType)
Deck_deckArray: Property = Property(name="deckArray", type=IntegerType)
Deck.attributes={Deck_deckArray, Deck_size}

# Cards class attributes and methods
Cards_cardName: Property = Property(name="cardName", type=StringType)
Cards_cardValue: Property = Property(name="cardValue", type=IntegerType)
Cards.attributes={Cards_cardName, Cards_cardValue}

# Dealer class attributes and methods
Dealer_handValue: Property = Property(name="handValue", type=IntegerType)
Dealer_handLimit: Property = Property(name="handLimit", type=IntegerType)
Dealer.attributes={Dealer_handValue, Dealer_handLimit}

# Hand class attributes and methods
Hand_handValue: Property = Property(name="handValue", type=IntegerType)
Hand.attributes={Hand_handValue}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player.attributes={Player_name}

# BlackjackGame class attributes and methods

# Integer_external class attributes and methods

# Relationships
Hand_Dealer: BinaryAssociation = BinaryAssociation(
    name="Hand_Dealer",
    ends={
        Property(name="dealer0", type=Dealer, multiplicity=Multiplicity(0, 1)),
        Property(name="hand1", type=Integer_external, multiplicity=Multiplicity(0, 1))
    }
)
BlackjackGame_Player: BinaryAssociation = BinaryAssociation(
    name="BlackjackGame_Player",
    ends={
        Property(name="player2", type=Player, multiplicity=Multiplicity(0, 1)),
        Property(name="blackjackGame3", type=BlackjackGame, multiplicity=Multiplicity(0, 1))
    }
)
BlackjackGame_Dealer: BinaryAssociation = BinaryAssociation(
    name="BlackjackGame_Dealer",
    ends={
        Property(name="dealer4", type=Dealer, multiplicity=Multiplicity(0, 1)),
        Property(name="blackjackGame5", type=BlackjackGame, multiplicity=Multiplicity(0, 1))
    }
)
Player_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Hand",
    ends={
        Property(name="hand6", type=Hand, multiplicity=Multiplicity(0, 1)),
        Property(name="player7", type=Player, multiplicity=Multiplicity(0, 9999))
    }
)
association: BinaryAssociation = BinaryAssociation(
    name="association",
    ends={
        Property(name="blackjackGame8", type=BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="association_19", type=_Interface, multiplicity=Multiplicity(0, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="deck10", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="association2_111", type=_Interface, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_EuTy4A4QEeiiG6cC1txh3Q",
    types={_Interface, Deck, Cards, Dealer, Hand, Player, BlackjackGame, Integer_external},
    associations={Hand_Dealer, BlackjackGame_Player, BlackjackGame_Dealer, Player_Hand, association, association2},
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