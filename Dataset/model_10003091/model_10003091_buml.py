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
Card = Class(name="Card")
Deck = Class(name="Deck")
CardGame = Class(name="CardGame")
Player = Class(name="Player")
GameBoard = Class(name="GameBoard")
SheddingGame = Class(name="SheddingGame")
TrickGame = Class(name="TrickGame")
MatchingGame = Class(name="MatchingGame")
int_Interface = Class(name="int_Interface")
GameController = Class(name="GameController")

# Card class attributes and methods
Card_face: Property = Property(name="face", type=IntegerType)
Card_suit: Property = Property(name="suit", type=StringType)
Card.attributes={Card_suit, Card_face}

# Deck class attributes and methods
Deck_deck: Property = Property(name="deck", type=StringType)
Deck_size: Property = Property(name="size", type=IntegerType)
Deck.attributes={Deck_size, Deck_deck}

# CardGame class attributes and methods
CardGame_players: Property = Property(name="players", type=StringType)
CardGame_round: Property = Property(name="round", type=IntegerType)
CardGame_winner: Property = Property(name="winner", type=Player)
CardGame.attributes={CardGame_players, CardGame_round, CardGame_winner}

# Player class attributes and methods
Player_hand: Property = Property(name="hand", type=StringType)
Player_score: Property = Property(name="score", type=IntegerType)
Player.attributes={Player_hand, Player_score}

# GameBoard class attributes and methods
GameBoard_startGame: Property = Property(name="startGame", type=StringType)
GameBoard_board: Property = Property(name="board", type=StringType)
GameBoard_selectCard: Property = Property(name="selectCard", type=StringType)
GameBoard_drawCard: Property = Property(name="drawCard", type=StringType)
GameBoard_score: Property = Property(name="score", type=StringType)
GameBoard.attributes={GameBoard_score, GameBoard_drawCard, GameBoard_selectCard, GameBoard_startGame, GameBoard_board}

# SheddingGame class attributes and methods

# TrickGame class attributes and methods
TrickGame_trickRules: Property = Property(name="trickRules", type=StringType)
TrickGame.attributes={TrickGame_trickRules}

# MatchingGame class attributes and methods
MatchingGame_matches: Property = Property(name="matches", type=IntegerType)
MatchingGame.attributes={MatchingGame_matches}

# int_Interface class attributes and methods

# GameController class attributes and methods
GameController_cardGame: Property = Property(name="cardGame", type=CardGame)
GameController_gameView: Property = Property(name="gameView", type=GameBoard)
GameController.attributes={GameController_cardGame, GameController_gameView}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="card0", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="deck1", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
holds: BinaryAssociation = BinaryAssociation(
    name="holds",
    ends={
        Property(name="player2", type=Player, multiplicity=Multiplicity(1, 1)),
        Property(name="card3", type=Card, multiplicity=Multiplicity(1, 9999))
    }
)
hasA: BinaryAssociation = BinaryAssociation(
    name="hasA",
    ends={
        Property(name="player4", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="game5", type=CardGame, multiplicity=Multiplicity(1, 1))
    }
)
drawsFrom: BinaryAssociation = BinaryAssociation(
    name="drawsFrom",
    ends={
        Property(name="deck6", type=Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="game7", type=CardGame, multiplicity=Multiplicity(1, 1))
    }
)
Game_Controller: BinaryAssociation = BinaryAssociation(
    name="Game_Controller",
    ends={
        Property(name="controller8", type=GameController, multiplicity=Multiplicity(1, 1)),
        Property(name="game9", type=CardGame, multiplicity=Multiplicity(1, 1))
    }
)
Controller_GameBoard: BinaryAssociation = BinaryAssociation(
    name="Controller_GameBoard",
    ends={
        Property(name="gameBoard10", type=GameBoard, multiplicity=Multiplicity(1, 1)),
        Property(name="controller11", type=GameController, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fdaee4c4_3760_436b_9300_3f585e5e1b7d",
    types={Card, Deck, CardGame, Player, GameBoard, SheddingGame, TrickGame, MatchingGame, int_Interface, GameController},
    associations={contains, holds, hasA, drawsFrom, Game_Controller, Controller_GameBoard},
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