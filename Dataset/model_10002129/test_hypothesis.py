import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Deck,
    Card,
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



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "CLUBS" in params, "Missing parameter 'CLUBS'"
    assert "JACK" in params, "Missing parameter 'JACK'"
    assert "DIAMONDS" in params, "Missing parameter 'DIAMONDS'"
    assert "SPADES" in params, "Missing parameter 'SPADES'"
    assert "HEARTS" in params, "Missing parameter 'HEARTS'"
    assert "ACE" in params, "Missing parameter 'ACE'"
    assert "QUEEN" in params, "Missing parameter 'QUEEN'"
    assert "value" in params, "Missing parameter 'value'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "KING" in params, "Missing parameter 'KING'"
    assert "JOKER" in params, "Missing parameter 'JOKER'"

def test_card_has_CLUBS():
    assert hasattr(Card, "CLUBS")
    descriptor = None
    for klass in Card.__mro__:
        if "CLUBS" in klass.__dict__:
            descriptor = klass.__dict__["CLUBS"]
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

def test_card_has_DIAMONDS():
    assert hasattr(Card, "DIAMONDS")
    descriptor = None
    for klass in Card.__mro__:
        if "DIAMONDS" in klass.__dict__:
            descriptor = klass.__dict__["DIAMONDS"]
            break
    assert isinstance(descriptor, property)

def test_card_has_SPADES():
    assert hasattr(Card, "SPADES")
    descriptor = None
    for klass in Card.__mro__:
        if "SPADES" in klass.__dict__:
            descriptor = klass.__dict__["SPADES"]
            break
    assert isinstance(descriptor, property)

def test_card_has_HEARTS():
    assert hasattr(Card, "HEARTS")
    descriptor = None
    for klass in Card.__mro__:
        if "HEARTS" in klass.__dict__:
            descriptor = klass.__dict__["HEARTS"]
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

def test_card_has_KING():
    assert hasattr(Card, "KING")
    descriptor = None
    for klass in Card.__mro__:
        if "KING" in klass.__dict__:
            descriptor = klass.__dict__["KING"]
            break
    assert isinstance(descriptor, property)

def test_card_has_JOKER():
    assert hasattr(Card, "JOKER")
    descriptor = None
    for klass in Card.__mro__:
        if "JOKER" in klass.__dict__:
            descriptor = klass.__dict__["JOKER"]
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
)
Card_strategy = st.builds(
    Card,
    CLUBS=
        st.integers(),
    JACK=
        st.integers(),
    DIAMONDS=
        st.integers(),
    SPADES=
        st.integers(),
    HEARTS=
        st.integers(),
    ACE=
        st.integers(),
    QUEEN=
        st.integers(),
    value=
        st.integers(),
    suit=
        st.integers(),
    KING=
        st.integers(),
    JOKER=
        st.integers()
)

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_CLUBS_setter(instance):
    original = instance.CLUBS
    instance.CLUBS = original
    assert instance.CLUBS == original



@given(instance=Card_strategy)
def test_card_JACK_setter(instance):
    original = instance.JACK
    instance.JACK = original
    assert instance.JACK == original



@given(instance=Card_strategy)
def test_card_DIAMONDS_setter(instance):
    original = instance.DIAMONDS
    instance.DIAMONDS = original
    assert instance.DIAMONDS == original



@given(instance=Card_strategy)
def test_card_SPADES_setter(instance):
    original = instance.SPADES
    instance.SPADES = original
    assert instance.SPADES == original



@given(instance=Card_strategy)
def test_card_HEARTS_setter(instance):
    original = instance.HEARTS
    instance.HEARTS = original
    assert instance.HEARTS == original



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



@given(instance=Card_strategy)
def test_card_KING_setter(instance):
    original = instance.KING
    instance.KING = original
    assert instance.KING == original



@given(instance=Card_strategy)
def test_card_JOKER_setter(instance):
    original = instance.JOKER
    instance.JOKER = original
    assert instance.JOKER == original
