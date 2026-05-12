import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Driver,
    T,
    Players,
    Card_Interface,
    Deck,
    Strategy1___Strategy2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_driver_is_not_abstract():
    assert not inspect.isabstract(Driver)


def test_driver_constructor_exists():
    assert callable(Driver.__init__)


def test_driver_constructor_args():
    sig = inspect.signature(Driver.__init__)
    params = list(sig.parameters.keys())
    assert "Score" in params, "Missing parameter 'Score'"
    assert "removedCard" in params, "Missing parameter 'removedCard'"

def test_driver_has_Score():
    assert hasattr(Driver, "Score")
    descriptor = None
    for klass in Driver.__mro__:
        if "Score" in klass.__dict__:
            descriptor = klass.__dict__["Score"]
            break
    assert isinstance(descriptor, property)

def test_driver_has_removedCard():
    assert hasattr(Driver, "removedCard")
    descriptor = None
    for klass in Driver.__mro__:
        if "removedCard" in klass.__dict__:
            descriptor = klass.__dict__["removedCard"]
            break
    assert isinstance(descriptor, property)



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_players_is_not_abstract():
    assert not inspect.isabstract(Players)


def test_players_constructor_exists():
    assert callable(Players.__init__)


def test_players_constructor_args():
    sig = inspect.signature(Players.__init__)
    params = list(sig.parameters.keys())
    assert "Planet" in params, "Missing parameter 'Planet'"
    assert "Player2" in params, "Missing parameter 'Player2'"
    assert "Player1" in params, "Missing parameter 'Player1'"

def test_players_has_Planet():
    assert hasattr(Players, "Planet")
    descriptor = None
    for klass in Players.__mro__:
        if "Planet" in klass.__dict__:
            descriptor = klass.__dict__["Planet"]
            break
    assert isinstance(descriptor, property)

def test_players_has_Player2():
    assert hasattr(Players, "Player2")
    descriptor = None
    for klass in Players.__mro__:
        if "Player2" in klass.__dict__:
            descriptor = klass.__dict__["Player2"]
            break
    assert isinstance(descriptor, property)

def test_players_has_Player1():
    assert hasattr(Players, "Player1")
    descriptor = None
    for klass in Players.__mro__:
        if "Player1" in klass.__dict__:
            descriptor = klass.__dict__["Player1"]
            break
    assert isinstance(descriptor, property)



def test_card_interface_is_not_abstract():
    assert not inspect.isabstract(Card_Interface)


def test_card_interface_constructor_exists():
    assert callable(Card_Interface.__init__)


def test_card_interface_constructor_args():
    sig = inspect.signature(Card_Interface.__init__)
    params = list(sig.parameters.keys())



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck__" in params, "Missing parameter 'deck__'"
    assert "shuffle__" in params, "Missing parameter 'shuffle__'"
    assert "isEmpty__" in params, "Missing parameter 'isEmpty__'"

def test_deck_has_deck__():
    assert hasattr(Deck, "deck__")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck__" in klass.__dict__:
            descriptor = klass.__dict__["deck__"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_shuffle__():
    assert hasattr(Deck, "shuffle__")
    descriptor = None
    for klass in Deck.__mro__:
        if "shuffle__" in klass.__dict__:
            descriptor = klass.__dict__["shuffle__"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_isEmpty__():
    assert hasattr(Deck, "isEmpty__")
    descriptor = None
    for klass in Deck.__mro__:
        if "isEmpty__" in klass.__dict__:
            descriptor = klass.__dict__["isEmpty__"]
            break
    assert isinstance(descriptor, property)



def test_strategy1___strategy2_is_not_abstract():
    assert not inspect.isabstract(Strategy1___Strategy2)


def test_strategy1___strategy2_constructor_exists():
    assert callable(Strategy1___Strategy2.__init__)


def test_strategy1___strategy2_constructor_args():
    sig = inspect.signature(Strategy1___Strategy2.__init__)
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
Driver_strategy = st.builds(
    Driver,
    Score=
        st.integers(),
    removedCard=
        st.integers()
)
T_strategy = st.builds(
    T,
)
Players_strategy = st.builds(
    Players,
    Planet=
        st.none(),
    Player2=
        st.none(),
    Player1=
        st.none()
)
Card_Interface_strategy = st.builds(
    Card_Interface,
)
Deck_strategy = st.builds(
    Deck,
    deck__=
        st.none(),
    shuffle__=
        safe_text,
    isEmpty__=
        st.booleans()
)
Strategy1___Strategy2_strategy = st.builds(
    Strategy1___Strategy2,
)

@given(instance=Driver_strategy)
@settings(max_examples=50)
def test_driver_instantiation(instance):
    assert isinstance(instance, Driver)



@given(instance=Driver_strategy)
def test_driver_Score_setter(instance):
    original = instance.Score
    instance.Score = original
    assert instance.Score == original



@given(instance=Driver_strategy)
def test_driver_removedCard_setter(instance):
    original = instance.removedCard
    instance.removedCard = original
    assert instance.removedCard == original

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=Players_strategy)
@settings(max_examples=50)
def test_players_instantiation(instance):
    assert isinstance(instance, Players)



@given(instance=Players_strategy)
def test_players_Planet_setter(instance):
    original = instance.Planet
    instance.Planet = original
    assert instance.Planet == original



@given(instance=Players_strategy)
def test_players_Player2_setter(instance):
    original = instance.Player2
    instance.Player2 = original
    assert instance.Player2 == original



@given(instance=Players_strategy)
def test_players_Player1_setter(instance):
    original = instance.Player1
    instance.Player1 = original
    assert instance.Player1 == original

@given(instance=Card_Interface_strategy)
@settings(max_examples=50)
def test_card_interface_instantiation(instance):
    assert isinstance(instance, Card_Interface)

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_deck___setter(instance):
    original = instance.deck__
    instance.deck__ = original
    assert instance.deck__ == original



@given(instance=Deck_strategy)
def test_deck_shuffle___setter(instance):
    original = instance.shuffle__
    instance.shuffle__ = original
    assert instance.shuffle__ == original



@given(instance=Deck_strategy)
def test_deck_isEmpty___setter(instance):
    original = instance.isEmpty__
    instance.isEmpty__ = original
    assert instance.isEmpty__ == original

@given(instance=Strategy1___Strategy2_strategy)
@settings(max_examples=50)
def test_strategy1___strategy2_instantiation(instance):
    assert isinstance(instance, Strategy1___Strategy2)
