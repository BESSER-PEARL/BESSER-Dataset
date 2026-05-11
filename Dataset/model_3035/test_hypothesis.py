import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myfsm::State,
    myfsm::Trans,
    myfsm::Machine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myfsm::state_is_not_abstract():
    assert not inspect.isabstract(myfsm::State)


def test_myfsm::state_constructor_exists():
    assert callable(myfsm::State.__init__)


def test_myfsm::state_constructor_args():
    sig = inspect.signature(myfsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myfsm::state_has_name():
    assert hasattr(myfsm::State, "name")
    descriptor = None
    for klass in myfsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myfsm::trans_is_not_abstract():
    assert not inspect.isabstract(myfsm::Trans)


def test_myfsm::trans_constructor_exists():
    assert callable(myfsm::Trans.__init__)


def test_myfsm::trans_constructor_args():
    sig = inspect.signature(myfsm::Trans.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_myfsm::trans_has_event():
    assert hasattr(myfsm::Trans, "event")
    descriptor = None
    for klass in myfsm::Trans.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_myfsm::machine_is_not_abstract():
    assert not inspect.isabstract(myfsm::Machine)


def test_myfsm::machine_constructor_exists():
    assert callable(myfsm::Machine.__init__)


def test_myfsm::machine_constructor_args():
    sig = inspect.signature(myfsm::Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myfsm::machine_has_name():
    assert hasattr(myfsm::Machine, "name")
    descriptor = None
    for klass in myfsm::Machine.__mro__:
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
myfsm::State_strategy = st.builds(
    myfsm::State,
    name=
        safe_text
)
myfsm::Trans_strategy = st.builds(
    myfsm::Trans,
    event=
        safe_text
)
myfsm::Machine_strategy = st.builds(
    myfsm::Machine,
    name=
        safe_text
)

@given(instance=myfsm::State_strategy)
@settings(max_examples=50)
def test_myfsm::state_instantiation(instance):
    assert isinstance(instance, myfsm::State)

@given(instance=myfsm::State_strategy)
def test_myfsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myfsm::State_strategy)
def test_myfsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myfsm::Trans_strategy)
@settings(max_examples=50)
def test_myfsm::trans_instantiation(instance):
    assert isinstance(instance, myfsm::Trans)

@given(instance=myfsm::Trans_strategy)
def test_myfsm::trans_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=myfsm::Trans_strategy)
def test_myfsm::trans_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=myfsm::Machine_strategy)
@settings(max_examples=50)
def test_myfsm::machine_instantiation(instance):
    assert isinstance(instance, myfsm::Machine)

@given(instance=myfsm::Machine_strategy)
def test_myfsm::machine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myfsm::Machine_strategy)
def test_myfsm::machine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
