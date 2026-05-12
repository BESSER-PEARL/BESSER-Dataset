import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CardPlayer__,
    CardGame,
    CardPlayer,
    CustomException_InvalidCardException,
    CustomException_DeckOrHandEmptyException,
    CustomException_CardException,
    Hand,
    Deck,
    Card,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cardplayer___is_not_abstract():
    assert not inspect.isabstract(CardPlayer__)


def test_cardplayer___constructor_exists():
    assert callable(CardPlayer__.__init__)


def test_cardplayer___constructor_args():
    sig = inspect.signature(CardPlayer__.__init__)
    params = list(sig.parameters.keys())



def test_cardgame_is_not_abstract():
    assert not inspect.isabstract(CardGame)


def test_cardgame_constructor_exists():
    assert callable(CardGame.__init__)


def test_cardgame_constructor_args():
    sig = inspect.signature(CardGame.__init__)
    params = list(sig.parameters.keys())



def test_cardplayer_is_not_abstract():
    assert not inspect.isabstract(CardPlayer)


def test_cardplayer_constructor_exists():
    assert callable(CardPlayer.__init__)


def test_cardplayer_constructor_args():
    sig = inspect.signature(CardPlayer.__init__)
    params = list(sig.parameters.keys())



def test_customexception_invalidcardexception_is_not_abstract():
    assert not inspect.isabstract(CustomException_InvalidCardException)


def test_customexception_invalidcardexception_constructor_exists():
    assert callable(CustomException_InvalidCardException.__init__)


def test_customexception_invalidcardexception_constructor_args():
    sig = inspect.signature(CustomException_InvalidCardException.__init__)
    params = list(sig.parameters.keys())



def test_customexception_deckorhandemptyexception_is_not_abstract():
    assert not inspect.isabstract(CustomException_DeckOrHandEmptyException)


def test_customexception_deckorhandemptyexception_constructor_exists():
    assert callable(CustomException_DeckOrHandEmptyException.__init__)


def test_customexception_deckorhandemptyexception_constructor_args():
    sig = inspect.signature(CustomException_DeckOrHandEmptyException.__init__)
    params = list(sig.parameters.keys())



def test_customexception_cardexception_is_not_abstract():
    assert not inspect.isabstract(CustomException_CardException)


def test_customexception_cardexception_constructor_exists():
    assert callable(CustomException_CardException.__init__)


def test_customexception_cardexception_constructor_args():
    sig = inspect.signature(CustomException_CardException.__init__)
    params = list(sig.parameters.keys())



def test_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())
    assert "HandOfCards" in params, "Missing parameter 'HandOfCards'"

def test_hand_has_HandOfCards():
    assert hasattr(Hand, "HandOfCards")
    descriptor = None
    for klass in Hand.__mro__:
        if "HandOfCards" in klass.__dict__:
            descriptor = klass.__dict__["HandOfCards"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "CardsList" in params, "Missing parameter 'CardsList'"

def test_deck_has_CardsList():
    assert hasattr(Deck, "CardsList")
    descriptor = None
    for klass in Deck.__mro__:
        if "CardsList" in klass.__dict__:
            descriptor = klass.__dict__["CardsList"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "Rank" in params, "Missing parameter 'Rank'"
    assert "Suit" in params, "Missing parameter 'Suit'"

def test_card_has_Rank():
    assert hasattr(Card, "Rank")
    descriptor = None
    for klass in Card.__mro__:
        if "Rank" in klass.__dict__:
            descriptor = klass.__dict__["Rank"]
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

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
CardPlayer___strategy = st.builds(
    CardPlayer__,
)
CardGame_strategy = st.builds(
    CardGame,
)
CardPlayer_strategy = st.builds(
    CardPlayer,
)
CustomException_InvalidCardException_strategy = st.builds(
    CustomException_InvalidCardException,
)
CustomException_DeckOrHandEmptyException_strategy = st.builds(
    CustomException_DeckOrHandEmptyException,
)
CustomException_CardException_strategy = st.builds(
    CustomException_CardException,
)
Hand_strategy = st.builds(
    Hand,
    HandOfCards=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    CardsList=
        safe_text
)
Card_strategy = st.builds(
    Card,
    Rank=
        st.integers(),
    Suit=
        st.none()
)

@given(instance=CardPlayer___strategy)
@settings(max_examples=50)
def test_cardplayer___instantiation(instance):
    assert isinstance(instance, CardPlayer__)

@given(instance=CardGame_strategy)
@settings(max_examples=50)
def test_cardgame_instantiation(instance):
    assert isinstance(instance, CardGame)

@given(instance=CardPlayer_strategy)
@settings(max_examples=50)
def test_cardplayer_instantiation(instance):
    assert isinstance(instance, CardPlayer)

@given(instance=CustomException_InvalidCardException_strategy)
@settings(max_examples=50)
def test_customexception_invalidcardexception_instantiation(instance):
    assert isinstance(instance, CustomException_InvalidCardException)

@given(instance=CustomException_DeckOrHandEmptyException_strategy)
@settings(max_examples=50)
def test_customexception_deckorhandemptyexception_instantiation(instance):
    assert isinstance(instance, CustomException_DeckOrHandEmptyException)

@given(instance=CustomException_CardException_strategy)
@settings(max_examples=50)
def test_customexception_cardexception_instantiation(instance):
    assert isinstance(instance, CustomException_CardException)

@given(instance=Hand_strategy)
@settings(max_examples=50)
def test_hand_instantiation(instance):
    assert isinstance(instance, Hand)



@given(instance=Hand_strategy)
def test_hand_HandOfCards_setter(instance):
    original = instance.HandOfCards
    instance.HandOfCards = original
    assert instance.HandOfCards == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_CardsList_setter(instance):
    original = instance.CardsList
    instance.CardsList = original
    assert instance.CardsList == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_Rank_setter(instance):
    original = instance.Rank
    instance.Rank = original
    assert instance.Rank == original



@given(instance=Card_strategy)
def test_card_Suit_setter(instance):
    original = instance.Suit
    instance.Suit = original
    assert instance.Suit == original
