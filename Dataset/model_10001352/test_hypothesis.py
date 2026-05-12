import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Player,
    Spectator,
    King,
    Checker,
    Piece,
    Square,
    Grid,
    Game,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_spectator_is_not_abstract():
    assert not inspect.isabstract(Spectator)


def test_spectator_constructor_exists():
    assert callable(Spectator.__init__)


def test_spectator_constructor_args():
    sig = inspect.signature(Spectator.__init__)
    params = list(sig.parameters.keys())



def test_king_is_not_abstract():
    assert not inspect.isabstract(King)


def test_king_constructor_exists():
    assert callable(King.__init__)


def test_king_constructor_args():
    sig = inspect.signature(King.__init__)
    params = list(sig.parameters.keys())



def test_checker_is_not_abstract():
    assert not inspect.isabstract(Checker)


def test_checker_constructor_exists():
    assert callable(Checker.__init__)


def test_checker_constructor_args():
    sig = inspect.signature(Checker.__init__)
    params = list(sig.parameters.keys())



def test_piece_is_not_abstract():
    assert not inspect.isabstract(Piece)


def test_piece_constructor_exists():
    assert callable(Piece.__init__)


def test_piece_constructor_args():
    sig = inspect.signature(Piece.__init__)
    params = list(sig.parameters.keys())



def test_square_is_not_abstract():
    assert not inspect.isabstract(Square)


def test_square_constructor_exists():
    assert callable(Square.__init__)


def test_square_constructor_args():
    sig = inspect.signature(Square.__init__)
    params = list(sig.parameters.keys())



def test_grid_is_not_abstract():
    assert not inspect.isabstract(Grid)


def test_grid_constructor_exists():
    assert callable(Grid.__init__)


def test_grid_constructor_args():
    sig = inspect.signature(Grid.__init__)
    params = list(sig.parameters.keys())



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
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
Player_strategy = st.builds(
    Player,
)
Spectator_strategy = st.builds(
    Spectator,
)
King_strategy = st.builds(
    King,
)
Checker_strategy = st.builds(
    Checker,
)
Piece_strategy = st.builds(
    Piece,
)
Square_strategy = st.builds(
    Square,
)
Grid_strategy = st.builds(
    Grid,
)
Game_strategy = st.builds(
    Game,
)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)

@given(instance=Spectator_strategy)
@settings(max_examples=50)
def test_spectator_instantiation(instance):
    assert isinstance(instance, Spectator)

@given(instance=King_strategy)
@settings(max_examples=50)
def test_king_instantiation(instance):
    assert isinstance(instance, King)

@given(instance=Checker_strategy)
@settings(max_examples=50)
def test_checker_instantiation(instance):
    assert isinstance(instance, Checker)

@given(instance=Piece_strategy)
@settings(max_examples=50)
def test_piece_instantiation(instance):
    assert isinstance(instance, Piece)

@given(instance=Square_strategy)
@settings(max_examples=50)
def test_square_instantiation(instance):
    assert isinstance(instance, Square)

@given(instance=Grid_strategy)
@settings(max_examples=50)
def test_grid_instantiation(instance):
    assert isinstance(instance, Grid)

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)
