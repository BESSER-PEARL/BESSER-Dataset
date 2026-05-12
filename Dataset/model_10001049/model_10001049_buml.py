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
AcePile = Class(name="AcePile")
Card = Class(name="Card")
CardStack = Class(name="CardStack")
ChangeAppearance = Class(name="ChangeAppearance")
ChangeOptions = Class(name="ChangeOptions")
Column = Class(name="Column")
DealDeck = Class(name="DealDeck")
Deck = Class(name="Deck")
DiscardPile = Class(name="DiscardPile")
FireworksDisplay = Class(name="FireworksDisplay")
FourRowSolitaire = Class(name="FourRowSolitaire")
SingleCell = Class(name="SingleCell")
SolitaireBoard = Class(name="SolitaireBoard")
SolitaireLayout = Class(name="SolitaireLayout")
SolitairePanel = Class(name="SolitairePanel")
WinScreen = Class(name="WinScreen")
Graphics = Class(name="Graphics")
ActionEvent = Class(name="ActionEvent")

# AcePile class attributes and methods
AcePile_suit: Property = Property(name="suit", type=StringType)
AcePile.attributes={AcePile_suit}

# Card class attributes and methods
Card_SPADES_SUIT: Property = Property(name="SPADES_SUIT", type=StringType)
Card_CLUBS_SUIT: Property = Property(name="CLUBS_SUIT", type=StringType)
Card_HEARTS_SUIT: Property = Property(name="HEARTS_SUIT", type=StringType)
Card_DIAMONDS_SUIT: Property = Property(name="DIAMONDS_SUIT", type=StringType)
Card_INVALID_SUIT: Property = Property(name="INVALID_SUIT", type=StringType)
Card_ACE: Property = Property(name="ACE", type=IntegerType)
Card_TWO: Property = Property(name="TWO", type=IntegerType)
Card_THREE: Property = Property(name="THREE", type=IntegerType)
Card_FOUR: Property = Property(name="FOUR", type=IntegerType)
Card_FIVE: Property = Property(name="FIVE", type=IntegerType)
Card_SIX: Property = Property(name="SIX", type=IntegerType)
Card_SEVEN: Property = Property(name="SEVEN", type=IntegerType)
Card_EIGHT: Property = Property(name="EIGHT", type=IntegerType)
Card_NINE: Property = Property(name="NINE", type=IntegerType)
Card_TEN: Property = Property(name="TEN", type=IntegerType)
Card_JACK: Property = Property(name="JACK", type=IntegerType)
Card_QUEEN: Property = Property(name="QUEEN", type=IntegerType)
Card_KING: Property = Property(name="KING", type=IntegerType)
Card_INVALID_NUMBER: Property = Property(name="INVALID_NUMBER", type=IntegerType)
Card_cardSuit: Property = Property(name="cardSuit", type=StringType)
Card_cardNumber: Property = Property(name="cardNumber", type=IntegerType)
Card_fullCardNumber: Property = Property(name="fullCardNumber", type=IntegerType)
Card_cardColor: Property = Property(name="cardColor", type=IntegerType)
Card_deckNumber: Property = Property(name="deckNumber", type=IntegerType)
Card_image: Property = Property(name="image", type=StringType)
Card_cardBack: Property = Property(name="cardBack", type=StringType)
Card_cardImageString: Property = Property(name="cardImageString", type=StringType)
Card_cardHighlighted: Property = Property(name="cardHighlighted", type=StringType)
Card_faceUp: Property = Property(name="faceUp", type=BooleanType)
Card_highlighted: Property = Property(name="highlighted", type=BooleanType)
Card_location: Property = Property(name="location", type=StringType)
Card.attributes={Card_KING, Card_INVALID_NUMBER, Card_HEARTS_SUIT, Card_cardColor, Card_CLUBS_SUIT, Card_FIVE, Card_cardImageString, Card_INVALID_SUIT, Card_FOUR, Card_cardBack, Card_TEN, Card_cardNumber, Card_TWO, Card_NINE, Card_fullCardNumber, Card_JACK, Card_SPADES_SUIT, Card_location, Card_DIAMONDS_SUIT, Card_faceUp, Card_SEVEN, Card_QUEEN, Card_THREE, Card_SIX, Card_cardHighlighted, Card_highlighted, Card_image, Card_deckNumber, Card_EIGHT, Card_ACE, Card_cardSuit}

# CardStack class attributes and methods

# ChangeAppearance class attributes and methods
ChangeAppearance_NUM_DECKS: Property = Property(name="NUM_DECKS", type=IntegerType)
ChangeAppearance_NUM_BACKGROUNDS: Property = Property(name="NUM_BACKGROUNDS", type=IntegerType)
ChangeAppearance_FRS_DECK: Property = Property(name="FRS_DECK", type=IntegerType)
ChangeAppearance_FRS_BACKGROUND: Property = Property(name="FRS_BACKGROUND", type=IntegerType)
ChangeAppearance_decks: Property = Property(name="decks", type=StringType)
ChangeAppearance_backgrounds: Property = Property(name="backgrounds", type=StringType)
ChangeAppearance_ok: Property = Property(name="ok", type=StringType)
ChangeAppearance_deckNumber: Property = Property(name="deckNumber", type=IntegerType)
ChangeAppearance_backgroundNumber: Property = Property(name="backgroundNumber", type=IntegerType)
ChangeAppearance_exited: Property = Property(name="exited", type=BooleanType)
ChangeAppearance_cardBackLabel: Property = Property(name="cardBackLabel", type=StringType)
ChangeAppearance_backgroundLabel: Property = Property(name="backgroundLabel", type=StringType)
ChangeAppearance.attributes={ChangeAppearance_backgroundNumber, ChangeAppearance_cardBackLabel, ChangeAppearance_backgroundLabel, ChangeAppearance_ok, ChangeAppearance_FRS_BACKGROUND, ChangeAppearance_NUM_DECKS, ChangeAppearance_FRS_DECK, ChangeAppearance_deckNumber, ChangeAppearance_NUM_BACKGROUNDS, ChangeAppearance_exited, ChangeAppearance_backgrounds, ChangeAppearance_decks}

# ChangeOptions class attributes and methods
ChangeOptions_ok: Property = Property(name="ok", type=StringType)
ChangeOptions_exited: Property = Property(name="exited", type=BooleanType)
ChangeOptions_drawCount: Property = Property(name="drawCount", type=IntegerType)
ChangeOptions_drawOne: Property = Property(name="drawOne", type=StringType)
ChangeOptions_drawThree: Property = Property(name="drawThree", type=StringType)
ChangeOptions_timerCheck: Property = Property(name="timerCheck", type=StringType)
ChangeOptions_timer: Property = Property(name="timer", type=IntegerType)
ChangeOptions_winAnimationCheck: Property = Property(name="winAnimationCheck", type=StringType)
ChangeOptions_animation: Property = Property(name="animation", type=IntegerType)
ChangeOptions_winSoundsCheck: Property = Property(name="winSoundsCheck", type=StringType)
ChangeOptions_sounds: Property = Property(name="sounds", type=IntegerType)
ChangeOptions_difficulty: Property = Property(name="difficulty", type=IntegerType)
ChangeOptions_easy: Property = Property(name="easy", type=StringType)
ChangeOptions_medium: Property = Property(name="medium", type=StringType)
ChangeOptions_hard: Property = Property(name="hard", type=StringType)
ChangeOptions.attributes={ChangeOptions_sounds, ChangeOptions_hard, ChangeOptions_timer, ChangeOptions_winSoundsCheck, ChangeOptions_exited, ChangeOptions_easy, ChangeOptions_animation, ChangeOptions_winAnimationCheck, ChangeOptions_difficulty, ChangeOptions_ok, ChangeOptions_timerCheck, ChangeOptions_medium, ChangeOptions_drawOne, ChangeOptions_drawCount, ChangeOptions_drawThree}

# Column class attributes and methods

# DealDeck class attributes and methods
DealDeck_numTimesThroughDeck: Property = Property(name="numTimesThroughDeck", type=IntegerType)
DealDeck_drawCount: Property = Property(name="drawCount", type=IntegerType)
DealDeck_difficulty: Property = Property(name="difficulty", type=IntegerType)
DealDeck_DRAW_ONE_THROUGH_LIMIT: Property = Property(name="DRAW_ONE_THROUGH_LIMIT", type=IntegerType)
DealDeck_DRAW_THREE_THROUGH_LIMIT: Property = Property(name="DRAW_THREE_THROUGH_LIMIT", type=IntegerType)
DealDeck_EASY_THROUGH_LIMIT: Property = Property(name="EASY_THROUGH_LIMIT", type=IntegerType)
DealDeck_MEDIUM_THROUGH_LIMIT: Property = Property(name="MEDIUM_THROUGH_LIMIT", type=IntegerType)
DealDeck_HARD_THROUGH_LIMIT: Property = Property(name="HARD_THROUGH_LIMIT", type=IntegerType)
DealDeck_deckThroughLimit: Property = Property(name="deckThroughLimit", type=IntegerType)
DealDeck_redealable: Property = Property(name="redealable", type=BooleanType)
DealDeck.attributes={DealDeck_DRAW_THREE_THROUGH_LIMIT, DealDeck_deckThroughLimit, DealDeck_HARD_THROUGH_LIMIT, DealDeck_drawCount, DealDeck_redealable, DealDeck_DRAW_ONE_THROUGH_LIMIT, DealDeck_MEDIUM_THROUGH_LIMIT, DealDeck_difficulty, DealDeck_EASY_THROUGH_LIMIT, DealDeck_numTimesThroughDeck}

# Deck class attributes and methods
Deck_deckNumber: Property = Property(name="deckNumber", type=IntegerType)
Deck.attributes={Deck_deckNumber}

# DiscardPile class attributes and methods
DiscardPile_drawCount: Property = Property(name="drawCount", type=IntegerType)
DiscardPile_cardsLeftFromDraw: Property = Property(name="cardsLeftFromDraw", type=IntegerType)
DiscardPile.attributes={DiscardPile_drawCount, DiscardPile_cardsLeftFromDraw}

# FireworksDisplay class attributes and methods
FireworksDisplay_NUM_FIREWORKS: Property = Property(name="NUM_FIREWORKS", type=IntegerType)
FireworksDisplay_FIREWORKS_SIZE: Property = Property(name="FIREWORKS_SIZE", type=IntegerType)
FireworksDisplay_SET_DELAY: Property = Property(name="SET_DELAY", type=IntegerType)
FireworksDisplay_FIREWORKS_TIME: Property = Property(name="FIREWORKS_TIME", type=IntegerType)
FireworksDisplay_x: Property = Property(name="x", type=StringType)
FireworksDisplay_y: Property = Property(name="y", type=StringType)
FireworksDisplay_colors: Property = Property(name="colors", type=StringType)
FireworksDisplay_xx: Property = Property(name="xx", type=StringType)
FireworksDisplay_yy: Property = Property(name="yy", type=StringType)
FireworksDisplay_num: Property = Property(name="num", type=IntegerType)
FireworksDisplay_numSets: Property = Property(name="numSets", type=IntegerType)
FireworksDisplay_startValue: Property = Property(name="startValue", type=IntegerType)
FireworksDisplay_timer: Property = Property(name="timer", type=StringType)
FireworksDisplay_random: Property = Property(name="random", type=StringType)
FireworksDisplay.attributes={FireworksDisplay_SET_DELAY, FireworksDisplay_num, FireworksDisplay_colors, FireworksDisplay_timer, FireworksDisplay_FIREWORKS_SIZE, FireworksDisplay_random, FireworksDisplay_xx, FireworksDisplay_x, FireworksDisplay_NUM_FIREWORKS, FireworksDisplay_numSets, FireworksDisplay_startValue, FireworksDisplay_y, FireworksDisplay_yy, FireworksDisplay_FIREWORKS_TIME}

# FourRowSolitaire class attributes and methods
FourRowSolitaire_version: Property = Property(name="version", type=AcePile)
FourRowSolitaire_menuBar: Property = Property(name="menuBar", type=StringType)
FourRowSolitaire_game: Property = Property(name="game", type=StringType)
FourRowSolitaire_helpMenu: Property = Property(name="helpMenu", type=StringType)
FourRowSolitaire_newGame: Property = Property(name="newGame", type=StringType)
FourRowSolitaire_undo: Property = Property(name="undo", type=StringType)
FourRowSolitaire_hint: Property = Property(name="hint", type=StringType)
FourRowSolitaire_statistics: Property = Property(name="statistics", type=StringType)
FourRowSolitaire_options: Property = Property(name="options", type=StringType)
FourRowSolitaire_appearance: Property = Property(name="appearance", type=StringType)
FourRowSolitaire_exit: Property = Property(name="exit", type=StringType)
FourRowSolitaire_help: Property = Property(name="help", type=StringType)
FourRowSolitaire_about: Property = Property(name="about", type=StringType)
FourRowSolitaire_checkUpdate: Property = Property(name="checkUpdate", type=StringType)
FourRowSolitaire.attributes={FourRowSolitaire_statistics, FourRowSolitaire_help, FourRowSolitaire_menuBar, FourRowSolitaire_about, FourRowSolitaire_exit, FourRowSolitaire_checkUpdate, FourRowSolitaire_options, FourRowSolitaire_hint, FourRowSolitaire_appearance, FourRowSolitaire_version, FourRowSolitaire_helpMenu, FourRowSolitaire_game, FourRowSolitaire_newGame, FourRowSolitaire_undo}

# SingleCell class attributes and methods

# SolitaireBoard class attributes and methods
SolitaireBoard_GAME_WON: Property = Property(name="GAME_WON", type=IntegerType)
SolitaireBoard_GAME_LOST: Property = Property(name="GAME_LOST", type=IntegerType)
SolitaireBoard_RESET_STATS: Property = Property(name="RESET_STATS", type=IntegerType)
SolitaireBoard_DO_NOTHING: Property = Property(name="DO_NOTHING", type=IntegerType)
SolitaireBoard_GAME_SAVED: Property = Property(name="GAME_SAVED", type=IntegerType)
SolitaireBoard_drawCount: Property = Property(name="drawCount", type=IntegerType)
SolitaireBoard_newDrawCount: Property = Property(name="newDrawCount", type=IntegerType)
SolitaireBoard_backgroundNumber: Property = Property(name="backgroundNumber", type=IntegerType)
SolitaireBoard_deckNumber: Property = Property(name="deckNumber", type=IntegerType)
SolitaireBoard_timer: Property = Property(name="timer", type=StringType)
SolitaireBoard_statusBar: Property = Property(name="statusBar", type=StringType)
SolitaireBoard_timerLabel: Property = Property(name="timerLabel", type=StringType)
SolitaireBoard_timerCount: Property = Property(name="timerCount", type=IntegerType)
SolitaireBoard_timerToRunNextGame: Property = Property(name="timerToRunNextGame", type=IntegerType)
SolitaireBoard_timerToRun: Property = Property(name="timerToRun", type=BooleanType)
SolitaireBoard_winAnimationStatus: Property = Property(name="winAnimationStatus", type=IntegerType)
SolitaireBoard_winSoundsStatus: Property = Property(name="winSoundsStatus", type=IntegerType)
SolitaireBoard_difficulty: Property = Property(name="difficulty", type=IntegerType)
SolitaireBoard_newDifficulty: Property = Property(name="newDifficulty", type=IntegerType)
SolitaireBoard_numCards: Property = Property(name="numCards", type=StringType)
SolitaireBoard_numCardsInDiscardView: Property = Property(name="numCardsInDiscardView", type=StringType)
SolitaireBoard.attributes={SolitaireBoard_RESET_STATS, SolitaireBoard_GAME_WON, SolitaireBoard_timerCount, SolitaireBoard_deckNumber, SolitaireBoard_numCardsInDiscardView, SolitaireBoard_timerToRun, SolitaireBoard_GAME_LOST, SolitaireBoard_statusBar, SolitaireBoard_difficulty, SolitaireBoard_timerToRunNextGame, SolitaireBoard_newDrawCount, SolitaireBoard_GAME_SAVED, SolitaireBoard_newDifficulty, SolitaireBoard_winAnimationStatus, SolitaireBoard_drawCount, SolitaireBoard_timerLabel, SolitaireBoard_backgroundNumber, SolitaireBoard_timer, SolitaireBoard_winSoundsStatus, SolitaireBoard_numCards, SolitaireBoard_DO_NOTHING}

# SolitaireLayout class attributes and methods
SolitaireLayout_COLUMEN_ONE: Property = Property(name="COLUMEN_ONE", type=StringType)
SolitaireLayout_COLUMN_TWO: Property = Property(name="COLUMN_TWO", type=StringType)
SolitaireLayout_COLUMN_THREE: Property = Property(name="COLUMN_THREE", type=StringType)
SolitaireLayout_COLUMN_FOUR: Property = Property(name="COLUMN_FOUR", type=StringType)
SolitaireLayout_SPADES_ACE_PILE: Property = Property(name="SPADES_ACE_PILE", type=StringType)
SolitaireLayout_CLUBS_ACE_PILE: Property = Property(name="CLUBS_ACE_PILE", type=StringType)
SolitaireLayout_DIAMONDS_ACE_PILE: Property = Property(name="DIAMONDS_ACE_PILE", type=StringType)
SolitaireLayout_HEARTS_ACE_PILE: Property = Property(name="HEARTS_ACE_PILE", type=StringType)
SolitaireLayout_DISCARD_PILE: Property = Property(name="DISCARD_PILE", type=StringType)
SolitaireLayout_DECK: Property = Property(name="DECK", type=StringType)
SolitaireLayout_CELL_ONE: Property = Property(name="CELL_ONE", type=StringType)
SolitaireLayout_CELL_TWO: Property = Property(name="CELL_TWO", type=StringType)
SolitaireLayout_CELL_THREE: Property = Property(name="CELL_THREE", type=StringType)
SolitaireLayout_CELL_FOUR: Property = Property(name="CELL_FOUR", type=StringType)
SolitaireLayout_colOne: Property = Property(name="colOne", type=StringType)
SolitaireLayout_colTwo: Property = Property(name="colTwo", type=StringType)
SolitaireLayout_colThree: Property = Property(name="colThree", type=StringType)
SolitaireLayout_colFour: Property = Property(name="colFour", type=StringType)
SolitaireLayout_aceSpades: Property = Property(name="aceSpades", type=StringType)
SolitaireLayout_aceClubs: Property = Property(name="aceClubs", type=StringType)
SolitaireLayout_aceDiamonds: Property = Property(name="aceDiamonds", type=StringType)
SolitaireLayout_aceHearts: Property = Property(name="aceHearts", type=StringType)
SolitaireLayout_discardPile: Property = Property(name="discardPile", type=StringType)
SolitaireLayout_deck: Property = Property(name="deck", type=StringType)
SolitaireLayout_cellOne: Property = Property(name="cellOne", type=StringType)
SolitaireLayout_cellTwo: Property = Property(name="cellTwo", type=StringType)
SolitaireLayout_cellThree: Property = Property(name="cellThree", type=StringType)
SolitaireLayout_cellFour: Property = Property(name="cellFour", type=StringType)
SolitaireLayout.attributes={SolitaireLayout_DECK, SolitaireLayout_DIAMONDS_ACE_PILE, SolitaireLayout_cellTwo, SolitaireLayout_COLUMEN_ONE, SolitaireLayout_CELL_FOUR, SolitaireLayout_cellFour, SolitaireLayout_aceClubs, SolitaireLayout_aceDiamonds, SolitaireLayout_CELL_TWO, SolitaireLayout_CELL_ONE, SolitaireLayout_SPADES_ACE_PILE, SolitaireLayout_COLUMN_THREE, SolitaireLayout_cellThree, SolitaireLayout_colFour, SolitaireLayout_cellOne, SolitaireLayout_discardPile, SolitaireLayout_COLUMN_FOUR, SolitaireLayout_HEARTS_ACE_PILE, SolitaireLayout_CELL_THREE, SolitaireLayout_colThree, SolitaireLayout_aceHearts, SolitaireLayout_DISCARD_PILE, SolitaireLayout_CLUBS_ACE_PILE, SolitaireLayout_colTwo, SolitaireLayout_deck, SolitaireLayout_COLUMN_TWO, SolitaireLayout_aceSpades, SolitaireLayout_colOne}

# SolitairePanel class attributes and methods
SolitairePanel_backgroundNumber: Property = Property(name="backgroundNumber", type=IntegerType)
SolitairePanel_background: Property = Property(name="background", type=StringType)
SolitairePanel.attributes={SolitairePanel_backgroundNumber, SolitairePanel_background}

# WinScreen class attributes and methods

# Graphics class attributes and methods

# ActionEvent class attributes and methods

# Relationships
SolitaireBoard_SolitairePanel: BinaryAssociation = BinaryAssociation(
    name="SolitaireBoard_SolitairePanel",
    ends={
        Property(name="solitairePanel0", type=SolitairePanel, multiplicity=Multiplicity(0, 1)),
        Property(name="solitaireBoard1", type=SolitaireBoard, multiplicity=Multiplicity(1, 1))
    }
)
SolitaireBoard_Deck: BinaryAssociation = BinaryAssociation(
    name="SolitaireBoard_Deck",
    ends={
        Property(name="deck2", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="solitaireBoard3", type=SolitaireBoard, multiplicity=Multiplicity(1, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card4", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="deck5", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
SolitaireBoard_AcePile: BinaryAssociation = BinaryAssociation(
    name="SolitaireBoard_AcePile",
    ends={
        Property(name="acePile6", type=AcePile, multiplicity=Multiplicity(0, 9999)),
        Property(name="solitaireBoard7", type=SolitaireBoard, multiplicity=Multiplicity(1, 1))
    }
)
SolitaireBoard_CardStack: BinaryAssociation = BinaryAssociation(
    name="SolitaireBoard_CardStack",
    ends={
        Property(name="cardStack8", type=CardStack, multiplicity=Multiplicity(0, 9999)),
        Property(name="solitaireBoard9", type=SolitaireBoard, multiplicity=Multiplicity(1, 1))
    }
)
CardStack_Card: BinaryAssociation = BinaryAssociation(
    name="CardStack_Card",
    ends={
        Property(name="card10", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="cardStack11", type=CardStack, multiplicity=Multiplicity(0, 1))
    }
)
DealDeck_DiscardPile: BinaryAssociation = BinaryAssociation(
    name="DealDeck_DiscardPile",
    ends={
        Property(name="discardPile12", type=DiscardPile, multiplicity=Multiplicity(0, 1)),
        Property(name="dealDeck13", type=DealDeck, multiplicity=Multiplicity(0, 1))
    }
)
SolitaireBoard_DiscardPile: BinaryAssociation = BinaryAssociation(
    name="SolitaireBoard_DiscardPile",
    ends={
        Property(name="discardPile14", type=DiscardPile, multiplicity=Multiplicity(0, 1)),
        Property(name="solitaireBoard15", type=SolitaireBoard, multiplicity=Multiplicity(1, 1))
    }
)
SolitaireBoard_SingleCell: BinaryAssociation = BinaryAssociation(
    name="SolitaireBoard_SingleCell",
    ends={
        Property(name="singleCell16", type=SingleCell, multiplicity=Multiplicity(0, 9999)),
        Property(name="solitaireBoard17", type=SolitaireBoard, multiplicity=Multiplicity(1, 1))
    }
)
SolitaireBoard_Column: BinaryAssociation = BinaryAssociation(
    name="SolitaireBoard_Column",
    ends={
        Property(name="column18", type=Column, multiplicity=Multiplicity(0, 9999)),
        Property(name="solitaireBoard19", type=SolitaireBoard, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7fc9b898_2499_4c6d_9c0f_b4cd417df6c1",
    types={AcePile, Card, CardStack, ChangeAppearance, ChangeOptions, Column, DealDeck, Deck, DiscardPile, FireworksDisplay, FourRowSolitaire, SingleCell, SolitaireBoard, SolitaireLayout, SolitairePanel, WinScreen, Graphics, ActionEvent},
    associations={SolitaireBoard_SolitairePanel, SolitaireBoard_Deck, Deck_Card, SolitaireBoard_AcePile, SolitaireBoard_CardStack, CardStack_Card, DealDeck_DiscardPile, SolitaireBoard_DiscardPile, SolitaireBoard_SingleCell, SolitaireBoard_Column},
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