import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cards,
    Deck,
    Player,
    Class,
    Elevens,
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
    assert "Character" in params, "Missing parameter 'Character'"
    assert "Suit" in params, "Missing parameter 'Suit'"

def test_cards_has_Character():
    assert hasattr(Cards, "Character")
    descriptor = None
    for klass in Cards.__mro__:
        if "Character" in klass.__dict__:
            descriptor = klass.__dict__["Character"]
            break
    assert isinstance(descriptor, property)

def test_cards_has_Suit():
    assert hasattr(Cards, "Suit")
    descriptor = None
    for klass in Cards.__mro__:
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
    assert "Cards" in params, "Missing parameter 'Cards'"

def test_deck_has_Cards():
    assert hasattr(Deck, "Cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "Cards" in klass.__dict__:
            descriptor = klass.__dict__["Cards"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "losses" in params, "Missing parameter 'losses'"
    assert "winRate" in params, "Missing parameter 'winRate'"
    assert "wins" in params, "Missing parameter 'wins'"

def test_player_has_losses():
    assert hasattr(Player, "losses")
    descriptor = None
    for klass in Player.__mro__:
        if "losses" in klass.__dict__:
            descriptor = klass.__dict__["losses"]
            break
    assert isinstance(descriptor, property)

def test_player_has_winRate():
    assert hasattr(Player, "winRate")
    descriptor = None
    for klass in Player.__mro__:
        if "winRate" in klass.__dict__:
            descriptor = klass.__dict__["winRate"]
            break
    assert isinstance(descriptor, property)

def test_player_has_wins():
    assert hasattr(Player, "wins")
    descriptor = None
    for klass in Player.__mro__:
        if "wins" in klass.__dict__:
            descriptor = klass.__dict__["wins"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_elevens_is_not_abstract():
    assert not inspect.isabstract(Elevens)


def test_elevens_constructor_exists():
    assert callable(Elevens.__init__)


def test_elevens_constructor_args():
    sig = inspect.signature(Elevens.__init__)
    params = list(sig.parameters.keys())
    assert "Deck" in params, "Missing parameter 'Deck'"
    assert "Player" in params, "Missing parameter 'Player'"

def test_elevens_has_Deck():
    assert hasattr(Elevens, "Deck")
    descriptor = None
    for klass in Elevens.__mro__:
        if "Deck" in klass.__dict__:
            descriptor = klass.__dict__["Deck"]
            break
    assert isinstance(descriptor, property)

def test_elevens_has_Player():
    assert hasattr(Elevens, "Player")
    descriptor = None
    for klass in Elevens.__mro__:
        if "Player" in klass.__dict__:
            descriptor = klass.__dict__["Player"]
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
    Character=
        safe_text,
    Suit=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    Cards=
        st.none()
)
Player_strategy = st.builds(
    Player,
    losses=
        st.integers(),
    winRate=
        safe_text,
    wins=
        st.integers()
)
Class_strategy = st.builds(
    Class,
)
Elevens_strategy = st.builds(
    Elevens,
    Deck=
        st.none(),
    Player=
        st.none()
)

@given(instance=Cards_strategy)
@settings(max_examples=50)
def test_cards_instantiation(instance):
    assert isinstance(instance, Cards)



@given(instance=Cards_strategy)
def test_cards_Character_setter(instance):
    original = instance.Character
    instance.Character = original
    assert instance.Character == original



@given(instance=Cards_strategy)
def test_cards_Suit_setter(instance):
    original = instance.Suit
    instance.Suit = original
    assert instance.Suit == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_Cards_setter(instance):
    original = instance.Cards
    instance.Cards = original
    assert instance.Cards == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_losses_setter(instance):
    original = instance.losses
    instance.losses = original
    assert instance.losses == original



@given(instance=Player_strategy)
def test_player_winRate_setter(instance):
    original = instance.winRate
    instance.winRate = original
    assert instance.winRate == original



@given(instance=Player_strategy)
def test_player_wins_setter(instance):
    original = instance.wins
    instance.wins = original
    assert instance.wins == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Elevens_strategy)
@settings(max_examples=50)
def test_elevens_instantiation(instance):
    assert isinstance(instance, Elevens)



@given(instance=Elevens_strategy)
def test_elevens_Deck_setter(instance):
    original = instance.Deck
    instance.Deck = original
    assert instance.Deck == original



@given(instance=Elevens_strategy)
def test_elevens_Player_setter(instance):
    original = instance.Player
    instance.Player = original
    assert instance.Player == original
