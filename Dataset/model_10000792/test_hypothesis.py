import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    JFrame,
    BlackjackGUI,
    BlackjackDriver,
    Card,
    Dealer,
    Player,
    Blackjack,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jframe_is_not_abstract():
    assert not inspect.isabstract(JFrame)


def test_jframe_constructor_exists():
    assert callable(JFrame.__init__)


def test_jframe_constructor_args():
    sig = inspect.signature(JFrame.__init__)
    params = list(sig.parameters.keys())



def test_blackjackgui_is_not_abstract():
    assert not inspect.isabstract(BlackjackGUI)


def test_blackjackgui_constructor_exists():
    assert callable(BlackjackGUI.__init__)


def test_blackjackgui_constructor_args():
    sig = inspect.signature(BlackjackGUI.__init__)
    params = list(sig.parameters.keys())



def test_blackjackdriver_is_not_abstract():
    assert not inspect.isabstract(BlackjackDriver)


def test_blackjackdriver_constructor_exists():
    assert callable(BlackjackDriver.__init__)


def test_blackjackdriver_constructor_args():
    sig = inspect.signature(BlackjackDriver.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "value" in params, "Missing parameter 'value'"

def test_card_has_rank():
    assert hasattr(Card, "rank")
    descriptor = None
    for klass in Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_value():
    assert hasattr(Card, "value")
    descriptor = None
    for klass in Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "totalAmount" in params, "Missing parameter 'totalAmount'"

def test_player_has_totalAmount():
    assert hasattr(Player, "totalAmount")
    descriptor = None
    for klass in Player.__mro__:
        if "totalAmount" in klass.__dict__:
            descriptor = klass.__dict__["totalAmount"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_is_not_abstract():
    assert not inspect.isabstract(Blackjack)


def test_blackjack_constructor_exists():
    assert callable(Blackjack.__init__)


def test_blackjack_constructor_args():
    sig = inspect.signature(Blackjack.__init__)
    params = list(sig.parameters.keys())
    assert "playerName" in params, "Missing parameter 'playerName'"
    assert "players" in params, "Missing parameter 'players'"
    assert "count" in params, "Missing parameter 'count'"
    assert "hand__" in params, "Missing parameter 'hand__'"

def test_blackjack_has_playerName():
    assert hasattr(Blackjack, "playerName")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "playerName" in klass.__dict__:
            descriptor = klass.__dict__["playerName"]
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

def test_blackjack_has_count():
    assert hasattr(Blackjack, "count")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_has_hand__():
    assert hasattr(Blackjack, "hand__")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "hand__" in klass.__dict__:
            descriptor = klass.__dict__["hand__"]
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
JFrame_strategy = st.builds(
    JFrame,
)
BlackjackGUI_strategy = st.builds(
    BlackjackGUI,
)
BlackjackDriver_strategy = st.builds(
    BlackjackDriver,
)
Card_strategy = st.builds(
    Card,
    rank=
        st.integers(),
    suit=
        safe_text,
    value=
        st.integers()
)
Dealer_strategy = st.builds(
    Dealer,
)
Player_strategy = st.builds(
    Player,
    totalAmount=
        st.integers()
)
Blackjack_strategy = st.builds(
    Blackjack,
    playerName=
        safe_text,
    players=
        st.integers(),
    count=
        st.integers(),
    hand__=
        st.none()
)

@given(instance=JFrame_strategy)
@settings(max_examples=50)
def test_jframe_instantiation(instance):
    assert isinstance(instance, JFrame)

@given(instance=BlackjackGUI_strategy)
@settings(max_examples=50)
def test_blackjackgui_instantiation(instance):
    assert isinstance(instance, BlackjackGUI)

@given(instance=BlackjackDriver_strategy)
@settings(max_examples=50)
def test_blackjackdriver_instantiation(instance):
    assert isinstance(instance, BlackjackDriver)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Dealer_strategy)
@settings(max_examples=50)
def test_dealer_instantiation(instance):
    assert isinstance(instance, Dealer)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_totalAmount_setter(instance):
    original = instance.totalAmount
    instance.totalAmount = original
    assert instance.totalAmount == original

@given(instance=Blackjack_strategy)
@settings(max_examples=50)
def test_blackjack_instantiation(instance):
    assert isinstance(instance, Blackjack)



@given(instance=Blackjack_strategy)
def test_blackjack_playerName_setter(instance):
    original = instance.playerName
    instance.playerName = original
    assert instance.playerName == original



@given(instance=Blackjack_strategy)
def test_blackjack_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=Blackjack_strategy)
def test_blackjack_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original



@given(instance=Blackjack_strategy)
def test_blackjack_hand___setter(instance):
    original = instance.hand__
    instance.hand__ = original
    assert instance.hand__ == original
