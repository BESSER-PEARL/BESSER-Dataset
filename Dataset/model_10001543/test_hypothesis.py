import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ElevensGame,
    Deck,
    Player,
    cardValue,
    cardFace,
    card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_elevensgame_is_not_abstract():
    assert not inspect.isabstract(ElevensGame)


def test_elevensgame_constructor_exists():
    assert callable(ElevensGame.__init__)


def test_elevensgame_constructor_args():
    sig = inspect.signature(ElevensGame.__init__)
    params = list(sig.parameters.keys())
    assert "creates_Play_and_Deck" in params, "Missing parameter 'creates_Play_and_Deck'"

def test_elevensgame_has_creates_Play_and_Deck():
    assert hasattr(ElevensGame, "creates_Play_and_Deck")
    descriptor = None
    for klass in ElevensGame.__mro__:
        if "creates_Play_and_Deck" in klass.__dict__:
            descriptor = klass.__dict__["creates_Play_and_Deck"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "creates_and_shuffles" in params, "Missing parameter 'creates_and_shuffles'"

def test_deck_has_creates_and_shuffles():
    assert hasattr(Deck, "creates_and_shuffles")
    descriptor = None
    for klass in Deck.__mro__:
        if "creates_and_shuffles" in klass.__dict__:
            descriptor = klass.__dict__["creates_and_shuffles"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "has_a" in params, "Missing parameter 'has_a'"

def test_player_has_has_a():
    assert hasattr(Player, "has_a")
    descriptor = None
    for klass in Player.__mro__:
        if "has_a" in klass.__dict__:
            descriptor = klass.__dict__["has_a"]
            break
    assert isinstance(descriptor, property)



def test_cardvalue_is_not_abstract():
    assert not inspect.isabstract(cardValue)


def test_cardvalue_constructor_exists():
    assert callable(cardValue.__init__)


def test_cardvalue_constructor_args():
    sig = inspect.signature(cardValue.__init__)
    params = list(sig.parameters.keys())
    assert "Jack" in params, "Missing parameter 'Jack'"
    assert "King" in params, "Missing parameter 'King'"
    assert "Ace" in params, "Missing parameter 'Ace'"
    assert "Queen" in params, "Missing parameter 'Queen'"

def test_cardvalue_has_Jack():
    assert hasattr(cardValue, "Jack")
    descriptor = None
    for klass in cardValue.__mro__:
        if "Jack" in klass.__dict__:
            descriptor = klass.__dict__["Jack"]
            break
    assert isinstance(descriptor, property)

def test_cardvalue_has_King():
    assert hasattr(cardValue, "King")
    descriptor = None
    for klass in cardValue.__mro__:
        if "King" in klass.__dict__:
            descriptor = klass.__dict__["King"]
            break
    assert isinstance(descriptor, property)

def test_cardvalue_has_Ace():
    assert hasattr(cardValue, "Ace")
    descriptor = None
    for klass in cardValue.__mro__:
        if "Ace" in klass.__dict__:
            descriptor = klass.__dict__["Ace"]
            break
    assert isinstance(descriptor, property)

def test_cardvalue_has_Queen():
    assert hasattr(cardValue, "Queen")
    descriptor = None
    for klass in cardValue.__mro__:
        if "Queen" in klass.__dict__:
            descriptor = klass.__dict__["Queen"]
            break
    assert isinstance(descriptor, property)



def test_cardface_is_not_abstract():
    assert not inspect.isabstract(cardFace)


def test_cardface_constructor_exists():
    assert callable(cardFace.__init__)


def test_cardface_constructor_args():
    sig = inspect.signature(cardFace.__init__)
    params = list(sig.parameters.keys())
    assert "Club" in params, "Missing parameter 'Club'"
    assert "has_a" in params, "Missing parameter 'has_a'"

def test_cardface_has_Club():
    assert hasattr(cardFace, "Club")
    descriptor = None
    for klass in cardFace.__mro__:
        if "Club" in klass.__dict__:
            descriptor = klass.__dict__["Club"]
            break
    assert isinstance(descriptor, property)

def test_cardface_has_has_a():
    assert hasattr(cardFace, "has_a")
    descriptor = None
    for klass in cardFace.__mro__:
        if "has_a" in klass.__dict__:
            descriptor = klass.__dict__["has_a"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(card)


def test_card_constructor_exists():
    assert callable(card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(card.__init__)
    params = list(sig.parameters.keys())
    assert "has_a1" in params, "Missing parameter 'has_a1'"
    assert "has_a" in params, "Missing parameter 'has_a'"

def test_card_has_has_a1():
    assert hasattr(card, "has_a1")
    descriptor = None
    for klass in card.__mro__:
        if "has_a1" in klass.__dict__:
            descriptor = klass.__dict__["has_a1"]
            break
    assert isinstance(descriptor, property)

def test_card_has_has_a():
    assert hasattr(card, "has_a")
    descriptor = None
    for klass in card.__mro__:
        if "has_a" in klass.__dict__:
            descriptor = klass.__dict__["has_a"]
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
ElevensGame_strategy = st.builds(
    ElevensGame,
    creates_Play_and_Deck=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    creates_and_shuffles=
        st.none()
)
Player_strategy = st.builds(
    Player,
    has_a=
        st.none()
)
cardValue_strategy = st.builds(
    cardValue,
    Jack=
        st.none(),
    King=
        st.none(),
    Ace=
        st.none(),
    Queen=
        st.none()
)
cardFace_strategy = st.builds(
    cardFace,
    Club=
        st.none(),
    has_a=
        st.none()
)
card_strategy = st.builds(
    card,
    has_a1=
        st.none(),
    has_a=
        st.none()
)

@given(instance=ElevensGame_strategy)
@settings(max_examples=50)
def test_elevensgame_instantiation(instance):
    assert isinstance(instance, ElevensGame)



@given(instance=ElevensGame_strategy)
def test_elevensgame_creates_Play_and_Deck_setter(instance):
    original = instance.creates_Play_and_Deck
    instance.creates_Play_and_Deck = original
    assert instance.creates_Play_and_Deck == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_creates_and_shuffles_setter(instance):
    original = instance.creates_and_shuffles
    instance.creates_and_shuffles = original
    assert instance.creates_and_shuffles == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_has_a_setter(instance):
    original = instance.has_a
    instance.has_a = original
    assert instance.has_a == original

@given(instance=cardValue_strategy)
@settings(max_examples=50)
def test_cardvalue_instantiation(instance):
    assert isinstance(instance, cardValue)



@given(instance=cardValue_strategy)
def test_cardvalue_Jack_setter(instance):
    original = instance.Jack
    instance.Jack = original
    assert instance.Jack == original



@given(instance=cardValue_strategy)
def test_cardvalue_King_setter(instance):
    original = instance.King
    instance.King = original
    assert instance.King == original



@given(instance=cardValue_strategy)
def test_cardvalue_Ace_setter(instance):
    original = instance.Ace
    instance.Ace = original
    assert instance.Ace == original



@given(instance=cardValue_strategy)
def test_cardvalue_Queen_setter(instance):
    original = instance.Queen
    instance.Queen = original
    assert instance.Queen == original

@given(instance=cardFace_strategy)
@settings(max_examples=50)
def test_cardface_instantiation(instance):
    assert isinstance(instance, cardFace)



@given(instance=cardFace_strategy)
def test_cardface_Club_setter(instance):
    original = instance.Club
    instance.Club = original
    assert instance.Club == original



@given(instance=cardFace_strategy)
def test_cardface_has_a_setter(instance):
    original = instance.has_a
    instance.has_a = original
    assert instance.has_a == original

@given(instance=card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, card)



@given(instance=card_strategy)
def test_card_has_a1_setter(instance):
    original = instance.has_a1
    instance.has_a1 = original
    assert instance.has_a1 == original



@given(instance=card_strategy)
def test_card_has_a_setter(instance):
    original = instance.has_a
    instance.has_a = original
    assert instance.has_a == original
