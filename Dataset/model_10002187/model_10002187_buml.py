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
War_Suit: Enumeration = Enumeration(
    name="War_Suit",
    literals={
            
    }
)

War_Rank: Enumeration = Enumeration(
    name="War_Rank",
    literals={
            
    }
)

War_Suit1: Enumeration = Enumeration(
    name="War_Suit1",
    literals={
            
    }
)

War_Rank1: Enumeration = Enumeration(
    name="War_Rank1",
    literals={
            
    }
)

# Classes
War_Card = Class(name="War_Card")
War_ClassicTwoPlayer = Class(name="War_ClassicTwoPlayer")
War_Deck = Class(name="War_Deck")
War_DeckIterator = Class(name="War_DeckIterator")
War_GameLogger = Class(name="War_GameLogger")
War_PlayGame = Class(name="War_PlayGame")
War_Player = Class(name="War_Player")
War_ThreePlayerPointPile = Class(name="War_ThreePlayerPointPile")
War_TwoPlayerPointPile = Class(name="War_TwoPlayerPointPile")
War_Card1 = Class(name="War_Card1")
War_ClassicTwoPlayer1 = Class(name="War_ClassicTwoPlayer1")
War_Deck1 = Class(name="War_Deck1")
War_DeckIterator1 = Class(name="War_DeckIterator1")
War_GameLogger1 = Class(name="War_GameLogger1")
War_PlayGame1 = Class(name="War_PlayGame1")
War_Player1 = Class(name="War_Player1")
War_ThreePlayerPointPile1 = Class(name="War_ThreePlayerPointPile1")
War_TwoPlayerPointPile1 = Class(name="War_TwoPlayerPointPile1")
War_WarGameVariation = Class(name="War_WarGameVariation", is_abstract=True)
War_WarVariationClassic = Class(name="War_WarVariationClassic")
War_WarVariationWithPoints = Class(name="War_WarVariationWithPoints")
War_WarGameVariation1 = Class(name="War_WarGameVariation1", is_abstract=True)
War_WarVariationClassic1 = Class(name="War_WarVariationClassic1")
War_WarVariationWithPoints1 = Class(name="War_WarVariationWithPoints1")
Comparable_Card__Interface = Class(name="Comparable_Card__Interface")
Iterable_Card__Interface = Class(name="Iterable_Card__Interface")
Iterator_Card__Interface = Class(name="Iterator_Card__Interface")

# War_Card class attributes and methods

# War_ClassicTwoPlayer class attributes and methods

# War_Deck class attributes and methods

# War_DeckIterator class attributes and methods

# War_GameLogger class attributes and methods

# War_PlayGame class attributes and methods

# War_Player class attributes and methods

# War_ThreePlayerPointPile class attributes and methods

# War_TwoPlayerPointPile class attributes and methods

# War_Card1 class attributes and methods
War_Card1_value: Property = Property(name="value", type=IntegerType)
War_Card1_suit: Property = Property(name="suit", type=War_Suit1)
War_Card1_rank: Property = Property(name="rank", type=War_Rank1)
War_Card1_value1: Property = Property(name="value1", type=IntegerType)
War_Card1_suit1: Property = Property(name="suit1", type=War_Suit1)
War_Card1_rank1: Property = Property(name="rank1", type=War_Rank1)
War_Card1.attributes={War_Card1_value1, War_Card1_rank, War_Card1_suit1, War_Card1_rank1, War_Card1_value, War_Card1_suit}

# War_ClassicTwoPlayer1 class attributes and methods

# War_Deck1 class attributes and methods
War_Deck1_TOP_CARD: Property = Property(name="TOP_CARD", type=IntegerType)
War_Deck1_NUMERIC_CARDS_IN_SUIT: Property = Property(name="NUMERIC_CARDS_IN_SUIT", type=IntegerType)
War_Deck1_LOWEST_NUMERIC_VALUE: Property = Property(name="LOWEST_NUMERIC_VALUE", type=IntegerType)
War_Deck1_TOP_CARD1: Property = Property(name="TOP_CARD1", type=IntegerType)
War_Deck1_NUMERIC_CARDS_IN_SUIT1: Property = Property(name="NUMERIC_CARDS_IN_SUIT1", type=IntegerType)
War_Deck1_LOWEST_NUMERIC_VALUE1: Property = Property(name="LOWEST_NUMERIC_VALUE1", type=IntegerType)
War_Deck1.attributes={War_Deck1_LOWEST_NUMERIC_VALUE1, War_Deck1_TOP_CARD1, War_Deck1_NUMERIC_CARDS_IN_SUIT, War_Deck1_NUMERIC_CARDS_IN_SUIT1, War_Deck1_LOWEST_NUMERIC_VALUE, War_Deck1_TOP_CARD}

# War_DeckIterator1 class attributes and methods
War_DeckIterator1_current: Property = Property(name="current", type=IntegerType)
War_DeckIterator1_current1: Property = Property(name="current1", type=IntegerType)
War_DeckIterator1.attributes={War_DeckIterator1_current1, War_DeckIterator1_current}

# War_GameLogger1 class attributes and methods
War_GameLogger1_gameLogWriter: Property = Property(name="gameLogWriter", type=StringType)
War_GameLogger1_gameLogWriter1: Property = Property(name="gameLogWriter1", type=StringType)
War_GameLogger1.attributes={War_GameLogger1_gameLogWriter, War_GameLogger1_gameLogWriter1}

# War_PlayGame1 class attributes and methods

# War_Player1 class attributes and methods
War_Player1_score: Property = Property(name="score", type=IntegerType)
War_Player1_name: Property = Property(name="name", type=StringType)
War_Player1_score1: Property = Property(name="score1", type=IntegerType)
War_Player1_name1: Property = Property(name="name1", type=StringType)
War_Player1.attributes={War_Player1_name, War_Player1_score1, War_Player1_name1, War_Player1_score}

# War_ThreePlayerPointPile1 class attributes and methods
War_ThreePlayerPointPile1_logger: Property = Property(name="logger", type=StringType)
War_ThreePlayerPointPile1_inWar: Property = Property(name="inWar", type=BooleanType)
War_ThreePlayerPointPile1_logger1: Property = Property(name="logger1", type=StringType)
War_ThreePlayerPointPile1_inWar1: Property = Property(name="inWar1", type=BooleanType)
War_ThreePlayerPointPile1.attributes={War_ThreePlayerPointPile1_logger, War_ThreePlayerPointPile1_inWar, War_ThreePlayerPointPile1_inWar1, War_ThreePlayerPointPile1_logger1}

# War_TwoPlayerPointPile1 class attributes and methods
War_TwoPlayerPointPile1_logger: Property = Property(name="logger", type=StringType)
War_TwoPlayerPointPile1_inWar: Property = Property(name="inWar", type=BooleanType)
War_TwoPlayerPointPile1_logger1: Property = Property(name="logger1", type=StringType)
War_TwoPlayerPointPile1_inWar1: Property = Property(name="inWar1", type=BooleanType)
War_TwoPlayerPointPile1.attributes={War_TwoPlayerPointPile1_inWar, War_TwoPlayerPointPile1_logger, War_TwoPlayerPointPile1_logger1, War_TwoPlayerPointPile1_inWar1}

# War_WarGameVariation class attributes and methods

# War_WarVariationClassic class attributes and methods

# War_WarVariationWithPoints class attributes and methods

# War_WarGameVariation1 class attributes and methods
War_WarGameVariation1_numOfPlayers: Property = Property(name="numOfPlayers", type=IntegerType)
War_WarGameVariation1_numOfPlayers1: Property = Property(name="numOfPlayers1", type=IntegerType)
War_WarGameVariation1.attributes={War_WarGameVariation1_numOfPlayers, War_WarGameVariation1_numOfPlayers1}

# War_WarVariationClassic1 class attributes and methods
War_WarVariationClassic1_numOfRounds: Property = Property(name="numOfRounds", type=IntegerType)
War_WarVariationClassic1_numOfRounds1: Property = Property(name="numOfRounds1", type=IntegerType)
War_WarVariationClassic1.attributes={War_WarVariationClassic1_numOfRounds, War_WarVariationClassic1_numOfRounds1}

# War_WarVariationWithPoints1 class attributes and methods
War_WarVariationWithPoints1_logger: Property = Property(name="logger", type=StringType)
War_WarVariationWithPoints1_inWar: Property = Property(name="inWar", type=BooleanType)
War_WarVariationWithPoints1_logger1: Property = Property(name="logger1", type=StringType)
War_WarVariationWithPoints1_inWar1: Property = Property(name="inWar1", type=BooleanType)
War_WarVariationWithPoints1.attributes={War_WarVariationWithPoints1_logger, War_WarVariationWithPoints1_inWar, War_WarVariationWithPoints1_inWar1, War_WarVariationWithPoints1_logger1}

# Comparable_Card__Interface class attributes and methods

# Iterable_Card__Interface class attributes and methods

# Iterator_Card__Interface class attributes and methods

# Relationships
players_WarGameVariation_Player_21: BinaryAssociation = BinaryAssociation(
    name="players_WarGameVariation_Player_21",
    ends={
        Property(name="wargamevariation0", type=War_WarGameVariation1, multiplicity=Multiplicity(0, 1)),
        Property(name="players1", type=War_Player1, multiplicity=Multiplicity(0, 9999))
    }
)
deck_Deck_Card_10: BinaryAssociation = BinaryAssociation(
    name="deck_Deck_Card_10",
    ends={
        Property(name="deck2", type=War_Deck1, multiplicity=Multiplicity(0, 1)),
        Property(name="deck3", type=War_Card1, multiplicity=Multiplicity(0, 9999))
    }
)
hand_Player_Deck_8: BinaryAssociation = BinaryAssociation(
    name="hand_Player_Deck_8",
    ends={
        Property(name="player4", type=War_Player1, multiplicity=Multiplicity(0, 1)),
        Property(name="hand5", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)
deck_DeckIterator_Deck_18: BinaryAssociation = BinaryAssociation(
    name="deck_DeckIterator_Deck_18",
    ends={
        Property(name="deckiterator6", type=War_DeckIterator1, multiplicity=Multiplicity(0, 1)),
        Property(name="deck7", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)
warLogger_WarGameVariation_GameLogger_15: BinaryAssociation = BinaryAssociation(
    name="warLogger_WarGameVariation_GameLogger_15",
    ends={
        Property(name="wargamevariation12", type=War_WarGameVariation1, multiplicity=Multiplicity(0, 1)),
        Property(name="warLogger13", type=War_GameLogger1, multiplicity=Multiplicity(0, 1))
    }
)
player2_WarVariationClassic_Player_5: BinaryAssociation = BinaryAssociation(
    name="player2_WarVariationClassic_Player_5",
    ends={
        Property(name="warvariationclassic14", type=War_WarVariationClassic1, multiplicity=Multiplicity(0, 1)),
        Property(name="player215", type=War_Player1, multiplicity=Multiplicity(0, 1))
    }
)
winPile_WarGameVariation_Deck_11: BinaryAssociation = BinaryAssociation(
    name="winPile_WarGameVariation_Deck_11",
    ends={
        Property(name="wargamevariation16", type=War_WarGameVariation1, multiplicity=Multiplicity(0, 1)),
        Property(name="winPile17", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)
card_Deck_Card_6: BinaryAssociation = BinaryAssociation(
    name="card_Deck_Card_6",
    ends={
        Property(name="deck18", type=War_Deck1, multiplicity=Multiplicity(0, 1)),
        Property(name="card19", type=War_Card1, multiplicity=Multiplicity(0, 1))
    }
)
card_Deck_Card_7: BinaryAssociation = BinaryAssociation(
    name="card_Deck_Card_7",
    ends={
        Property(name="deck20", type=War_Deck1, multiplicity=Multiplicity(0, 1)),
        Property(name="card21", type=War_Card1, multiplicity=Multiplicity(0, 1))
    }
)
deck_DeckIterator_Deck_3: BinaryAssociation = BinaryAssociation(
    name="deck_DeckIterator_Deck_3",
    ends={
        Property(name="deckiterator22", type=War_DeckIterator1, multiplicity=Multiplicity(0, 1)),
        Property(name="deck23", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)
warLogger_WarGameVariation_GameLogger_9: BinaryAssociation = BinaryAssociation(
    name="warLogger_WarGameVariation_GameLogger_9",
    ends={
        Property(name="wargamevariation24", type=War_WarGameVariation1, multiplicity=Multiplicity(0, 1)),
        Property(name="warLogger25", type=War_GameLogger1, multiplicity=Multiplicity(0, 1))
    }
)
player1_WarVariationClassic_Player_20: BinaryAssociation = BinaryAssociation(
    name="player1_WarVariationClassic_Player_20",
    ends={
        Property(name="warvariationclassic26", type=War_WarVariationClassic1, multiplicity=Multiplicity(0, 1)),
        Property(name="player127", type=War_Player1, multiplicity=Multiplicity(0, 1))
    }
)
player2_WarVariationClassic_Player_1: BinaryAssociation = BinaryAssociation(
    name="player2_WarVariationClassic_Player_1",
    ends={
        Property(name="warvariationclassic28", type=War_WarVariationClassic1, multiplicity=Multiplicity(0, 1)),
        Property(name="player229", type=War_Player1, multiplicity=Multiplicity(0, 1))
    }
)
winPile_WarGameVariation_Deck_16: BinaryAssociation = BinaryAssociation(
    name="winPile_WarGameVariation_Deck_16",
    ends={
        Property(name="wargamevariation30", type=War_WarGameVariation1, multiplicity=Multiplicity(0, 1)),
        Property(name="winPile31", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)
player1_WarVariationClassic_Player_2: BinaryAssociation = BinaryAssociation(
    name="player1_WarVariationClassic_Player_2",
    ends={
        Property(name="warvariationclassic32", type=War_WarVariationClassic1, multiplicity=Multiplicity(0, 1)),
        Property(name="player133", type=War_Player1, multiplicity=Multiplicity(0, 1))
    }
)
players_WarGameVariation_Player_13: BinaryAssociation = BinaryAssociation(
    name="players_WarGameVariation_Player_13",
    ends={
        Property(name="wargamevariation34", type=War_WarGameVariation1, multiplicity=Multiplicity(0, 1)),
        Property(name="players35", type=War_Player1, multiplicity=Multiplicity(0, 9999))
    }
)
cardsWon_Player_Deck_17: BinaryAssociation = BinaryAssociation(
    name="cardsWon_Player_Deck_17",
    ends={
        Property(name="player36", type=War_Player1, multiplicity=Multiplicity(0, 1)),
        Property(name="cardsWon37", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)
cardsWon_Player_Deck_19: BinaryAssociation = BinaryAssociation(
    name="cardsWon_Player_Deck_19",
    ends={
        Property(name="player38", type=War_Player1, multiplicity=Multiplicity(0, 1)),
        Property(name="cardsWon39", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)
deck_Deck_Card_4: BinaryAssociation = BinaryAssociation(
    name="deck_Deck_Card_4",
    ends={
        Property(name="deck8", type=War_Deck1, multiplicity=Multiplicity(0, 1)),
        Property(name="deck9", type=War_Card1, multiplicity=Multiplicity(0, 9999))
    }
)
hand_Player_Deck_0: BinaryAssociation = BinaryAssociation(
    name="hand_Player_Deck_0",
    ends={
        Property(name="player10", type=War_Player1, multiplicity=Multiplicity(0, 1)),
        Property(name="hand11", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)
deck_WarGameVariation_Deck_12: BinaryAssociation = BinaryAssociation(
    name="deck_WarGameVariation_Deck_12",
    ends={
        Property(name="wargamevariation40", type=War_WarGameVariation1, multiplicity=Multiplicity(0, 1)),
        Property(name="deck41", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)
deck_WarGameVariation_Deck_14: BinaryAssociation = BinaryAssociation(
    name="deck_WarGameVariation_Deck_14",
    ends={
        Property(name="wargamevariation42", type=War_WarGameVariation1, multiplicity=Multiplicity(0, 1)),
        Property(name="deck43", type=War_Deck1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vFv4QMt7Eeib_M6EW71F_A",
    types={War_Card, War_ClassicTwoPlayer, War_Deck, War_DeckIterator, War_GameLogger, War_PlayGame, War_Player, War_ThreePlayerPointPile, War_TwoPlayerPointPile, War_Card1, War_ClassicTwoPlayer1, War_Deck1, War_DeckIterator1, War_GameLogger1, War_PlayGame1, War_Player1, War_ThreePlayerPointPile1, War_TwoPlayerPointPile1, War_WarGameVariation, War_WarVariationClassic, War_WarVariationWithPoints, War_WarGameVariation1, War_WarVariationClassic1, War_WarVariationWithPoints1, Comparable_Card__Interface, Iterable_Card__Interface, Iterator_Card__Interface, War_Suit, War_Rank, War_Suit1, War_Rank1},
    associations={players_WarGameVariation_Player_21, deck_Deck_Card_10, hand_Player_Deck_8, deck_DeckIterator_Deck_18, warLogger_WarGameVariation_GameLogger_15, player2_WarVariationClassic_Player_5, winPile_WarGameVariation_Deck_11, card_Deck_Card_6, card_Deck_Card_7, deck_DeckIterator_Deck_3, warLogger_WarGameVariation_GameLogger_9, player1_WarVariationClassic_Player_20, player2_WarVariationClassic_Player_1, winPile_WarGameVariation_Deck_16, player1_WarVariationClassic_Player_2, players_WarGameVariation_Player_13, cardsWon_Player_Deck_17, cardsWon_Player_Deck_19, deck_Deck_Card_4, hand_Player_Deck_0, deck_WarGameVariation_Deck_12, deck_WarGameVariation_Deck_14},
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