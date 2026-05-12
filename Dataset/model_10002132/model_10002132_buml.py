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
Rank: Enumeration = Enumeration(
    name="Rank",
    literals={
            
    }
)

Suit: Enumeration = Enumeration(
    name="Suit",
    literals={
            
    }
)

# Classes
BlackJack = Class(name="BlackJack")
T = Class(name="T")
T2 = Class(name="T2")
Card = Class(name="Card")
Context = Class(name="Context")
Dealer = Class(name="Dealer")
Deck = Class(name="Deck")
Hand = Class(name="Hand")
Hit = Class(name="Hit")
Person_Interface = Class(name="Person_Interface")
Player = Class(name="Player")
Stay = Class(name="Stay")
Strategy_Interface = Class(name="Strategy_Interface")
genmymodelreverse_java_util_Scanner = Class(name="genmymodelreverse_java_util_Scanner")

# BlackJack class attributes and methods
BlackJack_scan: Property = Property(name="scan", type=genmymodelreverse_java_util_Scanner)
BlackJack.attributes={BlackJack_scan}

# T class attributes and methods

# T2 class attributes and methods

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=Suit)
Card_rank: Property = Property(name="rank", type=Rank)
Card.attributes={Card_suit, Card_rank}

# Context class attributes and methods

# Dealer class attributes and methods
Dealer_firstName: Property = Property(name="firstName", type=StringType)
Dealer.attributes={Dealer_firstName}

# Deck class attributes and methods

# Hand class attributes and methods
Hand_startHand: Property = Property(name="startHand", type=IntegerType)
Hand.attributes={Hand_startHand}

# Hit class attributes and methods

# Person_Interface class attributes and methods

# Player class attributes and methods
Player_firstName: Property = Property(name="firstName", type=StringType)
Player.attributes={Player_firstName}

# Stay class attributes and methods

# Strategy_Interface class attributes and methods

# genmymodelreverse_java_util_Scanner class attributes and methods

# Relationships
dHand_BlackJack_Hand_0: BinaryAssociation = BinaryAssociation(
    name="dHand_BlackJack_Hand_0",
    ends={
        Property(name="blackjack0", type=BlackJack, multiplicity=Multiplicity(0, 1)),
        Property(name="dHand1", type=Hand, multiplicity=Multiplicity(0, 1))
    }
)
d_BlackJack_Deck_1: BinaryAssociation = BinaryAssociation(
    name="d_BlackJack_Deck_1",
    ends={
        Property(name="blackjack6", type=BlackJack, multiplicity=Multiplicity(0, 1)),
        Property(name="d7", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
d_Dealer_Deck_7: BinaryAssociation = BinaryAssociation(
    name="d_Dealer_Deck_7",
    ends={
        Property(name="dealer8", type=Dealer, multiplicity=Multiplicity(0, 1)),
        Property(name="d9", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
h_Player_Hand_8: BinaryAssociation = BinaryAssociation(
    name="h_Player_Hand_8",
    ends={
        Property(name="player10", type=Player, multiplicity=Multiplicity(0, 1)),
        Property(name="h11", type=Hand, multiplicity=Multiplicity(0, 1))
    }
)
dealer_BlackJack_Dealer_5: BinaryAssociation = BinaryAssociation(
    name="dealer_BlackJack_Dealer_5",
    ends={
        Property(name="blackjack12", type=BlackJack, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer13", type=Dealer, multiplicity=Multiplicity(0, 1))
    }
)
d_Deck_Deck_11: BinaryAssociation = BinaryAssociation(
    name="d_Deck_Deck_11",
    ends={
        Property(name="deck14", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="d15", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
p_BlackJack_Player_4: BinaryAssociation = BinaryAssociation(
    name="p_BlackJack_Player_4",
    ends={
        Property(name="blackjack16", type=BlackJack, multiplicity=Multiplicity(0, 1)),
        Property(name="p17", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
hand_BlackJack_Hand_3: BinaryAssociation = BinaryAssociation(
    name="hand_BlackJack_Hand_3",
    ends={
        Property(name="blackjack2", type=BlackJack, multiplicity=Multiplicity(0, 1)),
        Property(name="hand3", type=Hand, multiplicity=Multiplicity(0, 1))
    }
)
hand_Hand_Card_10: BinaryAssociation = BinaryAssociation(
    name="hand_Hand_Card_10",
    ends={
        Property(name="hand4", type=Hand, multiplicity=Multiplicity(0, 1)),
        Property(name="hand5", type=Card, multiplicity=Multiplicity(0, 9999))
    }
)
strat_Context_Strategy_6: BinaryAssociation = BinaryAssociation(
    name="strat_Context_Strategy_6",
    ends={
        Property(name="context18", type=Context, multiplicity=Multiplicity(0, 1)),
        Property(name="strat19", type=Strategy_Interface, multiplicity=Multiplicity(0, 1))
    }
)
deck_Deck_Card_2: BinaryAssociation = BinaryAssociation(
    name="deck_Deck_Card_2",
    ends={
        Property(name="deck20", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="deck21", type=Card, multiplicity=Multiplicity(0, 9999))
    }
)
hand_Dealer_Hand_9: BinaryAssociation = BinaryAssociation(
    name="hand_Dealer_Hand_9",
    ends={
        Property(name="dealer22", type=Dealer, multiplicity=Multiplicity(0, 1)),
        Property(name="hand23", type=Hand, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_qcmb0NrZEeeQi8PFukjNiw",
    types={BlackJack, T, T2, Card, Context, Dealer, Deck, Hand, Hit, Person_Interface, Player, Stay, Strategy_Interface, genmymodelreverse_java_util_Scanner, Rank, Suit},
    associations={dHand_BlackJack_Hand_0, d_BlackJack_Deck_1, d_Dealer_Deck_7, h_Player_Hand_8, dealer_BlackJack_Dealer_5, d_Deck_Deck_11, p_BlackJack_Player_4, hand_BlackJack_Hand_3, hand_Hand_Card_10, strat_Context_Strategy_6, deck_Deck_Card_2, hand_Dealer_Hand_9},
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