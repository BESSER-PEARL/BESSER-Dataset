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
    Elevens,
    Enumeration,
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
    assert "Suit" in params, "Missing parameter 'Suit'"
    assert "Character" in params, "Missing parameter 'Character'"

def test_cards_has_Suit():
    assert hasattr(Cards, "Suit")
    descriptor = None
    for klass in Cards.__mro__:
        if "Suit" in klass.__dict__:
            descriptor = klass.__dict__["Suit"]
            break
    assert isinstance(descriptor, property)

def test_cards_has_Character():
    assert hasattr(Cards, "Character")
    descriptor = None
    for klass in Cards.__mro__:
        if "Character" in klass.__dict__:
            descriptor = klass.__dict__["Character"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_deck_has_attribute():
    assert hasattr(Deck, "attribute")
    descriptor = None
    for klass in Deck.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
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



def test_elevens_is_not_abstract():
    assert not inspect.isabstract(Elevens)


def test_elevens_constructor_exists():
    assert callable(Elevens.__init__)


def test_elevens_constructor_args():
    sig = inspect.signature(Elevens.__init__)
    params = list(sig.parameters.keys())
    assert "_attr" in params, "Missing parameter '_attr'"

def test_elevens_has__attr():
    assert hasattr(Elevens, "_attr")
    descriptor = None
    for klass in Elevens.__mro__:
        if "_attr" in klass.__dict__:
            descriptor = klass.__dict__["_attr"]
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
Cards_strategy = st.builds(
    Cards,
    Suit=
        safe_text,
    Character=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    attribute=
        safe_text
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
Elevens_strategy = st.builds(
    Elevens,
    _attr=
        st.none()
)

@given(instance=Cards_strategy)
@settings(max_examples=50)
def test_cards_instantiation(instance):
    assert isinstance(instance, Cards)



@given(instance=Cards_strategy)
def test_cards_Suit_setter(instance):
    original = instance.Suit
    instance.Suit = original
    assert instance.Suit == original



@given(instance=Cards_strategy)
def test_cards_Character_setter(instance):
    original = instance.Character
    instance.Character = original
    assert instance.Character == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

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

@given(instance=Elevens_strategy)
@settings(max_examples=50)
def test_elevens_instantiation(instance):
    assert isinstance(instance, Elevens)



@given(instance=Elevens_strategy)
def test_elevens__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original
