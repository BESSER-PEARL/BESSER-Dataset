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
Card_Deck = Class(name="Card_Deck")
Card_Cards = Class(name="Card_Cards")
Game_Ranking = Class(name="Game_Ranking")
Game_Display = Class(name="Game_Display")
Game_EvaluateHand = Class(name="Game_EvaluateHand")
Player_Players = Class(name="Player_Players")
Main_StartGame = Class(name="Main_StartGame")
Comparable_Interface = Class(name="Comparable_Interface")
GUI_Interface = Class(name="GUI_Interface")
Money_PlayerMoney = Class(name="Money_PlayerMoney")

# Card_Deck class attributes and methods
Card_Deck_decksize: Property = Property(name="decksize", type=IntegerType)
Card_Deck_shuffletimes: Property = Property(name="shuffletimes", type=IntegerType)
Card_Deck_handsize: Property = Property(name="handsize", type=IntegerType)
Card_Deck_remainder: Property = Property(name="remainder", type=IntegerType)
Card_Deck_deck: Property = Property(name="deck", type=StringType)
Card_Deck_random: Property = Property(name="random", type=StringType)
Card_Deck.attributes={Card_Deck_shuffletimes, Card_Deck_remainder, Card_Deck_decksize, Card_Deck_handsize, Card_Deck_random, Card_Deck_deck}

# Card_Cards class attributes and methods
Card_Cards_suit: Property = Property(name="suit", type=IntegerType)
Card_Cards_rank: Property = Property(name="rank", type=IntegerType)
Card_Cards.attributes={Card_Cards_rank, Card_Cards_suit}

# Game_Ranking class attributes and methods
Game_Ranking_card: Property = Property(name="card", type=StringType)
Game_Ranking.attributes={Game_Ranking_card}

# Game_Display class attributes and methods
Game_Display_card: Property = Property(name="card", type=StringType)
Game_Display_money: Property = Property(name="money", type=StringType)
Game_Display.attributes={Game_Display_money, Game_Display_card}

# Game_EvaluateHand class attributes and methods
Game_EvaluateHand_card: Property = Property(name="card", type=StringType)
Game_EvaluateHand.attributes={Game_EvaluateHand_card}

# Player_Players class attributes and methods

# Main_StartGame class attributes and methods
Main_StartGame_hand: Property = Property(name="hand", type=StringType)
Main_StartGame_handsize: Property = Property(name="handsize", type=IntegerType)
Main_StartGame_scanner: Property = Property(name="scanner", type=StringType)
Main_StartGame_deck: Property = Property(name="deck", type=StringType)
Main_StartGame_player: Property = Property(name="player", type=StringType)
Main_StartGame.attributes={Main_StartGame_handsize, Main_StartGame_scanner, Main_StartGame_deck, Main_StartGame_hand, Main_StartGame_player}

# Comparable_Interface class attributes and methods

# GUI_Interface class attributes and methods

# Money_PlayerMoney class attributes and methods
Money_PlayerMoney_numofplayers: Property = Property(name="numofplayers", type=StringType)
Money_PlayerMoney_totalmoney: Property = Property(name="totalmoney", type=StringType)
Money_PlayerMoney.attributes={Money_PlayerMoney_numofplayers, Money_PlayerMoney_totalmoney}

# Domain Model
domain_model = DomainModel(
    name="_2ykZAAqnEeihOuC11hdjgA",
    types={Card_Deck, Card_Cards, Game_Ranking, Game_Display, Game_EvaluateHand, Player_Players, Main_StartGame, Comparable_Interface, GUI_Interface, Money_PlayerMoney},
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