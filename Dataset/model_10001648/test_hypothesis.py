import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CardDeck,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_carddeck_is_not_abstract():
    assert not inspect.isabstract(CardDeck)


def test_carddeck_constructor_exists():
    assert callable(CardDeck.__init__)


def test_carddeck_constructor_args():
    sig = inspect.signature(CardDeck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "suits" in params, "Missing parameter 'suits'"

def test_carddeck_has_cards():
    assert hasattr(CardDeck, "cards")
    descriptor = None
    for klass in CardDeck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_carddeck_has_suits():
    assert hasattr(CardDeck, "suits")
    descriptor = None
    for klass in CardDeck.__mro__:
        if "suits" in klass.__dict__:
            descriptor = klass.__dict__["suits"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "cardSuit" in params, "Missing parameter 'cardSuit'"
    assert "cardFace" in params, "Missing parameter 'cardFace'"

def test_card_has_cardSuit():
    assert hasattr(Card, "cardSuit")
    descriptor = None
    for klass in Card.__mro__:
        if "cardSuit" in klass.__dict__:
            descriptor = klass.__dict__["cardSuit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardFace():
    assert hasattr(Card, "cardFace")
    descriptor = None
    for klass in Card.__mro__:
        if "cardFace" in klass.__dict__:
            descriptor = klass.__dict__["cardFace"]
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
CardDeck_strategy = st.builds(
    CardDeck,
    cards=
        safe_text,
    suits=
        safe_text
)
Card_strategy = st.builds(
    Card,
    cardSuit=
        safe_text,
    cardFace=
        st.integers()
)

@given(instance=CardDeck_strategy)
@settings(max_examples=50)
def test_carddeck_instantiation(instance):
    assert isinstance(instance, CardDeck)



@given(instance=CardDeck_strategy)
def test_carddeck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=CardDeck_strategy)
def test_carddeck_suits_setter(instance):
    original = instance.suits
    instance.suits = original
    assert instance.suits == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_cardSuit_setter(instance):
    original = instance.cardSuit
    instance.cardSuit = original
    assert instance.cardSuit == original



@given(instance=Card_strategy)
def test_card_cardFace_setter(instance):
    original = instance.cardFace
    instance.cardFace = original
    assert instance.cardFace == original
