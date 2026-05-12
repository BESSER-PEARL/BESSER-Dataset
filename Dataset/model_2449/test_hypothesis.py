import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    gfsm_Guard,
    gfsm_State,
    gfsm_Transition,
    gfsm_Machine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gfsm_guard_is_not_abstract():
    assert not inspect.isabstract(gfsm_Guard)


def test_gfsm_guard_constructor_exists():
    assert callable(gfsm_Guard.__init__)


def test_gfsm_guard_constructor_args():
    sig = inspect.signature(gfsm_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gfsm_guard_has_value():
    assert hasattr(gfsm_Guard, "value")
    descriptor = None
    for klass in gfsm_Guard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gfsm_state_is_not_abstract():
    assert not inspect.isabstract(gfsm_State)


def test_gfsm_state_constructor_exists():
    assert callable(gfsm_State.__init__)


def test_gfsm_state_constructor_args():
    sig = inspect.signature(gfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm_state_has_name():
    assert hasattr(gfsm_State, "name")
    descriptor = None
    for klass in gfsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gfsm_transition_is_not_abstract():
    assert not inspect.isabstract(gfsm_Transition)


def test_gfsm_transition_constructor_exists():
    assert callable(gfsm_Transition.__init__)


def test_gfsm_transition_constructor_args():
    sig = inspect.signature(gfsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_gfsm_transition_has_event():
    assert hasattr(gfsm_Transition, "event")
    descriptor = None
    for klass in gfsm_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_gfsm_machine_is_not_abstract():
    assert not inspect.isabstract(gfsm_Machine)


def test_gfsm_machine_constructor_exists():
    assert callable(gfsm_Machine.__init__)


def test_gfsm_machine_constructor_args():
    sig = inspect.signature(gfsm_Machine.__init__)
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
gfsm_Guard_strategy = st.builds(
    gfsm_Guard,
    value=
        safe_text
)
gfsm_State_strategy = st.builds(
    gfsm_State,
    name=
        safe_text
)
gfsm_Transition_strategy = st.builds(
    gfsm_Transition,
    event=
        safe_text
)
gfsm_Machine_strategy = st.builds(
    gfsm_Machine,
)

@given(instance=gfsm_Guard_strategy)
@settings(max_examples=50)
def test_gfsm_guard_instantiation(instance):
    assert isinstance(instance, gfsm_Guard)



@given(instance=gfsm_Guard_strategy)
def test_gfsm_guard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gfsm_State_strategy)
@settings(max_examples=50)
def test_gfsm_state_instantiation(instance):
    assert isinstance(instance, gfsm_State)



@given(instance=gfsm_State_strategy)
def test_gfsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gfsm_Transition_strategy)
@settings(max_examples=50)
def test_gfsm_transition_instantiation(instance):
    assert isinstance(instance, gfsm_Transition)



@given(instance=gfsm_Transition_strategy)
def test_gfsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=gfsm_Machine_strategy)
@settings(max_examples=50)
def test_gfsm_machine_instantiation(instance):
    assert isinstance(instance, gfsm_Machine)
