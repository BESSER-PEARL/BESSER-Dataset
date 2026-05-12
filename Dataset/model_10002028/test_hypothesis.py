import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cards_external,
    Human_Player_external,
    Interface_Interface,
    Business_Owner,
    Banker,
    ComputerPlayer,
    Creator,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cards_external_is_not_abstract():
    assert not inspect.isabstract(Cards_external)


def test_cards_external_constructor_exists():
    assert callable(Cards_external.__init__)


def test_cards_external_constructor_args():
    sig = inspect.signature(Cards_external.__init__)
    params = list(sig.parameters.keys())



def test_human_player_external_is_not_abstract():
    assert not inspect.isabstract(Human_Player_external)


def test_human_player_external_constructor_exists():
    assert callable(Human_Player_external.__init__)


def test_human_player_external_constructor_args():
    sig = inspect.signature(Human_Player_external.__init__)
    params = list(sig.parameters.keys())



def test_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_business_owner_is_not_abstract():
    assert not inspect.isabstract(Business_Owner)


def test_business_owner_constructor_exists():
    assert callable(Business_Owner.__init__)


def test_business_owner_constructor_args():
    sig = inspect.signature(Business_Owner.__init__)
    params = list(sig.parameters.keys())
    assert "_Card_cards_5_" in params, "Missing parameter '_Card_cards_5_'"

def test_business_owner_has__Card_cards_5_():
    assert hasattr(Business_Owner, "_Card_cards_5_")
    descriptor = None
    for klass in Business_Owner.__mro__:
        if "_Card_cards_5_" in klass.__dict__:
            descriptor = klass.__dict__["_Card_cards_5_"]
            break
    assert isinstance(descriptor, property)



def test_banker_is_not_abstract():
    assert not inspect.isabstract(Banker)


def test_banker_constructor_exists():
    assert callable(Banker.__init__)


def test_banker_constructor_args():
    sig = inspect.signature(Banker.__init__)
    params = list(sig.parameters.keys())
    assert "_Card_cards_52_" in params, "Missing parameter '_Card_cards_52_'"

def test_banker_has__Card_cards_52_():
    assert hasattr(Banker, "_Card_cards_52_")
    descriptor = None
    for klass in Banker.__mro__:
        if "_Card_cards_52_" in klass.__dict__:
            descriptor = klass.__dict__["_Card_cards_52_"]
            break
    assert isinstance(descriptor, property)



def test_computerplayer_is_not_abstract():
    assert not inspect.isabstract(ComputerPlayer)


def test_computerplayer_constructor_exists():
    assert callable(ComputerPlayer.__init__)


def test_computerplayer_constructor_args():
    sig = inspect.signature(ComputerPlayer.__init__)
    params = list(sig.parameters.keys())
    assert "difficulty" in params, "Missing parameter 'difficulty'"

def test_computerplayer_has_difficulty():
    assert hasattr(ComputerPlayer, "difficulty")
    descriptor = None
    for klass in ComputerPlayer.__mro__:
        if "difficulty" in klass.__dict__:
            descriptor = klass.__dict__["difficulty"]
            break
    assert isinstance(descriptor, property)



def test_creator_is_not_abstract():
    assert not inspect.isabstract(Creator)


def test_creator_constructor_exists():
    assert callable(Creator.__init__)


def test_creator_constructor_args():
    sig = inspect.signature(Creator.__init__)
    params = list(sig.parameters.keys())
    assert "money" in params, "Missing parameter 'money'"
    assert "currentBet" in params, "Missing parameter 'currentBet'"
    assert "folded" in params, "Missing parameter 'folded'"
    assert "name" in params, "Missing parameter 'name'"

def test_creator_has_money():
    assert hasattr(Creator, "money")
    descriptor = None
    for klass in Creator.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)

def test_creator_has_currentBet():
    assert hasattr(Creator, "currentBet")
    descriptor = None
    for klass in Creator.__mro__:
        if "currentBet" in klass.__dict__:
            descriptor = klass.__dict__["currentBet"]
            break
    assert isinstance(descriptor, property)

def test_creator_has_folded():
    assert hasattr(Creator, "folded")
    descriptor = None
    for klass in Creator.__mro__:
        if "folded" in klass.__dict__:
            descriptor = klass.__dict__["folded"]
            break
    assert isinstance(descriptor, property)

def test_creator_has_name():
    assert hasattr(Creator, "name")
    descriptor = None
    for klass in Creator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Cards_external_strategy = st.builds(
    Cards_external,
)
Human_Player_external_strategy = st.builds(
    Human_Player_external,
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
Business_Owner_strategy = st.builds(
    Business_Owner,
    _Card_cards_5_=
        st.integers()
)
Banker_strategy = st.builds(
    Banker,
    _Card_cards_52_=
        st.integers()
)
ComputerPlayer_strategy = st.builds(
    ComputerPlayer,
    difficulty=
        st.integers()
)
Creator_strategy = st.builds(
    Creator,
    money=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    currentBet=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    folded=
        st.booleans(),
    name=
        safe_text
)

@given(instance=Cards_external_strategy)
@settings(max_examples=50)
def test_cards_external_instantiation(instance):
    assert isinstance(instance, Cards_external)

@given(instance=Human_Player_external_strategy)
@settings(max_examples=50)
def test_human_player_external_instantiation(instance):
    assert isinstance(instance, Human_Player_external)

@given(instance=Interface_Interface_strategy)
@settings(max_examples=50)
def test_interface_interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)

@given(instance=Business_Owner_strategy)
@settings(max_examples=50)
def test_business_owner_instantiation(instance):
    assert isinstance(instance, Business_Owner)



@given(instance=Business_Owner_strategy)
def test_business_owner__Card_cards_5__setter(instance):
    original = instance._Card_cards_5_
    instance._Card_cards_5_ = original
    assert instance._Card_cards_5_ == original

@given(instance=Banker_strategy)
@settings(max_examples=50)
def test_banker_instantiation(instance):
    assert isinstance(instance, Banker)



@given(instance=Banker_strategy)
def test_banker__Card_cards_52__setter(instance):
    original = instance._Card_cards_52_
    instance._Card_cards_52_ = original
    assert instance._Card_cards_52_ == original

@given(instance=ComputerPlayer_strategy)
@settings(max_examples=50)
def test_computerplayer_instantiation(instance):
    assert isinstance(instance, ComputerPlayer)



@given(instance=ComputerPlayer_strategy)
def test_computerplayer_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original

@given(instance=Creator_strategy)
@settings(max_examples=50)
def test_creator_instantiation(instance):
    assert isinstance(instance, Creator)



@given(instance=Creator_strategy)
def test_creator_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=Creator_strategy)
def test_creator_currentBet_setter(instance):
    original = instance.currentBet
    instance.currentBet = original
    assert instance.currentBet == original



@given(instance=Creator_strategy)
def test_creator_folded_setter(instance):
    original = instance.folded
    instance.folded = original
    assert instance.folded == original



@given(instance=Creator_strategy)
def test_creator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
