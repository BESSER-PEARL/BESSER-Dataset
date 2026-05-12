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
Suits: Enumeration = Enumeration(
    name="Suits",
    literals={
            
    }
)

# Classes
Card_Interface = Class(name="Card_Interface")
Game = Class(name="Game")
Round = Class(name="Round")
Piquet = Class(name="Piquet")
ScoreSheet_Interface = Class(name="ScoreSheet_Interface")
Trick = Class(name="Trick")
Scores = Class(name="Scores")
IBlind_Interface = Class(name="IBlind_Interface")
Table = Class(name="Table")
Human = Class(name="Human")
Hand = Class(name="Hand")
Cards = Class(name="Cards")
Deck_Interface = Class(name="Deck_Interface")
Player_Interface = Class(name="Player_Interface")
Bot = Class(name="Bot")

# Card_Interface class attributes and methods

# Game class attributes and methods
Game_rounds_6_: Property = Property(name="rounds_6_", type=Round)
Game_deck: Property = Property(name="deck", type=Deck_Interface)
Game_isCracked: Property = Property(name="isCracked", type=BooleanType)
Game_picker: Property = Property(name="picker", type=Player_Interface)
Game_partner: Property = Property(name="partner", type=Player_Interface)
Game_blind: Property = Property(name="blind", type=IBlind_Interface)
Game_partnerCard: Property = Property(name="partnerCard", type=Card_Interface)
Game.attributes={Game_isCracked, Game_picker, Game_partnerCard, Game_partner, Game_deck, Game_rounds_6_, Game_blind}

# Round class attributes and methods
Round_roundNum: Property = Property(name="roundNum", type=IntegerType)
Round_turnToPlay: Property = Property(name="turnToPlay", type=Player_Interface)
Round_trick: Property = Property(name="trick", type=Trick)
Round_RoundStarter: Property = Property(name="RoundStarter", type=Player_Interface)
Round.attributes={Round_trick, Round_RoundStarter, Round_roundNum, Round_turnToPlay}

# Piquet class attributes and methods
Piquet_cards_32_: Property = Property(name="cards_32_", type=Card_Interface)
Piquet.attributes={Piquet_cards_32_}

# ScoreSheet_Interface class attributes and methods

# Trick class attributes and methods
Trick_Card_5_: Property = Property(name="Card_5_", type=StringType)
Trick_trickWinner: Property = Property(name="trickWinner", type=Player_Interface)
Trick.attributes={Trick_trickWinner, Trick_Card_5_}

# Scores class attributes and methods

# IBlind_Interface class attributes and methods

# Table class attributes and methods
Table_players_5_: Property = Property(name="players_5_", type=Player_Interface)
Table_Games_6___: Property = Property(name="Games_6___", type=Game)
Table_scoreSheet: Property = Property(name="scoreSheet", type=ScoreSheet_Interface)
Table_dealer: Property = Property(name="dealer", type=Player_Interface)
Table_numOfGames: Property = Property(name="numOfGames", type=IntegerType)
Table.attributes={Table_players_5_, Table_dealer, Table_numOfGames, Table_scoreSheet, Table_Games_6___}

# Human class attributes and methods
Human_name: Property = Property(name="name", type=StringType)
Human_hand: Property = Property(name="hand", type=Hand)
Human.attributes={Human_hand, Human_name}

# Hand class attributes and methods
Hand_cards_6_: Property = Property(name="cards_6_", type=StringType)
Hand.attributes={Hand_cards_6_}

# Cards class attributes and methods
Cards_num: Property = Property(name="num", type=IntegerType)
Cards_suit: Property = Property(name="suit", type=Suits)
Cards_power: Property = Property(name="power", type=IntegerType)
Cards_value: Property = Property(name="value", type=IntegerType)
Cards.attributes={Cards_suit, Cards_power, Cards_num, Cards_value}

# Deck_Interface class attributes and methods

# Player_Interface class attributes and methods

# Bot class attributes and methods
Bot_name: Property = Property(name="name", type=StringType)
Bot_hand: Property = Property(name="hand", type=Hand)
Bot.attributes={Bot_name, Bot_hand}

# Relationships
Game_Table: BinaryAssociation = BinaryAssociation(
    name="Game_Table",
    ends={
        Property(name="table0", type=Table, multiplicity=Multiplicity(0, 1)),
        Property(name="game1", type=Game, multiplicity=Multiplicity(0, 1))
    }
)
Game_Round: BinaryAssociation = BinaryAssociation(
    name="Game_Round",
    ends={
        Property(name="round2", type=Round, multiplicity=Multiplicity(0, 1)),
        Property(name="game3", type=Game, multiplicity=Multiplicity(0, 1))
    }
)
Hand_Card: BinaryAssociation = BinaryAssociation(
    name="Hand_Card",
    ends={
        Property(name="card4", type=Card_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="hand5", type=Hand, multiplicity=Multiplicity(0, 1))
    }
)
Trick_Round: BinaryAssociation = BinaryAssociation(
    name="Trick_Round",
    ends={
        Property(name="round6", type=Round, multiplicity=Multiplicity(0, 1)),
        Property(name="trick27", type=Trick, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ois8IAIDEeifsJ80ec9hDw",
    types={Card_Interface, Game, Round, Piquet, ScoreSheet_Interface, Trick, Scores, IBlind_Interface, Table, Human, Hand, Cards, Deck_Interface, Player_Interface, Bot, Suits},
    associations={Game_Table, Game_Round, Hand_Card, Trick_Round},
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