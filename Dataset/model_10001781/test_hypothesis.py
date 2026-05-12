import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    T3,
    Queue,
    CasinoManager,
    T2,
    T1,
    Tuple,
    Player,
    T,
    Stack,
    Deck,
    Table,
    Executive,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_t3_is_not_abstract():
    assert not inspect.isabstract(T3)


def test_t3_constructor_exists():
    assert callable(T3.__init__)


def test_t3_constructor_args():
    sig = inspect.signature(T3.__init__)
    params = list(sig.parameters.keys())



def test_queue_is_not_abstract():
    assert not inspect.isabstract(Queue)


def test_queue_constructor_exists():
    assert callable(Queue.__init__)


def test_queue_constructor_args():
    sig = inspect.signature(Queue.__init__)
    params = list(sig.parameters.keys())



def test_casinomanager_is_not_abstract():
    assert not inspect.isabstract(CasinoManager)


def test_casinomanager_constructor_exists():
    assert callable(CasinoManager.__init__)


def test_casinomanager_constructor_args():
    sig = inspect.signature(CasinoManager.__init__)
    params = list(sig.parameters.keys())
    assert "waitList" in params, "Missing parameter 'waitList'"
    assert "table" in params, "Missing parameter 'table'"

def test_casinomanager_has_waitList():
    assert hasattr(CasinoManager, "waitList")
    descriptor = None
    for klass in CasinoManager.__mro__:
        if "waitList" in klass.__dict__:
            descriptor = klass.__dict__["waitList"]
            break
    assert isinstance(descriptor, property)

def test_casinomanager_has_table():
    assert hasattr(CasinoManager, "table")
    descriptor = None
    for klass in CasinoManager.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)



def test_t2_is_not_abstract():
    assert not inspect.isabstract(T2)


def test_t2_constructor_exists():
    assert callable(T2.__init__)


def test_t2_constructor_args():
    sig = inspect.signature(T2.__init__)
    params = list(sig.parameters.keys())



def test_t1_is_not_abstract():
    assert not inspect.isabstract(T1)


def test_t1_constructor_exists():
    assert callable(T1.__init__)


def test_t1_constructor_args():
    sig = inspect.signature(T1.__init__)
    params = list(sig.parameters.keys())



def test_tuple_is_not_abstract():
    assert not inspect.isabstract(Tuple)


def test_tuple_constructor_exists():
    assert callable(Tuple.__init__)


def test_tuple_constructor_args():
    sig = inspect.signature(Tuple.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_stack_is_not_abstract():
    assert not inspect.isabstract(Stack)


def test_stack_constructor_exists():
    assert callable(Stack.__init__)


def test_stack_constructor_args():
    sig = inspect.signature(Stack.__init__)
    params = list(sig.parameters.keys())



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"

def test_deck_has_cards():
    assert hasattr(Deck, "cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "currPlayers" in params, "Missing parameter 'currPlayers'"
    assert "deck" in params, "Missing parameter 'deck'"

def test_table_has_currPlayers():
    assert hasattr(Table, "currPlayers")
    descriptor = None
    for klass in Table.__mro__:
        if "currPlayers" in klass.__dict__:
            descriptor = klass.__dict__["currPlayers"]
            break
    assert isinstance(descriptor, property)

def test_table_has_deck():
    assert hasattr(Table, "deck")
    descriptor = None
    for klass in Table.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)



def test_executive_is_not_abstract():
    assert not inspect.isabstract(Executive)


def test_executive_constructor_exists():
    assert callable(Executive.__init__)


def test_executive_constructor_args():
    sig = inspect.signature(Executive.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_value():
    assert hasattr(Card, "value")
    descriptor = None
    for klass in Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
T3_strategy = st.builds(
    T3,
)
Queue_strategy = st.builds(
    Queue,
)
CasinoManager_strategy = st.builds(
    CasinoManager,
    waitList=
        safe_text,
    table=
        st.none()
)
T2_strategy = st.builds(
    T2,
)
T1_strategy = st.builds(
    T1,
)
Tuple_strategy = st.builds(
    Tuple,
)
Player_strategy = st.builds(
    Player,
)
T_strategy = st.builds(
    T,
)
Stack_strategy = st.builds(
    Stack,
)
Deck_strategy = st.builds(
    Deck,
    cards=
        safe_text
)
Table_strategy = st.builds(
    Table,
    currPlayers=
        safe_text,
    deck=
        st.none()
)
Executive_strategy = st.builds(
    Executive,
)
Card_strategy = st.builds(
    Card,
    value=
        st.integers(),
    suit=
        safe_text
)

@given(instance=T3_strategy)
@settings(max_examples=50)
def test_t3_instantiation(instance):
    assert isinstance(instance, T3)

@given(instance=Queue_strategy)
@settings(max_examples=50)
def test_queue_instantiation(instance):
    assert isinstance(instance, Queue)

@given(instance=CasinoManager_strategy)
@settings(max_examples=50)
def test_casinomanager_instantiation(instance):
    assert isinstance(instance, CasinoManager)



@given(instance=CasinoManager_strategy)
def test_casinomanager_waitList_setter(instance):
    original = instance.waitList
    instance.waitList = original
    assert instance.waitList == original



@given(instance=CasinoManager_strategy)
def test_casinomanager_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original

@given(instance=T2_strategy)
@settings(max_examples=50)
def test_t2_instantiation(instance):
    assert isinstance(instance, T2)

@given(instance=T1_strategy)
@settings(max_examples=50)
def test_t1_instantiation(instance):
    assert isinstance(instance, T1)

@given(instance=Tuple_strategy)
@settings(max_examples=50)
def test_tuple_instantiation(instance):
    assert isinstance(instance, Tuple)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=Stack_strategy)
@settings(max_examples=50)
def test_stack_instantiation(instance):
    assert isinstance(instance, Stack)

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_currPlayers_setter(instance):
    original = instance.currPlayers
    instance.currPlayers = original
    assert instance.currPlayers == original



@given(instance=Table_strategy)
def test_table_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original

@given(instance=Executive_strategy)
@settings(max_examples=50)
def test_executive_instantiation(instance):
    assert isinstance(instance, Executive)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original
