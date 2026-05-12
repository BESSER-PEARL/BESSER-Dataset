import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Deck,
    CardTester,
    Card,
    Suit,
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



def test_cardtester_is_not_abstract():
    assert not inspect.isabstract(CardTester)


def test_cardtester_constructor_exists():
    assert callable(CardTester.__init__)


def test_cardtester_constructor_args():
    sig = inspect.signature(CardTester.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "pointValue" in params, "Missing parameter 'pointValue'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_rank():
    assert hasattr(Card, "rank")
    descriptor = None
    for klass in Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_card_has_pointValue():
    assert hasattr(Card, "pointValue")
    descriptor = None
    for klass in Card.__mro__:
        if "pointValue" in klass.__dict__:
            descriptor = klass.__dict__["pointValue"]
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

def test_suit_exists():
    # Check that the Enumeration exists
    assert Suit is not None

def test_suit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Suit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Suit"


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
CardTester_strategy = st.builds(
    CardTester,
)
Card_strategy = st.builds(
    Card,
    rank=
        safe_text,
    pointValue=
        st.integers(),
    suit=
        safe_text
)

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)

@given(instance=CardTester_strategy)
@settings(max_examples=50)
def test_cardtester_instantiation(instance):
    assert isinstance(instance, CardTester)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=Card_strategy)
def test_card_pointValue_setter(instance):
    original = instance.pointValue
    instance.pointValue = original
    assert instance.pointValue == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original
