import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Blackjack,
    Player,
    Card,
    Cards,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_blackjack_is_not_abstract():
    assert not inspect.isabstract(Blackjack)


def test_blackjack_constructor_exists():
    assert callable(Blackjack.__init__)


def test_blackjack_constructor_args():
    sig = inspect.signature(Blackjack.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "players" in params, "Missing parameter 'players'"
    assert "dealer" in params, "Missing parameter 'dealer'"

def test_blackjack_has_cards():
    assert hasattr(Blackjack, "cards")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_has_players():
    assert hasattr(Blackjack, "players")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_has_dealer():
    assert hasattr(Blackjack, "dealer")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "dealer" in klass.__dict__:
            descriptor = klass.__dict__["dealer"]
            break
    assert isinstance(descriptor, property)



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



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value_dict" in params, "Missing parameter 'value_dict'"

def test_card_has_value_dict():
    assert hasattr(Card, "value_dict")
    descriptor = None
    for klass in Card.__mro__:
        if "value_dict" in klass.__dict__:
            descriptor = klass.__dict__["value_dict"]
            break
    assert isinstance(descriptor, property)



def test_cards_is_not_abstract():
    assert not inspect.isabstract(Cards)


def test_cards_constructor_exists():
    assert callable(Cards.__init__)


def test_cards_constructor_args():
    sig = inspect.signature(Cards.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "number" in params, "Missing parameter 'number'"

def test_cards_has_color():
    assert hasattr(Cards, "color")
    descriptor = None
    for klass in Cards.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_cards_has_number():
    assert hasattr(Cards, "number")
    descriptor = None
    for klass in Cards.__mro__:
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
Blackjack_strategy = st.builds(
    Blackjack,
    cards=
        st.none(),
    players=
        safe_text,
    dealer=
        st.none()
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    hand=
        safe_text
)
Card_strategy = st.builds(
    Card,
    value_dict=
        safe_text
)
Cards_strategy = st.builds(
    Cards,
    color=
        safe_text,
    number=
        safe_text
)

@given(instance=Blackjack_strategy)
@settings(max_examples=50)
def test_blackjack_instantiation(instance):
    assert isinstance(instance, Blackjack)



@given(instance=Blackjack_strategy)
def test_blackjack_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Blackjack_strategy)
def test_blackjack_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=Blackjack_strategy)
def test_blackjack_dealer_setter(instance):
    original = instance.dealer
    instance.dealer = original
    assert instance.dealer == original

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

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_value_dict_setter(instance):
    original = instance.value_dict
    instance.value_dict = original
    assert instance.value_dict == original

@given(instance=Cards_strategy)
@settings(max_examples=50)
def test_cards_instantiation(instance):
    assert isinstance(instance, Cards)



@given(instance=Cards_strategy)
def test_cards_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Cards_strategy)
def test_cards_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original
