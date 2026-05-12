import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BlackJack_Card,
    BlackJack_Game,
    BlackJack_House,
    BlackJack_Player,
    BlackJack_Deck,
    BlackJack_Generic_Player,
    BlackJack_Hand,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_blackjack_card_is_not_abstract():
    assert not inspect.isabstract(BlackJack_Card)


def test_blackjack_card_constructor_exists():
    assert callable(BlackJack_Card.__init__)


def test_blackjack_card_constructor_args():
    sig = inspect.signature(BlackJack_Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "rank" in params, "Missing parameter 'rank'"
    assert "color" in params, "Missing parameter 'color'"

def test_blackjack_card_has_value():
    assert hasattr(BlackJack_Card, "value")
    descriptor = None
    for klass in BlackJack_Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_card_has_rank():
    assert hasattr(BlackJack_Card, "rank")
    descriptor = None
    for klass in BlackJack_Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_card_has_color():
    assert hasattr(BlackJack_Card, "color")
    descriptor = None
    for klass in BlackJack_Card.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_game_is_not_abstract():
    assert not inspect.isabstract(BlackJack_Game)


def test_blackjack_game_constructor_exists():
    assert callable(BlackJack_Game.__init__)


def test_blackjack_game_constructor_args():
    sig = inspect.signature(BlackJack_Game.__init__)
    params = list(sig.parameters.keys())
    assert "win_loose" in params, "Missing parameter 'win_loose'"

def test_blackjack_game_has_win_loose():
    assert hasattr(BlackJack_Game, "win_loose")
    descriptor = None
    for klass in BlackJack_Game.__mro__:
        if "win_loose" in klass.__dict__:
            descriptor = klass.__dict__["win_loose"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_house_is_not_abstract():
    assert not inspect.isabstract(BlackJack_House)


def test_blackjack_house_constructor_exists():
    assert callable(BlackJack_House.__init__)


def test_blackjack_house_constructor_args():
    sig = inspect.signature(BlackJack_House.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_player_is_not_abstract():
    assert not inspect.isabstract(BlackJack_Player)


def test_blackjack_player_constructor_exists():
    assert callable(BlackJack_Player.__init__)


def test_blackjack_player_constructor_args():
    sig = inspect.signature(BlackJack_Player.__init__)
    params = list(sig.parameters.keys())
    assert "limit" in params, "Missing parameter 'limit'"

def test_blackjack_player_has_limit():
    assert hasattr(BlackJack_Player, "limit")
    descriptor = None
    for klass in BlackJack_Player.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_deck_is_not_abstract():
    assert not inspect.isabstract(BlackJack_Deck)


def test_blackjack_deck_constructor_exists():
    assert callable(BlackJack_Deck.__init__)


def test_blackjack_deck_constructor_args():
    sig = inspect.signature(BlackJack_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "nextItem" in params, "Missing parameter 'nextItem'"

def test_blackjack_deck_has_nextItem():
    assert hasattr(BlackJack_Deck, "nextItem")
    descriptor = None
    for klass in BlackJack_Deck.__mro__:
        if "nextItem" in klass.__dict__:
            descriptor = klass.__dict__["nextItem"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_generic_player_is_not_abstract():
    assert not inspect.isabstract(BlackJack_Generic_Player)


def test_blackjack_generic_player_constructor_exists():
    assert callable(BlackJack_Generic_Player.__init__)


def test_blackjack_generic_player_constructor_args():
    sig = inspect.signature(BlackJack_Generic_Player.__init__)
    params = list(sig.parameters.keys())
    assert "valueOfHand" in params, "Missing parameter 'valueOfHand'"

def test_blackjack_generic_player_has_valueOfHand():
    assert hasattr(BlackJack_Generic_Player, "valueOfHand")
    descriptor = None
    for klass in BlackJack_Generic_Player.__mro__:
        if "valueOfHand" in klass.__dict__:
            descriptor = klass.__dict__["valueOfHand"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_hand_is_not_abstract():
    assert not inspect.isabstract(BlackJack_Hand)


def test_blackjack_hand_constructor_exists():
    assert callable(BlackJack_Hand.__init__)


def test_blackjack_hand_constructor_args():
    sig = inspect.signature(BlackJack_Hand.__init__)
    params = list(sig.parameters.keys())
    assert "ArrayList" in params, "Missing parameter 'ArrayList'"

def test_blackjack_hand_has_ArrayList():
    assert hasattr(BlackJack_Hand, "ArrayList")
    descriptor = None
    for klass in BlackJack_Hand.__mro__:
        if "ArrayList" in klass.__dict__:
            descriptor = klass.__dict__["ArrayList"]
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
BlackJack_Card_strategy = st.builds(
    BlackJack_Card,
    value=
        st.integers(),
    rank=
        st.integers(),
    color=
        safe_text
)
BlackJack_Game_strategy = st.builds(
    BlackJack_Game,
    win_loose=
        st.booleans()
)
BlackJack_House_strategy = st.builds(
    BlackJack_House,
)
BlackJack_Player_strategy = st.builds(
    BlackJack_Player,
    limit=
        st.integers()
)
BlackJack_Deck_strategy = st.builds(
    BlackJack_Deck,
    nextItem=
        st.integers()
)
BlackJack_Generic_Player_strategy = st.builds(
    BlackJack_Generic_Player,
    valueOfHand=
        st.integers()
)
BlackJack_Hand_strategy = st.builds(
    BlackJack_Hand,
    ArrayList=
        st.none()
)

@given(instance=BlackJack_Card_strategy)
@settings(max_examples=50)
def test_blackjack_card_instantiation(instance):
    assert isinstance(instance, BlackJack_Card)



@given(instance=BlackJack_Card_strategy)
def test_blackjack_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=BlackJack_Card_strategy)
def test_blackjack_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=BlackJack_Card_strategy)
def test_blackjack_card_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=BlackJack_Game_strategy)
@settings(max_examples=50)
def test_blackjack_game_instantiation(instance):
    assert isinstance(instance, BlackJack_Game)



@given(instance=BlackJack_Game_strategy)
def test_blackjack_game_win_loose_setter(instance):
    original = instance.win_loose
    instance.win_loose = original
    assert instance.win_loose == original

@given(instance=BlackJack_House_strategy)
@settings(max_examples=50)
def test_blackjack_house_instantiation(instance):
    assert isinstance(instance, BlackJack_House)

@given(instance=BlackJack_Player_strategy)
@settings(max_examples=50)
def test_blackjack_player_instantiation(instance):
    assert isinstance(instance, BlackJack_Player)



@given(instance=BlackJack_Player_strategy)
def test_blackjack_player_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original

@given(instance=BlackJack_Deck_strategy)
@settings(max_examples=50)
def test_blackjack_deck_instantiation(instance):
    assert isinstance(instance, BlackJack_Deck)



@given(instance=BlackJack_Deck_strategy)
def test_blackjack_deck_nextItem_setter(instance):
    original = instance.nextItem
    instance.nextItem = original
    assert instance.nextItem == original

@given(instance=BlackJack_Generic_Player_strategy)
@settings(max_examples=50)
def test_blackjack_generic_player_instantiation(instance):
    assert isinstance(instance, BlackJack_Generic_Player)



@given(instance=BlackJack_Generic_Player_strategy)
def test_blackjack_generic_player_valueOfHand_setter(instance):
    original = instance.valueOfHand
    instance.valueOfHand = original
    assert instance.valueOfHand == original

@given(instance=BlackJack_Hand_strategy)
@settings(max_examples=50)
def test_blackjack_hand_instantiation(instance):
    assert isinstance(instance, BlackJack_Hand)



@given(instance=BlackJack_Hand_strategy)
def test_blackjack_hand_ArrayList_setter(instance):
    original = instance.ArrayList
    instance.ArrayList = original
    assert instance.ArrayList == original
