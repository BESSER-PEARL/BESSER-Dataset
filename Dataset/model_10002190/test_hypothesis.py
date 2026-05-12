import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Player,
    Deck,
    Card,
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
    assert "cards" in params, "Missing parameter 'cards'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_player_has_cards():
    assert hasattr(Player, "cards")
    descriptor = None
    for klass in Player.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_player_has_type():
    assert hasattr(Player, "type")
    descriptor = None
    for klass in Player.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_player_has_value():
    assert hasattr(Player, "value")
    descriptor = None
    for klass in Player.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
    assert "usedCards" in params, "Missing parameter 'usedCards'"

def test_deck_has_deck():
    assert hasattr(Deck, "deck")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_usedCards():
    assert hasattr(Deck, "usedCards")
    descriptor = None
    for klass in Deck.__mro__:
        if "usedCards" in klass.__dict__:
            descriptor = klass.__dict__["usedCards"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "faceUp" in params, "Missing parameter 'faceUp'"
    assert "value" in params, "Missing parameter 'value'"
    assert "display" in params, "Missing parameter 'display'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_faceUp():
    assert hasattr(Card, "faceUp")
    descriptor = None
    for klass in Card.__mro__:
        if "faceUp" in klass.__dict__:
            descriptor = klass.__dict__["faceUp"]
            break
    assert isinstance(descriptor, property)

def test_card_has_value():
    assert hasattr(Card, "value")
    descriptor = None
    for klass in Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_card_has_display():
    assert hasattr(Card, "display")
    descriptor = None
    for klass in Card.__mro__:
        if "display" in klass.__dict__:
            descriptor = klass.__dict__["display"]
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
Player_strategy = st.builds(
    Player,
    cards=
        safe_text,
    type=
        safe_text,
    value=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    deck=
        safe_text,
    usedCards=
        safe_text
)
Card_strategy = st.builds(
    Card,
    faceUp=
        st.booleans(),
    value=
        st.integers(),
    display=
        safe_text,
    suit=
        st.integers()
)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Player_strategy)
def test_player_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Player_strategy)
def test_player_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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
def test_deck_usedCards_setter(instance):
    original = instance.usedCards
    instance.usedCards = original
    assert instance.usedCards == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_faceUp_setter(instance):
    original = instance.faceUp
    instance.faceUp = original
    assert instance.faceUp == original



@given(instance=Card_strategy)
def test_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Card_strategy)
def test_card_display_setter(instance):
    original = instance.display
    instance.display = original
    assert instance.display == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original
