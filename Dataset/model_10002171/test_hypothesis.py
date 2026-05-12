import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Card,
    Deck,
    BlackjackGameSimulator,
    Suit,
    Value,
    CardSuit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "toString" in params, "Missing parameter 'toString'"
    assert "_CardSuit" in params, "Missing parameter '_CardSuit'"
    assert "Value" in params, "Missing parameter 'Value'"

def test_card_has_toString():
    assert hasattr(Card, "toString")
    descriptor = None
    for klass in Card.__mro__:
        if "toString" in klass.__dict__:
            descriptor = klass.__dict__["toString"]
            break
    assert isinstance(descriptor, property)

def test_card_has__CardSuit():
    assert hasattr(Card, "_CardSuit")
    descriptor = None
    for klass in Card.__mro__:
        if "_CardSuit" in klass.__dict__:
            descriptor = klass.__dict__["_CardSuit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_Value():
    assert hasattr(Card, "Value")
    descriptor = None
    for klass in Card.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "ArrayList" in params, "Missing parameter 'ArrayList'"

def test_deck_has_ArrayList():
    assert hasattr(Deck, "ArrayList")
    descriptor = None
    for klass in Deck.__mro__:
        if "ArrayList" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList"]
            break
    assert isinstance(descriptor, property)



def test_blackjackgamesimulator_is_not_abstract():
    assert not inspect.isabstract(BlackjackGameSimulator)


def test_blackjackgamesimulator_constructor_exists():
    assert callable(BlackjackGameSimulator.__init__)


def test_blackjackgamesimulator_constructor_args():
    sig = inspect.signature(BlackjackGameSimulator.__init__)
    params = list(sig.parameters.keys())

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

def test_value_exists():
    # Check that the Enumeration exists
    assert Value is not None

def test_value_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Value]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Value"

def test_cardsuit_exists():
    # Check that the Enumeration exists
    assert CardSuit is not None

def test_cardsuit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardSuit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardSuit"


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
Card_strategy = st.builds(
    Card,
    toString=
        safe_text,
    _CardSuit=
        st.integers(),
    Value=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    ArrayList=
        safe_text
)
BlackjackGameSimulator_strategy = st.builds(
    BlackjackGameSimulator,
)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_toString_setter(instance):
    original = instance.toString
    instance.toString = original
    assert instance.toString == original



@given(instance=Card_strategy)
def test_card__CardSuit_setter(instance):
    original = instance._CardSuit
    instance._CardSuit = original
    assert instance._CardSuit == original



@given(instance=Card_strategy)
def test_card_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_ArrayList_setter(instance):
    original = instance.ArrayList
    instance.ArrayList = original
    assert instance.ArrayList == original

@given(instance=BlackjackGameSimulator_strategy)
@settings(max_examples=50)
def test_blackjackgamesimulator_instantiation(instance):
    assert isinstance(instance, BlackjackGameSimulator)
