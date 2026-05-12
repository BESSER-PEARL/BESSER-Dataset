import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CardCollection,
    EndCardPile,
    Hand,
    Card,
    Deck,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cardcollection_is_not_abstract():
    assert not inspect.isabstract(CardCollection)


def test_cardcollection_constructor_exists():
    assert callable(CardCollection.__init__)


def test_cardcollection_constructor_args():
    sig = inspect.signature(CardCollection.__init__)
    params = list(sig.parameters.keys())
    assert "collection" in params, "Missing parameter 'collection'"

def test_cardcollection_has_collection():
    assert hasattr(CardCollection, "collection")
    descriptor = None
    for klass in CardCollection.__mro__:
        if "collection" in klass.__dict__:
            descriptor = klass.__dict__["collection"]
            break
    assert isinstance(descriptor, property)



def test_endcardpile_is_not_abstract():
    assert not inspect.isabstract(EndCardPile)


def test_endcardpile_constructor_exists():
    assert callable(EndCardPile.__init__)


def test_endcardpile_constructor_args():
    sig = inspect.signature(EndCardPile.__init__)
    params = list(sig.parameters.keys())



def test_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "Number" in params, "Missing parameter 'Number'"
    assert "Suit" in params, "Missing parameter 'Suit'"

def test_card_has_Number():
    assert hasattr(Card, "Number")
    descriptor = None
    for klass in Card.__mro__:
        if "Number" in klass.__dict__:
            descriptor = klass.__dict__["Number"]
            break
    assert isinstance(descriptor, property)

def test_card_has_Suit():
    assert hasattr(Card, "Suit")
    descriptor = None
    for klass in Card.__mro__:
        if "Suit" in klass.__dict__:
            descriptor = klass.__dict__["Suit"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())


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
CardCollection_strategy = st.builds(
    CardCollection,
    collection=
        safe_text
)
EndCardPile_strategy = st.builds(
    EndCardPile,
)
Hand_strategy = st.builds(
    Hand,
)
Card_strategy = st.builds(
    Card,
    Number=
        st.integers(),
    Suit=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
)

@given(instance=CardCollection_strategy)
@settings(max_examples=50)
def test_cardcollection_instantiation(instance):
    assert isinstance(instance, CardCollection)



@given(instance=CardCollection_strategy)
def test_cardcollection_collection_setter(instance):
    original = instance.collection
    instance.collection = original
    assert instance.collection == original

@given(instance=EndCardPile_strategy)
@settings(max_examples=50)
def test_endcardpile_instantiation(instance):
    assert isinstance(instance, EndCardPile)

@given(instance=Hand_strategy)
@settings(max_examples=50)
def test_hand_instantiation(instance):
    assert isinstance(instance, Hand)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_Number_setter(instance):
    original = instance.Number
    instance.Number = original
    assert instance.Number == original



@given(instance=Card_strategy)
def test_card_Suit_setter(instance):
    original = instance.Suit
    instance.Suit = original
    assert instance.Suit == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)
