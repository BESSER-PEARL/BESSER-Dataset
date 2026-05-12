import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Stack,
    Card,
    Deck,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stack_is_not_abstract():
    assert not inspect.isabstract(Stack)


def test_stack_constructor_exists():
    assert callable(Stack.__init__)


def test_stack_constructor_args():
    sig = inspect.signature(Stack.__init__)
    params = list(sig.parameters.keys())
    assert "numOfCards" in params, "Missing parameter 'numOfCards'"
    assert "cards__" in params, "Missing parameter 'cards__'"

def test_stack_has_numOfCards():
    assert hasattr(Stack, "numOfCards")
    descriptor = None
    for klass in Stack.__mro__:
        if "numOfCards" in klass.__dict__:
            descriptor = klass.__dict__["numOfCards"]
            break
    assert isinstance(descriptor, property)

def test_stack_has_cards__():
    assert hasattr(Stack, "cards__")
    descriptor = None
    for klass in Stack.__mro__:
        if "cards__" in klass.__dict__:
            descriptor = klass.__dict__["cards__"]
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



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "numOfCards" in params, "Missing parameter 'numOfCards'"
    assert "Card__" in params, "Missing parameter 'Card__'"

def test_deck_has_numOfCards():
    assert hasattr(Deck, "numOfCards")
    descriptor = None
    for klass in Deck.__mro__:
        if "numOfCards" in klass.__dict__:
            descriptor = klass.__dict__["numOfCards"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_Card__():
    assert hasattr(Deck, "Card__")
    descriptor = None
    for klass in Deck.__mro__:
        if "Card__" in klass.__dict__:
            descriptor = klass.__dict__["Card__"]
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
Stack_strategy = st.builds(
    Stack,
    numOfCards=
        st.integers(),
    cards__=
        st.none()
)
Card_strategy = st.builds(
    Card,
    value=
        st.integers(),
    suit=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    numOfCards=
        st.integers(),
    Card__=
        st.none()
)

@given(instance=Stack_strategy)
@settings(max_examples=50)
def test_stack_instantiation(instance):
    assert isinstance(instance, Stack)



@given(instance=Stack_strategy)
def test_stack_numOfCards_setter(instance):
    original = instance.numOfCards
    instance.numOfCards = original
    assert instance.numOfCards == original



@given(instance=Stack_strategy)
def test_stack_cards___setter(instance):
    original = instance.cards__
    instance.cards__ = original
    assert instance.cards__ == original

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

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_numOfCards_setter(instance):
    original = instance.numOfCards
    instance.numOfCards = original
    assert instance.numOfCards == original



@given(instance=Deck_strategy)
def test_deck_Card___setter(instance):
    original = instance.Card__
    instance.Card__ = original
    assert instance.Card__ == original
