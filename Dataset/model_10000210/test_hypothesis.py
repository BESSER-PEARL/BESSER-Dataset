import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Queen,
    King,
    Knight,
    Bishop,
    Rook,
    Pawn,
    Piece,
    Player,
    STATE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_knight_is_not_abstract():
    assert not inspect.isabstract(Knight)


def test_knight_constructor_exists():
    assert callable(Knight.__init__)


def test_knight_constructor_args():
    sig = inspect.signature(Knight.__init__)
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
    assert "Name" in params, "Missing parameter 'Name'"

def test_piece_has_Name():
    assert hasattr(Piece, "Name")
    descriptor = None
    for klass in Piece.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_player_exists():
    # Check that the Enumeration exists
    assert Player is not None

def test_player_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Player]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Player"

def test_state_exists():
    # Check that the Enumeration exists
    assert STATE is not None

def test_state_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in STATE]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in STATE"


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
Queen_strategy = st.builds(
    Queen,
)
King_strategy = st.builds(
    King,
)
Knight_strategy = st.builds(
    Knight,
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
    Name=
        safe_text
)

@given(instance=Queen_strategy)
@settings(max_examples=50)
def test_queen_instantiation(instance):
    assert isinstance(instance, Queen)

@given(instance=King_strategy)
@settings(max_examples=50)
def test_king_instantiation(instance):
    assert isinstance(instance, King)

@given(instance=Knight_strategy)
@settings(max_examples=50)
def test_knight_instantiation(instance):
    assert isinstance(instance, Knight)

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
def test_piece_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
