import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    GoFish,
    Rules,
    Game,
    Computer,
    b,
    Player,
    Deck,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_gofish_is_not_abstract():
    assert not inspect.isabstract(GoFish)


def test_gofish_constructor_exists():
    assert callable(GoFish.__init__)


def test_gofish_constructor_args():
    sig = inspect.signature(GoFish.__init__)
    params = list(sig.parameters.keys())



def test_rules_is_not_abstract():
    assert not inspect.isabstract(Rules)


def test_rules_constructor_exists():
    assert callable(Rules.__init__)


def test_rules_constructor_args():
    sig = inspect.signature(Rules.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "currentRules" in params, "Missing parameter 'currentRules'"

def test_rules_has_attribute():
    assert hasattr(Rules, "attribute")
    descriptor = None
    for klass in Rules.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_rules_has_currentRules():
    assert hasattr(Rules, "currentRules")
    descriptor = None
    for klass in Rules.__mro__:
        if "currentRules" in klass.__dict__:
            descriptor = klass.__dict__["currentRules"]
            break
    assert isinstance(descriptor, property)



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())



def test_computer_is_not_abstract():
    assert not inspect.isabstract(Computer)


def test_computer_constructor_exists():
    assert callable(Computer.__init__)


def test_computer_constructor_args():
    sig = inspect.signature(Computer.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(b)


def test_b_constructor_exists():
    assert callable(b.__init__)


def test_b_constructor_args():
    sig = inspect.signature(b.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hand" in params, "Missing parameter 'hand'"

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_player_has_hand():
    assert hasattr(Player, "hand")
    descriptor = None
    for klass in Player.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)



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



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "color" in params, "Missing parameter 'color'"
    assert "number" in params, "Missing parameter 'number'"

def test_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_color():
    assert hasattr(Card, "color")
    descriptor = None
    for klass in Card.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_card_has_number():
    assert hasattr(Card, "number")
    descriptor = None
    for klass in Card.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
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
Class_strategy = st.builds(
    Class,
)
GoFish_strategy = st.builds(
    GoFish,
)
Rules_strategy = st.builds(
    Rules,
    attribute=
        safe_text,
    currentRules=
        st.booleans()
)
Game_strategy = st.builds(
    Game,
)
Computer_strategy = st.builds(
    Computer,
)
b_strategy = st.builds(
    b,
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    hand=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    deck=
        safe_text
)
Card_strategy = st.builds(
    Card,
    suit=
        safe_text,
    color=
        safe_text,
    number=
        st.integers()
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=GoFish_strategy)
@settings(max_examples=50)
def test_gofish_instantiation(instance):
    assert isinstance(instance, GoFish)

@given(instance=Rules_strategy)
@settings(max_examples=50)
def test_rules_instantiation(instance):
    assert isinstance(instance, Rules)



@given(instance=Rules_strategy)
def test_rules_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Rules_strategy)
def test_rules_currentRules_setter(instance):
    original = instance.currentRules
    instance.currentRules = original
    assert instance.currentRules == original

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)

@given(instance=Computer_strategy)
@settings(max_examples=50)
def test_computer_instantiation(instance):
    assert isinstance(instance, Computer)

@given(instance=b_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, b)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_card_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Card_strategy)
def test_card_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original
