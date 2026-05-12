import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    Cards,
    CardGame,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cards_is_not_abstract():
    assert not inspect.isabstract(Cards)


def test_cards_constructor_exists():
    assert callable(Cards.__init__)


def test_cards_constructor_args():
    sig = inspect.signature(Cards.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_cards_has_card():
    assert hasattr(Cards, "card")
    descriptor = None
    for klass in Cards.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)

def test_cards_has_attribute3():
    assert hasattr(Cards, "attribute3")
    descriptor = None
    for klass in Cards.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_cards_has_attribute2():
    assert hasattr(Cards, "attribute2")
    descriptor = None
    for klass in Cards.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_cardgame_is_not_abstract():
    assert not inspect.isabstract(CardGame)


def test_cardgame_constructor_exists():
    assert callable(CardGame.__init__)


def test_cardgame_constructor_args():
    sig = inspect.signature(CardGame.__init__)
    params = list(sig.parameters.keys())
    assert "CardNumber" in params, "Missing parameter 'CardNumber'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_cardgame_has_CardNumber():
    assert hasattr(CardGame, "CardNumber")
    descriptor = None
    for klass in CardGame.__mro__:
        if "CardNumber" in klass.__dict__:
            descriptor = klass.__dict__["CardNumber"]
            break
    assert isinstance(descriptor, property)

def test_cardgame_has_suit():
    assert hasattr(CardGame, "suit")
    descriptor = None
    for klass in CardGame.__mro__:
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
Cards_strategy = st.builds(
    Cards,
    card=
        st.none(),
    attribute3=
        safe_text,
    attribute2=
        st.integers()
)
CardGame_strategy = st.builds(
    CardGame,
    CardNumber=
        st.integers(),
    suit=
        safe_text
)

@given(instance=Cards_strategy)
@settings(max_examples=50)
def test_cards_instantiation(instance):
    assert isinstance(instance, Cards)

@given(instance=Cards_strategy)
def test_cards_card_type(instance):
    assert isinstance(instance.card, cardgame)


@given(instance=Cards_strategy)
def test_cards_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=Cards_strategy)
def test_cards_attribute3_type(instance):
    assert isinstance(instance.attribute3, str)


@given(instance=Cards_strategy)
def test_cards_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original

@given(instance=Cards_strategy)
def test_cards_attribute2_type(instance):
    assert isinstance(instance.attribute2, int)


@given(instance=Cards_strategy)
def test_cards_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=CardGame_strategy)
@settings(max_examples=50)
def test_cardgame_instantiation(instance):
    assert isinstance(instance, CardGame)

@given(instance=CardGame_strategy)
def test_cardgame_CardNumber_type(instance):
    assert isinstance(instance.CardNumber, int)


@given(instance=CardGame_strategy)
def test_cardgame_CardNumber_setter(instance):
    original = instance.CardNumber
    instance.CardNumber = original
    assert instance.CardNumber == original

@given(instance=CardGame_strategy)
def test_cardgame_suit_type(instance):
    assert isinstance(instance.suit, str)


@given(instance=CardGame_strategy)
def test_cardgame_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original
