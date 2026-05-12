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
Cards_Cardinality: Enumeration = Enumeration(
    name="Cards_Cardinality",
    literals={
            
    }
)

# Classes
Cards_CardImpl = Class(name="Cards_CardImpl")
Cards_Card_Interface = Class(name="Cards_Card_Interface")
Cards_Deck = Class(name="Cards_Deck")
Game_GUI = Class(name="Game_GUI")
Game_Ranker = Class(name="Game_Ranker")
Players_Player = Class(name="Players_Player")
Players_PokerHand = Class(name="Players_PokerHand")
Players_Person = Class(name="Players_Person")
Players_Wallet = Class(name="Players_Wallet")
Main_MainGame = Class(name="Main_MainGame")
Card___Interface = Class(name="Card___Interface")

# Cards_CardImpl class attributes and methods
Cards_CardImpl_Suit: Property = Property(name="Suit", type=StringType)
Cards_CardImpl_Cardinality: Property = Property(name="Cardinality", type=Cards_Cardinality)
Cards_CardImpl_isMarked: Property = Property(name="isMarked", type=BooleanType)
Cards_CardImpl.attributes={Cards_CardImpl_Cardinality, Cards_CardImpl_isMarked, Cards_CardImpl_Suit}

# Cards_Card_Interface class attributes and methods

# Cards_Deck class attributes and methods
Cards_Deck_list: Property = Property(name="list", type=StringType)
Cards_Deck_burnt: Property = Property(name="burnt", type=Cards_Card_Interface)
Cards_Deck.attributes={Cards_Deck_list, Cards_Deck_burnt}

# Game_GUI class attributes and methods

# Game_Ranker class attributes and methods
Game_Ranker_hand: Property = Property(name="hand", type=Players_PokerHand)
Game_Ranker.attributes={Game_Ranker_hand}

# Players_Player class attributes and methods
Players_Player_isSmallBlind: Property = Property(name="isSmallBlind", type=BooleanType)
Players_Player_isBigBlind: Property = Property(name="isBigBlind", type=BooleanType)
Players_Player_isDealer: Property = Property(name="isDealer", type=BooleanType)
Players_Player_Hand: Property = Property(name="Hand", type=Players_PokerHand)
Players_Player_hasFolded: Property = Property(name="hasFolded", type=BooleanType)
Players_Player_chips: Property = Property(name="chips", type=Players_Wallet)
Players_Player.attributes={Players_Player_isBigBlind, Players_Player_hasFolded, Players_Player_chips, Players_Player_isSmallBlind, Players_Player_isDealer, Players_Player_Hand}

# Players_PokerHand class attributes and methods
Players_PokerHand_highCard: Property = Property(name="highCard", type=Cards_Cardinality)
Players_PokerHand_value: Property = Property(name="value", type=IntegerType)
Players_PokerHand_Cards: Property = Property(name="Cards", type=Card___Interface)
Players_PokerHand.attributes={Players_PokerHand_Cards, Players_PokerHand_value, Players_PokerHand_highCard}

# Players_Person class attributes and methods
Players_Person_name: Property = Property(name="name", type=StringType)
Players_Person_personNumber: Property = Property(name="personNumber", type=StringType)
Players_Person.attributes={Players_Person_personNumber, Players_Person_name}

# Players_Wallet class attributes and methods
Players_Wallet_balance: Property = Property(name="balance", type=IntegerType)
Players_Wallet.attributes={Players_Wallet_balance}

# Main_MainGame class attributes and methods
Main_MainGame_Players: Property = Property(name="Players", type=StringType)
Main_MainGame_screen: Property = Property(name="screen", type=Game_GUI)
Main_MainGame_SmallBlind: Property = Property(name="SmallBlind", type=IntegerType)
Main_MainGame_Bigblind: Property = Property(name="Bigblind", type=IntegerType)
Main_MainGame_Dealer: Property = Property(name="Dealer", type=IntegerType)
Main_MainGame_HighestBid: Property = Property(name="HighestBid", type=IntegerType)
Main_MainGame.attributes={Main_MainGame_SmallBlind, Main_MainGame_Bigblind, Main_MainGame_HighestBid, Main_MainGame_screen, Main_MainGame_Players, Main_MainGame_Dealer}

# Card___Interface class attributes and methods

# Relationships
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card0", type=Cards_Card_Interface, multiplicity=Multiplicity(52, 52)),
        Property(name="deck1", type=Cards_Deck, multiplicity=Multiplicity(1, 1))
    }
)
GUI_Main_Game: BinaryAssociation = BinaryAssociation(
    name="GUI_Main_Game",
    ends={
        Property(name="Owner2", type=Main_MainGame, multiplicity=Multiplicity(0, 1)),
        Property(name="gUI3", type=Game_GUI, multiplicity=Multiplicity(0, 1))
    }
)
Player_Deck: BinaryAssociation = BinaryAssociation(
    name="Player_Deck",
    ends={
        Property(name="deck4", type=Cards_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="player5", type=Players_Player, multiplicity=Multiplicity(0, 1))
    }
)
PokerHand_Card: BinaryAssociation = BinaryAssociation(
    name="PokerHand_Card",
    ends={
        Property(name="card6", type=Cards_Card_Interface, multiplicity=Multiplicity(0, 5)),
        Property(name="pokerHand7", type=Players_PokerHand, multiplicity=Multiplicity(0, 1))
    }
)
Player_PokerHand: BinaryAssociation = BinaryAssociation(
    name="Player_PokerHand",
    ends={
        Property(name="pokerHand8", type=Players_PokerHand, multiplicity=Multiplicity(0, 1)),
        Property(name="Holder9", type=Players_Player, multiplicity=Multiplicity(0, 1))
    }
)
Wallet_Player: BinaryAssociation = BinaryAssociation(
    name="Wallet_Player",
    ends={
        Property(name="player10", type=Players_Player, multiplicity=Multiplicity(0, 1)),
        Property(name="owner11", type=Players_Wallet, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_mXzfEC_dEeqqcaoAsxFIeg",
    types={Cards_CardImpl, Cards_Card_Interface, Cards_Deck, Game_GUI, Game_Ranker, Players_Player, Players_PokerHand, Players_Person, Players_Wallet, Main_MainGame, Card___Interface, Cards_Cardinality},
    associations={Deck_Card, GUI_Main_Game, Player_Deck, PokerHand_Card, Player_PokerHand, Wallet_Player},
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