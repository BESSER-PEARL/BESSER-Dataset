import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Help_external,
    Game_external,
    Main_Game_Board_external,
    SoundThread,
    WinScreen,
    SolitairePanel,
    SolitaireLayout,
    windowclosing,
    TimerListener,
    MyMouseListener,
    SolitaireBoard,
    SingleCell,
    FourRowSolitaire,
    FireworksDisplay,
    DiscardPile,
    Deck,
    DealDeck,
    Column,
    ChangeOptions,
    ChangeAppearance,
    CardStack,
    Card,
    AcePile,
    Four_Row_Solitaire___Component,
    User_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_help_external_is_not_abstract():
    assert not inspect.isabstract(Help_external)


def test_help_external_constructor_exists():
    assert callable(Help_external.__init__)


def test_help_external_constructor_args():
    sig = inspect.signature(Help_external.__init__)
    params = list(sig.parameters.keys())



def test_game_external_is_not_abstract():
    assert not inspect.isabstract(Game_external)


def test_game_external_constructor_exists():
    assert callable(Game_external.__init__)


def test_game_external_constructor_args():
    sig = inspect.signature(Game_external.__init__)
    params = list(sig.parameters.keys())



def test_main_game_board_external_is_not_abstract():
    assert not inspect.isabstract(Main_Game_Board_external)


def test_main_game_board_external_constructor_exists():
    assert callable(Main_Game_Board_external.__init__)


def test_main_game_board_external_constructor_args():
    sig = inspect.signature(Main_Game_Board_external.__init__)
    params = list(sig.parameters.keys())



def test_soundthread_is_not_abstract():
    assert not inspect.isabstract(SoundThread)


def test_soundthread_constructor_exists():
    assert callable(SoundThread.__init__)


def test_soundthread_constructor_args():
    sig = inspect.signature(SoundThread.__init__)
    params = list(sig.parameters.keys())
    assert "sequencer" in params, "Missing parameter 'sequencer'"

def test_soundthread_has_sequencer():
    assert hasattr(SoundThread, "sequencer")
    descriptor = None
    for klass in SoundThread.__mro__:
        if "sequencer" in klass.__dict__:
            descriptor = klass.__dict__["sequencer"]
            break
    assert isinstance(descriptor, property)



def test_winscreen_is_not_abstract():
    assert not inspect.isabstract(WinScreen)


def test_winscreen_constructor_exists():
    assert callable(WinScreen.__init__)


def test_winscreen_constructor_args():
    sig = inspect.signature(WinScreen.__init__)
    params = list(sig.parameters.keys())
    assert "sound" in params, "Missing parameter 'sound'"

def test_winscreen_has_sound():
    assert hasattr(WinScreen, "sound")
    descriptor = None
    for klass in WinScreen.__mro__:
        if "sound" in klass.__dict__:
            descriptor = klass.__dict__["sound"]
            break
    assert isinstance(descriptor, property)



def test_solitairepanel_is_not_abstract():
    assert not inspect.isabstract(SolitairePanel)


def test_solitairepanel_constructor_exists():
    assert callable(SolitairePanel.__init__)


def test_solitairepanel_constructor_args():
    sig = inspect.signature(SolitairePanel.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "backGroundNumber" in params, "Missing parameter 'backGroundNumber'"

def test_solitairepanel_has_background():
    assert hasattr(SolitairePanel, "background")
    descriptor = None
    for klass in SolitairePanel.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_solitairepanel_has_backGroundNumber():
    assert hasattr(SolitairePanel, "backGroundNumber")
    descriptor = None
    for klass in SolitairePanel.__mro__:
        if "backGroundNumber" in klass.__dict__:
            descriptor = klass.__dict__["backGroundNumber"]
            break
    assert isinstance(descriptor, property)



def test_solitairelayout_is_not_abstract():
    assert not inspect.isabstract(SolitaireLayout)


def test_solitairelayout_constructor_exists():
    assert callable(SolitaireLayout.__init__)


def test_solitairelayout_constructor_args():
    sig = inspect.signature(SolitaireLayout.__init__)
    params = list(sig.parameters.keys())
    assert "COLUMN_TWO" in params, "Missing parameter 'COLUMN_TWO'"
    assert "DECK" in params, "Missing parameter 'DECK'"
    assert "CELL_ONE" in params, "Missing parameter 'CELL_ONE'"
    assert "cellThree" in params, "Missing parameter 'cellThree'"
    assert "CLUBS_ACE_PILE" in params, "Missing parameter 'CLUBS_ACE_PILE'"
    assert "discardPile" in params, "Missing parameter 'discardPile'"
    assert "DISCARD_PILE" in params, "Missing parameter 'DISCARD_PILE'"
    assert "DIAMONDS_ACE_PILE" in params, "Missing parameter 'DIAMONDS_ACE_PILE'"
    assert "colOne" in params, "Missing parameter 'colOne'"
    assert "CELL_THREE" in params, "Missing parameter 'CELL_THREE'"
    assert "aceDiamonds" in params, "Missing parameter 'aceDiamonds'"
    assert "HEARTS_ACE_PILE" in params, "Missing parameter 'HEARTS_ACE_PILE'"
    assert "CELL_FOUR" in params, "Missing parameter 'CELL_FOUR'"
    assert "ColFour" in params, "Missing parameter 'ColFour'"
    assert "acespades" in params, "Missing parameter 'acespades'"
    assert "CELL_TWO" in params, "Missing parameter 'CELL_TWO'"
    assert "aceClubs" in params, "Missing parameter 'aceClubs'"
    assert "COLUMN_FOUR" in params, "Missing parameter 'COLUMN_FOUR'"
    assert "aceHearts" in params, "Missing parameter 'aceHearts'"
    assert "ColTwo" in params, "Missing parameter 'ColTwo'"
    assert "cellTwo" in params, "Missing parameter 'cellTwo'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "COLUMN_ONE" in params, "Missing parameter 'COLUMN_ONE'"
    assert "cellFour" in params, "Missing parameter 'cellFour'"
    assert "SPADES_ACE_PILE" in params, "Missing parameter 'SPADES_ACE_PILE'"
    assert "cellOne" in params, "Missing parameter 'cellOne'"
    assert "COLUMN_THREE" in params, "Missing parameter 'COLUMN_THREE'"
    assert "ColThree" in params, "Missing parameter 'ColThree'"

def test_solitairelayout_has_COLUMN_TWO():
    assert hasattr(SolitaireLayout, "COLUMN_TWO")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "COLUMN_TWO" in klass.__dict__:
            descriptor = klass.__dict__["COLUMN_TWO"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_DECK():
    assert hasattr(SolitaireLayout, "DECK")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "DECK" in klass.__dict__:
            descriptor = klass.__dict__["DECK"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CELL_ONE():
    assert hasattr(SolitaireLayout, "CELL_ONE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CELL_ONE" in klass.__dict__:
            descriptor = klass.__dict__["CELL_ONE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_cellThree():
    assert hasattr(SolitaireLayout, "cellThree")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "cellThree" in klass.__dict__:
            descriptor = klass.__dict__["cellThree"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CLUBS_ACE_PILE():
    assert hasattr(SolitaireLayout, "CLUBS_ACE_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CLUBS_ACE_PILE" in klass.__dict__:
            descriptor = klass.__dict__["CLUBS_ACE_PILE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_discardPile():
    assert hasattr(SolitaireLayout, "discardPile")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "discardPile" in klass.__dict__:
            descriptor = klass.__dict__["discardPile"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_DISCARD_PILE():
    assert hasattr(SolitaireLayout, "DISCARD_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "DISCARD_PILE" in klass.__dict__:
            descriptor = klass.__dict__["DISCARD_PILE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_DIAMONDS_ACE_PILE():
    assert hasattr(SolitaireLayout, "DIAMONDS_ACE_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "DIAMONDS_ACE_PILE" in klass.__dict__:
            descriptor = klass.__dict__["DIAMONDS_ACE_PILE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_colOne():
    assert hasattr(SolitaireLayout, "colOne")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "colOne" in klass.__dict__:
            descriptor = klass.__dict__["colOne"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CELL_THREE():
    assert hasattr(SolitaireLayout, "CELL_THREE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CELL_THREE" in klass.__dict__:
            descriptor = klass.__dict__["CELL_THREE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_aceDiamonds():
    assert hasattr(SolitaireLayout, "aceDiamonds")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "aceDiamonds" in klass.__dict__:
            descriptor = klass.__dict__["aceDiamonds"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_HEARTS_ACE_PILE():
    assert hasattr(SolitaireLayout, "HEARTS_ACE_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "HEARTS_ACE_PILE" in klass.__dict__:
            descriptor = klass.__dict__["HEARTS_ACE_PILE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CELL_FOUR():
    assert hasattr(SolitaireLayout, "CELL_FOUR")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CELL_FOUR" in klass.__dict__:
            descriptor = klass.__dict__["CELL_FOUR"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_ColFour():
    assert hasattr(SolitaireLayout, "ColFour")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "ColFour" in klass.__dict__:
            descriptor = klass.__dict__["ColFour"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_acespades():
    assert hasattr(SolitaireLayout, "acespades")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "acespades" in klass.__dict__:
            descriptor = klass.__dict__["acespades"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_CELL_TWO():
    assert hasattr(SolitaireLayout, "CELL_TWO")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "CELL_TWO" in klass.__dict__:
            descriptor = klass.__dict__["CELL_TWO"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_aceClubs():
    assert hasattr(SolitaireLayout, "aceClubs")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "aceClubs" in klass.__dict__:
            descriptor = klass.__dict__["aceClubs"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_COLUMN_FOUR():
    assert hasattr(SolitaireLayout, "COLUMN_FOUR")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "COLUMN_FOUR" in klass.__dict__:
            descriptor = klass.__dict__["COLUMN_FOUR"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_aceHearts():
    assert hasattr(SolitaireLayout, "aceHearts")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "aceHearts" in klass.__dict__:
            descriptor = klass.__dict__["aceHearts"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_ColTwo():
    assert hasattr(SolitaireLayout, "ColTwo")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "ColTwo" in klass.__dict__:
            descriptor = klass.__dict__["ColTwo"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_cellTwo():
    assert hasattr(SolitaireLayout, "cellTwo")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "cellTwo" in klass.__dict__:
            descriptor = klass.__dict__["cellTwo"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_deck():
    assert hasattr(SolitaireLayout, "deck")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_COLUMN_ONE():
    assert hasattr(SolitaireLayout, "COLUMN_ONE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "COLUMN_ONE" in klass.__dict__:
            descriptor = klass.__dict__["COLUMN_ONE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_cellFour():
    assert hasattr(SolitaireLayout, "cellFour")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "cellFour" in klass.__dict__:
            descriptor = klass.__dict__["cellFour"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_SPADES_ACE_PILE():
    assert hasattr(SolitaireLayout, "SPADES_ACE_PILE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "SPADES_ACE_PILE" in klass.__dict__:
            descriptor = klass.__dict__["SPADES_ACE_PILE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_cellOne():
    assert hasattr(SolitaireLayout, "cellOne")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "cellOne" in klass.__dict__:
            descriptor = klass.__dict__["cellOne"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_COLUMN_THREE():
    assert hasattr(SolitaireLayout, "COLUMN_THREE")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "COLUMN_THREE" in klass.__dict__:
            descriptor = klass.__dict__["COLUMN_THREE"]
            break
    assert isinstance(descriptor, property)

def test_solitairelayout_has_ColThree():
    assert hasattr(SolitaireLayout, "ColThree")
    descriptor = None
    for klass in SolitaireLayout.__mro__:
        if "ColThree" in klass.__dict__:
            descriptor = klass.__dict__["ColThree"]
            break
    assert isinstance(descriptor, property)



def test_windowclosing_is_not_abstract():
    assert not inspect.isabstract(windowclosing)


def test_windowclosing_constructor_exists():
    assert callable(windowclosing.__init__)


def test_windowclosing_constructor_args():
    sig = inspect.signature(windowclosing.__init__)
    params = list(sig.parameters.keys())



def test_timerlistener_is_not_abstract():
    assert not inspect.isabstract(TimerListener)


def test_timerlistener_constructor_exists():
    assert callable(TimerListener.__init__)


def test_timerlistener_constructor_args():
    sig = inspect.signature(TimerListener.__init__)
    params = list(sig.parameters.keys())



def test_mymouselistener_is_not_abstract():
    assert not inspect.isabstract(MyMouseListener)


def test_mymouselistener_constructor_exists():
    assert callable(MyMouseListener.__init__)


def test_mymouselistener_constructor_args():
    sig = inspect.signature(MyMouseListener.__init__)
    params = list(sig.parameters.keys())
    assert "temp" in params, "Missing parameter 'temp'"
    assert "rightClicked" in params, "Missing parameter 'rightClicked'"
    assert "source" in params, "Missing parameter 'source'"
    assert "singleCardSelected" in params, "Missing parameter 'singleCardSelected'"
    assert "tempCard" in params, "Missing parameter 'tempCard'"
    assert "hasSelected" in params, "Missing parameter 'hasSelected'"
    assert "clickedCard" in params, "Missing parameter 'clickedCard'"
    assert "destination" in params, "Missing parameter 'destination'"

def test_mymouselistener_has_temp():
    assert hasattr(MyMouseListener, "temp")
    descriptor = None
    for klass in MyMouseListener.__mro__:
        if "temp" in klass.__dict__:
            descriptor = klass.__dict__["temp"]
            break
    assert isinstance(descriptor, property)

def test_mymouselistener_has_rightClicked():
    assert hasattr(MyMouseListener, "rightClicked")
    descriptor = None
    for klass in MyMouseListener.__mro__:
        if "rightClicked" in klass.__dict__:
            descriptor = klass.__dict__["rightClicked"]
            break
    assert isinstance(descriptor, property)

def test_mymouselistener_has_source():
    assert hasattr(MyMouseListener, "source")
    descriptor = None
    for klass in MyMouseListener.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_mymouselistener_has_singleCardSelected():
    assert hasattr(MyMouseListener, "singleCardSelected")
    descriptor = None
    for klass in MyMouseListener.__mro__:
        if "singleCardSelected" in klass.__dict__:
            descriptor = klass.__dict__["singleCardSelected"]
            break
    assert isinstance(descriptor, property)

def test_mymouselistener_has_tempCard():
    assert hasattr(MyMouseListener, "tempCard")
    descriptor = None
    for klass in MyMouseListener.__mro__:
        if "tempCard" in klass.__dict__:
            descriptor = klass.__dict__["tempCard"]
            break
    assert isinstance(descriptor, property)

def test_mymouselistener_has_hasSelected():
    assert hasattr(MyMouseListener, "hasSelected")
    descriptor = None
    for klass in MyMouseListener.__mro__:
        if "hasSelected" in klass.__dict__:
            descriptor = klass.__dict__["hasSelected"]
            break
    assert isinstance(descriptor, property)

def test_mymouselistener_has_clickedCard():
    assert hasattr(MyMouseListener, "clickedCard")
    descriptor = None
    for klass in MyMouseListener.__mro__:
        if "clickedCard" in klass.__dict__:
            descriptor = klass.__dict__["clickedCard"]
            break
    assert isinstance(descriptor, property)

def test_mymouselistener_has_destination():
    assert hasattr(MyMouseListener, "destination")
    descriptor = None
    for klass in MyMouseListener.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)



def test_solitaireboard_is_not_abstract():
    assert not inspect.isabstract(SolitaireBoard)


def test_solitaireboard_constructor_exists():
    assert callable(SolitaireBoard.__init__)


def test_solitaireboard_constructor_args():
    sig = inspect.signature(SolitaireBoard.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"
    assert "newDrawCount" in params, "Missing parameter 'newDrawCount'"
    assert "sourceList" in params, "Missing parameter 'sourceList'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"
    assert "RESET_STATS" in params, "Missing parameter 'RESET_STATS'"
    assert "DO_NOTHING" in params, "Missing parameter 'DO_NOTHING'"
    assert "GAME_LOST" in params, "Missing parameter 'GAME_LOST'"
    assert "timerCount" in params, "Missing parameter 'timerCount'"
    assert "destinationList" in params, "Missing parameter 'destinationList'"
    assert "timer" in params, "Missing parameter 'timer'"
    assert "columns" in params, "Missing parameter 'columns'"
    assert "statusBar" in params, "Missing parameter 'statusBar'"
    assert "wl" in params, "Missing parameter 'wl'"
    assert "timerToRun" in params, "Missing parameter 'timerToRun'"
    assert "winAnimationStatus" in params, "Missing parameter 'winAnimationStatus'"
    assert "numCards" in params, "Missing parameter 'numCards'"
    assert "acePiles" in params, "Missing parameter 'acePiles'"
    assert "numCardsInDiscardView" in params, "Missing parameter 'numCardsInDiscardView'"
    assert "GAME_WON" in params, "Missing parameter 'GAME_WON'"
    assert "cells" in params, "Missing parameter 'cells'"
    assert "dealDeck" in params, "Missing parameter 'dealDeck'"
    assert "GAME_SAVED" in params, "Missing parameter 'GAME_SAVED'"
    assert "newDifficulty" in params, "Missing parameter 'newDifficulty'"
    assert "timerLabel" in params, "Missing parameter 'timerLabel'"
    assert "discardPile" in params, "Missing parameter 'discardPile'"
    assert "backgroundNumber" in params, "Missing parameter 'backgroundNumber'"
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"
    assert "timerToRunNextGame" in params, "Missing parameter 'timerToRunNextGame'"
    assert "ml" in params, "Missing parameter 'ml'"
    assert "mainPanel" in params, "Missing parameter 'mainPanel'"

def test_solitaireboard_has_deck():
    assert hasattr(SolitaireBoard, "deck")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_newDrawCount():
    assert hasattr(SolitaireBoard, "newDrawCount")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "newDrawCount" in klass.__dict__:
            descriptor = klass.__dict__["newDrawCount"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_sourceList():
    assert hasattr(SolitaireBoard, "sourceList")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "sourceList" in klass.__dict__:
            descriptor = klass.__dict__["sourceList"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_drawCount():
    assert hasattr(SolitaireBoard, "drawCount")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "drawCount" in klass.__dict__:
            descriptor = klass.__dict__["drawCount"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_RESET_STATS():
    assert hasattr(SolitaireBoard, "RESET_STATS")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "RESET_STATS" in klass.__dict__:
            descriptor = klass.__dict__["RESET_STATS"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_DO_NOTHING():
    assert hasattr(SolitaireBoard, "DO_NOTHING")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "DO_NOTHING" in klass.__dict__:
            descriptor = klass.__dict__["DO_NOTHING"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_GAME_LOST():
    assert hasattr(SolitaireBoard, "GAME_LOST")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "GAME_LOST" in klass.__dict__:
            descriptor = klass.__dict__["GAME_LOST"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timerCount():
    assert hasattr(SolitaireBoard, "timerCount")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timerCount" in klass.__dict__:
            descriptor = klass.__dict__["timerCount"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_destinationList():
    assert hasattr(SolitaireBoard, "destinationList")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "destinationList" in klass.__dict__:
            descriptor = klass.__dict__["destinationList"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timer():
    assert hasattr(SolitaireBoard, "timer")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timer" in klass.__dict__:
            descriptor = klass.__dict__["timer"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_columns():
    assert hasattr(SolitaireBoard, "columns")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_statusBar():
    assert hasattr(SolitaireBoard, "statusBar")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "statusBar" in klass.__dict__:
            descriptor = klass.__dict__["statusBar"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_wl():
    assert hasattr(SolitaireBoard, "wl")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "wl" in klass.__dict__:
            descriptor = klass.__dict__["wl"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timerToRun():
    assert hasattr(SolitaireBoard, "timerToRun")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timerToRun" in klass.__dict__:
            descriptor = klass.__dict__["timerToRun"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_winAnimationStatus():
    assert hasattr(SolitaireBoard, "winAnimationStatus")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "winAnimationStatus" in klass.__dict__:
            descriptor = klass.__dict__["winAnimationStatus"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_numCards():
    assert hasattr(SolitaireBoard, "numCards")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "numCards" in klass.__dict__:
            descriptor = klass.__dict__["numCards"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_acePiles():
    assert hasattr(SolitaireBoard, "acePiles")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "acePiles" in klass.__dict__:
            descriptor = klass.__dict__["acePiles"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_numCardsInDiscardView():
    assert hasattr(SolitaireBoard, "numCardsInDiscardView")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "numCardsInDiscardView" in klass.__dict__:
            descriptor = klass.__dict__["numCardsInDiscardView"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_GAME_WON():
    assert hasattr(SolitaireBoard, "GAME_WON")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "GAME_WON" in klass.__dict__:
            descriptor = klass.__dict__["GAME_WON"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_cells():
    assert hasattr(SolitaireBoard, "cells")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "cells" in klass.__dict__:
            descriptor = klass.__dict__["cells"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_dealDeck():
    assert hasattr(SolitaireBoard, "dealDeck")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "dealDeck" in klass.__dict__:
            descriptor = klass.__dict__["dealDeck"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_GAME_SAVED():
    assert hasattr(SolitaireBoard, "GAME_SAVED")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "GAME_SAVED" in klass.__dict__:
            descriptor = klass.__dict__["GAME_SAVED"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_newDifficulty():
    assert hasattr(SolitaireBoard, "newDifficulty")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "newDifficulty" in klass.__dict__:
            descriptor = klass.__dict__["newDifficulty"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timerLabel():
    assert hasattr(SolitaireBoard, "timerLabel")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timerLabel" in klass.__dict__:
            descriptor = klass.__dict__["timerLabel"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_discardPile():
    assert hasattr(SolitaireBoard, "discardPile")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "discardPile" in klass.__dict__:
            descriptor = klass.__dict__["discardPile"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_backgroundNumber():
    assert hasattr(SolitaireBoard, "backgroundNumber")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "backgroundNumber" in klass.__dict__:
            descriptor = klass.__dict__["backgroundNumber"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_deckNumber():
    assert hasattr(SolitaireBoard, "deckNumber")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "deckNumber" in klass.__dict__:
            descriptor = klass.__dict__["deckNumber"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_timerToRunNextGame():
    assert hasattr(SolitaireBoard, "timerToRunNextGame")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "timerToRunNextGame" in klass.__dict__:
            descriptor = klass.__dict__["timerToRunNextGame"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_ml():
    assert hasattr(SolitaireBoard, "ml")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "ml" in klass.__dict__:
            descriptor = klass.__dict__["ml"]
            break
    assert isinstance(descriptor, property)

def test_solitaireboard_has_mainPanel():
    assert hasattr(SolitaireBoard, "mainPanel")
    descriptor = None
    for klass in SolitaireBoard.__mro__:
        if "mainPanel" in klass.__dict__:
            descriptor = klass.__dict__["mainPanel"]
            break
    assert isinstance(descriptor, property)



def test_singlecell_is_not_abstract():
    assert not inspect.isabstract(SingleCell)


def test_singlecell_constructor_exists():
    assert callable(SingleCell.__init__)


def test_singlecell_constructor_args():
    sig = inspect.signature(SingleCell.__init__)
    params = list(sig.parameters.keys())



def test_fourrowsolitaire_is_not_abstract():
    assert not inspect.isabstract(FourRowSolitaire)


def test_fourrowsolitaire_constructor_exists():
    assert callable(FourRowSolitaire.__init__)


def test_fourrowsolitaire_constructor_args():
    sig = inspect.signature(FourRowSolitaire.__init__)
    params = list(sig.parameters.keys())
    assert "about" in params, "Missing parameter 'about'"
    assert "options" in params, "Missing parameter 'options'"
    assert "game" in params, "Missing parameter 'game'"
    assert "undo" in params, "Missing parameter 'undo'"
    assert "helpMenu" in params, "Missing parameter 'helpMenu'"
    assert "version" in params, "Missing parameter 'version'"
    assert "menubar" in params, "Missing parameter 'menubar'"
    assert "checkUpdate" in params, "Missing parameter 'checkUpdate'"
    assert "statistics" in params, "Missing parameter 'statistics'"
    assert "help" in params, "Missing parameter 'help'"
    assert "newGame" in params, "Missing parameter 'newGame'"
    assert "exit" in params, "Missing parameter 'exit'"
    assert "hint" in params, "Missing parameter 'hint'"
    assert "appearance" in params, "Missing parameter 'appearance'"

def test_fourrowsolitaire_has_about():
    assert hasattr(FourRowSolitaire, "about")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "about" in klass.__dict__:
            descriptor = klass.__dict__["about"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_options():
    assert hasattr(FourRowSolitaire, "options")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_game():
    assert hasattr(FourRowSolitaire, "game")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "game" in klass.__dict__:
            descriptor = klass.__dict__["game"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_undo():
    assert hasattr(FourRowSolitaire, "undo")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "undo" in klass.__dict__:
            descriptor = klass.__dict__["undo"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_helpMenu():
    assert hasattr(FourRowSolitaire, "helpMenu")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "helpMenu" in klass.__dict__:
            descriptor = klass.__dict__["helpMenu"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_version():
    assert hasattr(FourRowSolitaire, "version")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_menubar():
    assert hasattr(FourRowSolitaire, "menubar")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "menubar" in klass.__dict__:
            descriptor = klass.__dict__["menubar"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_checkUpdate():
    assert hasattr(FourRowSolitaire, "checkUpdate")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "checkUpdate" in klass.__dict__:
            descriptor = klass.__dict__["checkUpdate"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_statistics():
    assert hasattr(FourRowSolitaire, "statistics")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "statistics" in klass.__dict__:
            descriptor = klass.__dict__["statistics"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_help():
    assert hasattr(FourRowSolitaire, "help")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "help" in klass.__dict__:
            descriptor = klass.__dict__["help"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_newGame():
    assert hasattr(FourRowSolitaire, "newGame")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "newGame" in klass.__dict__:
            descriptor = klass.__dict__["newGame"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_exit():
    assert hasattr(FourRowSolitaire, "exit")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_hint():
    assert hasattr(FourRowSolitaire, "hint")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "hint" in klass.__dict__:
            descriptor = klass.__dict__["hint"]
            break
    assert isinstance(descriptor, property)

def test_fourrowsolitaire_has_appearance():
    assert hasattr(FourRowSolitaire, "appearance")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "appearance" in klass.__dict__:
            descriptor = klass.__dict__["appearance"]
            break
    assert isinstance(descriptor, property)



def test_fireworksdisplay_is_not_abstract():
    assert not inspect.isabstract(FireworksDisplay)


def test_fireworksdisplay_constructor_exists():
    assert callable(FireworksDisplay.__init__)


def test_fireworksdisplay_constructor_args():
    sig = inspect.signature(FireworksDisplay.__init__)
    params = list(sig.parameters.keys())
    assert "SET_DELAY" in params, "Missing parameter 'SET_DELAY'"
    assert "num" in params, "Missing parameter 'num'"
    assert "yy" in params, "Missing parameter 'yy'"
    assert "NUM_FIREWORKS" in params, "Missing parameter 'NUM_FIREWORKS'"
    assert "FIREWORKS_SIZE" in params, "Missing parameter 'FIREWORKS_SIZE'"
    assert "xx" in params, "Missing parameter 'xx'"
    assert "startValue" in params, "Missing parameter 'startValue'"
    assert "FIREWORKS_TIME" in params, "Missing parameter 'FIREWORKS_TIME'"
    assert "time" in params, "Missing parameter 'time'"
    assert "numSets" in params, "Missing parameter 'numSets'"
    assert "random" in params, "Missing parameter 'random'"
    assert "colors" in params, "Missing parameter 'colors'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_fireworksdisplay_has_SET_DELAY():
    assert hasattr(FireworksDisplay, "SET_DELAY")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "SET_DELAY" in klass.__dict__:
            descriptor = klass.__dict__["SET_DELAY"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_num():
    assert hasattr(FireworksDisplay, "num")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_yy():
    assert hasattr(FireworksDisplay, "yy")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "yy" in klass.__dict__:
            descriptor = klass.__dict__["yy"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_NUM_FIREWORKS():
    assert hasattr(FireworksDisplay, "NUM_FIREWORKS")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "NUM_FIREWORKS" in klass.__dict__:
            descriptor = klass.__dict__["NUM_FIREWORKS"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_FIREWORKS_SIZE():
    assert hasattr(FireworksDisplay, "FIREWORKS_SIZE")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "FIREWORKS_SIZE" in klass.__dict__:
            descriptor = klass.__dict__["FIREWORKS_SIZE"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_xx():
    assert hasattr(FireworksDisplay, "xx")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "xx" in klass.__dict__:
            descriptor = klass.__dict__["xx"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_startValue():
    assert hasattr(FireworksDisplay, "startValue")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "startValue" in klass.__dict__:
            descriptor = klass.__dict__["startValue"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_FIREWORKS_TIME():
    assert hasattr(FireworksDisplay, "FIREWORKS_TIME")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "FIREWORKS_TIME" in klass.__dict__:
            descriptor = klass.__dict__["FIREWORKS_TIME"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_time():
    assert hasattr(FireworksDisplay, "time")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_numSets():
    assert hasattr(FireworksDisplay, "numSets")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "numSets" in klass.__dict__:
            descriptor = klass.__dict__["numSets"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_random():
    assert hasattr(FireworksDisplay, "random")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_colors():
    assert hasattr(FireworksDisplay, "colors")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "colors" in klass.__dict__:
            descriptor = klass.__dict__["colors"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_y():
    assert hasattr(FireworksDisplay, "y")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_fireworksdisplay_has_x():
    assert hasattr(FireworksDisplay, "x")
    descriptor = None
    for klass in FireworksDisplay.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_discardpile_is_not_abstract():
    assert not inspect.isabstract(DiscardPile)


def test_discardpile_constructor_exists():
    assert callable(DiscardPile.__init__)


def test_discardpile_constructor_args():
    sig = inspect.signature(DiscardPile.__init__)
    params = list(sig.parameters.keys())
    assert "CardsLeftFromDraw" in params, "Missing parameter 'CardsLeftFromDraw'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"

def test_discardpile_has_CardsLeftFromDraw():
    assert hasattr(DiscardPile, "CardsLeftFromDraw")
    descriptor = None
    for klass in DiscardPile.__mro__:
        if "CardsLeftFromDraw" in klass.__dict__:
            descriptor = klass.__dict__["CardsLeftFromDraw"]
            break
    assert isinstance(descriptor, property)

def test_discardpile_has_drawCount():
    assert hasattr(DiscardPile, "drawCount")
    descriptor = None
    for klass in DiscardPile.__mro__:
        if "drawCount" in klass.__dict__:
            descriptor = klass.__dict__["drawCount"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"

def test_deck_has_deck():
    assert hasattr(Deck, "deck")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_deckNumber():
    assert hasattr(Deck, "deckNumber")
    descriptor = None
    for klass in Deck.__mro__:
        if "deckNumber" in klass.__dict__:
            descriptor = klass.__dict__["deckNumber"]
            break
    assert isinstance(descriptor, property)



def test_dealdeck_is_not_abstract():
    assert not inspect.isabstract(DealDeck)


def test_dealdeck_constructor_exists():
    assert callable(DealDeck.__init__)


def test_dealdeck_constructor_args():
    sig = inspect.signature(DealDeck.__init__)
    params = list(sig.parameters.keys())
    assert "MEDIUM_THROUGH_LIMIT" in params, "Missing parameter 'MEDIUM_THROUGH_LIMIT'"
    assert "DRAW_THREE_THROUGH_LIMIT" in params, "Missing parameter 'DRAW_THREE_THROUGH_LIMIT'"
    assert "deckThroughLimit" in params, "Missing parameter 'deckThroughLimit'"
    assert "redealable" in params, "Missing parameter 'redealable'"
    assert "EASY_THROUGH_LIMIT" in params, "Missing parameter 'EASY_THROUGH_LIMIT'"
    assert "HARD_THROUGH_LIMIT" in params, "Missing parameter 'HARD_THROUGH_LIMIT'"
    assert "numTimesThroughDeck" in params, "Missing parameter 'numTimesThroughDeck'"
    assert "discardPile" in params, "Missing parameter 'discardPile'"
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "DRAW_ONE_THROUGH_LIMIT" in params, "Missing parameter 'DRAW_ONE_THROUGH_LIMIT'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"

def test_dealdeck_has_MEDIUM_THROUGH_LIMIT():
    assert hasattr(DealDeck, "MEDIUM_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "MEDIUM_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["MEDIUM_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_DRAW_THREE_THROUGH_LIMIT():
    assert hasattr(DealDeck, "DRAW_THREE_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "DRAW_THREE_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["DRAW_THREE_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_deckThroughLimit():
    assert hasattr(DealDeck, "deckThroughLimit")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "deckThroughLimit" in klass.__dict__:
            descriptor = klass.__dict__["deckThroughLimit"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_redealable():
    assert hasattr(DealDeck, "redealable")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "redealable" in klass.__dict__:
            descriptor = klass.__dict__["redealable"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_EASY_THROUGH_LIMIT():
    assert hasattr(DealDeck, "EASY_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "EASY_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["EASY_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_HARD_THROUGH_LIMIT():
    assert hasattr(DealDeck, "HARD_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "HARD_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["HARD_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_numTimesThroughDeck():
    assert hasattr(DealDeck, "numTimesThroughDeck")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "numTimesThroughDeck" in klass.__dict__:
            descriptor = klass.__dict__["numTimesThroughDeck"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_discardPile():
    assert hasattr(DealDeck, "discardPile")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "discardPile" in klass.__dict__:
            descriptor = klass.__dict__["discardPile"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_difficulty():
    assert hasattr(DealDeck, "difficulty")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "difficulty" in klass.__dict__:
            descriptor = klass.__dict__["difficulty"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_DRAW_ONE_THROUGH_LIMIT():
    assert hasattr(DealDeck, "DRAW_ONE_THROUGH_LIMIT")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "DRAW_ONE_THROUGH_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["DRAW_ONE_THROUGH_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_dealdeck_has_drawCount():
    assert hasattr(DealDeck, "drawCount")
    descriptor = None
    for klass in DealDeck.__mro__:
        if "drawCount" in klass.__dict__:
            descriptor = klass.__dict__["drawCount"]
            break
    assert isinstance(descriptor, property)



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_changeoptions_is_not_abstract():
    assert not inspect.isabstract(ChangeOptions)


def test_changeoptions_constructor_exists():
    assert callable(ChangeOptions.__init__)


def test_changeoptions_constructor_args():
    sig = inspect.signature(ChangeOptions.__init__)
    params = list(sig.parameters.keys())
    assert "medium" in params, "Missing parameter 'medium'"
    assert "drawThree" in params, "Missing parameter 'drawThree'"
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "hard" in params, "Missing parameter 'hard'"
    assert "exited" in params, "Missing parameter 'exited'"
    assert "drawOne" in params, "Missing parameter 'drawOne'"
    assert "timerCheck" in params, "Missing parameter 'timerCheck'"
    assert "easy" in params, "Missing parameter 'easy'"
    assert "animation" in params, "Missing parameter 'animation'"
    assert "ok" in params, "Missing parameter 'ok'"
    assert "timer" in params, "Missing parameter 'timer'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"
    assert "winAnimationCheck" in params, "Missing parameter 'winAnimationCheck'"
    assert "sounds" in params, "Missing parameter 'sounds'"
    assert "winSoundCheck" in params, "Missing parameter 'winSoundCheck'"

def test_changeoptions_has_medium():
    assert hasattr(ChangeOptions, "medium")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "medium" in klass.__dict__:
            descriptor = klass.__dict__["medium"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_drawThree():
    assert hasattr(ChangeOptions, "drawThree")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "drawThree" in klass.__dict__:
            descriptor = klass.__dict__["drawThree"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_difficulty():
    assert hasattr(ChangeOptions, "difficulty")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "difficulty" in klass.__dict__:
            descriptor = klass.__dict__["difficulty"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_hard():
    assert hasattr(ChangeOptions, "hard")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "hard" in klass.__dict__:
            descriptor = klass.__dict__["hard"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_exited():
    assert hasattr(ChangeOptions, "exited")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "exited" in klass.__dict__:
            descriptor = klass.__dict__["exited"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_drawOne():
    assert hasattr(ChangeOptions, "drawOne")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "drawOne" in klass.__dict__:
            descriptor = klass.__dict__["drawOne"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_timerCheck():
    assert hasattr(ChangeOptions, "timerCheck")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "timerCheck" in klass.__dict__:
            descriptor = klass.__dict__["timerCheck"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_easy():
    assert hasattr(ChangeOptions, "easy")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "easy" in klass.__dict__:
            descriptor = klass.__dict__["easy"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_animation():
    assert hasattr(ChangeOptions, "animation")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "animation" in klass.__dict__:
            descriptor = klass.__dict__["animation"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_ok():
    assert hasattr(ChangeOptions, "ok")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "ok" in klass.__dict__:
            descriptor = klass.__dict__["ok"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_timer():
    assert hasattr(ChangeOptions, "timer")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "timer" in klass.__dict__:
            descriptor = klass.__dict__["timer"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_drawCount():
    assert hasattr(ChangeOptions, "drawCount")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "drawCount" in klass.__dict__:
            descriptor = klass.__dict__["drawCount"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_winAnimationCheck():
    assert hasattr(ChangeOptions, "winAnimationCheck")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "winAnimationCheck" in klass.__dict__:
            descriptor = klass.__dict__["winAnimationCheck"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_sounds():
    assert hasattr(ChangeOptions, "sounds")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "sounds" in klass.__dict__:
            descriptor = klass.__dict__["sounds"]
            break
    assert isinstance(descriptor, property)

def test_changeoptions_has_winSoundCheck():
    assert hasattr(ChangeOptions, "winSoundCheck")
    descriptor = None
    for klass in ChangeOptions.__mro__:
        if "winSoundCheck" in klass.__dict__:
            descriptor = klass.__dict__["winSoundCheck"]
            break
    assert isinstance(descriptor, property)



def test_changeappearance_is_not_abstract():
    assert not inspect.isabstract(ChangeAppearance)


def test_changeappearance_constructor_exists():
    assert callable(ChangeAppearance.__init__)


def test_changeappearance_constructor_args():
    sig = inspect.signature(ChangeAppearance.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundNumber" in params, "Missing parameter 'backgroundNumber'"
    assert "backgrounds" in params, "Missing parameter 'backgrounds'"
    assert "backGroundLabel" in params, "Missing parameter 'backGroundLabel'"
    assert "ok" in params, "Missing parameter 'ok'"
    assert "NUM_DECKS" in params, "Missing parameter 'NUM_DECKS'"
    assert "FRS_BACKGROUND" in params, "Missing parameter 'FRS_BACKGROUND'"
    assert "cardBackLabel" in params, "Missing parameter 'cardBackLabel'"
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"
    assert "decks" in params, "Missing parameter 'decks'"
    assert "FRS_DECK" in params, "Missing parameter 'FRS_DECK'"
    assert "exited" in params, "Missing parameter 'exited'"
    assert "NUM_BACKGROUNDS" in params, "Missing parameter 'NUM_BACKGROUNDS'"

def test_changeappearance_has_backgroundNumber():
    assert hasattr(ChangeAppearance, "backgroundNumber")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "backgroundNumber" in klass.__dict__:
            descriptor = klass.__dict__["backgroundNumber"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_backgrounds():
    assert hasattr(ChangeAppearance, "backgrounds")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "backgrounds" in klass.__dict__:
            descriptor = klass.__dict__["backgrounds"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_backGroundLabel():
    assert hasattr(ChangeAppearance, "backGroundLabel")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "backGroundLabel" in klass.__dict__:
            descriptor = klass.__dict__["backGroundLabel"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_ok():
    assert hasattr(ChangeAppearance, "ok")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "ok" in klass.__dict__:
            descriptor = klass.__dict__["ok"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_NUM_DECKS():
    assert hasattr(ChangeAppearance, "NUM_DECKS")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "NUM_DECKS" in klass.__dict__:
            descriptor = klass.__dict__["NUM_DECKS"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_FRS_BACKGROUND():
    assert hasattr(ChangeAppearance, "FRS_BACKGROUND")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "FRS_BACKGROUND" in klass.__dict__:
            descriptor = klass.__dict__["FRS_BACKGROUND"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_cardBackLabel():
    assert hasattr(ChangeAppearance, "cardBackLabel")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "cardBackLabel" in klass.__dict__:
            descriptor = klass.__dict__["cardBackLabel"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_deckNumber():
    assert hasattr(ChangeAppearance, "deckNumber")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "deckNumber" in klass.__dict__:
            descriptor = klass.__dict__["deckNumber"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_decks():
    assert hasattr(ChangeAppearance, "decks")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "decks" in klass.__dict__:
            descriptor = klass.__dict__["decks"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_FRS_DECK():
    assert hasattr(ChangeAppearance, "FRS_DECK")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "FRS_DECK" in klass.__dict__:
            descriptor = klass.__dict__["FRS_DECK"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_exited():
    assert hasattr(ChangeAppearance, "exited")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "exited" in klass.__dict__:
            descriptor = klass.__dict__["exited"]
            break
    assert isinstance(descriptor, property)

def test_changeappearance_has_NUM_BACKGROUNDS():
    assert hasattr(ChangeAppearance, "NUM_BACKGROUNDS")
    descriptor = None
    for klass in ChangeAppearance.__mro__:
        if "NUM_BACKGROUNDS" in klass.__dict__:
            descriptor = klass.__dict__["NUM_BACKGROUNDS"]
            break
    assert isinstance(descriptor, property)



def test_cardstack_is_not_abstract():
    assert not inspect.isabstract(CardStack)


def test_cardstack_constructor_exists():
    assert callable(CardStack.__init__)


def test_cardstack_constructor_args():
    sig = inspect.signature(CardStack.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"

def test_cardstack_has_cards():
    assert hasattr(CardStack, "cards")
    descriptor = None
    for klass in CardStack.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "TWO" in params, "Missing parameter 'TWO'"
    assert "HEARTS_SUIT" in params, "Missing parameter 'HEARTS_SUIT'"
    assert "SIX" in params, "Missing parameter 'SIX'"
    assert "cardSuit" in params, "Missing parameter 'cardSuit'"
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"
    assert "cardImageString" in params, "Missing parameter 'cardImageString'"
    assert "INVALID_NUMBER" in params, "Missing parameter 'INVALID_NUMBER'"
    assert "FIVE" in params, "Missing parameter 'FIVE'"
    assert "highlighted" in params, "Missing parameter 'highlighted'"
    assert "FOUR" in params, "Missing parameter 'FOUR'"
    assert "fullCardNumber" in params, "Missing parameter 'fullCardNumber'"
    assert "int_deckNumber" in params, "Missing parameter 'int_deckNumber'"
    assert "KING" in params, "Missing parameter 'KING'"
    assert "TEN" in params, "Missing parameter 'TEN'"
    assert "SPADES_SUIT" in params, "Missing parameter 'SPADES_SUIT'"
    assert "INVALID_SUIT" in params, "Missing parameter 'INVALID_SUIT'"
    assert "image" in params, "Missing parameter 'image'"
    assert "cardColor" in params, "Missing parameter 'cardColor'"
    assert "CLUBS_SUIT" in params, "Missing parameter 'CLUBS_SUIT'"
    assert "faceUp" in params, "Missing parameter 'faceUp'"
    assert "EIGHT" in params, "Missing parameter 'EIGHT'"
    assert "JACK" in params, "Missing parameter 'JACK'"
    assert "THREE" in params, "Missing parameter 'THREE'"
    assert "NINE" in params, "Missing parameter 'NINE'"
    assert "cardBack" in params, "Missing parameter 'cardBack'"
    assert "SEVEN" in params, "Missing parameter 'SEVEN'"
    assert "DIAMONDS_SUIT" in params, "Missing parameter 'DIAMONDS_SUIT'"
    assert "location" in params, "Missing parameter 'location'"
    assert "cardHighLighted" in params, "Missing parameter 'cardHighLighted'"
    assert "ACE" in params, "Missing parameter 'ACE'"
    assert "QUEEN" in params, "Missing parameter 'QUEEN'"

def test_card_has_TWO():
    assert hasattr(Card, "TWO")
    descriptor = None
    for klass in Card.__mro__:
        if "TWO" in klass.__dict__:
            descriptor = klass.__dict__["TWO"]
            break
    assert isinstance(descriptor, property)

def test_card_has_HEARTS_SUIT():
    assert hasattr(Card, "HEARTS_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "HEARTS_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["HEARTS_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_SIX():
    assert hasattr(Card, "SIX")
    descriptor = None
    for klass in Card.__mro__:
        if "SIX" in klass.__dict__:
            descriptor = klass.__dict__["SIX"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardSuit():
    assert hasattr(Card, "cardSuit")
    descriptor = None
    for klass in Card.__mro__:
        if "cardSuit" in klass.__dict__:
            descriptor = klass.__dict__["cardSuit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardNumber():
    assert hasattr(Card, "cardNumber")
    descriptor = None
    for klass in Card.__mro__:
        if "cardNumber" in klass.__dict__:
            descriptor = klass.__dict__["cardNumber"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardImageString():
    assert hasattr(Card, "cardImageString")
    descriptor = None
    for klass in Card.__mro__:
        if "cardImageString" in klass.__dict__:
            descriptor = klass.__dict__["cardImageString"]
            break
    assert isinstance(descriptor, property)

def test_card_has_INVALID_NUMBER():
    assert hasattr(Card, "INVALID_NUMBER")
    descriptor = None
    for klass in Card.__mro__:
        if "INVALID_NUMBER" in klass.__dict__:
            descriptor = klass.__dict__["INVALID_NUMBER"]
            break
    assert isinstance(descriptor, property)

def test_card_has_FIVE():
    assert hasattr(Card, "FIVE")
    descriptor = None
    for klass in Card.__mro__:
        if "FIVE" in klass.__dict__:
            descriptor = klass.__dict__["FIVE"]
            break
    assert isinstance(descriptor, property)

def test_card_has_highlighted():
    assert hasattr(Card, "highlighted")
    descriptor = None
    for klass in Card.__mro__:
        if "highlighted" in klass.__dict__:
            descriptor = klass.__dict__["highlighted"]
            break
    assert isinstance(descriptor, property)

def test_card_has_FOUR():
    assert hasattr(Card, "FOUR")
    descriptor = None
    for klass in Card.__mro__:
        if "FOUR" in klass.__dict__:
            descriptor = klass.__dict__["FOUR"]
            break
    assert isinstance(descriptor, property)

def test_card_has_fullCardNumber():
    assert hasattr(Card, "fullCardNumber")
    descriptor = None
    for klass in Card.__mro__:
        if "fullCardNumber" in klass.__dict__:
            descriptor = klass.__dict__["fullCardNumber"]
            break
    assert isinstance(descriptor, property)

def test_card_has_int_deckNumber():
    assert hasattr(Card, "int_deckNumber")
    descriptor = None
    for klass in Card.__mro__:
        if "int_deckNumber" in klass.__dict__:
            descriptor = klass.__dict__["int_deckNumber"]
            break
    assert isinstance(descriptor, property)

def test_card_has_KING():
    assert hasattr(Card, "KING")
    descriptor = None
    for klass in Card.__mro__:
        if "KING" in klass.__dict__:
            descriptor = klass.__dict__["KING"]
            break
    assert isinstance(descriptor, property)

def test_card_has_TEN():
    assert hasattr(Card, "TEN")
    descriptor = None
    for klass in Card.__mro__:
        if "TEN" in klass.__dict__:
            descriptor = klass.__dict__["TEN"]
            break
    assert isinstance(descriptor, property)

def test_card_has_SPADES_SUIT():
    assert hasattr(Card, "SPADES_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "SPADES_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["SPADES_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_INVALID_SUIT():
    assert hasattr(Card, "INVALID_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "INVALID_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["INVALID_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_image():
    assert hasattr(Card, "image")
    descriptor = None
    for klass in Card.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardColor():
    assert hasattr(Card, "cardColor")
    descriptor = None
    for klass in Card.__mro__:
        if "cardColor" in klass.__dict__:
            descriptor = klass.__dict__["cardColor"]
            break
    assert isinstance(descriptor, property)

def test_card_has_CLUBS_SUIT():
    assert hasattr(Card, "CLUBS_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "CLUBS_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["CLUBS_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_faceUp():
    assert hasattr(Card, "faceUp")
    descriptor = None
    for klass in Card.__mro__:
        if "faceUp" in klass.__dict__:
            descriptor = klass.__dict__["faceUp"]
            break
    assert isinstance(descriptor, property)

def test_card_has_EIGHT():
    assert hasattr(Card, "EIGHT")
    descriptor = None
    for klass in Card.__mro__:
        if "EIGHT" in klass.__dict__:
            descriptor = klass.__dict__["EIGHT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_JACK():
    assert hasattr(Card, "JACK")
    descriptor = None
    for klass in Card.__mro__:
        if "JACK" in klass.__dict__:
            descriptor = klass.__dict__["JACK"]
            break
    assert isinstance(descriptor, property)

def test_card_has_THREE():
    assert hasattr(Card, "THREE")
    descriptor = None
    for klass in Card.__mro__:
        if "THREE" in klass.__dict__:
            descriptor = klass.__dict__["THREE"]
            break
    assert isinstance(descriptor, property)

def test_card_has_NINE():
    assert hasattr(Card, "NINE")
    descriptor = None
    for klass in Card.__mro__:
        if "NINE" in klass.__dict__:
            descriptor = klass.__dict__["NINE"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardBack():
    assert hasattr(Card, "cardBack")
    descriptor = None
    for klass in Card.__mro__:
        if "cardBack" in klass.__dict__:
            descriptor = klass.__dict__["cardBack"]
            break
    assert isinstance(descriptor, property)

def test_card_has_SEVEN():
    assert hasattr(Card, "SEVEN")
    descriptor = None
    for klass in Card.__mro__:
        if "SEVEN" in klass.__dict__:
            descriptor = klass.__dict__["SEVEN"]
            break
    assert isinstance(descriptor, property)

def test_card_has_DIAMONDS_SUIT():
    assert hasattr(Card, "DIAMONDS_SUIT")
    descriptor = None
    for klass in Card.__mro__:
        if "DIAMONDS_SUIT" in klass.__dict__:
            descriptor = klass.__dict__["DIAMONDS_SUIT"]
            break
    assert isinstance(descriptor, property)

def test_card_has_location():
    assert hasattr(Card, "location")
    descriptor = None
    for klass in Card.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardHighLighted():
    assert hasattr(Card, "cardHighLighted")
    descriptor = None
    for klass in Card.__mro__:
        if "cardHighLighted" in klass.__dict__:
            descriptor = klass.__dict__["cardHighLighted"]
            break
    assert isinstance(descriptor, property)

def test_card_has_ACE():
    assert hasattr(Card, "ACE")
    descriptor = None
    for klass in Card.__mro__:
        if "ACE" in klass.__dict__:
            descriptor = klass.__dict__["ACE"]
            break
    assert isinstance(descriptor, property)

def test_card_has_QUEEN():
    assert hasattr(Card, "QUEEN")
    descriptor = None
    for klass in Card.__mro__:
        if "QUEEN" in klass.__dict__:
            descriptor = klass.__dict__["QUEEN"]
            break
    assert isinstance(descriptor, property)



def test_acepile_is_not_abstract():
    assert not inspect.isabstract(AcePile)


def test_acepile_constructor_exists():
    assert callable(AcePile.__init__)


def test_acepile_constructor_args():
    sig = inspect.signature(AcePile.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"

def test_acepile_has_suit():
    assert hasattr(AcePile, "suit")
    descriptor = None
    for klass in AcePile.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)



def test_four_row_solitaire___component_is_not_abstract():
    assert not inspect.isabstract(Four_Row_Solitaire___Component)


def test_four_row_solitaire___component_constructor_exists():
    assert callable(Four_Row_Solitaire___Component.__init__)


def test_four_row_solitaire___component_constructor_args():
    sig = inspect.signature(Four_Row_Solitaire___Component.__init__)
    params = list(sig.parameters.keys())



def test_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Help_external_strategy = st.builds(
    Help_external,
)
Game_external_strategy = st.builds(
    Game_external,
)
Main_Game_Board_external_strategy = st.builds(
    Main_Game_Board_external,
)
SoundThread_strategy = st.builds(
    SoundThread,
    sequencer=
        safe_text
)
WinScreen_strategy = st.builds(
    WinScreen,
    sound=
        safe_text
)
SolitairePanel_strategy = st.builds(
    SolitairePanel,
    background=
        safe_text,
    backGroundNumber=
        safe_text
)
SolitaireLayout_strategy = st.builds(
    SolitaireLayout,
    COLUMN_TWO=
        safe_text,
    DECK=
        safe_text,
    CELL_ONE=
        safe_text,
    cellThree=
        safe_text,
    CLUBS_ACE_PILE=
        safe_text,
    discardPile=
        safe_text,
    DISCARD_PILE=
        safe_text,
    DIAMONDS_ACE_PILE=
        safe_text,
    colOne=
        safe_text,
    CELL_THREE=
        safe_text,
    aceDiamonds=
        safe_text,
    HEARTS_ACE_PILE=
        safe_text,
    CELL_FOUR=
        safe_text,
    ColFour=
        safe_text,
    acespades=
        safe_text,
    CELL_TWO=
        safe_text,
    aceClubs=
        safe_text,
    COLUMN_FOUR=
        safe_text,
    aceHearts=
        safe_text,
    ColTwo=
        safe_text,
    cellTwo=
        safe_text,
    deck=
        safe_text,
    COLUMN_ONE=
        safe_text,
    cellFour=
        safe_text,
    SPADES_ACE_PILE=
        safe_text,
    cellOne=
        safe_text,
    COLUMN_THREE=
        safe_text,
    ColThree=
        safe_text
)
windowclosing_strategy = st.builds(
    windowclosing,
)
TimerListener_strategy = st.builds(
    TimerListener,
)
MyMouseListener_strategy = st.builds(
    MyMouseListener,
    temp=
        safe_text,
    rightClicked=
        st.booleans(),
    source=
        safe_text,
    singleCardSelected=
        st.booleans(),
    tempCard=
        safe_text,
    hasSelected=
        st.booleans(),
    clickedCard=
        safe_text,
    destination=
        safe_text
)
SolitaireBoard_strategy = st.builds(
    SolitaireBoard,
    deck=
        st.none(),
    newDrawCount=
        safe_text,
    sourceList=
        safe_text,
    drawCount=
        safe_text,
    RESET_STATS=
        safe_text,
    DO_NOTHING=
        safe_text,
    GAME_LOST=
        safe_text,
    timerCount=
        safe_text,
    destinationList=
        safe_text,
    timer=
        safe_text,
    columns=
        safe_text,
    statusBar=
        safe_text,
    wl=
        safe_text,
    timerToRun=
        st.booleans(),
    winAnimationStatus=
        safe_text,
    numCards=
        safe_text,
    acePiles=
        safe_text,
    numCardsInDiscardView=
        safe_text,
    GAME_WON=
        safe_text,
    cells=
        safe_text,
    dealDeck=
        st.none(),
    GAME_SAVED=
        safe_text,
    newDifficulty=
        safe_text,
    timerLabel=
        safe_text,
    discardPile=
        safe_text,
    backgroundNumber=
        safe_text,
    deckNumber=
        safe_text,
    timerToRunNextGame=
        safe_text,
    ml=
        safe_text,
    mainPanel=
        safe_text
)
SingleCell_strategy = st.builds(
    SingleCell,
)
FourRowSolitaire_strategy = st.builds(
    FourRowSolitaire,
    about=
        safe_text,
    options=
        safe_text,
    game=
        safe_text,
    undo=
        safe_text,
    helpMenu=
        safe_text,
    version=
        safe_text,
    menubar=
        safe_text,
    checkUpdate=
        safe_text,
    statistics=
        safe_text,
    help=
        safe_text,
    newGame=
        safe_text,
    exit=
        safe_text,
    hint=
        safe_text,
    appearance=
        safe_text
)
FireworksDisplay_strategy = st.builds(
    FireworksDisplay,
    SET_DELAY=
        safe_text,
    num=
        safe_text,
    yy=
        safe_text,
    NUM_FIREWORKS=
        safe_text,
    FIREWORKS_SIZE=
        safe_text,
    xx=
        safe_text,
    startValue=
        safe_text,
    FIREWORKS_TIME=
        safe_text,
    time=
        safe_text,
    numSets=
        safe_text,
    random=
        safe_text,
    colors=
        safe_text,
    y=
        safe_text,
    x=
        safe_text
)
DiscardPile_strategy = st.builds(
    DiscardPile,
    CardsLeftFromDraw=
        safe_text,
    drawCount=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    deck=
        safe_text,
    deckNumber=
        safe_text
)
DealDeck_strategy = st.builds(
    DealDeck,
    MEDIUM_THROUGH_LIMIT=
        safe_text,
    DRAW_THREE_THROUGH_LIMIT=
        safe_text,
    deckThroughLimit=
        safe_text,
    redealable=
        st.booleans(),
    EASY_THROUGH_LIMIT=
        safe_text,
    HARD_THROUGH_LIMIT=
        safe_text,
    numTimesThroughDeck=
        safe_text,
    discardPile=
        safe_text,
    difficulty=
        safe_text,
    DRAW_ONE_THROUGH_LIMIT=
        safe_text,
    drawCount=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
ChangeOptions_strategy = st.builds(
    ChangeOptions,
    medium=
        safe_text,
    drawThree=
        safe_text,
    difficulty=
        safe_text,
    hard=
        safe_text,
    exited=
        st.booleans(),
    drawOne=
        safe_text,
    timerCheck=
        safe_text,
    easy=
        safe_text,
    animation=
        safe_text,
    ok=
        safe_text,
    timer=
        safe_text,
    drawCount=
        safe_text,
    winAnimationCheck=
        safe_text,
    sounds=
        safe_text,
    winSoundCheck=
        safe_text
)
ChangeAppearance_strategy = st.builds(
    ChangeAppearance,
    backgroundNumber=
        safe_text,
    backgrounds=
        safe_text,
    backGroundLabel=
        safe_text,
    ok=
        safe_text,
    NUM_DECKS=
        safe_text,
    FRS_BACKGROUND=
        safe_text,
    cardBackLabel=
        safe_text,
    deckNumber=
        safe_text,
    decks=
        safe_text,
    FRS_DECK=
        safe_text,
    exited=
        st.booleans(),
    NUM_BACKGROUNDS=
        safe_text
)
CardStack_strategy = st.builds(
    CardStack,
    cards=
        safe_text
)
Card_strategy = st.builds(
    Card,
    TWO=
        safe_text,
    HEARTS_SUIT=
        safe_text,
    SIX=
        safe_text,
    cardSuit=
        safe_text,
    cardNumber=
        safe_text,
    cardImageString=
        safe_text,
    INVALID_NUMBER=
        safe_text,
    FIVE=
        safe_text,
    highlighted=
        st.booleans(),
    FOUR=
        safe_text,
    fullCardNumber=
        safe_text,
    int_deckNumber=
        safe_text,
    KING=
        safe_text,
    TEN=
        safe_text,
    SPADES_SUIT=
        safe_text,
    INVALID_SUIT=
        safe_text,
    image=
        safe_text,
    cardColor=
        safe_text,
    CLUBS_SUIT=
        safe_text,
    faceUp=
        st.booleans(),
    EIGHT=
        safe_text,
    JACK=
        safe_text,
    THREE=
        safe_text,
    NINE=
        safe_text,
    cardBack=
        safe_text,
    SEVEN=
        safe_text,
    DIAMONDS_SUIT=
        safe_text,
    location=
        safe_text,
    cardHighLighted=
        safe_text,
    ACE=
        safe_text,
    QUEEN=
        safe_text
)
AcePile_strategy = st.builds(
    AcePile,
    suit=
        safe_text
)
Four_Row_Solitaire___Component_strategy = st.builds(
    Four_Row_Solitaire___Component,
)
User_Actor_strategy = st.builds(
    User_Actor,
)

@given(instance=Help_external_strategy)
@settings(max_examples=50)
def test_help_external_instantiation(instance):
    assert isinstance(instance, Help_external)

@given(instance=Game_external_strategy)
@settings(max_examples=50)
def test_game_external_instantiation(instance):
    assert isinstance(instance, Game_external)

@given(instance=Main_Game_Board_external_strategy)
@settings(max_examples=50)
def test_main_game_board_external_instantiation(instance):
    assert isinstance(instance, Main_Game_Board_external)

@given(instance=SoundThread_strategy)
@settings(max_examples=50)
def test_soundthread_instantiation(instance):
    assert isinstance(instance, SoundThread)



@given(instance=SoundThread_strategy)
def test_soundthread_sequencer_setter(instance):
    original = instance.sequencer
    instance.sequencer = original
    assert instance.sequencer == original

@given(instance=WinScreen_strategy)
@settings(max_examples=50)
def test_winscreen_instantiation(instance):
    assert isinstance(instance, WinScreen)



@given(instance=WinScreen_strategy)
def test_winscreen_sound_setter(instance):
    original = instance.sound
    instance.sound = original
    assert instance.sound == original

@given(instance=SolitairePanel_strategy)
@settings(max_examples=50)
def test_solitairepanel_instantiation(instance):
    assert isinstance(instance, SolitairePanel)



@given(instance=SolitairePanel_strategy)
def test_solitairepanel_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=SolitairePanel_strategy)
def test_solitairepanel_backGroundNumber_setter(instance):
    original = instance.backGroundNumber
    instance.backGroundNumber = original
    assert instance.backGroundNumber == original

@given(instance=SolitaireLayout_strategy)
@settings(max_examples=50)
def test_solitairelayout_instantiation(instance):
    assert isinstance(instance, SolitaireLayout)



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_COLUMN_TWO_setter(instance):
    original = instance.COLUMN_TWO
    instance.COLUMN_TWO = original
    assert instance.COLUMN_TWO == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_DECK_setter(instance):
    original = instance.DECK
    instance.DECK = original
    assert instance.DECK == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CELL_ONE_setter(instance):
    original = instance.CELL_ONE
    instance.CELL_ONE = original
    assert instance.CELL_ONE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_cellThree_setter(instance):
    original = instance.cellThree
    instance.cellThree = original
    assert instance.cellThree == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CLUBS_ACE_PILE_setter(instance):
    original = instance.CLUBS_ACE_PILE
    instance.CLUBS_ACE_PILE = original
    assert instance.CLUBS_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_discardPile_setter(instance):
    original = instance.discardPile
    instance.discardPile = original
    assert instance.discardPile == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_DISCARD_PILE_setter(instance):
    original = instance.DISCARD_PILE
    instance.DISCARD_PILE = original
    assert instance.DISCARD_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_DIAMONDS_ACE_PILE_setter(instance):
    original = instance.DIAMONDS_ACE_PILE
    instance.DIAMONDS_ACE_PILE = original
    assert instance.DIAMONDS_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_colOne_setter(instance):
    original = instance.colOne
    instance.colOne = original
    assert instance.colOne == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CELL_THREE_setter(instance):
    original = instance.CELL_THREE
    instance.CELL_THREE = original
    assert instance.CELL_THREE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_aceDiamonds_setter(instance):
    original = instance.aceDiamonds
    instance.aceDiamonds = original
    assert instance.aceDiamonds == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_HEARTS_ACE_PILE_setter(instance):
    original = instance.HEARTS_ACE_PILE
    instance.HEARTS_ACE_PILE = original
    assert instance.HEARTS_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CELL_FOUR_setter(instance):
    original = instance.CELL_FOUR
    instance.CELL_FOUR = original
    assert instance.CELL_FOUR == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_ColFour_setter(instance):
    original = instance.ColFour
    instance.ColFour = original
    assert instance.ColFour == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_acespades_setter(instance):
    original = instance.acespades
    instance.acespades = original
    assert instance.acespades == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_CELL_TWO_setter(instance):
    original = instance.CELL_TWO
    instance.CELL_TWO = original
    assert instance.CELL_TWO == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_aceClubs_setter(instance):
    original = instance.aceClubs
    instance.aceClubs = original
    assert instance.aceClubs == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_COLUMN_FOUR_setter(instance):
    original = instance.COLUMN_FOUR
    instance.COLUMN_FOUR = original
    assert instance.COLUMN_FOUR == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_aceHearts_setter(instance):
    original = instance.aceHearts
    instance.aceHearts = original
    assert instance.aceHearts == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_ColTwo_setter(instance):
    original = instance.ColTwo
    instance.ColTwo = original
    assert instance.ColTwo == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_cellTwo_setter(instance):
    original = instance.cellTwo
    instance.cellTwo = original
    assert instance.cellTwo == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_COLUMN_ONE_setter(instance):
    original = instance.COLUMN_ONE
    instance.COLUMN_ONE = original
    assert instance.COLUMN_ONE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_cellFour_setter(instance):
    original = instance.cellFour
    instance.cellFour = original
    assert instance.cellFour == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_SPADES_ACE_PILE_setter(instance):
    original = instance.SPADES_ACE_PILE
    instance.SPADES_ACE_PILE = original
    assert instance.SPADES_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_cellOne_setter(instance):
    original = instance.cellOne
    instance.cellOne = original
    assert instance.cellOne == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_COLUMN_THREE_setter(instance):
    original = instance.COLUMN_THREE
    instance.COLUMN_THREE = original
    assert instance.COLUMN_THREE == original



@given(instance=SolitaireLayout_strategy)
def test_solitairelayout_ColThree_setter(instance):
    original = instance.ColThree
    instance.ColThree = original
    assert instance.ColThree == original

@given(instance=windowclosing_strategy)
@settings(max_examples=50)
def test_windowclosing_instantiation(instance):
    assert isinstance(instance, windowclosing)

@given(instance=TimerListener_strategy)
@settings(max_examples=50)
def test_timerlistener_instantiation(instance):
    assert isinstance(instance, TimerListener)

@given(instance=MyMouseListener_strategy)
@settings(max_examples=50)
def test_mymouselistener_instantiation(instance):
    assert isinstance(instance, MyMouseListener)



@given(instance=MyMouseListener_strategy)
def test_mymouselistener_temp_setter(instance):
    original = instance.temp
    instance.temp = original
    assert instance.temp == original



@given(instance=MyMouseListener_strategy)
def test_mymouselistener_rightClicked_setter(instance):
    original = instance.rightClicked
    instance.rightClicked = original
    assert instance.rightClicked == original



@given(instance=MyMouseListener_strategy)
def test_mymouselistener_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=MyMouseListener_strategy)
def test_mymouselistener_singleCardSelected_setter(instance):
    original = instance.singleCardSelected
    instance.singleCardSelected = original
    assert instance.singleCardSelected == original



@given(instance=MyMouseListener_strategy)
def test_mymouselistener_tempCard_setter(instance):
    original = instance.tempCard
    instance.tempCard = original
    assert instance.tempCard == original



@given(instance=MyMouseListener_strategy)
def test_mymouselistener_hasSelected_setter(instance):
    original = instance.hasSelected
    instance.hasSelected = original
    assert instance.hasSelected == original



@given(instance=MyMouseListener_strategy)
def test_mymouselistener_clickedCard_setter(instance):
    original = instance.clickedCard
    instance.clickedCard = original
    assert instance.clickedCard == original



@given(instance=MyMouseListener_strategy)
def test_mymouselistener_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original

@given(instance=SolitaireBoard_strategy)
@settings(max_examples=50)
def test_solitaireboard_instantiation(instance):
    assert isinstance(instance, SolitaireBoard)



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_newDrawCount_setter(instance):
    original = instance.newDrawCount
    instance.newDrawCount = original
    assert instance.newDrawCount == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_sourceList_setter(instance):
    original = instance.sourceList
    instance.sourceList = original
    assert instance.sourceList == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_RESET_STATS_setter(instance):
    original = instance.RESET_STATS
    instance.RESET_STATS = original
    assert instance.RESET_STATS == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_DO_NOTHING_setter(instance):
    original = instance.DO_NOTHING
    instance.DO_NOTHING = original
    assert instance.DO_NOTHING == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_GAME_LOST_setter(instance):
    original = instance.GAME_LOST
    instance.GAME_LOST = original
    assert instance.GAME_LOST == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timerCount_setter(instance):
    original = instance.timerCount
    instance.timerCount = original
    assert instance.timerCount == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_destinationList_setter(instance):
    original = instance.destinationList
    instance.destinationList = original
    assert instance.destinationList == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_statusBar_setter(instance):
    original = instance.statusBar
    instance.statusBar = original
    assert instance.statusBar == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_wl_setter(instance):
    original = instance.wl
    instance.wl = original
    assert instance.wl == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timerToRun_setter(instance):
    original = instance.timerToRun
    instance.timerToRun = original
    assert instance.timerToRun == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_winAnimationStatus_setter(instance):
    original = instance.winAnimationStatus
    instance.winAnimationStatus = original
    assert instance.winAnimationStatus == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_numCards_setter(instance):
    original = instance.numCards
    instance.numCards = original
    assert instance.numCards == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_acePiles_setter(instance):
    original = instance.acePiles
    instance.acePiles = original
    assert instance.acePiles == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_numCardsInDiscardView_setter(instance):
    original = instance.numCardsInDiscardView
    instance.numCardsInDiscardView = original
    assert instance.numCardsInDiscardView == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_GAME_WON_setter(instance):
    original = instance.GAME_WON
    instance.GAME_WON = original
    assert instance.GAME_WON == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_cells_setter(instance):
    original = instance.cells
    instance.cells = original
    assert instance.cells == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_dealDeck_setter(instance):
    original = instance.dealDeck
    instance.dealDeck = original
    assert instance.dealDeck == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_GAME_SAVED_setter(instance):
    original = instance.GAME_SAVED
    instance.GAME_SAVED = original
    assert instance.GAME_SAVED == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_newDifficulty_setter(instance):
    original = instance.newDifficulty
    instance.newDifficulty = original
    assert instance.newDifficulty == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timerLabel_setter(instance):
    original = instance.timerLabel
    instance.timerLabel = original
    assert instance.timerLabel == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_discardPile_setter(instance):
    original = instance.discardPile
    instance.discardPile = original
    assert instance.discardPile == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_backgroundNumber_setter(instance):
    original = instance.backgroundNumber
    instance.backgroundNumber = original
    assert instance.backgroundNumber == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_timerToRunNextGame_setter(instance):
    original = instance.timerToRunNextGame
    instance.timerToRunNextGame = original
    assert instance.timerToRunNextGame == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_ml_setter(instance):
    original = instance.ml
    instance.ml = original
    assert instance.ml == original



@given(instance=SolitaireBoard_strategy)
def test_solitaireboard_mainPanel_setter(instance):
    original = instance.mainPanel
    instance.mainPanel = original
    assert instance.mainPanel == original

@given(instance=SingleCell_strategy)
@settings(max_examples=50)
def test_singlecell_instantiation(instance):
    assert isinstance(instance, SingleCell)

@given(instance=FourRowSolitaire_strategy)
@settings(max_examples=50)
def test_fourrowsolitaire_instantiation(instance):
    assert isinstance(instance, FourRowSolitaire)



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_about_setter(instance):
    original = instance.about
    instance.about = original
    assert instance.about == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_game_setter(instance):
    original = instance.game
    instance.game = original
    assert instance.game == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_undo_setter(instance):
    original = instance.undo
    instance.undo = original
    assert instance.undo == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_helpMenu_setter(instance):
    original = instance.helpMenu
    instance.helpMenu = original
    assert instance.helpMenu == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_menubar_setter(instance):
    original = instance.menubar
    instance.menubar = original
    assert instance.menubar == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_checkUpdate_setter(instance):
    original = instance.checkUpdate
    instance.checkUpdate = original
    assert instance.checkUpdate == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_statistics_setter(instance):
    original = instance.statistics
    instance.statistics = original
    assert instance.statistics == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_help_setter(instance):
    original = instance.help
    instance.help = original
    assert instance.help == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_newGame_setter(instance):
    original = instance.newGame
    instance.newGame = original
    assert instance.newGame == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_hint_setter(instance):
    original = instance.hint
    instance.hint = original
    assert instance.hint == original



@given(instance=FourRowSolitaire_strategy)
def test_fourrowsolitaire_appearance_setter(instance):
    original = instance.appearance
    instance.appearance = original
    assert instance.appearance == original

@given(instance=FireworksDisplay_strategy)
@settings(max_examples=50)
def test_fireworksdisplay_instantiation(instance):
    assert isinstance(instance, FireworksDisplay)



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_SET_DELAY_setter(instance):
    original = instance.SET_DELAY
    instance.SET_DELAY = original
    assert instance.SET_DELAY == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_yy_setter(instance):
    original = instance.yy
    instance.yy = original
    assert instance.yy == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_NUM_FIREWORKS_setter(instance):
    original = instance.NUM_FIREWORKS
    instance.NUM_FIREWORKS = original
    assert instance.NUM_FIREWORKS == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_FIREWORKS_SIZE_setter(instance):
    original = instance.FIREWORKS_SIZE
    instance.FIREWORKS_SIZE = original
    assert instance.FIREWORKS_SIZE == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_xx_setter(instance):
    original = instance.xx
    instance.xx = original
    assert instance.xx == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_FIREWORKS_TIME_setter(instance):
    original = instance.FIREWORKS_TIME
    instance.FIREWORKS_TIME = original
    assert instance.FIREWORKS_TIME == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_numSets_setter(instance):
    original = instance.numSets
    instance.numSets = original
    assert instance.numSets == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_colors_setter(instance):
    original = instance.colors
    instance.colors = original
    assert instance.colors == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=FireworksDisplay_strategy)
def test_fireworksdisplay_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=DiscardPile_strategy)
@settings(max_examples=50)
def test_discardpile_instantiation(instance):
    assert isinstance(instance, DiscardPile)



@given(instance=DiscardPile_strategy)
def test_discardpile_CardsLeftFromDraw_setter(instance):
    original = instance.CardsLeftFromDraw
    instance.CardsLeftFromDraw = original
    assert instance.CardsLeftFromDraw == original



@given(instance=DiscardPile_strategy)
def test_discardpile_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=Deck_strategy)
def test_deck_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original

@given(instance=DealDeck_strategy)
@settings(max_examples=50)
def test_dealdeck_instantiation(instance):
    assert isinstance(instance, DealDeck)



@given(instance=DealDeck_strategy)
def test_dealdeck_MEDIUM_THROUGH_LIMIT_setter(instance):
    original = instance.MEDIUM_THROUGH_LIMIT
    instance.MEDIUM_THROUGH_LIMIT = original
    assert instance.MEDIUM_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_dealdeck_DRAW_THREE_THROUGH_LIMIT_setter(instance):
    original = instance.DRAW_THREE_THROUGH_LIMIT
    instance.DRAW_THREE_THROUGH_LIMIT = original
    assert instance.DRAW_THREE_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_dealdeck_deckThroughLimit_setter(instance):
    original = instance.deckThroughLimit
    instance.deckThroughLimit = original
    assert instance.deckThroughLimit == original



@given(instance=DealDeck_strategy)
def test_dealdeck_redealable_setter(instance):
    original = instance.redealable
    instance.redealable = original
    assert instance.redealable == original



@given(instance=DealDeck_strategy)
def test_dealdeck_EASY_THROUGH_LIMIT_setter(instance):
    original = instance.EASY_THROUGH_LIMIT
    instance.EASY_THROUGH_LIMIT = original
    assert instance.EASY_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_dealdeck_HARD_THROUGH_LIMIT_setter(instance):
    original = instance.HARD_THROUGH_LIMIT
    instance.HARD_THROUGH_LIMIT = original
    assert instance.HARD_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_dealdeck_numTimesThroughDeck_setter(instance):
    original = instance.numTimesThroughDeck
    instance.numTimesThroughDeck = original
    assert instance.numTimesThroughDeck == original



@given(instance=DealDeck_strategy)
def test_dealdeck_discardPile_setter(instance):
    original = instance.discardPile
    instance.discardPile = original
    assert instance.discardPile == original



@given(instance=DealDeck_strategy)
def test_dealdeck_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original



@given(instance=DealDeck_strategy)
def test_dealdeck_DRAW_ONE_THROUGH_LIMIT_setter(instance):
    original = instance.DRAW_ONE_THROUGH_LIMIT
    instance.DRAW_ONE_THROUGH_LIMIT = original
    assert instance.DRAW_ONE_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_dealdeck_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=ChangeOptions_strategy)
@settings(max_examples=50)
def test_changeoptions_instantiation(instance):
    assert isinstance(instance, ChangeOptions)



@given(instance=ChangeOptions_strategy)
def test_changeoptions_medium_setter(instance):
    original = instance.medium
    instance.medium = original
    assert instance.medium == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_drawThree_setter(instance):
    original = instance.drawThree
    instance.drawThree = original
    assert instance.drawThree == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_hard_setter(instance):
    original = instance.hard
    instance.hard = original
    assert instance.hard == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_exited_setter(instance):
    original = instance.exited
    instance.exited = original
    assert instance.exited == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_drawOne_setter(instance):
    original = instance.drawOne
    instance.drawOne = original
    assert instance.drawOne == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_timerCheck_setter(instance):
    original = instance.timerCheck
    instance.timerCheck = original
    assert instance.timerCheck == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_easy_setter(instance):
    original = instance.easy
    instance.easy = original
    assert instance.easy == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_animation_setter(instance):
    original = instance.animation
    instance.animation = original
    assert instance.animation == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_ok_setter(instance):
    original = instance.ok
    instance.ok = original
    assert instance.ok == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_winAnimationCheck_setter(instance):
    original = instance.winAnimationCheck
    instance.winAnimationCheck = original
    assert instance.winAnimationCheck == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_sounds_setter(instance):
    original = instance.sounds
    instance.sounds = original
    assert instance.sounds == original



@given(instance=ChangeOptions_strategy)
def test_changeoptions_winSoundCheck_setter(instance):
    original = instance.winSoundCheck
    instance.winSoundCheck = original
    assert instance.winSoundCheck == original

@given(instance=ChangeAppearance_strategy)
@settings(max_examples=50)
def test_changeappearance_instantiation(instance):
    assert isinstance(instance, ChangeAppearance)



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_backgroundNumber_setter(instance):
    original = instance.backgroundNumber
    instance.backgroundNumber = original
    assert instance.backgroundNumber == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_backgrounds_setter(instance):
    original = instance.backgrounds
    instance.backgrounds = original
    assert instance.backgrounds == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_backGroundLabel_setter(instance):
    original = instance.backGroundLabel
    instance.backGroundLabel = original
    assert instance.backGroundLabel == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_ok_setter(instance):
    original = instance.ok
    instance.ok = original
    assert instance.ok == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_NUM_DECKS_setter(instance):
    original = instance.NUM_DECKS
    instance.NUM_DECKS = original
    assert instance.NUM_DECKS == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_FRS_BACKGROUND_setter(instance):
    original = instance.FRS_BACKGROUND
    instance.FRS_BACKGROUND = original
    assert instance.FRS_BACKGROUND == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_cardBackLabel_setter(instance):
    original = instance.cardBackLabel
    instance.cardBackLabel = original
    assert instance.cardBackLabel == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_decks_setter(instance):
    original = instance.decks
    instance.decks = original
    assert instance.decks == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_FRS_DECK_setter(instance):
    original = instance.FRS_DECK
    instance.FRS_DECK = original
    assert instance.FRS_DECK == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_exited_setter(instance):
    original = instance.exited
    instance.exited = original
    assert instance.exited == original



@given(instance=ChangeAppearance_strategy)
def test_changeappearance_NUM_BACKGROUNDS_setter(instance):
    original = instance.NUM_BACKGROUNDS
    instance.NUM_BACKGROUNDS = original
    assert instance.NUM_BACKGROUNDS == original

@given(instance=CardStack_strategy)
@settings(max_examples=50)
def test_cardstack_instantiation(instance):
    assert isinstance(instance, CardStack)



@given(instance=CardStack_strategy)
def test_cardstack_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_TWO_setter(instance):
    original = instance.TWO
    instance.TWO = original
    assert instance.TWO == original



@given(instance=Card_strategy)
def test_card_HEARTS_SUIT_setter(instance):
    original = instance.HEARTS_SUIT
    instance.HEARTS_SUIT = original
    assert instance.HEARTS_SUIT == original



@given(instance=Card_strategy)
def test_card_SIX_setter(instance):
    original = instance.SIX
    instance.SIX = original
    assert instance.SIX == original



@given(instance=Card_strategy)
def test_card_cardSuit_setter(instance):
    original = instance.cardSuit
    instance.cardSuit = original
    assert instance.cardSuit == original



@given(instance=Card_strategy)
def test_card_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original



@given(instance=Card_strategy)
def test_card_cardImageString_setter(instance):
    original = instance.cardImageString
    instance.cardImageString = original
    assert instance.cardImageString == original



@given(instance=Card_strategy)
def test_card_INVALID_NUMBER_setter(instance):
    original = instance.INVALID_NUMBER
    instance.INVALID_NUMBER = original
    assert instance.INVALID_NUMBER == original



@given(instance=Card_strategy)
def test_card_FIVE_setter(instance):
    original = instance.FIVE
    instance.FIVE = original
    assert instance.FIVE == original



@given(instance=Card_strategy)
def test_card_highlighted_setter(instance):
    original = instance.highlighted
    instance.highlighted = original
    assert instance.highlighted == original



@given(instance=Card_strategy)
def test_card_FOUR_setter(instance):
    original = instance.FOUR
    instance.FOUR = original
    assert instance.FOUR == original



@given(instance=Card_strategy)
def test_card_fullCardNumber_setter(instance):
    original = instance.fullCardNumber
    instance.fullCardNumber = original
    assert instance.fullCardNumber == original



@given(instance=Card_strategy)
def test_card_int_deckNumber_setter(instance):
    original = instance.int_deckNumber
    instance.int_deckNumber = original
    assert instance.int_deckNumber == original



@given(instance=Card_strategy)
def test_card_KING_setter(instance):
    original = instance.KING
    instance.KING = original
    assert instance.KING == original



@given(instance=Card_strategy)
def test_card_TEN_setter(instance):
    original = instance.TEN
    instance.TEN = original
    assert instance.TEN == original



@given(instance=Card_strategy)
def test_card_SPADES_SUIT_setter(instance):
    original = instance.SPADES_SUIT
    instance.SPADES_SUIT = original
    assert instance.SPADES_SUIT == original



@given(instance=Card_strategy)
def test_card_INVALID_SUIT_setter(instance):
    original = instance.INVALID_SUIT
    instance.INVALID_SUIT = original
    assert instance.INVALID_SUIT == original



@given(instance=Card_strategy)
def test_card_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=Card_strategy)
def test_card_cardColor_setter(instance):
    original = instance.cardColor
    instance.cardColor = original
    assert instance.cardColor == original



@given(instance=Card_strategy)
def test_card_CLUBS_SUIT_setter(instance):
    original = instance.CLUBS_SUIT
    instance.CLUBS_SUIT = original
    assert instance.CLUBS_SUIT == original



@given(instance=Card_strategy)
def test_card_faceUp_setter(instance):
    original = instance.faceUp
    instance.faceUp = original
    assert instance.faceUp == original



@given(instance=Card_strategy)
def test_card_EIGHT_setter(instance):
    original = instance.EIGHT
    instance.EIGHT = original
    assert instance.EIGHT == original



@given(instance=Card_strategy)
def test_card_JACK_setter(instance):
    original = instance.JACK
    instance.JACK = original
    assert instance.JACK == original



@given(instance=Card_strategy)
def test_card_THREE_setter(instance):
    original = instance.THREE
    instance.THREE = original
    assert instance.THREE == original



@given(instance=Card_strategy)
def test_card_NINE_setter(instance):
    original = instance.NINE
    instance.NINE = original
    assert instance.NINE == original



@given(instance=Card_strategy)
def test_card_cardBack_setter(instance):
    original = instance.cardBack
    instance.cardBack = original
    assert instance.cardBack == original



@given(instance=Card_strategy)
def test_card_SEVEN_setter(instance):
    original = instance.SEVEN
    instance.SEVEN = original
    assert instance.SEVEN == original



@given(instance=Card_strategy)
def test_card_DIAMONDS_SUIT_setter(instance):
    original = instance.DIAMONDS_SUIT
    instance.DIAMONDS_SUIT = original
    assert instance.DIAMONDS_SUIT == original



@given(instance=Card_strategy)
def test_card_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Card_strategy)
def test_card_cardHighLighted_setter(instance):
    original = instance.cardHighLighted
    instance.cardHighLighted = original
    assert instance.cardHighLighted == original



@given(instance=Card_strategy)
def test_card_ACE_setter(instance):
    original = instance.ACE
    instance.ACE = original
    assert instance.ACE == original



@given(instance=Card_strategy)
def test_card_QUEEN_setter(instance):
    original = instance.QUEEN
    instance.QUEEN = original
    assert instance.QUEEN == original

@given(instance=AcePile_strategy)
@settings(max_examples=50)
def test_acepile_instantiation(instance):
    assert isinstance(instance, AcePile)



@given(instance=AcePile_strategy)
def test_acepile_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original

@given(instance=Four_Row_Solitaire___Component_strategy)
@settings(max_examples=50)
def test_four_row_solitaire___component_instantiation(instance):
    assert isinstance(instance, Four_Row_Solitaire___Component)

@given(instance=User_Actor_strategy)
@settings(max_examples=50)
def test_user_actor_instantiation(instance):
    assert isinstance(instance, User_Actor)
