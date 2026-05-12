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
User_Actor = Class(name="User_Actor")
Four_Row_Solitaire___Component = Class(name="Four_Row_Solitaire___Component")
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
MyMouseListener = Class(name="MyMouseListener")
TimerListener = Class(name="TimerListener")
windowclosing = Class(name="windowclosing")
SolitaireLayout = Class(name="SolitaireLayout")
SolitairePanel = Class(name="SolitairePanel")
WinScreen = Class(name="WinScreen")
SoundThread = Class(name="SoundThread")
Main_Game_Board_external = Class(name="Main_Game_Board_external")
Game_external = Class(name="Game_external")
Help_external = Class(name="Help_external")

# User_Actor class attributes and methods

# Four_Row_Solitaire___Component class attributes and methods

# AcePile class attributes and methods
AcePile_suit: Property = Property(name="suit", type=StringType)
AcePile.attributes={AcePile_suit}

# Card class attributes and methods
Card_SPADES_SUIT: Property = Property(name="SPADES_SUIT", type=StringType)
Card_CLUBS_SUIT: Property = Property(name="CLUBS_SUIT", type=StringType)
Card_HEARTS_SUIT: Property = Property(name="HEARTS_SUIT", type=StringType)
Card_DIAMONDS_SUIT: Property = Property(name="DIAMONDS_SUIT", type=StringType)
Card_INVALID_SUIT: Property = Property(name="INVALID_SUIT", type=StringType)
Card_ACE: Property = Property(name="ACE", type=StringType)
Card_TWO: Property = Property(name="TWO", type=StringType)
Card_THREE: Property = Property(name="THREE", type=StringType)
Card_FOUR: Property = Property(name="FOUR", type=StringType)
Card_FIVE: Property = Property(name="FIVE", type=StringType)
Card_SIX: Property = Property(name="SIX", type=StringType)
Card_SEVEN: Property = Property(name="SEVEN", type=StringType)
Card_EIGHT: Property = Property(name="EIGHT", type=StringType)
Card_NINE: Property = Property(name="NINE", type=StringType)
Card_TEN: Property = Property(name="TEN", type=StringType)
Card_JACK: Property = Property(name="JACK", type=StringType)
Card_QUEEN: Property = Property(name="QUEEN", type=StringType)
Card_KING: Property = Property(name="KING", type=StringType)
Card_INVALID_NUMBER: Property = Property(name="INVALID_NUMBER", type=StringType)
Card_cardSuit: Property = Property(name="cardSuit", type=StringType)
Card_cardNumber: Property = Property(name="cardNumber", type=StringType)
Card_fullCardNumber: Property = Property(name="fullCardNumber", type=StringType)
Card_cardColor: Property = Property(name="cardColor", type=StringType)
Card_int_deckNumber: Property = Property(name="int_deckNumber", type=StringType)
Card_image: Property = Property(name="image", type=StringType)
Card_cardBack: Property = Property(name="cardBack", type=StringType)
Card_cardImageString: Property = Property(name="cardImageString", type=StringType)
Card_cardHighLighted: Property = Property(name="cardHighLighted", type=StringType)
Card_faceUp: Property = Property(name="faceUp", type=BooleanType)
Card_highlighted: Property = Property(name="highlighted", type=BooleanType)
Card_location: Property = Property(name="location", type=StringType)
Card.attributes={Card_fullCardNumber, Card_TEN, Card_CLUBS_SUIT, Card_TWO, Card_SIX, Card_FIVE, Card_ACE, Card_JACK, Card_QUEEN, Card_cardNumber, Card_INVALID_SUIT, Card_int_deckNumber, Card_cardHighLighted, Card_SEVEN, Card_location, Card_cardImageString, Card_FOUR, Card_highlighted, Card_EIGHT, Card_NINE, Card_cardSuit, Card_INVALID_NUMBER, Card_image, Card_HEARTS_SUIT, Card_THREE, Card_faceUp, Card_SPADES_SUIT, Card_DIAMONDS_SUIT, Card_cardColor, Card_KING, Card_cardBack}

# CardStack class attributes and methods
CardStack_cards: Property = Property(name="cards", type=StringType)
CardStack.attributes={CardStack_cards}

# ChangeAppearance class attributes and methods
ChangeAppearance_cardBackLabel: Property = Property(name="cardBackLabel", type=StringType)
ChangeAppearance_backGroundLabel: Property = Property(name="backGroundLabel", type=StringType)
ChangeAppearance_NUM_DECKS: Property = Property(name="NUM_DECKS", type=StringType)
ChangeAppearance_NUM_BACKGROUNDS: Property = Property(name="NUM_BACKGROUNDS", type=StringType)
ChangeAppearance_FRS_DECK: Property = Property(name="FRS_DECK", type=StringType)
ChangeAppearance_FRS_BACKGROUND: Property = Property(name="FRS_BACKGROUND", type=StringType)
ChangeAppearance_decks: Property = Property(name="decks", type=StringType)
ChangeAppearance_backgrounds: Property = Property(name="backgrounds", type=StringType)
ChangeAppearance_ok: Property = Property(name="ok", type=StringType)
ChangeAppearance_deckNumber: Property = Property(name="deckNumber", type=StringType)
ChangeAppearance_backgroundNumber: Property = Property(name="backgroundNumber", type=StringType)
ChangeAppearance_exited: Property = Property(name="exited", type=BooleanType)
ChangeAppearance.attributes={ChangeAppearance_backGroundLabel, ChangeAppearance_NUM_DECKS, ChangeAppearance_NUM_BACKGROUNDS, ChangeAppearance_FRS_BACKGROUND, ChangeAppearance_ok, ChangeAppearance_backgrounds, ChangeAppearance_exited, ChangeAppearance_cardBackLabel, ChangeAppearance_deckNumber, ChangeAppearance_FRS_DECK, ChangeAppearance_backgroundNumber, ChangeAppearance_decks}

# ChangeOptions class attributes and methods
ChangeOptions_drawCount: Property = Property(name="drawCount", type=StringType)
ChangeOptions_drawOne: Property = Property(name="drawOne", type=StringType)
ChangeOptions_drawThree: Property = Property(name="drawThree", type=StringType)
ChangeOptions_timerCheck: Property = Property(name="timerCheck", type=StringType)
ChangeOptions_timer: Property = Property(name="timer", type=StringType)
ChangeOptions_winAnimationCheck: Property = Property(name="winAnimationCheck", type=StringType)
ChangeOptions_animation: Property = Property(name="animation", type=StringType)
ChangeOptions_winSoundCheck: Property = Property(name="winSoundCheck", type=StringType)
ChangeOptions_sounds: Property = Property(name="sounds", type=StringType)
ChangeOptions_difficulty: Property = Property(name="difficulty", type=StringType)
ChangeOptions_easy: Property = Property(name="easy", type=StringType)
ChangeOptions_medium: Property = Property(name="medium", type=StringType)
ChangeOptions_hard: Property = Property(name="hard", type=StringType)
ChangeOptions_ok: Property = Property(name="ok", type=StringType)
ChangeOptions_exited: Property = Property(name="exited", type=BooleanType)
ChangeOptions.attributes={ChangeOptions_sounds, ChangeOptions_drawCount, ChangeOptions_timerCheck, ChangeOptions_exited, ChangeOptions_drawOne, ChangeOptions_winSoundCheck, ChangeOptions_difficulty, ChangeOptions_animation, ChangeOptions_drawThree, ChangeOptions_timer, ChangeOptions_easy, ChangeOptions_hard, ChangeOptions_ok, ChangeOptions_medium, ChangeOptions_winAnimationCheck}

# Column class attributes and methods

# DealDeck class attributes and methods
DealDeck_discardPile: Property = Property(name="discardPile", type=StringType)
DealDeck_numTimesThroughDeck: Property = Property(name="numTimesThroughDeck", type=StringType)
DealDeck_drawCount: Property = Property(name="drawCount", type=StringType)
DealDeck_difficulty: Property = Property(name="difficulty", type=StringType)
DealDeck_DRAW_ONE_THROUGH_LIMIT: Property = Property(name="DRAW_ONE_THROUGH_LIMIT", type=StringType)
DealDeck_DRAW_THREE_THROUGH_LIMIT: Property = Property(name="DRAW_THREE_THROUGH_LIMIT", type=StringType)
DealDeck_EASY_THROUGH_LIMIT: Property = Property(name="EASY_THROUGH_LIMIT", type=StringType)
DealDeck_MEDIUM_THROUGH_LIMIT: Property = Property(name="MEDIUM_THROUGH_LIMIT", type=StringType)
DealDeck_HARD_THROUGH_LIMIT: Property = Property(name="HARD_THROUGH_LIMIT", type=StringType)
DealDeck_deckThroughLimit: Property = Property(name="deckThroughLimit", type=StringType)
DealDeck_redealable: Property = Property(name="redealable", type=BooleanType)
DealDeck.attributes={DealDeck_difficulty, DealDeck_DRAW_ONE_THROUGH_LIMIT, DealDeck_MEDIUM_THROUGH_LIMIT, DealDeck_drawCount, DealDeck_discardPile, DealDeck_DRAW_THREE_THROUGH_LIMIT, DealDeck_HARD_THROUGH_LIMIT, DealDeck_deckThroughLimit, DealDeck_redealable, DealDeck_numTimesThroughDeck, DealDeck_EASY_THROUGH_LIMIT}

# Deck class attributes and methods
Deck_deckNumber: Property = Property(name="deckNumber", type=StringType)
Deck_deck: Property = Property(name="deck", type=StringType)
Deck.attributes={Deck_deckNumber, Deck_deck}

# DiscardPile class attributes and methods
DiscardPile_drawCount: Property = Property(name="drawCount", type=StringType)
DiscardPile_CardsLeftFromDraw: Property = Property(name="CardsLeftFromDraw", type=StringType)
DiscardPile.attributes={DiscardPile_drawCount, DiscardPile_CardsLeftFromDraw}

# FireworksDisplay class attributes and methods
FireworksDisplay_x: Property = Property(name="x", type=StringType)
FireworksDisplay_y: Property = Property(name="y", type=StringType)
FireworksDisplay_colors: Property = Property(name="colors", type=StringType)
FireworksDisplay_xx: Property = Property(name="xx", type=StringType)
FireworksDisplay_yy: Property = Property(name="yy", type=StringType)
FireworksDisplay_num: Property = Property(name="num", type=StringType)
FireworksDisplay_numSets: Property = Property(name="numSets", type=StringType)
FireworksDisplay_startValue: Property = Property(name="startValue", type=StringType)
FireworksDisplay_time: Property = Property(name="time", type=StringType)
FireworksDisplay_random: Property = Property(name="random", type=StringType)
FireworksDisplay_NUM_FIREWORKS: Property = Property(name="NUM_FIREWORKS", type=StringType)
FireworksDisplay_FIREWORKS_SIZE: Property = Property(name="FIREWORKS_SIZE", type=StringType)
FireworksDisplay_SET_DELAY: Property = Property(name="SET_DELAY", type=StringType)
FireworksDisplay_FIREWORKS_TIME: Property = Property(name="FIREWORKS_TIME", type=StringType)
FireworksDisplay.attributes={FireworksDisplay_y, FireworksDisplay_SET_DELAY, FireworksDisplay_yy, FireworksDisplay_NUM_FIREWORKS, FireworksDisplay_numSets, FireworksDisplay_startValue, FireworksDisplay_random, FireworksDisplay_FIREWORKS_TIME, FireworksDisplay_FIREWORKS_SIZE, FireworksDisplay_time, FireworksDisplay_xx, FireworksDisplay_colors, FireworksDisplay_num, FireworksDisplay_x}

# FourRowSolitaire class attributes and methods
FourRowSolitaire_version: Property = Property(name="version", type=StringType)
FourRowSolitaire_menubar: Property = Property(name="menubar", type=StringType)
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
FourRowSolitaire.attributes={FourRowSolitaire_help, FourRowSolitaire_exit, FourRowSolitaire_hint, FourRowSolitaire_statistics, FourRowSolitaire_appearance, FourRowSolitaire_about, FourRowSolitaire_menubar, FourRowSolitaire_checkUpdate, FourRowSolitaire_version, FourRowSolitaire_helpMenu, FourRowSolitaire_options, FourRowSolitaire_newGame, FourRowSolitaire_undo, FourRowSolitaire_game}

# SingleCell class attributes and methods

# SolitaireBoard class attributes and methods
SolitaireBoard_acePiles: Property = Property(name="acePiles", type=StringType)
SolitaireBoard_cells: Property = Property(name="cells", type=StringType)
SolitaireBoard_mainPanel: Property = Property(name="mainPanel", type=StringType)
SolitaireBoard_ml: Property = Property(name="ml", type=StringType)
SolitaireBoard_wl: Property = Property(name="wl", type=StringType)
SolitaireBoard_timer: Property = Property(name="timer", type=StringType)
SolitaireBoard_statusBar: Property = Property(name="statusBar", type=StringType)
SolitaireBoard_timerLabel: Property = Property(name="timerLabel", type=StringType)
SolitaireBoard_timerCount: Property = Property(name="timerCount", type=StringType)
SolitaireBoard_timerToRunNextGame: Property = Property(name="timerToRunNextGame", type=StringType)
SolitaireBoard_timerToRun: Property = Property(name="timerToRun", type=BooleanType)
SolitaireBoard_winAnimationStatus: Property = Property(name="winAnimationStatus", type=StringType)
SolitaireBoard_newDifficulty: Property = Property(name="newDifficulty", type=StringType)
SolitaireBoard_sourceList: Property = Property(name="sourceList", type=StringType)
SolitaireBoard_destinationList: Property = Property(name="destinationList", type=StringType)
SolitaireBoard_numCards: Property = Property(name="numCards", type=StringType)
SolitaireBoard_numCardsInDiscardView: Property = Property(name="numCardsInDiscardView", type=StringType)
SolitaireBoard_GAME_WON: Property = Property(name="GAME_WON", type=StringType)
SolitaireBoard_GAME_LOST: Property = Property(name="GAME_LOST", type=StringType)
SolitaireBoard_RESET_STATS: Property = Property(name="RESET_STATS", type=StringType)
SolitaireBoard_DO_NOTHING: Property = Property(name="DO_NOTHING", type=StringType)
SolitaireBoard_GAME_SAVED: Property = Property(name="GAME_SAVED", type=StringType)
SolitaireBoard_drawCount: Property = Property(name="drawCount", type=StringType)
SolitaireBoard_newDrawCount: Property = Property(name="newDrawCount", type=StringType)
SolitaireBoard_backgroundNumber: Property = Property(name="backgroundNumber", type=StringType)
SolitaireBoard_deckNumber: Property = Property(name="deckNumber", type=StringType)
SolitaireBoard_deck: Property = Property(name="deck", type=Deck)
SolitaireBoard_columns: Property = Property(name="columns", type=StringType)
SolitaireBoard_discardPile: Property = Property(name="discardPile", type=StringType)
SolitaireBoard_dealDeck: Property = Property(name="dealDeck", type=DealDeck)
SolitaireBoard.attributes={SolitaireBoard_dealDeck, SolitaireBoard_winAnimationStatus, SolitaireBoard_cells, SolitaireBoard_destinationList, SolitaireBoard_numCardsInDiscardView, SolitaireBoard_deckNumber, SolitaireBoard_acePiles, SolitaireBoard_mainPanel, SolitaireBoard_wl, SolitaireBoard_GAME_LOST, SolitaireBoard_timerToRun, SolitaireBoard_GAME_WON, SolitaireBoard_numCards, SolitaireBoard_timerToRunNextGame, SolitaireBoard_timerLabel, SolitaireBoard_DO_NOTHING, SolitaireBoard_deck, SolitaireBoard_sourceList, SolitaireBoard_backgroundNumber, SolitaireBoard_ml, SolitaireBoard_statusBar, SolitaireBoard_discardPile, SolitaireBoard_drawCount, SolitaireBoard_timerCount, SolitaireBoard_newDrawCount, SolitaireBoard_timer, SolitaireBoard_newDifficulty, SolitaireBoard_columns, SolitaireBoard_GAME_SAVED, SolitaireBoard_RESET_STATS}

# MyMouseListener class attributes and methods
MyMouseListener_hasSelected: Property = Property(name="hasSelected", type=BooleanType)
MyMouseListener_singleCardSelected: Property = Property(name="singleCardSelected", type=BooleanType)
MyMouseListener_clickedCard: Property = Property(name="clickedCard", type=StringType)
MyMouseListener_source: Property = Property(name="source", type=StringType)
MyMouseListener_destination: Property = Property(name="destination", type=StringType)
MyMouseListener_temp: Property = Property(name="temp", type=StringType)
MyMouseListener_tempCard: Property = Property(name="tempCard", type=StringType)
MyMouseListener_rightClicked: Property = Property(name="rightClicked", type=BooleanType)
MyMouseListener.attributes={MyMouseListener_temp, MyMouseListener_rightClicked, MyMouseListener_source, MyMouseListener_clickedCard, MyMouseListener_tempCard, MyMouseListener_destination, MyMouseListener_hasSelected, MyMouseListener_singleCardSelected}

# TimerListener class attributes and methods

# windowclosing class attributes and methods

# SolitaireLayout class attributes and methods
SolitaireLayout_COLUMN_ONE: Property = Property(name="COLUMN_ONE", type=StringType)
SolitaireLayout_COLUMN_TWO: Property = Property(name="COLUMN_TWO", type=StringType)
SolitaireLayout_COLUMN_THREE: Property = Property(name="COLUMN_THREE", type=StringType)
SolitaireLayout_COLUMN_FOUR: Property = Property(name="COLUMN_FOUR", type=StringType)
SolitaireLayout_SPADES_ACE_PILE: Property = Property(name="SPADES_ACE_PILE", type=StringType)
SolitaireLayout_deck: Property = Property(name="deck", type=StringType)
SolitaireLayout_cellOne: Property = Property(name="cellOne", type=StringType)
SolitaireLayout_cellTwo: Property = Property(name="cellTwo", type=StringType)
SolitaireLayout_cellThree: Property = Property(name="cellThree", type=StringType)
SolitaireLayout_cellFour: Property = Property(name="cellFour", type=StringType)
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
SolitaireLayout_ColTwo: Property = Property(name="ColTwo", type=StringType)
SolitaireLayout_ColThree: Property = Property(name="ColThree", type=StringType)
SolitaireLayout_ColFour: Property = Property(name="ColFour", type=StringType)
SolitaireLayout_acespades: Property = Property(name="acespades", type=StringType)
SolitaireLayout_aceClubs: Property = Property(name="aceClubs", type=StringType)
SolitaireLayout_aceDiamonds: Property = Property(name="aceDiamonds", type=StringType)
SolitaireLayout_aceHearts: Property = Property(name="aceHearts", type=StringType)
SolitaireLayout_discardPile: Property = Property(name="discardPile", type=StringType)
SolitaireLayout.attributes={SolitaireLayout_COLUMN_TWO, SolitaireLayout_cellTwo, SolitaireLayout_cellThree, SolitaireLayout_COLUMN_FOUR, SolitaireLayout_acespades, SolitaireLayout_cellFour, SolitaireLayout_CLUBS_ACE_PILE, SolitaireLayout_aceHearts, SolitaireLayout_discardPile, SolitaireLayout_CELL_FOUR, SolitaireLayout_ColFour, SolitaireLayout_COLUMN_ONE, SolitaireLayout_colOne, SolitaireLayout_DECK, SolitaireLayout_CELL_TWO, SolitaireLayout_CELL_ONE, SolitaireLayout_ColThree, SolitaireLayout_ColTwo, SolitaireLayout_deck, SolitaireLayout_CELL_THREE, SolitaireLayout_cellOne, SolitaireLayout_DIAMONDS_ACE_PILE, SolitaireLayout_HEARTS_ACE_PILE, SolitaireLayout_COLUMN_THREE, SolitaireLayout_aceClubs, SolitaireLayout_DISCARD_PILE, SolitaireLayout_SPADES_ACE_PILE, SolitaireLayout_aceDiamonds}

# SolitairePanel class attributes and methods
SolitairePanel_backGroundNumber: Property = Property(name="backGroundNumber", type=StringType)
SolitairePanel_background: Property = Property(name="background", type=StringType)
SolitairePanel.attributes={SolitairePanel_backGroundNumber, SolitairePanel_background}

# WinScreen class attributes and methods
WinScreen_sound: Property = Property(name="sound", type=StringType)
WinScreen.attributes={WinScreen_sound}

# SoundThread class attributes and methods
SoundThread_sequencer: Property = Property(name="sequencer", type=StringType)
SoundThread.attributes={SoundThread_sequencer}

# Main_Game_Board_external class attributes and methods

# Game_external class attributes and methods

# Help_external class attributes and methods

# Relationships
User_Main_Game_Board: BinaryAssociation = BinaryAssociation(
    name="User_Main_Game_Board",
    ends={
        Property(name="main_Game_Board0", type=Main_Game_Board_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Game: BinaryAssociation = BinaryAssociation(
    name="User_Game",
    ends={
        Property(name="game2", type=Game_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Help: BinaryAssociation = BinaryAssociation(
    name="User_Help",
    ends={
        Property(name="help4", type=Help_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8a70f32a_16c6_45b2_8ced_9ca375092adf",
    types={User_Actor, Four_Row_Solitaire___Component, AcePile, Card, CardStack, ChangeAppearance, ChangeOptions, Column, DealDeck, Deck, DiscardPile, FireworksDisplay, FourRowSolitaire, SingleCell, SolitaireBoard, MyMouseListener, TimerListener, windowclosing, SolitaireLayout, SolitairePanel, WinScreen, SoundThread, Main_Game_Board_external, Game_external, Help_external},
    associations={User_Main_Game_Board, User_Game, User_Help},
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