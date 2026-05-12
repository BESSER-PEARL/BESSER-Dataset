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
    Account,
    InputValidation,
    Blackjack,
    Main,
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
    assert "int" in params, "Missing parameter 'int'"
    assert "int1" in params, "Missing parameter 'int1'"
    assert "string" in params, "Missing parameter 'string'"
    assert "bool" in params, "Missing parameter 'bool'"

def test_cards_has_int():
    assert hasattr(Cards, "int")
    descriptor = None
    for klass in Cards.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_cards_has_int1():
    assert hasattr(Cards, "int1")
    descriptor = None
    for klass in Cards.__mro__:
        if "int1" in klass.__dict__:
            descriptor = klass.__dict__["int1"]
            break
    assert isinstance(descriptor, property)

def test_cards_has_string():
    assert hasattr(Cards, "string")
    descriptor = None
    for klass in Cards.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_cards_has_bool():
    assert hasattr(Cards, "bool")
    descriptor = None
    for klass in Cards.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"

def test_deck_has_int():
    assert hasattr(Deck, "int")
    descriptor = None
    for klass in Deck.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "Deck" in params, "Missing parameter 'Deck'"
    assert "int" in params, "Missing parameter 'int'"
    assert "Card" in params, "Missing parameter 'Card'"
    assert "int1" in params, "Missing parameter 'int1'"

def test_player_has_Deck():
    assert hasattr(Player, "Deck")
    descriptor = None
    for klass in Player.__mro__:
        if "Deck" in klass.__dict__:
            descriptor = klass.__dict__["Deck"]
            break
    assert isinstance(descriptor, property)

def test_player_has_int():
    assert hasattr(Player, "int")
    descriptor = None
    for klass in Player.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_player_has_Card():
    assert hasattr(Player, "Card")
    descriptor = None
    for klass in Player.__mro__:
        if "Card" in klass.__dict__:
            descriptor = klass.__dict__["Card"]
            break
    assert isinstance(descriptor, property)

def test_player_has_int1():
    assert hasattr(Player, "int1")
    descriptor = None
    for klass in Player.__mro__:
        if "int1" in klass.__dict__:
            descriptor = klass.__dict__["int1"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"
    assert "string" in params, "Missing parameter 'string'"
    assert "int1" in params, "Missing parameter 'int1'"

def test_account_has_int():
    assert hasattr(Account, "int")
    descriptor = None
    for klass in Account.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_account_has_string():
    assert hasattr(Account, "string")
    descriptor = None
    for klass in Account.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_account_has_int1():
    assert hasattr(Account, "int1")
    descriptor = None
    for klass in Account.__mro__:
        if "int1" in klass.__dict__:
            descriptor = klass.__dict__["int1"]
            break
    assert isinstance(descriptor, property)



def test_inputvalidation_is_not_abstract():
    assert not inspect.isabstract(InputValidation)


def test_inputvalidation_constructor_exists():
    assert callable(InputValidation.__init__)


def test_inputvalidation_constructor_args():
    sig = inspect.signature(InputValidation.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_is_not_abstract():
    assert not inspect.isabstract(Blackjack)


def test_blackjack_constructor_exists():
    assert callable(Blackjack.__init__)


def test_blackjack_constructor_args():
    sig = inspect.signature(Blackjack.__init__)
    params = list(sig.parameters.keys())



def test_main_is_not_abstract():
    assert not inspect.isabstract(Main)


def test_main_constructor_exists():
    assert callable(Main.__init__)


def test_main_constructor_args():
    sig = inspect.signature(Main.__init__)
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
Cards_strategy = st.builds(
    Cards,
    int=
        safe_text,
    int1=
        safe_text,
    string=
        safe_text,
    bool=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    int=
        safe_text
)
Player_strategy = st.builds(
    Player,
    Deck=
        safe_text,
    int=
        safe_text,
    Card=
        safe_text,
    int1=
        safe_text
)
Account_strategy = st.builds(
    Account,
    int=
        safe_text,
    string=
        safe_text,
    int1=
        safe_text
)
InputValidation_strategy = st.builds(
    InputValidation,
)
Blackjack_strategy = st.builds(
    Blackjack,
)
Main_strategy = st.builds(
    Main,
)

@given(instance=Cards_strategy)
@settings(max_examples=50)
def test_cards_instantiation(instance):
    assert isinstance(instance, Cards)



@given(instance=Cards_strategy)
def test_cards_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=Cards_strategy)
def test_cards_int1_setter(instance):
    original = instance.int1
    instance.int1 = original
    assert instance.int1 == original



@given(instance=Cards_strategy)
def test_cards_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=Cards_strategy)
def test_cards_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_Deck_setter(instance):
    original = instance.Deck
    instance.Deck = original
    assert instance.Deck == original



@given(instance=Player_strategy)
def test_player_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=Player_strategy)
def test_player_Card_setter(instance):
    original = instance.Card
    instance.Card = original
    assert instance.Card == original



@given(instance=Player_strategy)
def test_player_int1_setter(instance):
    original = instance.int1
    instance.int1 = original
    assert instance.int1 == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=Account_strategy)
def test_account_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=Account_strategy)
def test_account_int1_setter(instance):
    original = instance.int1
    instance.int1 = original
    assert instance.int1 == original

@given(instance=InputValidation_strategy)
@settings(max_examples=50)
def test_inputvalidation_instantiation(instance):
    assert isinstance(instance, InputValidation)

@given(instance=Blackjack_strategy)
@settings(max_examples=50)
def test_blackjack_instantiation(instance):
    assert isinstance(instance, Blackjack)

@given(instance=Main_strategy)
@settings(max_examples=50)
def test_main_instantiation(instance):
    assert isinstance(instance, Main)
