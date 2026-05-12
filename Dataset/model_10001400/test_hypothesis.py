import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class2,
    Class,
    blackjackCard,
    Deck,
    Blackjack,
    blackjackHand,
    Hand,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_blackjackcard_is_not_abstract():
    assert not inspect.isabstract(blackjackCard)


def test_blackjackcard_constructor_exists():
    assert callable(blackjackCard.__init__)


def test_blackjackcard_constructor_args():
    sig = inspect.signature(blackjackCard.__init__)
    params = list(sig.parameters.keys())



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"

def test_deck_has_deck():
    assert hasattr(Deck, "deck")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_is_not_abstract():
    assert not inspect.isabstract(Blackjack)


def test_blackjack_constructor_exists():
    assert callable(Blackjack.__init__)


def test_blackjack_constructor_args():
    sig = inspect.signature(Blackjack.__init__)
    params = list(sig.parameters.keys())



def test_blackjackhand_is_not_abstract():
    assert not inspect.isabstract(blackjackHand)


def test_blackjackhand_constructor_exists():
    assert callable(blackjackHand.__init__)


def test_blackjackhand_constructor_args():
    sig = inspect.signature(blackjackHand.__init__)
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
    assert "face" in params, "Missing parameter 'face'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_face():
    assert hasattr(Card, "face")
    descriptor = None
    for klass in Card.__mro__:
        if "face" in klass.__dict__:
            descriptor = klass.__dict__["face"]
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
Class2_strategy = st.builds(
    Class2,
)
Class_strategy = st.builds(
    Class,
)
blackjackCard_strategy = st.builds(
    blackjackCard,
)
Deck_strategy = st.builds(
    Deck,
    deck=
        safe_text
)
Blackjack_strategy = st.builds(
    Blackjack,
)
blackjackHand_strategy = st.builds(
    blackjackHand,
)
Hand_strategy = st.builds(
    Hand,
)
Card_strategy = st.builds(
    Card,
    face=
        st.integers(),
    suit=
        st.integers()
)

@given(instance=Class2_strategy)
@settings(max_examples=50)
def test_class2_instantiation(instance):
    assert isinstance(instance, Class2)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=blackjackCard_strategy)
@settings(max_examples=50)
def test_blackjackcard_instantiation(instance):
    assert isinstance(instance, blackjackCard)

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original

@given(instance=Blackjack_strategy)
@settings(max_examples=50)
def test_blackjack_instantiation(instance):
    assert isinstance(instance, Blackjack)

@given(instance=blackjackHand_strategy)
@settings(max_examples=50)
def test_blackjackhand_instantiation(instance):
    assert isinstance(instance, blackjackHand)

@given(instance=Hand_strategy)
@settings(max_examples=50)
def test_hand_instantiation(instance):
    assert isinstance(instance, Hand)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original
