import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Dice,
    Pawn,
    Card,
    Board,
    Player,
    CardType,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dice_is_not_abstract():
    assert not inspect.isabstract(Dice)


def test_dice_constructor_exists():
    assert callable(Dice.__init__)


def test_dice_constructor_args():
    sig = inspect.signature(Dice.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dice_has_value():
    assert hasattr(Dice, "value")
    descriptor = None
    for klass in Dice.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pawn_is_not_abstract():
    assert not inspect.isabstract(Pawn)


def test_pawn_constructor_exists():
    assert callable(Pawn.__init__)


def test_pawn_constructor_args():
    sig = inspect.signature(Pawn.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "color" in params, "Missing parameter 'color'"

def test_pawn_has_position():
    assert hasattr(Pawn, "position")
    descriptor = None
    for klass in Pawn.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_pawn_has_color():
    assert hasattr(Pawn, "color")
    descriptor = None
    for klass in Pawn.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"

def test_card_has_card():
    assert hasattr(Card, "card")
    descriptor = None
    for klass in Card.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_board_is_not_abstract():
    assert not inspect.isabstract(Board)


def test_board_constructor_exists():
    assert callable(Board.__init__)


def test_board_constructor_args():
    sig = inspect.signature(Board.__init__)
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

def test_cardtype_exists():
    # Check that the Enumeration exists
    assert CardType is not None

def test_cardtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardType"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
Dice_strategy = st.builds(
    Dice,
    value=
        st.integers()
)
Pawn_strategy = st.builds(
    Pawn,
    position=
        st.integers(),
    color=
        st.none()
)
Card_strategy = st.builds(
    Card,
    card=
        st.none()
)
Board_strategy = st.builds(
    Board,
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text
)

@given(instance=Dice_strategy)
@settings(max_examples=50)
def test_dice_instantiation(instance):
    assert isinstance(instance, Dice)



@given(instance=Dice_strategy)
def test_dice_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Pawn_strategy)
@settings(max_examples=50)
def test_pawn_instantiation(instance):
    assert isinstance(instance, Pawn)



@given(instance=Pawn_strategy)
def test_pawn_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=Pawn_strategy)
def test_pawn_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=Board_strategy)
@settings(max_examples=50)
def test_board_instantiation(instance):
    assert isinstance(instance, Board)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
