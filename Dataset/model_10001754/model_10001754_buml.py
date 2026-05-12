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
CardSuits: Enumeration = Enumeration(
    name="CardSuits",
    literals={
            
    }
)

# Classes
User_Actor = Class(name="User_Actor")
Game_Component = Class(name="Game_Component")
Move_a_Card_two_Spaces_UseCase = Class(name="Move_a_Card_two_Spaces_UseCase")
Automatic_play_UseCase = Class(name="Automatic_play_UseCase")
Print_Cards_text_form__UseCase = Class(name="Print_Cards_text_form__UseCase")
Amalgamate_Middle_Cards_UseCase = Class(name="Amalgamate_Middle_Cards_UseCase")
Display_leaderboard_UseCase = Class(name="Display_leaderboard_UseCase")
Display_Rulebook_UseCase = Class(name="Display_Rulebook_UseCase")
Game = Class(name="Game")
Card = Class(name="Card")
Board = Class(name="Board")
CardTable = Class(name="CardTable")
Rules = Class(name="Rules")
Deck = Class(name="Deck")
Deal_A_Card_external = Class(name="Deal_A_Card_external")
Shuffle_Deck_external = Class(name="Shuffle_Deck_external")
Move_a_Card_one_Space_external = Class(name="Move_a_Card_one_Space_external")

# User_Actor class attributes and methods

# Game_Component class attributes and methods

# Move_a_Card_two_Spaces_UseCase class attributes and methods

# Automatic_play_UseCase class attributes and methods

# Print_Cards_text_form__UseCase class attributes and methods

# Amalgamate_Middle_Cards_UseCase class attributes and methods

# Display_leaderboard_UseCase class attributes and methods

# Display_Rulebook_UseCase class attributes and methods

# Game class attributes and methods
Game_deck: Property = Property(name="deck", type=Deck)
Game_board: Property = Property(name="board", type=Board)
Game_scan: Property = Property(name="scan", type=StringType)
Game.attributes={Game_deck, Game_board, Game_scan}

# Card class attributes and methods
Card_suit: Property = Property(name="suit", type=CardSuits)
Card_name: Property = Property(name="name", type=StringType)
Card_cardNames: Property = Property(name="cardNames", type=StringType)
Card.attributes={Card_name, Card_cardNames, Card_suit}

# Board class attributes and methods
Board_scores: Property = Property(name="scores", type=Card)
Board_board: Property = Property(name="board", type=Card)
Board_boardGui: Property = Property(name="boardGui", type=Card)
Board.attributes={Board_board, Board_scores, Board_boardGui}

# CardTable class attributes and methods
CardTable_stage: Property = Property(name="stage", type=StringType)
CardTable_cards: Property = Property(name="cards", type=Card)
CardTable_done: Property = Property(name="done", type=BooleanType)
CardTable.attributes={CardTable_stage, CardTable_done, CardTable_cards}

# Rules class attributes and methods

# Deck class attributes and methods
Deck_card: Property = Property(name="card", type=Card)
Deck_deck___: Property = Property(name="deck___", type=StringType)
Deck.attributes={Deck_deck___, Deck_card}

# Deal_A_Card_external class attributes and methods

# Shuffle_Deck_external class attributes and methods

# Move_a_Card_one_Space_external class attributes and methods

# Relationships
User_Deal_A_Card: BinaryAssociation = BinaryAssociation(
    name="User_Deal_A_Card",
    ends={
        Property(name="deal_A_Card0", type=Deal_A_Card_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Shuffle_Deck: BinaryAssociation = BinaryAssociation(
    name="User_Shuffle_Deck",
    ends={
        Property(name="shuffle_Deck2", type=Shuffle_Deck_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Move_a_Card_one_Space: BinaryAssociation = BinaryAssociation(
    name="User_Move_a_Card_one_Space",
    ends={
        Property(name="move_a_Card_one_Space4", type=Move_a_Card_one_Space_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Amalgamate_Middle_Cards: BinaryAssociation = BinaryAssociation(
    name="User_Amalgamate_Middle_Cards",
    ends={
        Property(name="amalgamate_Middle_Cards6", type=Amalgamate_Middle_Cards_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Move_a_Card_two_Spaces: BinaryAssociation = BinaryAssociation(
    name="User_Move_a_Card_two_Spaces",
    ends={
        Property(name="move_a_Card_two_Spaces8", type=Move_a_Card_two_Spaces_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user9", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Print_Cards_text_form_: BinaryAssociation = BinaryAssociation(
    name="User_Print_Cards_text_form_",
    ends={
        Property(name="print_Cards_text_form_10", type=Print_Cards_text_form__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Automatic_play: BinaryAssociation = BinaryAssociation(
    name="User_Automatic_play",
    ends={
        Property(name="automatic_play12", type=Automatic_play_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Display_leaderboard: BinaryAssociation = BinaryAssociation(
    name="User_Display_leaderboard",
    ends={
        Property(name="display_leaderboard14", type=Display_leaderboard_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user15", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Display_Rulebook: BinaryAssociation = BinaryAssociation(
    name="User_Display_Rulebook",
    ends={
        Property(name="display_Rulebook16", type=Display_Rulebook_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user17", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Game_Rules: BinaryAssociation = BinaryAssociation(
    name="Game_Rules",
    ends={
        Property(name="rules18", type=Rules, multiplicity=Multiplicity(1, 1)),
        Property(name="game19", type=Game, multiplicity=Multiplicity(1, 1))
    }
)
Game_Board: BinaryAssociation = BinaryAssociation(
    name="Game_Board",
    ends={
        Property(name="board20", type=Board, multiplicity=Multiplicity(0, 1)),
        Property(name="game21", type=Game, multiplicity=Multiplicity(1, 1))
    }
)
Game_Deck: BinaryAssociation = BinaryAssociation(
    name="Game_Deck",
    ends={
        Property(name="deck22", type=Deck, multiplicity=Multiplicity(0, 9999)),
        Property(name="game23", type=Game, multiplicity=Multiplicity(1, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card24", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="deck25", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_T41gME7mEeict5GQq2fjkw",
    types={User_Actor, Game_Component, Move_a_Card_two_Spaces_UseCase, Automatic_play_UseCase, Print_Cards_text_form__UseCase, Amalgamate_Middle_Cards_UseCase, Display_leaderboard_UseCase, Display_Rulebook_UseCase, Game, Card, Board, CardTable, Rules, Deck, Deal_A_Card_external, Shuffle_Deck_external, Move_a_Card_one_Space_external, CardSuits},
    associations={User_Deal_A_Card, User_Shuffle_Deck, User_Move_a_Card_one_Space, User_Amalgamate_Middle_Cards, User_Move_a_Card_two_Spaces, User_Print_Cards_text_form_, User_Automatic_play, User_Display_leaderboard, User_Display_Rulebook, Game_Rules, Game_Board, Game_Deck, Deck_Card},
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