import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TarotCard___Card,
    Card___Abstract__,
    FortuneTeller,
    Deck,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tarotcard___card_is_not_abstract():
    assert not inspect.isabstract(TarotCard___Card)


def test_tarotcard___card_constructor_exists():
    assert callable(TarotCard___Card.__init__)


def test_tarotcard___card_constructor_args():
    sig = inspect.signature(TarotCard___Card.__init__)
    params = list(sig.parameters.keys())
    assert "_fortunes" in params, "Missing parameter '_fortunes'"
    assert "_fileName" in params, "Missing parameter '_fileName'"
    assert "_id" in params, "Missing parameter '_id'"

def test_tarotcard___card_has__fortunes():
    assert hasattr(TarotCard___Card, "_fortunes")
    descriptor = None
    for klass in TarotCard___Card.__mro__:
        if "_fortunes" in klass.__dict__:
            descriptor = klass.__dict__["_fortunes"]
            break
    assert isinstance(descriptor, property)

def test_tarotcard___card_has__fileName():
    assert hasattr(TarotCard___Card, "_fileName")
    descriptor = None
    for klass in TarotCard___Card.__mro__:
        if "_fileName" in klass.__dict__:
            descriptor = klass.__dict__["_fileName"]
            break
    assert isinstance(descriptor, property)

def test_tarotcard___card_has__id():
    assert hasattr(TarotCard___Card, "_id")
    descriptor = None
    for klass in TarotCard___Card.__mro__:
        if "_id" in klass.__dict__:
            descriptor = klass.__dict__["_id"]
            break
    assert isinstance(descriptor, property)



def test_card___abstract___is_not_abstract():
    assert not inspect.isabstract(Card___Abstract__)


def test_card___abstract___constructor_exists():
    assert callable(Card___Abstract__.__init__)


def test_card___abstract___constructor_args():
    sig = inspect.signature(Card___Abstract__.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"

def test_card___abstract___has__id():
    assert hasattr(Card___Abstract__, "_id")
    descriptor = None
    for klass in Card___Abstract__.__mro__:
        if "_id" in klass.__dict__:
            descriptor = klass.__dict__["_id"]
            break
    assert isinstance(descriptor, property)



def test_fortuneteller_is_not_abstract():
    assert not inspect.isabstract(FortuneTeller)


def test_fortuneteller_constructor_exists():
    assert callable(FortuneTeller.__init__)


def test_fortuneteller_constructor_args():
    sig = inspect.signature(FortuneTeller.__init__)
    params = list(sig.parameters.keys())
    assert "_tarotDeck" in params, "Missing parameter '_tarotDeck'"

def test_fortuneteller_has__tarotDeck():
    assert hasattr(FortuneTeller, "_tarotDeck")
    descriptor = None
    for klass in FortuneTeller.__mro__:
        if "_tarotDeck" in klass.__dict__:
            descriptor = klass.__dict__["_tarotDeck"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "_deck" in params, "Missing parameter '_deck'"

def test_deck_has__deck():
    assert hasattr(Deck, "_deck")
    descriptor = None
    for klass in Deck.__mro__:
        if "_deck" in klass.__dict__:
            descriptor = klass.__dict__["_deck"]
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
TarotCard___Card_strategy = st.builds(
    TarotCard___Card,
    _fortunes=
        safe_text,
    _fileName=
        safe_text,
    _id=
        st.integers()
)
Card___Abstract___strategy = st.builds(
    Card___Abstract__,
    _id=
        st.integers()
)
FortuneTeller_strategy = st.builds(
    FortuneTeller,
    _tarotDeck=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    _deck=
        safe_text
)

@given(instance=TarotCard___Card_strategy)
@settings(max_examples=50)
def test_tarotcard___card_instantiation(instance):
    assert isinstance(instance, TarotCard___Card)



@given(instance=TarotCard___Card_strategy)
def test_tarotcard___card__fortunes_setter(instance):
    original = instance._fortunes
    instance._fortunes = original
    assert instance._fortunes == original



@given(instance=TarotCard___Card_strategy)
def test_tarotcard___card__fileName_setter(instance):
    original = instance._fileName
    instance._fileName = original
    assert instance._fileName == original



@given(instance=TarotCard___Card_strategy)
def test_tarotcard___card__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original

@given(instance=Card___Abstract___strategy)
@settings(max_examples=50)
def test_card___abstract___instantiation(instance):
    assert isinstance(instance, Card___Abstract__)



@given(instance=Card___Abstract___strategy)
def test_card___abstract____id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original

@given(instance=FortuneTeller_strategy)
@settings(max_examples=50)
def test_fortuneteller_instantiation(instance):
    assert isinstance(instance, FortuneTeller)



@given(instance=FortuneTeller_strategy)
def test_fortuneteller__tarotDeck_setter(instance):
    original = instance._tarotDeck
    instance._tarotDeck = original
    assert instance._tarotDeck == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck__deck_setter(instance):
    original = instance._deck
    instance._deck = original
    assert instance._deck == original
