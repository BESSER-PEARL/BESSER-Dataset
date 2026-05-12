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
Cards_Card = Class(name="Cards_Card")
Players_Player = Class(name="Players_Player")
MainGame_Main = Class(name="MainGame_Main")
MainGame_Deck = Class(name="MainGame_Deck")
MainGame_GUI = Class(name="MainGame_GUI")
MainGame_Hand = Class(name="MainGame_Hand")

# Cards_Card class attributes and methods
Cards_Card_suit: Property = Property(name="suit", type=StringType)
Cards_Card_value: Property = Property(name="value", type=IntegerType)
Cards_Card.attributes={Cards_Card_value, Cards_Card_suit}

# Players_Player class attributes and methods
Players_Player_name: Property = Property(name="name", type=StringType)
Players_Player_bet: Property = Property(name="bet", type=IntegerType)
Players_Player_hand: Property = Property(name="hand", type=MainGame_Hand)
Players_Player.attributes={Players_Player_name, Players_Player_bet, Players_Player_hand}

# MainGame_Main class attributes and methods
MainGame_Main_dealNumber: Property = Property(name="dealNumber", type=IntegerType)
MainGame_Main_deck: Property = Property(name="deck", type=MainGame_Deck)
MainGame_Main.attributes={MainGame_Main_dealNumber, MainGame_Main_deck}

# MainGame_Deck class attributes and methods
MainGame_Deck_Cards: Property = Property(name="Cards", type=StringType)
MainGame_Deck.attributes={MainGame_Deck_Cards}

# MainGame_GUI class attributes and methods

# MainGame_Hand class attributes and methods
MainGame_Hand_Hand: Property = Property(name="Hand", type=StringType)
MainGame_Hand_straightFlush: Property = Property(name="straightFlush", type=BooleanType)
MainGame_Hand_fourKind: Property = Property(name="fourKind", type=BooleanType)
MainGame_Hand_fullHouse: Property = Property(name="fullHouse", type=BooleanType)
MainGame_Hand_flush: Property = Property(name="flush", type=BooleanType)
MainGame_Hand_straight: Property = Property(name="straight", type=BooleanType)
MainGame_Hand_threeKing: Property = Property(name="threeKing", type=BooleanType)
MainGame_Hand_twoPair: Property = Property(name="twoPair", type=BooleanType)
MainGame_Hand_onePair: Property = Property(name="onePair", type=BooleanType)
MainGame_Hand_highCard: Property = Property(name="highCard", type=BooleanType)
MainGame_Hand.attributes={MainGame_Hand_onePair, MainGame_Hand_twoPair, MainGame_Hand_flush, MainGame_Hand_fullHouse, MainGame_Hand_fourKind, MainGame_Hand_straightFlush, MainGame_Hand_straight, MainGame_Hand_highCard, MainGame_Hand_Hand, MainGame_Hand_threeKing}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="deck0", type=MainGame_Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="card1", type=Cards_Card, multiplicity=Multiplicity(0, 52))
    }
)
deals_manages: BinaryAssociation = BinaryAssociation(
    name="deals_manages",
    ends={
        Property(name="main2", type=MainGame_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="deck3", type=MainGame_Deck, multiplicity=Multiplicity(1, 1))
    }
)
composed_of: BinaryAssociation = BinaryAssociation(
    name="composed_of",
    ends={
        Property(name="card4", type=Cards_Card, multiplicity=Multiplicity(0, 5)),
        Property(name="hand5", type=MainGame_Hand, multiplicity=Multiplicity(1, 1))
    }
)
plays: BinaryAssociation = BinaryAssociation(
    name="plays",
    ends={
        Property(name="player6", type=Players_Player, multiplicity=Multiplicity(1, 1)),
        Property(name="hand7", type=MainGame_Hand, multiplicity=Multiplicity(1, 1))
    }
)
displays_GUI: BinaryAssociation = BinaryAssociation(
    name="displays_GUI",
    ends={
        Property(name="main8", type=MainGame_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="gUI9", type=MainGame_GUI, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_p_lBYAe3Eeipbtix_oa2Dg",
    types={Cards_Card, Players_Player, MainGame_Main, MainGame_Deck, MainGame_GUI, MainGame_Hand},
    associations={contains, deals_manages, composed_of, plays, displays_GUI},
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