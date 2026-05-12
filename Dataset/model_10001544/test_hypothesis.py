import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Integer_external,
    BlackjackGame,
    Player,
    Hand,
    Dealer,
    Cards,
    Deck,
    _Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_integer_external_is_not_abstract():
    assert not inspect.isabstract(Integer_external)


def test_integer_external_constructor_exists():
    assert callable(Integer_external.__init__)


def test_integer_external_constructor_args():
    sig = inspect.signature(Integer_external.__init__)
    params = list(sig.parameters.keys())



def test_blackjackgame_is_not_abstract():
    assert not inspect.isabstract(BlackjackGame)


def test_blackjackgame_constructor_exists():
    assert callable(BlackjackGame.__init__)


def test_blackjackgame_constructor_args():
    sig = inspect.signature(BlackjackGame.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())
    assert "handValue" in params, "Missing parameter 'handValue'"

def test_hand_has_handValue():
    assert hasattr(Hand, "handValue")
    descriptor = None
    for klass in Hand.__mro__:
        if "handValue" in klass.__dict__:
            descriptor = klass.__dict__["handValue"]
            break
    assert isinstance(descriptor, property)



def test_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "handValue" in params, "Missing parameter 'handValue'"
    assert "handLimit" in params, "Missing parameter 'handLimit'"

def test_dealer_has_handValue():
    assert hasattr(Dealer, "handValue")
    descriptor = None
    for klass in Dealer.__mro__:
        if "handValue" in klass.__dict__:
            descriptor = klass.__dict__["handValue"]
            break
    assert isinstance(descriptor, property)

def test_dealer_has_handLimit():
    assert hasattr(Dealer, "handLimit")
    descriptor = None
    for klass in Dealer.__mro__:
        if "handLimit" in klass.__dict__:
            descriptor = klass.__dict__["handLimit"]
            break
    assert isinstance(descriptor, property)



def test_cards_is_not_abstract():
    assert not inspect.isabstract(Cards)


def test_cards_constructor_exists():
    assert callable(Cards.__init__)


def test_cards_constructor_args():
    sig = inspect.signature(Cards.__init__)
    params = list(sig.parameters.keys())
    assert "cardValue" in params, "Missing parameter 'cardValue'"
    assert "cardName" in params, "Missing parameter 'cardName'"

def test_cards_has_cardValue():
    assert hasattr(Cards, "cardValue")
    descriptor = None
    for klass in Cards.__mro__:
        if "cardValue" in klass.__dict__:
            descriptor = klass.__dict__["cardValue"]
            break
    assert isinstance(descriptor, property)

def test_cards_has_cardName():
    assert hasattr(Cards, "cardName")
    descriptor = None
    for klass in Cards.__mro__:
        if "cardName" in klass.__dict__:
            descriptor = klass.__dict__["cardName"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "deckArray" in params, "Missing parameter 'deckArray'"

def test_deck_has_size():
    assert hasattr(Deck, "size")
    descriptor = None
    for klass in Deck.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_deckArray():
    assert hasattr(Deck, "deckArray")
    descriptor = None
    for klass in Deck.__mro__:
        if "deckArray" in klass.__dict__:
            descriptor = klass.__dict__["deckArray"]
            break
    assert isinstance(descriptor, property)



def test__interface_is_not_abstract():
    assert not inspect.isabstract(_Interface)


def test__interface_constructor_exists():
    assert callable(_Interface.__init__)


def test__interface_constructor_args():
    sig = inspect.signature(_Interface.__init__)
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
Integer_external_strategy = st.builds(
    Integer_external,
)
BlackjackGame_strategy = st.builds(
    BlackjackGame,
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text
)
Hand_strategy = st.builds(
    Hand,
    handValue=
        st.integers()
)
Dealer_strategy = st.builds(
    Dealer,
    handValue=
        st.integers(),
    handLimit=
        st.integers()
)
Cards_strategy = st.builds(
    Cards,
    cardValue=
        st.integers(),
    cardName=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    size=
        st.integers(),
    deckArray=
        st.integers()
)
_Interface_strategy = st.builds(
    _Interface,
)

@given(instance=Integer_external_strategy)
@settings(max_examples=50)
def test_integer_external_instantiation(instance):
    assert isinstance(instance, Integer_external)

@given(instance=BlackjackGame_strategy)
@settings(max_examples=50)
def test_blackjackgame_instantiation(instance):
    assert isinstance(instance, BlackjackGame)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Hand_strategy)
@settings(max_examples=50)
def test_hand_instantiation(instance):
    assert isinstance(instance, Hand)



@given(instance=Hand_strategy)
def test_hand_handValue_setter(instance):
    original = instance.handValue
    instance.handValue = original
    assert instance.handValue == original

@given(instance=Dealer_strategy)
@settings(max_examples=50)
def test_dealer_instantiation(instance):
    assert isinstance(instance, Dealer)



@given(instance=Dealer_strategy)
def test_dealer_handValue_setter(instance):
    original = instance.handValue
    instance.handValue = original
    assert instance.handValue == original



@given(instance=Dealer_strategy)
def test_dealer_handLimit_setter(instance):
    original = instance.handLimit
    instance.handLimit = original
    assert instance.handLimit == original

@given(instance=Cards_strategy)
@settings(max_examples=50)
def test_cards_instantiation(instance):
    assert isinstance(instance, Cards)



@given(instance=Cards_strategy)
def test_cards_cardValue_setter(instance):
    original = instance.cardValue
    instance.cardValue = original
    assert instance.cardValue == original



@given(instance=Cards_strategy)
def test_cards_cardName_setter(instance):
    original = instance.cardName
    instance.cardName = original
    assert instance.cardName == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=Deck_strategy)
def test_deck_deckArray_setter(instance):
    original = instance.deckArray
    instance.deckArray = original
    assert instance.deckArray == original

@given(instance=_Interface_strategy)
@settings(max_examples=50)
def test__interface_instantiation(instance):
    assert isinstance(instance, _Interface)
