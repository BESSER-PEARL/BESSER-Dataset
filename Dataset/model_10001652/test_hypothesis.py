import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    List,
    Player,
    Board,
    T,
    Spot,
    Knight,
    Queen,
    King,
    Bishop,
    Rook,
    Pawn,
    Piece,
    Color,
    List_Pieces_,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_list_is_not_abstract():
    assert not inspect.isabstract(List)


def test_list_constructor_exists():
    assert callable(List.__init__)


def test_list_constructor_args():
    sig = inspect.signature(List.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pieces" in params, "Missing parameter 'pieces'"
    assert "color" in params, "Missing parameter 'color'"

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_player_has_pieces():
    assert hasattr(Player, "pieces")
    descriptor = None
    for klass in Player.__mro__:
        if "pieces" in klass.__dict__:
            descriptor = klass.__dict__["pieces"]
            break
    assert isinstance(descriptor, property)

def test_player_has_color():
    assert hasattr(Player, "color")
    descriptor = None
    for klass in Player.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_board_is_not_abstract():
    assert not inspect.isabstract(Board)


def test_board_constructor_exists():
    assert callable(Board.__init__)


def test_board_constructor_args():
    sig = inspect.signature(Board.__init__)
    params = list(sig.parameters.keys())
    assert "isStaleMate" in params, "Missing parameter 'isStaleMate'"
    assert "blackPlayer" in params, "Missing parameter 'blackPlayer'"
    assert "currentPlayer" in params, "Missing parameter 'currentPlayer'"
    assert "spots" in params, "Missing parameter 'spots'"
    assert "whitePlayer" in params, "Missing parameter 'whitePlayer'"
    assert "isCheck" in params, "Missing parameter 'isCheck'"
    assert "isCheckMate" in params, "Missing parameter 'isCheckMate'"

def test_board_has_isStaleMate():
    assert hasattr(Board, "isStaleMate")
    descriptor = None
    for klass in Board.__mro__:
        if "isStaleMate" in klass.__dict__:
            descriptor = klass.__dict__["isStaleMate"]
            break
    assert isinstance(descriptor, property)

def test_board_has_blackPlayer():
    assert hasattr(Board, "blackPlayer")
    descriptor = None
    for klass in Board.__mro__:
        if "blackPlayer" in klass.__dict__:
            descriptor = klass.__dict__["blackPlayer"]
            break
    assert isinstance(descriptor, property)

def test_board_has_currentPlayer():
    assert hasattr(Board, "currentPlayer")
    descriptor = None
    for klass in Board.__mro__:
        if "currentPlayer" in klass.__dict__:
            descriptor = klass.__dict__["currentPlayer"]
            break
    assert isinstance(descriptor, property)

def test_board_has_spots():
    assert hasattr(Board, "spots")
    descriptor = None
    for klass in Board.__mro__:
        if "spots" in klass.__dict__:
            descriptor = klass.__dict__["spots"]
            break
    assert isinstance(descriptor, property)

def test_board_has_whitePlayer():
    assert hasattr(Board, "whitePlayer")
    descriptor = None
    for klass in Board.__mro__:
        if "whitePlayer" in klass.__dict__:
            descriptor = klass.__dict__["whitePlayer"]
            break
    assert isinstance(descriptor, property)

def test_board_has_isCheck():
    assert hasattr(Board, "isCheck")
    descriptor = None
    for klass in Board.__mro__:
        if "isCheck" in klass.__dict__:
            descriptor = klass.__dict__["isCheck"]
            break
    assert isinstance(descriptor, property)

def test_board_has_isCheckMate():
    assert hasattr(Board, "isCheckMate")
    descriptor = None
    for klass in Board.__mro__:
        if "isCheckMate" in klass.__dict__:
            descriptor = klass.__dict__["isCheckMate"]
            break
    assert isinstance(descriptor, property)



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_spot_is_not_abstract():
    assert not inspect.isabstract(Spot)


def test_spot_constructor_exists():
    assert callable(Spot.__init__)


def test_spot_constructor_args():
    sig = inspect.signature(Spot.__init__)
    params = list(sig.parameters.keys())
    assert "piece" in params, "Missing parameter 'piece'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_spot_has_piece():
    assert hasattr(Spot, "piece")
    descriptor = None
    for klass in Spot.__mro__:
        if "piece" in klass.__dict__:
            descriptor = klass.__dict__["piece"]
            break
    assert isinstance(descriptor, property)

def test_spot_has_x():
    assert hasattr(Spot, "x")
    descriptor = None
    for klass in Spot.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_spot_has_y():
    assert hasattr(Spot, "y")
    descriptor = None
    for klass in Spot.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_knight_is_not_abstract():
    assert not inspect.isabstract(Knight)


def test_knight_constructor_exists():
    assert callable(Knight.__init__)


def test_knight_constructor_args():
    sig = inspect.signature(Knight.__init__)
    params = list(sig.parameters.keys())



def test_queen_is_not_abstract():
    assert not inspect.isabstract(Queen)


def test_queen_constructor_exists():
    assert callable(Queen.__init__)


def test_queen_constructor_args():
    sig = inspect.signature(Queen.__init__)
    params = list(sig.parameters.keys())



def test_king_is_not_abstract():
    assert not inspect.isabstract(King)


def test_king_constructor_exists():
    assert callable(King.__init__)


def test_king_constructor_args():
    sig = inspect.signature(King.__init__)
    params = list(sig.parameters.keys())



def test_bishop_is_not_abstract():
    assert not inspect.isabstract(Bishop)


def test_bishop_constructor_exists():
    assert callable(Bishop.__init__)


def test_bishop_constructor_args():
    sig = inspect.signature(Bishop.__init__)
    params = list(sig.parameters.keys())



def test_rook_is_not_abstract():
    assert not inspect.isabstract(Rook)


def test_rook_constructor_exists():
    assert callable(Rook.__init__)


def test_rook_constructor_args():
    sig = inspect.signature(Rook.__init__)
    params = list(sig.parameters.keys())



def test_pawn_is_not_abstract():
    assert not inspect.isabstract(Pawn)


def test_pawn_constructor_exists():
    assert callable(Pawn.__init__)


def test_pawn_constructor_args():
    sig = inspect.signature(Pawn.__init__)
    params = list(sig.parameters.keys())



def test_piece_is_not_abstract():
    assert not inspect.isabstract(Piece)


def test_piece_constructor_exists():
    assert callable(Piece.__init__)


def test_piece_constructor_args():
    sig = inspect.signature(Piece.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "color" in params, "Missing parameter 'color'"
    assert "y" in params, "Missing parameter 'y'"

def test_piece_has_x():
    assert hasattr(Piece, "x")
    descriptor = None
    for klass in Piece.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_piece_has_color():
    assert hasattr(Piece, "color")
    descriptor = None
    for klass in Piece.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_piece_has_y():
    assert hasattr(Piece, "y")
    descriptor = None
    for klass in Piece.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_list_pieces__exists():
    # Check that the Enumeration exists
    assert List_Pieces_ is not None

def test_list_pieces__has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in List_Pieces_]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in List_Pieces_"


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
List_strategy = st.builds(
    List,
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    pieces=
        st.none(),
    color=
        st.none()
)
Board_strategy = st.builds(
    Board,
    isStaleMate=
        st.booleans(),
    blackPlayer=
        st.none(),
    currentPlayer=
        st.none(),
    spots=
        safe_text,
    whitePlayer=
        st.none(),
    isCheck=
        st.booleans(),
    isCheckMate=
        st.booleans()
)
T_strategy = st.builds(
    T,
)
Spot_strategy = st.builds(
    Spot,
    piece=
        st.none(),
    x=
        st.integers(),
    y=
        st.integers()
)
Knight_strategy = st.builds(
    Knight,
)
Queen_strategy = st.builds(
    Queen,
)
King_strategy = st.builds(
    King,
)
Bishop_strategy = st.builds(
    Bishop,
)
Rook_strategy = st.builds(
    Rook,
)
Pawn_strategy = st.builds(
    Pawn,
)
Piece_strategy = st.builds(
    Piece,
    x=
        st.integers(),
    color=
        st.none(),
    y=
        st.integers()
)

@given(instance=List_strategy)
@settings(max_examples=50)
def test_list_instantiation(instance):
    assert isinstance(instance, List)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_player_pieces_setter(instance):
    original = instance.pieces
    instance.pieces = original
    assert instance.pieces == original



@given(instance=Player_strategy)
def test_player_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=Board_strategy)
@settings(max_examples=50)
def test_board_instantiation(instance):
    assert isinstance(instance, Board)



@given(instance=Board_strategy)
def test_board_isStaleMate_setter(instance):
    original = instance.isStaleMate
    instance.isStaleMate = original
    assert instance.isStaleMate == original



@given(instance=Board_strategy)
def test_board_blackPlayer_setter(instance):
    original = instance.blackPlayer
    instance.blackPlayer = original
    assert instance.blackPlayer == original



@given(instance=Board_strategy)
def test_board_currentPlayer_setter(instance):
    original = instance.currentPlayer
    instance.currentPlayer = original
    assert instance.currentPlayer == original



@given(instance=Board_strategy)
def test_board_spots_setter(instance):
    original = instance.spots
    instance.spots = original
    assert instance.spots == original



@given(instance=Board_strategy)
def test_board_whitePlayer_setter(instance):
    original = instance.whitePlayer
    instance.whitePlayer = original
    assert instance.whitePlayer == original



@given(instance=Board_strategy)
def test_board_isCheck_setter(instance):
    original = instance.isCheck
    instance.isCheck = original
    assert instance.isCheck == original



@given(instance=Board_strategy)
def test_board_isCheckMate_setter(instance):
    original = instance.isCheckMate
    instance.isCheckMate = original
    assert instance.isCheckMate == original

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=Spot_strategy)
@settings(max_examples=50)
def test_spot_instantiation(instance):
    assert isinstance(instance, Spot)



@given(instance=Spot_strategy)
def test_spot_piece_setter(instance):
    original = instance.piece
    instance.piece = original
    assert instance.piece == original



@given(instance=Spot_strategy)
def test_spot_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Spot_strategy)
def test_spot_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Knight_strategy)
@settings(max_examples=50)
def test_knight_instantiation(instance):
    assert isinstance(instance, Knight)

@given(instance=Queen_strategy)
@settings(max_examples=50)
def test_queen_instantiation(instance):
    assert isinstance(instance, Queen)

@given(instance=King_strategy)
@settings(max_examples=50)
def test_king_instantiation(instance):
    assert isinstance(instance, King)

@given(instance=Bishop_strategy)
@settings(max_examples=50)
def test_bishop_instantiation(instance):
    assert isinstance(instance, Bishop)

@given(instance=Rook_strategy)
@settings(max_examples=50)
def test_rook_instantiation(instance):
    assert isinstance(instance, Rook)

@given(instance=Pawn_strategy)
@settings(max_examples=50)
def test_pawn_instantiation(instance):
    assert isinstance(instance, Pawn)

@given(instance=Piece_strategy)
@settings(max_examples=50)
def test_piece_instantiation(instance):
    assert isinstance(instance, Piece)



@given(instance=Piece_strategy)
def test_piece_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Piece_strategy)
def test_piece_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Piece_strategy)
def test_piece_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original
