import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Player,
    SUIT_external,
    RANK_external,
    Role_external,
    PlayerView,
    PokerTableView,
    StandardDeck,
    T,
    GameRound,
    __abstract___BaseDeck,
    PokerTable,
    PlayCard,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "stack" in params, "Missing parameter 'stack'"
    assert "bid" in params, "Missing parameter 'bid'"

def test_player_has_stack():
    assert hasattr(Player, "stack")
    descriptor = None
    for klass in Player.__mro__:
        if "stack" in klass.__dict__:
            descriptor = klass.__dict__["stack"]
            break
    assert isinstance(descriptor, property)

def test_player_has_bid():
    assert hasattr(Player, "bid")
    descriptor = None
    for klass in Player.__mro__:
        if "bid" in klass.__dict__:
            descriptor = klass.__dict__["bid"]
            break
    assert isinstance(descriptor, property)



def test_suit_external_is_not_abstract():
    assert not inspect.isabstract(SUIT_external)


def test_suit_external_constructor_exists():
    assert callable(SUIT_external.__init__)


def test_suit_external_constructor_args():
    sig = inspect.signature(SUIT_external.__init__)
    params = list(sig.parameters.keys())



def test_rank_external_is_not_abstract():
    assert not inspect.isabstract(RANK_external)


def test_rank_external_constructor_exists():
    assert callable(RANK_external.__init__)


def test_rank_external_constructor_args():
    sig = inspect.signature(RANK_external.__init__)
    params = list(sig.parameters.keys())



def test_role_external_is_not_abstract():
    assert not inspect.isabstract(Role_external)


def test_role_external_constructor_exists():
    assert callable(Role_external.__init__)


def test_role_external_constructor_args():
    sig = inspect.signature(Role_external.__init__)
    params = list(sig.parameters.keys())



def test_playerview_is_not_abstract():
    assert not inspect.isabstract(PlayerView)


def test_playerview_constructor_exists():
    assert callable(PlayerView.__init__)


def test_playerview_constructor_args():
    sig = inspect.signature(PlayerView.__init__)
    params = list(sig.parameters.keys())



def test_pokertableview_is_not_abstract():
    assert not inspect.isabstract(PokerTableView)


def test_pokertableview_constructor_exists():
    assert callable(PokerTableView.__init__)


def test_pokertableview_constructor_args():
    sig = inspect.signature(PokerTableView.__init__)
    params = list(sig.parameters.keys())



def test_standarddeck_is_not_abstract():
    assert not inspect.isabstract(StandardDeck)


def test_standarddeck_constructor_exists():
    assert callable(StandardDeck.__init__)


def test_standarddeck_constructor_args():
    sig = inspect.signature(StandardDeck.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_gameround_is_not_abstract():
    assert not inspect.isabstract(GameRound)


def test_gameround_constructor_exists():
    assert callable(GameRound.__init__)


def test_gameround_constructor_args():
    sig = inspect.signature(GameRound.__init__)
    params = list(sig.parameters.keys())



def test___abstract___basedeck_is_not_abstract():
    assert not inspect.isabstract(__abstract___BaseDeck)


def test___abstract___basedeck_constructor_exists():
    assert callable(__abstract___BaseDeck.__init__)


def test___abstract___basedeck_constructor_args():
    sig = inspect.signature(__abstract___BaseDeck.__init__)
    params = list(sig.parameters.keys())



def test_pokertable_is_not_abstract():
    assert not inspect.isabstract(PokerTable)


def test_pokertable_constructor_exists():
    assert callable(PokerTable.__init__)


def test_pokertable_constructor_args():
    sig = inspect.signature(PokerTable.__init__)
    params = list(sig.parameters.keys())



def test_playcard_is_not_abstract():
    assert not inspect.isabstract(PlayCard)


def test_playcard_constructor_exists():
    assert callable(PlayCard.__init__)


def test_playcard_constructor_args():
    sig = inspect.signature(PlayCard.__init__)
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
Player_strategy = st.builds(
    Player,
    stack=
        st.integers(),
    bid=
        st.integers()
)
SUIT_external_strategy = st.builds(
    SUIT_external,
)
RANK_external_strategy = st.builds(
    RANK_external,
)
Role_external_strategy = st.builds(
    Role_external,
)
PlayerView_strategy = st.builds(
    PlayerView,
)
PokerTableView_strategy = st.builds(
    PokerTableView,
)
StandardDeck_strategy = st.builds(
    StandardDeck,
)
T_strategy = st.builds(
    T,
)
GameRound_strategy = st.builds(
    GameRound,
)
__abstract___BaseDeck_strategy = st.builds(
    __abstract___BaseDeck,
)
PokerTable_strategy = st.builds(
    PokerTable,
)
PlayCard_strategy = st.builds(
    PlayCard,
)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_stack_setter(instance):
    original = instance.stack
    instance.stack = original
    assert instance.stack == original



@given(instance=Player_strategy)
def test_player_bid_setter(instance):
    original = instance.bid
    instance.bid = original
    assert instance.bid == original

@given(instance=SUIT_external_strategy)
@settings(max_examples=50)
def test_suit_external_instantiation(instance):
    assert isinstance(instance, SUIT_external)

@given(instance=RANK_external_strategy)
@settings(max_examples=50)
def test_rank_external_instantiation(instance):
    assert isinstance(instance, RANK_external)

@given(instance=Role_external_strategy)
@settings(max_examples=50)
def test_role_external_instantiation(instance):
    assert isinstance(instance, Role_external)

@given(instance=PlayerView_strategy)
@settings(max_examples=50)
def test_playerview_instantiation(instance):
    assert isinstance(instance, PlayerView)

@given(instance=PokerTableView_strategy)
@settings(max_examples=50)
def test_pokertableview_instantiation(instance):
    assert isinstance(instance, PokerTableView)

@given(instance=StandardDeck_strategy)
@settings(max_examples=50)
def test_standarddeck_instantiation(instance):
    assert isinstance(instance, StandardDeck)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=GameRound_strategy)
@settings(max_examples=50)
def test_gameround_instantiation(instance):
    assert isinstance(instance, GameRound)

@given(instance=__abstract___BaseDeck_strategy)
@settings(max_examples=50)
def test___abstract___basedeck_instantiation(instance):
    assert isinstance(instance, __abstract___BaseDeck)

@given(instance=PokerTable_strategy)
@settings(max_examples=50)
def test_pokertable_instantiation(instance):
    assert isinstance(instance, PokerTable)

@given(instance=PlayCard_strategy)
@settings(max_examples=50)
def test_playcard_instantiation(instance):
    assert isinstance(instance, PlayCard)
