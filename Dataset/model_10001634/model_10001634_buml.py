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
common_Ranks: Enumeration = Enumeration(
    name="common_Ranks",
    literals={
            
    }
)

common_States: Enumeration = Enumeration(
    name="common_States",
    literals={
            
    }
)

table_Suit: Enumeration = Enumeration(
    name="table_Suit",
    literals={
            
    }
)

table_Rank: Enumeration = Enumeration(
    name="table_Rank",
    literals={
            
    }
)

table_UpcomingCards: Enumeration = Enumeration(
    name="table_UpcomingCards",
    literals={
            
    }
)

# Classes
calculations_PokerRules = Class(name="calculations_PokerRules")
common_Hand = Class(name="common_Hand")
common_Observer_Interface = Class(name="common_Observer_Interface")
common_Subject_Interface = Class(name="common_Subject_Interface")
managers_GameManager = Class(name="managers_GameManager")
managers_LoginManager = Class(name="managers_LoginManager")
player_Player = Class(name="player_Player")
player_Players = Class(name="player_Players")
server_MultiServer = Class(name="server_MultiServer")
table_Card = Class(name="table_Card")
table_Deck = Class(name="table_Deck")
table_Table = Class(name="table_Table")
genmymodelreverse_java_io_BufferedReader = Class(name="genmymodelreverse_java_io_BufferedReader")
genmymodelreverse_java_io_PrintWriter = Class(name="genmymodelreverse_java_io_PrintWriter")
genmymodelreverse_java_io_IOException = Class(name="genmymodelreverse_java_io_IOException")

# calculations_PokerRules class attributes and methods
calculations_PokerRules_tableCardRank: Property = Property(name="tableCardRank", type=common_Ranks)
calculations_PokerRules_numberOfPlayers: Property = Property(name="numberOfPlayers", type=IntegerType)
calculations_PokerRules_cardsOnTable: Property = Property(name="cardsOnTable", type=StringType)
calculations_PokerRules_arrayWithHands: Property = Property(name="arrayWithHands", type=StringType)
calculations_PokerRules_highestCardStraight: Property = Property(name="highestCardStraight", type=StringType)
calculations_PokerRules.attributes={calculations_PokerRules_highestCardStraight, calculations_PokerRules_numberOfPlayers, calculations_PokerRules_tableCardRank, calculations_PokerRules_cardsOnTable, calculations_PokerRules_arrayWithHands}

# common_Hand class attributes and methods
common_Hand_rank: Property = Property(name="rank", type=common_Ranks)
common_Hand.attributes={common_Hand_rank}

# common_Observer_Interface class attributes and methods

# common_Subject_Interface class attributes and methods

# managers_GameManager class attributes and methods
managers_GameManager_newRound: Property = Property(name="newRound", type=BooleanType)
managers_GameManager_smallblind: Property = Property(name="smallblind", type=FloatType)
managers_GameManager_raise: Property = Property(name="raise", type=FloatType)
managers_GameManager_dealer: Property = Property(name="dealer", type=IntegerType)
managers_GameManager_playerTurn: Property = Property(name="playerTurn", type=IntegerType)
managers_GameManager_initialBigID: Property = Property(name="initialBigID", type=IntegerType)
managers_GameManager_initialSmallID: Property = Property(name="initialSmallID", type=IntegerType)
managers_GameManager_playerIDs: Property = Property(name="playerIDs", type=StringType)
managers_GameManager_stateOfPlayersArr: Property = Property(name="stateOfPlayersArr", type=StringType)
managers_GameManager_playerNames: Property = Property(name="playerNames", type=StringType)
managers_GameManager_playerHands: Property = Property(name="playerHands", type=StringType)
managers_GameManager_playerBets: Property = Property(name="playerBets", type=StringType)
managers_GameManager_tableCards: Property = Property(name="tableCards", type=StringType)
managers_GameManager_minimumState: Property = Property(name="minimumState", type=common_States)
managers_GameManager_playersLeftInTheGame: Property = Property(name="playersLeftInTheGame", type=IntegerType)
managers_GameManager.attributes={managers_GameManager_minimumState, managers_GameManager_smallblind, managers_GameManager_playerTurn, managers_GameManager_playerNames, managers_GameManager_playerBets, managers_GameManager_newRound, managers_GameManager_playerIDs, managers_GameManager_stateOfPlayersArr, managers_GameManager_tableCards, managers_GameManager_playerHands, managers_GameManager_initialBigID, managers_GameManager_raise, managers_GameManager_playersLeftInTheGame, managers_GameManager_initialSmallID, managers_GameManager_dealer}

# managers_LoginManager class attributes and methods
managers_LoginManager_inputLine: Property = Property(name="inputLine", type=StringType)
managers_LoginManager_out: Property = Property(name="out", type=genmymodelreverse_java_io_PrintWriter)
managers_LoginManager_in: Property = Property(name="in", type=genmymodelreverse_java_io_BufferedReader)
managers_LoginManager.attributes={managers_LoginManager_out, managers_LoginManager_inputLine, managers_LoginManager_in}

# player_Player class attributes and methods
player_Player_name: Property = Property(name="name", type=StringType)
player_Player_wealth: Property = Property(name="wealth", type=FloatType)
player_Player_bigB: Property = Property(name="bigB", type=FloatType)
player_Player_state: Property = Property(name="state", type=common_States)
player_Player_dealer: Property = Property(name="dealer", type=BooleanType)
player_Player_observerIDTracker: Property = Property(name="observerIDTracker", type=IntegerType)
player_Player_observerID: Property = Property(name="observerID", type=IntegerType)
player_Player.attributes={player_Player_name, player_Player_state, player_Player_observerIDTracker, player_Player_dealer, player_Player_bigB, player_Player_observerID, player_Player_wealth}

# player_Players class attributes and methods
player_Players_goodToGo: Property = Property(name="goodToGo", type=BooleanType)
player_Players_MaxAmountOfPlayers: Property = Property(name="MaxAmountOfPlayers", type=IntegerType)
player_Players_wealth: Property = Property(name="wealth", type=FloatType)
player_Players_AmountOfPlayers: Property = Property(name="AmountOfPlayers", type=IntegerType)
player_Players.attributes={player_Players_goodToGo, player_Players_AmountOfPlayers, player_Players_wealth, player_Players_MaxAmountOfPlayers}

# server_MultiServer class attributes and methods

# table_Card class attributes and methods
table_Card_suit: Property = Property(name="suit", type=table_Suit)
table_Card_rank: Property = Property(name="rank", type=table_Rank)
table_Card.attributes={table_Card_rank, table_Card_suit}

# table_Deck class attributes and methods
table_Deck_suit: Property = Property(name="suit", type=table_Suit)
table_Deck_rank: Property = Property(name="rank", type=table_Rank)
table_Deck_numCardsInDeck: Property = Property(name="numCardsInDeck", type=IntegerType)
table_Deck_randomNumbers: Property = Property(name="randomNumbers", type=IntegerType)
table_Deck.attributes={table_Deck_randomNumbers, table_Deck_numCardsInDeck, table_Deck_rank, table_Deck_suit}

# table_Table class attributes and methods
table_Table_upcomingCards: Property = Property(name="upcomingCards", type=table_UpcomingCards)
table_Table_turnedCards: Property = Property(name="turnedCards", type=StringType)
table_Table_amountOfCards: Property = Property(name="amountOfCards", type=IntegerType)
table_Table.attributes={table_Table_turnedCards, table_Table_amountOfCards, table_Table_upcomingCards}

# genmymodelreverse_java_io_BufferedReader class attributes and methods

# genmymodelreverse_java_io_PrintWriter class attributes and methods

# genmymodelreverse_java_io_IOException class attributes and methods

# Relationships
deck_Table_Deck_10: BinaryAssociation = BinaryAssociation(
    name="deck_Table_Deck_10",
    ends={
        Property(name="table0", type=table_Table, multiplicity=Multiplicity(0, 1)),
        Property(name="deck1", type=table_Deck, multiplicity=Multiplicity(0, 1))
    }
)
pokerRules_GameManager_PokerRules_14: BinaryAssociation = BinaryAssociation(
    name="pokerRules_GameManager_PokerRules_14",
    ends={
        Property(name="gamemanager2", type=managers_GameManager, multiplicity=Multiplicity(0, 1)),
        Property(name="pokerRules3", type=calculations_PokerRules, multiplicity=Multiplicity(0, 1))
    }
)
cardBelow_Deck_Card_12: BinaryAssociation = BinaryAssociation(
    name="cardBelow_Deck_Card_12",
    ends={
        Property(name="deck10", type=table_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="cardBelow11", type=table_Card, multiplicity=Multiplicity(0, 1))
    }
)
card1_Hand_Card_7: BinaryAssociation = BinaryAssociation(
    name="card1_Hand_Card_7",
    ends={
        Property(name="hand4", type=common_Hand, multiplicity=Multiplicity(0, 1)),
        Property(name="card15", type=table_Card, multiplicity=Multiplicity(0, 1))
    }
)
hand_Player_Hand_0: BinaryAssociation = BinaryAssociation(
    name="hand_Player_Hand_0",
    ends={
        Property(name="player6", type=player_Player, multiplicity=Multiplicity(0, 1)),
        Property(name="hand7", type=common_Hand, multiplicity=Multiplicity(0, 1))
    }
)
players_Table_Players_1: BinaryAssociation = BinaryAssociation(
    name="players_Table_Players_1",
    ends={
        Property(name="table8", type=table_Table, multiplicity=Multiplicity(0, 1)),
        Property(name="players9", type=player_Players, multiplicity=Multiplicity(0, 1))
    }
)
card2_Hand_Card_17: BinaryAssociation = BinaryAssociation(
    name="card2_Hand_Card_17",
    ends={
        Property(name="hand12", type=common_Hand, multiplicity=Multiplicity(0, 1)),
        Property(name="card213", type=table_Card, multiplicity=Multiplicity(0, 1))
    }
)
gameManager_Player_GameManager_13: BinaryAssociation = BinaryAssociation(
    name="gameManager_Player_GameManager_13",
    ends={
        Property(name="player14", type=player_Player, multiplicity=Multiplicity(0, 1)),
        Property(name="gameManager15", type=managers_GameManager, multiplicity=Multiplicity(0, 1))
    }
)
players_LoginManager_Players_8: BinaryAssociation = BinaryAssociation(
    name="players_LoginManager_Players_8",
    ends={
        Property(name="loginmanager16", type=managers_LoginManager, multiplicity=Multiplicity(0, 1)),
        Property(name="players17", type=player_Players, multiplicity=Multiplicity(0, 1))
    }
)
player_LoginManager_Player_11: BinaryAssociation = BinaryAssociation(
    name="player_LoginManager_Player_11",
    ends={
        Property(name="loginmanager18", type=managers_LoginManager, multiplicity=Multiplicity(0, 1)),
        Property(name="player19", type=player_Player, multiplicity=Multiplicity(0, 1))
    }
)
players_GameManager_Observer_5: BinaryAssociation = BinaryAssociation(
    name="players_GameManager_Observer_5",
    ends={
        Property(name="gamemanager20", type=managers_GameManager, multiplicity=Multiplicity(0, 1)),
        Property(name="players21", type=common_Observer_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
gameManager_Players_GameManager_9: BinaryAssociation = BinaryAssociation(
    name="gameManager_Players_GameManager_9",
    ends={
        Property(name="players22", type=player_Players, multiplicity=Multiplicity(0, 1)),
        Property(name="gameManager23", type=managers_GameManager, multiplicity=Multiplicity(0, 1))
    }
)
topCard_Deck_Card_2: BinaryAssociation = BinaryAssociation(
    name="topCard_Deck_Card_2",
    ends={
        Property(name="deck24", type=table_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="topCard25", type=table_Card, multiplicity=Multiplicity(0, 1))
    }
)
table_GameManager_Table_4: BinaryAssociation = BinaryAssociation(
    name="table_GameManager_Table_4",
    ends={
        Property(name="gamemanager26", type=managers_GameManager, multiplicity=Multiplicity(0, 1)),
        Property(name="table27", type=table_Table, multiplicity=Multiplicity(0, 1))
    }
)
reference_Card_Card_15: BinaryAssociation = BinaryAssociation(
    name="reference_Card_Card_15",
    ends={
        Property(name="card28", type=table_Card, multiplicity=Multiplicity(0, 1)),
        Property(name="reference29", type=table_Card, multiplicity=Multiplicity(0, 1))
    }
)
burnedCard_Table_Card_16: BinaryAssociation = BinaryAssociation(
    name="burnedCard_Table_Card_16",
    ends={
        Property(name="table30", type=table_Table, multiplicity=Multiplicity(0, 1)),
        Property(name="burnedCard31", type=table_Card, multiplicity=Multiplicity(0, 1))
    }
)
playersObj_GameManager_Players_3: BinaryAssociation = BinaryAssociation(
    name="playersObj_GameManager_Players_3",
    ends={
        Property(name="gamemanager32", type=managers_GameManager, multiplicity=Multiplicity(0, 1)),
        Property(name="playersObj33", type=player_Players, multiplicity=Multiplicity(0, 1))
    }
)
players_Players_Observer_6: BinaryAssociation = BinaryAssociation(
    name="players_Players_Observer_6",
    ends={
        Property(name="players34", type=player_Players, multiplicity=Multiplicity(0, 1)),
        Property(name="players35", type=common_Observer_Interface, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Kylh0C_MEeme_prEJQaJbA",
    types={calculations_PokerRules, common_Hand, common_Observer_Interface, common_Subject_Interface, managers_GameManager, managers_LoginManager, player_Player, player_Players, server_MultiServer, table_Card, table_Deck, table_Table, genmymodelreverse_java_io_BufferedReader, genmymodelreverse_java_io_PrintWriter, genmymodelreverse_java_io_IOException, common_Ranks, common_States, table_Suit, table_Rank, table_UpcomingCards},
    associations={deck_Table_Deck_10, pokerRules_GameManager_PokerRules_14, cardBelow_Deck_Card_12, card1_Hand_Card_7, hand_Player_Hand_0, players_Table_Players_1, card2_Hand_Card_17, gameManager_Player_GameManager_13, players_LoginManager_Players_8, player_LoginManager_Player_11, players_GameManager_Observer_5, gameManager_Players_GameManager_9, topCard_Deck_Card_2, table_GameManager_Table_4, reference_Card_Card_15, burnedCard_Table_Card_16, playersObj_GameManager_Players_3, players_Players_Observer_6},
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