import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Card_Interface,
    ElevensGame,
    Player,
    Deck,
    Board,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_card_interface_is_not_abstract():
    assert not inspect.isabstract(Card_Interface)


def test_card_interface_constructor_exists():
    assert callable(Card_Interface.__init__)


def test_card_interface_constructor_args():
    sig = inspect.signature(Card_Interface.__init__)
    params = list(sig.parameters.keys())



def test_elevensgame_is_not_abstract():
    assert not inspect.isabstract(ElevensGame)


def test_elevensgame_constructor_exists():
    assert callable(ElevensGame.__init__)


def test_elevensgame_constructor_args():
    sig = inspect.signature(ElevensGame.__init__)
    params = list(sig.parameters.keys())
    assert "Board_9_" in params, "Missing parameter 'Board_9_'"
    assert "win" in params, "Missing parameter 'win'"

def test_elevensgame_has_Board_9_():
    assert hasattr(ElevensGame, "Board_9_")
    descriptor = None
    for klass in ElevensGame.__mro__:
        if "Board_9_" in klass.__dict__:
            descriptor = klass.__dict__["Board_9_"]
            break
    assert isinstance(descriptor, property)

def test_elevensgame_has_win():
    assert hasattr(ElevensGame, "win")
    descriptor = None
    for klass in ElevensGame.__mro__:
        if "win" in klass.__dict__:
            descriptor = klass.__dict__["win"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "Deck_ArrayList_" in params, "Missing parameter 'Deck_ArrayList_'"
    assert "Topcard" in params, "Missing parameter 'Topcard'"

def test_deck_has_Deck_ArrayList_():
    assert hasattr(Deck, "Deck_ArrayList_")
    descriptor = None
    for klass in Deck.__mro__:
        if "Deck_ArrayList_" in klass.__dict__:
            descriptor = klass.__dict__["Deck_ArrayList_"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_Topcard():
    assert hasattr(Deck, "Topcard")
    descriptor = None
    for klass in Deck.__mro__:
        if "Topcard" in klass.__dict__:
            descriptor = klass.__dict__["Topcard"]
            break
    assert isinstance(descriptor, property)

def test_board_exists():
    # Check that the Enumeration exists
    assert Board is not None

def test_board_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Board]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Board"


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
Card_Interface_strategy = st.builds(
    Card_Interface,
)
ElevensGame_strategy = st.builds(
    ElevensGame,
    Board_9_=
        st.integers(),
    win=
        st.booleans()
)
Player_strategy = st.builds(
    Player,
)
Deck_strategy = st.builds(
    Deck,
    Deck_ArrayList_=
        st.integers(),
    Topcard=
        st.integers()
)

@given(instance=Card_Interface_strategy)
@settings(max_examples=50)
def test_card_interface_instantiation(instance):
    assert isinstance(instance, Card_Interface)

@given(instance=ElevensGame_strategy)
@settings(max_examples=50)
def test_elevensgame_instantiation(instance):
    assert isinstance(instance, ElevensGame)



@given(instance=ElevensGame_strategy)
def test_elevensgame_Board_9__setter(instance):
    original = instance.Board_9_
    instance.Board_9_ = original
    assert instance.Board_9_ == original



@given(instance=ElevensGame_strategy)
def test_elevensgame_win_setter(instance):
    original = instance.win
    instance.win = original
    assert instance.win == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_Deck_ArrayList__setter(instance):
    original = instance.Deck_ArrayList_
    instance.Deck_ArrayList_ = original
    assert instance.Deck_ArrayList_ == original



@given(instance=Deck_strategy)
def test_deck_Topcard_setter(instance):
    original = instance.Topcard
    instance.Topcard = original
    assert instance.Topcard == original
