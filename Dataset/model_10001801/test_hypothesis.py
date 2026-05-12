import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Deck,
    Card,
    Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck_of_cards" in params, "Missing parameter 'deck_of_cards'"
    assert "deck_position" in params, "Missing parameter 'deck_position'"

def test_deck_has_deck_of_cards():
    assert hasattr(Deck, "deck_of_cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck_of_cards" in klass.__dict__:
            descriptor = klass.__dict__["deck_of_cards"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_deck_position():
    assert hasattr(Deck, "deck_position")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck_position" in klass.__dict__:
            descriptor = klass.__dict__["deck_position"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "front" in params, "Missing parameter 'front'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_value():
    assert hasattr(Card, "value")
    descriptor = None
    for klass in Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_card_has_front():
    assert hasattr(Card, "front")
    descriptor = None
    for klass in Card.__mro__:
        if "front" in klass.__dict__:
            descriptor = klass.__dict__["front"]
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



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "name" in params, "Missing parameter 'name'"

def test_player_has_points():
    assert hasattr(Player, "points")
    descriptor = None
    for klass in Player.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Deck_strategy = st.builds(
    Deck,
    deck_of_cards=
        safe_text,
    deck_position=
        st.integers()
)
Card_strategy = st.builds(
    Card,
    value=
        safe_text,
    front=
        safe_text,
    suit=
        safe_text
)
Player_strategy = st.builds(
    Player,
    points=
        safe_text,
    name=
        safe_text
)

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_deck_of_cards_setter(instance):
    original = instance.deck_of_cards
    instance.deck_of_cards = original
    assert instance.deck_of_cards == original



@given(instance=Deck_strategy)
def test_deck_deck_position_setter(instance):
    original = instance.deck_position
    instance.deck_position = original
    assert instance.deck_position == original

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
def test_card_front_setter(instance):
    original = instance.front
    instance.front = original
    assert instance.front == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original

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
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
