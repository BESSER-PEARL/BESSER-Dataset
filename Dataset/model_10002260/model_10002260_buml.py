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
List_Card_: Enumeration = Enumeration(
    name="List_Card_",
    literals={
            
    }
)

List_User_S_: Enumeration = Enumeration(
    name="List_User_S_",
    literals={
            
    }
)

# Classes
dutycalls_view_About = Class(name="dutycalls_view_About")
dutycalls_view_Home = Class(name="dutycalls_view_Home")
dutycalls_view_Instructions = Class(name="dutycalls_view_Instructions")
dutycalls_view_JoinGame = Class(name="dutycalls_view_JoinGame")
dutycalls_view_PokerTable = Class(name="dutycalls_view_PokerTable")
dutycalls_view_WaitingForPlayer = Class(name="dutycalls_view_WaitingForPlayer")
dutycalls_view_User = Class(name="dutycalls_view_User")
dutycalls_model_AIUser = Class(name="dutycalls_model_AIUser")
dutycalls_model_Dealer_SINGLEPLAYER = Class(name="dutycalls_model_Dealer_SINGLEPLAYER")
dutycalls_model_BestHand = Class(name="dutycalls_model_BestHand")
dutycalls_model_Deck = Class(name="dutycalls_model_Deck")
dutycalls_model_Card = Class(name="dutycalls_model_Card")
dutycalls_model_PlayerHand = Class(name="dutycalls_model_PlayerHand")
dutycalls_model_PokerHand = Class(name="dutycalls_model_PokerHand")
dutycalls_model_GameType = Class(name="dutycalls_model_GameType")
dutycalls_model_WildHand = Class(name="dutycalls_model_WildHand")
dutycalls_model_Suit = Class(name="dutycalls_model_Suit")
dutycalls_model_Value = Class(name="dutycalls_model_Value")
dutycalls_model_User_S = Class(name="dutycalls_model_User_S")
dutycalls_contoller_Dealer_Control = Class(name="dutycalls_contoller_Dealer_Control")
dutycalls_contoller_HomeControl = Class(name="dutycalls_contoller_HomeControl")

# dutycalls_view_About class attributes and methods

# dutycalls_view_Home class attributes and methods

# dutycalls_view_Instructions class attributes and methods

# dutycalls_view_JoinGame class attributes and methods

# dutycalls_view_PokerTable class attributes and methods

# dutycalls_view_WaitingForPlayer class attributes and methods

# dutycalls_view_User class attributes and methods

# dutycalls_model_AIUser class attributes and methods

# dutycalls_model_Dealer_SINGLEPLAYER class attributes and methods
dutycalls_model_Dealer_SINGLEPLAYER_allIn: Property = Property(name="allIn", type=BooleanType)
dutycalls_model_Dealer_SINGLEPLAYER_bet: Property = Property(name="bet", type=IntegerType)
dutycalls_model_Dealer_SINGLEPLAYER_deck: Property = Property(name="deck", type=dutycalls_model_Deck)
dutycalls_model_Dealer_SINGLEPLAYER_main_userList: Property = Property(name="main_userList", type=List_User_S_)
dutycalls_model_Dealer_SINGLEPLAYER_openBet: Property = Property(name="openBet", type=IntegerType)
dutycalls_model_Dealer_SINGLEPLAYER_tableValue: Property = Property(name="tableValue", type=IntegerType)
dutycalls_model_Dealer_SINGLEPLAYER_userList: Property = Property(name="userList", type=List_User_S_)
dutycalls_model_Dealer_SINGLEPLAYER.attributes={dutycalls_model_Dealer_SINGLEPLAYER_allIn, dutycalls_model_Dealer_SINGLEPLAYER_openBet, dutycalls_model_Dealer_SINGLEPLAYER_bet, dutycalls_model_Dealer_SINGLEPLAYER_tableValue, dutycalls_model_Dealer_SINGLEPLAYER_deck, dutycalls_model_Dealer_SINGLEPLAYER_userList, dutycalls_model_Dealer_SINGLEPLAYER_main_userList}

# dutycalls_model_BestHand class attributes and methods
dutycalls_model_BestHand_handValue: Property = Property(name="handValue", type=IntegerType)
dutycalls_model_BestHand.attributes={dutycalls_model_BestHand_handValue}

# dutycalls_model_Deck class attributes and methods

# dutycalls_model_Card class attributes and methods

# dutycalls_model_PlayerHand class attributes and methods

# dutycalls_model_PokerHand class attributes and methods

# dutycalls_model_GameType class attributes and methods

# dutycalls_model_WildHand class attributes and methods

# dutycalls_model_Suit class attributes and methods

# dutycalls_model_Value class attributes and methods

# dutycalls_model_User_S class attributes and methods
dutycalls_model_User_S_id: Property = Property(name="id", type=IntegerType)
dutycalls_model_User_S.attributes={dutycalls_model_User_S_id}

# dutycalls_contoller_Dealer_Control class attributes and methods
dutycalls_contoller_Dealer_Control_cardCount: Property = Property(name="cardCount", type=IntegerType)
dutycalls_contoller_Dealer_Control_userid: Property = Property(name="userid", type=IntegerType)
dutycalls_contoller_Dealer_Control.attributes={dutycalls_contoller_Dealer_Control_cardCount, dutycalls_contoller_Dealer_Control_userid}

# dutycalls_contoller_HomeControl class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="a04b98cd_ee7d_47e9_8ddc_91167a90f31f",
    types={dutycalls_view_About, dutycalls_view_Home, dutycalls_view_Instructions, dutycalls_view_JoinGame, dutycalls_view_PokerTable, dutycalls_view_WaitingForPlayer, dutycalls_view_User, dutycalls_model_AIUser, dutycalls_model_Dealer_SINGLEPLAYER, dutycalls_model_BestHand, dutycalls_model_Deck, dutycalls_model_Card, dutycalls_model_PlayerHand, dutycalls_model_PokerHand, dutycalls_model_GameType, dutycalls_model_WildHand, dutycalls_model_Suit, dutycalls_model_Value, dutycalls_model_User_S, dutycalls_contoller_Dealer_Control, dutycalls_contoller_HomeControl, List_Card_, List_User_S_},
    associations={},
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