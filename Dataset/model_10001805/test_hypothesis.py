import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GUI,
    Player,
    GameBoard,
    Deck,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gui_is_not_abstract():
    assert not inspect.isabstract(GUI)


def test_gui_constructor_exists():
    assert callable(GUI.__init__)


def test_gui_constructor_args():
    sig = inspect.signature(GUI.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "hand" in params, "Missing parameter 'hand'"

def test_player_has_points():
    assert hasattr(Player, "points")
    descriptor = None
    for klass in Player.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_player_has_hand():
    assert hasattr(Player, "hand")
    descriptor = None
    for klass in Player.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)



def test_gameboard_is_not_abstract():
    assert not inspect.isabstract(GameBoard)


def test_gameboard_constructor_exists():
    assert callable(GameBoard.__init__)


def test_gameboard_constructor_args():
    sig = inspect.signature(GameBoard.__init__)
    params = list(sig.parameters.keys())
    assert "garbagePile" in params, "Missing parameter 'garbagePile'"
    assert "shelf" in params, "Missing parameter 'shelf'"
    assert "discardPile" in params, "Missing parameter 'discardPile'"

def test_gameboard_has_garbagePile():
    assert hasattr(GameBoard, "garbagePile")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "garbagePile" in klass.__dict__:
            descriptor = klass.__dict__["garbagePile"]
            break
    assert isinstance(descriptor, property)

def test_gameboard_has_shelf():
    assert hasattr(GameBoard, "shelf")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "shelf" in klass.__dict__:
            descriptor = klass.__dict__["shelf"]
            break
    assert isinstance(descriptor, property)

def test_gameboard_has_discardPile():
    assert hasattr(GameBoard, "discardPile")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "discardPile" in klass.__dict__:
            descriptor = klass.__dict__["discardPile"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_value():
    assert hasattr(Card, "value")
    descriptor = None
    for klass in Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)


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
GUI_strategy = st.builds(
    GUI,
)
Player_strategy = st.builds(
    Player,
    points=
        st.integers(),
    hand=
        st.none()
)
GameBoard_strategy = st.builds(
    GameBoard,
    garbagePile=
        safe_text,
    shelf=
        safe_text,
    discardPile=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
)
Card_strategy = st.builds(
    Card,
    value=
        st.integers(),
    suit=
        st.integers()
)

@given(instance=GUI_strategy)
@settings(max_examples=50)
def test_gui_instantiation(instance):
    assert isinstance(instance, GUI)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=Player_strategy)
def test_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original

@given(instance=GameBoard_strategy)
@settings(max_examples=50)
def test_gameboard_instantiation(instance):
    assert isinstance(instance, GameBoard)



@given(instance=GameBoard_strategy)
def test_gameboard_garbagePile_setter(instance):
    original = instance.garbagePile
    instance.garbagePile = original
    assert instance.garbagePile == original



@given(instance=GameBoard_strategy)
def test_gameboard_shelf_setter(instance):
    original = instance.shelf
    instance.shelf = original
    assert instance.shelf == original



@given(instance=GameBoard_strategy)
def test_gameboard_discardPile_setter(instance):
    original = instance.discardPile
    instance.discardPile = original
    assert instance.discardPile == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original
