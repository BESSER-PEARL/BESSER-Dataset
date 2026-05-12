import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Connect4,
    MainMenuGUI,
    GameBoard,
    ScoreBoardGUI,
    Button,
    Connect4GUI,
    GameboardGUI,
    Piece,
    RandomPlayer,
    AIplayer,
    ConsolePlayer,
    Player_Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_connect4_is_not_abstract():
    assert not inspect.isabstract(Connect4)


def test_connect4_constructor_exists():
    assert callable(Connect4.__init__)


def test_connect4_constructor_args():
    sig = inspect.signature(Connect4.__init__)
    params = list(sig.parameters.keys())



def test_mainmenugui_is_not_abstract():
    assert not inspect.isabstract(MainMenuGUI)


def test_mainmenugui_constructor_exists():
    assert callable(MainMenuGUI.__init__)


def test_mainmenugui_constructor_args():
    sig = inspect.signature(MainMenuGUI.__init__)
    params = list(sig.parameters.keys())



def test_gameboard_is_not_abstract():
    assert not inspect.isabstract(GameBoard)


def test_gameboard_constructor_exists():
    assert callable(GameBoard.__init__)


def test_gameboard_constructor_args():
    sig = inspect.signature(GameBoard.__init__)
    params = list(sig.parameters.keys())
    assert "player2" in params, "Missing parameter 'player2'"
    assert "whoPlay" in params, "Missing parameter 'whoPlay'"
    assert "board" in params, "Missing parameter 'board'"
    assert "player1" in params, "Missing parameter 'player1'"

def test_gameboard_has_player2():
    assert hasattr(GameBoard, "player2")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "player2" in klass.__dict__:
            descriptor = klass.__dict__["player2"]
            break
    assert isinstance(descriptor, property)

def test_gameboard_has_whoPlay():
    assert hasattr(GameBoard, "whoPlay")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "whoPlay" in klass.__dict__:
            descriptor = klass.__dict__["whoPlay"]
            break
    assert isinstance(descriptor, property)

def test_gameboard_has_board():
    assert hasattr(GameBoard, "board")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)

def test_gameboard_has_player1():
    assert hasattr(GameBoard, "player1")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "player1" in klass.__dict__:
            descriptor = klass.__dict__["player1"]
            break
    assert isinstance(descriptor, property)



def test_scoreboardgui_is_not_abstract():
    assert not inspect.isabstract(ScoreBoardGUI)


def test_scoreboardgui_constructor_exists():
    assert callable(ScoreBoardGUI.__init__)


def test_scoreboardgui_constructor_args():
    sig = inspect.signature(ScoreBoardGUI.__init__)
    params = list(sig.parameters.keys())
    assert "playersList" in params, "Missing parameter 'playersList'"

def test_scoreboardgui_has_playersList():
    assert hasattr(ScoreBoardGUI, "playersList")
    descriptor = None
    for klass in ScoreBoardGUI.__mro__:
        if "playersList" in klass.__dict__:
            descriptor = klass.__dict__["playersList"]
            break
    assert isinstance(descriptor, property)



def test_button_is_not_abstract():
    assert not inspect.isabstract(Button)


def test_button_constructor_exists():
    assert callable(Button.__init__)


def test_button_constructor_args():
    sig = inspect.signature(Button.__init__)
    params = list(sig.parameters.keys())



def test_connect4gui_is_not_abstract():
    assert not inspect.isabstract(Connect4GUI)


def test_connect4gui_constructor_exists():
    assert callable(Connect4GUI.__init__)


def test_connect4gui_constructor_args():
    sig = inspect.signature(Connect4GUI.__init__)
    params = list(sig.parameters.keys())
    assert "undo" in params, "Missing parameter 'undo'"
    assert "root" in params, "Missing parameter 'root'"

def test_connect4gui_has_undo():
    assert hasattr(Connect4GUI, "undo")
    descriptor = None
    for klass in Connect4GUI.__mro__:
        if "undo" in klass.__dict__:
            descriptor = klass.__dict__["undo"]
            break
    assert isinstance(descriptor, property)

def test_connect4gui_has_root():
    assert hasattr(Connect4GUI, "root")
    descriptor = None
    for klass in Connect4GUI.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)



def test_gameboardgui_is_not_abstract():
    assert not inspect.isabstract(GameboardGUI)


def test_gameboardgui_constructor_exists():
    assert callable(GameboardGUI.__init__)


def test_gameboardgui_constructor_args():
    sig = inspect.signature(GameboardGUI.__init__)
    params = list(sig.parameters.keys())
    assert "rows" in params, "Missing parameter 'rows'"
    assert "columns" in params, "Missing parameter 'columns'"
    assert "piecesList" in params, "Missing parameter 'piecesList'"

def test_gameboardgui_has_rows():
    assert hasattr(GameboardGUI, "rows")
    descriptor = None
    for klass in GameboardGUI.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)

def test_gameboardgui_has_columns():
    assert hasattr(GameboardGUI, "columns")
    descriptor = None
    for klass in GameboardGUI.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)

def test_gameboardgui_has_piecesList():
    assert hasattr(GameboardGUI, "piecesList")
    descriptor = None
    for klass in GameboardGUI.__mro__:
        if "piecesList" in klass.__dict__:
            descriptor = klass.__dict__["piecesList"]
            break
    assert isinstance(descriptor, property)



def test_piece_is_not_abstract():
    assert not inspect.isabstract(Piece)


def test_piece_constructor_exists():
    assert callable(Piece.__init__)


def test_piece_constructor_args():
    sig = inspect.signature(Piece.__init__)
    params = list(sig.parameters.keys())
    assert "pieceColor" in params, "Missing parameter 'pieceColor'"
    assert "pieceSize" in params, "Missing parameter 'pieceSize'"

def test_piece_has_pieceColor():
    assert hasattr(Piece, "pieceColor")
    descriptor = None
    for klass in Piece.__mro__:
        if "pieceColor" in klass.__dict__:
            descriptor = klass.__dict__["pieceColor"]
            break
    assert isinstance(descriptor, property)

def test_piece_has_pieceSize():
    assert hasattr(Piece, "pieceSize")
    descriptor = None
    for klass in Piece.__mro__:
        if "pieceSize" in klass.__dict__:
            descriptor = klass.__dict__["pieceSize"]
            break
    assert isinstance(descriptor, property)



def test_randomplayer_is_not_abstract():
    assert not inspect.isabstract(RandomPlayer)


def test_randomplayer_constructor_exists():
    assert callable(RandomPlayer.__init__)


def test_randomplayer_constructor_args():
    sig = inspect.signature(RandomPlayer.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"
    assert "name" in params, "Missing parameter 'name'"

def test_randomplayer_has_score():
    assert hasattr(RandomPlayer, "score")
    descriptor = None
    for klass in RandomPlayer.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)

def test_randomplayer_has_name():
    assert hasattr(RandomPlayer, "name")
    descriptor = None
    for klass in RandomPlayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_aiplayer_is_not_abstract():
    assert not inspect.isabstract(AIplayer)


def test_aiplayer_constructor_exists():
    assert callable(AIplayer.__init__)


def test_aiplayer_constructor_args():
    sig = inspect.signature(AIplayer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "score" in params, "Missing parameter 'score'"

def test_aiplayer_has_name():
    assert hasattr(AIplayer, "name")
    descriptor = None
    for klass in AIplayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_aiplayer_has_score():
    assert hasattr(AIplayer, "score")
    descriptor = None
    for klass in AIplayer.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)



def test_consoleplayer_is_not_abstract():
    assert not inspect.isabstract(ConsolePlayer)


def test_consoleplayer_constructor_exists():
    assert callable(ConsolePlayer.__init__)


def test_consoleplayer_constructor_args():
    sig = inspect.signature(ConsolePlayer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "score" in params, "Missing parameter 'score'"

def test_consoleplayer_has_name():
    assert hasattr(ConsolePlayer, "name")
    descriptor = None
    for klass in ConsolePlayer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_consoleplayer_has_score():
    assert hasattr(ConsolePlayer, "score")
    descriptor = None
    for klass in ConsolePlayer.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)



def test_player_interface_is_not_abstract():
    assert not inspect.isabstract(Player_Interface)


def test_player_interface_constructor_exists():
    assert callable(Player_Interface.__init__)


def test_player_interface_constructor_args():
    sig = inspect.signature(Player_Interface.__init__)
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
Connect4_strategy = st.builds(
    Connect4,
)
MainMenuGUI_strategy = st.builds(
    MainMenuGUI,
)
GameBoard_strategy = st.builds(
    GameBoard,
    player2=
        st.none(),
    whoPlay=
        safe_text,
    board=
        safe_text,
    player1=
        st.none()
)
ScoreBoardGUI_strategy = st.builds(
    ScoreBoardGUI,
    playersList=
        safe_text
)
Button_strategy = st.builds(
    Button,
)
Connect4GUI_strategy = st.builds(
    Connect4GUI,
    undo=
        st.none(),
    root=
        safe_text
)
GameboardGUI_strategy = st.builds(
    GameboardGUI,
    rows=
        st.integers(),
    columns=
        st.integers(),
    piecesList=
        safe_text
)
Piece_strategy = st.builds(
    Piece,
    pieceColor=
        safe_text,
    pieceSize=
        st.integers()
)
RandomPlayer_strategy = st.builds(
    RandomPlayer,
    score=
        safe_text,
    name=
        safe_text
)
AIplayer_strategy = st.builds(
    AIplayer,
    name=
        safe_text,
    score=
        safe_text
)
ConsolePlayer_strategy = st.builds(
    ConsolePlayer,
    name=
        safe_text,
    score=
        safe_text
)
Player_Interface_strategy = st.builds(
    Player_Interface,
)

@given(instance=Connect4_strategy)
@settings(max_examples=50)
def test_connect4_instantiation(instance):
    assert isinstance(instance, Connect4)

@given(instance=MainMenuGUI_strategy)
@settings(max_examples=50)
def test_mainmenugui_instantiation(instance):
    assert isinstance(instance, MainMenuGUI)

@given(instance=GameBoard_strategy)
@settings(max_examples=50)
def test_gameboard_instantiation(instance):
    assert isinstance(instance, GameBoard)



@given(instance=GameBoard_strategy)
def test_gameboard_player2_setter(instance):
    original = instance.player2
    instance.player2 = original
    assert instance.player2 == original



@given(instance=GameBoard_strategy)
def test_gameboard_whoPlay_setter(instance):
    original = instance.whoPlay
    instance.whoPlay = original
    assert instance.whoPlay == original



@given(instance=GameBoard_strategy)
def test_gameboard_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original



@given(instance=GameBoard_strategy)
def test_gameboard_player1_setter(instance):
    original = instance.player1
    instance.player1 = original
    assert instance.player1 == original

@given(instance=ScoreBoardGUI_strategy)
@settings(max_examples=50)
def test_scoreboardgui_instantiation(instance):
    assert isinstance(instance, ScoreBoardGUI)



@given(instance=ScoreBoardGUI_strategy)
def test_scoreboardgui_playersList_setter(instance):
    original = instance.playersList
    instance.playersList = original
    assert instance.playersList == original

@given(instance=Button_strategy)
@settings(max_examples=50)
def test_button_instantiation(instance):
    assert isinstance(instance, Button)

@given(instance=Connect4GUI_strategy)
@settings(max_examples=50)
def test_connect4gui_instantiation(instance):
    assert isinstance(instance, Connect4GUI)



@given(instance=Connect4GUI_strategy)
def test_connect4gui_undo_setter(instance):
    original = instance.undo
    instance.undo = original
    assert instance.undo == original



@given(instance=Connect4GUI_strategy)
def test_connect4gui_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original

@given(instance=GameboardGUI_strategy)
@settings(max_examples=50)
def test_gameboardgui_instantiation(instance):
    assert isinstance(instance, GameboardGUI)



@given(instance=GameboardGUI_strategy)
def test_gameboardgui_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original



@given(instance=GameboardGUI_strategy)
def test_gameboardgui_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=GameboardGUI_strategy)
def test_gameboardgui_piecesList_setter(instance):
    original = instance.piecesList
    instance.piecesList = original
    assert instance.piecesList == original

@given(instance=Piece_strategy)
@settings(max_examples=50)
def test_piece_instantiation(instance):
    assert isinstance(instance, Piece)



@given(instance=Piece_strategy)
def test_piece_pieceColor_setter(instance):
    original = instance.pieceColor
    instance.pieceColor = original
    assert instance.pieceColor == original



@given(instance=Piece_strategy)
def test_piece_pieceSize_setter(instance):
    original = instance.pieceSize
    instance.pieceSize = original
    assert instance.pieceSize == original

@given(instance=RandomPlayer_strategy)
@settings(max_examples=50)
def test_randomplayer_instantiation(instance):
    assert isinstance(instance, RandomPlayer)



@given(instance=RandomPlayer_strategy)
def test_randomplayer_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=RandomPlayer_strategy)
def test_randomplayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AIplayer_strategy)
@settings(max_examples=50)
def test_aiplayer_instantiation(instance):
    assert isinstance(instance, AIplayer)



@given(instance=AIplayer_strategy)
def test_aiplayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=AIplayer_strategy)
def test_aiplayer_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original

@given(instance=ConsolePlayer_strategy)
@settings(max_examples=50)
def test_consoleplayer_instantiation(instance):
    assert isinstance(instance, ConsolePlayer)



@given(instance=ConsolePlayer_strategy)
def test_consoleplayer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ConsolePlayer_strategy)
def test_consoleplayer_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original

@given(instance=Player_Interface_strategy)
@settings(max_examples=50)
def test_player_interface_instantiation(instance):
    assert isinstance(instance, Player_Interface)
