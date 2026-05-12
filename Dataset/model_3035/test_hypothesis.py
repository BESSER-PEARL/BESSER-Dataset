import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myfsm_State,
    myfsm_Trans,
    myfsm_Machine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myfsm_state_is_not_abstract():
    assert not inspect.isabstract(myfsm_State)


def test_myfsm_state_constructor_exists():
    assert callable(myfsm_State.__init__)


def test_myfsm_state_constructor_args():
    sig = inspect.signature(myfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myfsm_state_has_name():
    assert hasattr(myfsm_State, "name")
    descriptor = None
    for klass in myfsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myfsm_trans_is_not_abstract():
    assert not inspect.isabstract(myfsm_Trans)


def test_myfsm_trans_constructor_exists():
    assert callable(myfsm_Trans.__init__)


def test_myfsm_trans_constructor_args():
    sig = inspect.signature(myfsm_Trans.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_myfsm_trans_has_event():
    assert hasattr(myfsm_Trans, "event")
    descriptor = None
    for klass in myfsm_Trans.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_myfsm_machine_is_not_abstract():
    assert not inspect.isabstract(myfsm_Machine)


def test_myfsm_machine_constructor_exists():
    assert callable(myfsm_Machine.__init__)


def test_myfsm_machine_constructor_args():
    sig = inspect.signature(myfsm_Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myfsm_machine_has_name():
    assert hasattr(myfsm_Machine, "name")
    descriptor = None
    for klass in myfsm_Machine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
myfsm_State_strategy = st.builds(
    myfsm_State,
    name=
        safe_text
)
myfsm_Trans_strategy = st.builds(
    myfsm_Trans,
    event=
        safe_text
)
myfsm_Machine_strategy = st.builds(
    myfsm_Machine,
    name=
        safe_text
)

@given(instance=myfsm_State_strategy)
@settings(max_examples=50)
def test_myfsm_state_instantiation(instance):
    assert isinstance(instance, myfsm_State)



@given(instance=myfsm_State_strategy)
def test_myfsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myfsm_Trans_strategy)
@settings(max_examples=50)
def test_myfsm_trans_instantiation(instance):
    assert isinstance(instance, myfsm_Trans)



@given(instance=myfsm_Trans_strategy)
def test_myfsm_trans_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=myfsm_Machine_strategy)
@settings(max_examples=50)
def test_myfsm_machine_instantiation(instance):
    assert isinstance(instance, myfsm_Machine)



@given(instance=myfsm_Machine_strategy)
def test_myfsm_machine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
