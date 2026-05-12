import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplefsm_State,
    simplefsm_SimpleFiniteStateMachine,
    simplefsm_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplefsm_state_is_not_abstract():
    assert not inspect.isabstract(simplefsm_State)


def test_simplefsm_state_constructor_exists():
    assert callable(simplefsm_State.__init__)


def test_simplefsm_state_constructor_args():
    sig = inspect.signature(simplefsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplefsm_state_has_action():
    assert hasattr(simplefsm_State, "action")
    descriptor = None
    for klass in simplefsm_State.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_simplefsm_state_has_name():
    assert hasattr(simplefsm_State, "name")
    descriptor = None
    for klass in simplefsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplefsm_simplefinitestatemachine_is_not_abstract():
    assert not inspect.isabstract(simplefsm_SimpleFiniteStateMachine)


def test_simplefsm_simplefinitestatemachine_constructor_exists():
    assert callable(simplefsm_SimpleFiniteStateMachine.__init__)


def test_simplefsm_simplefinitestatemachine_constructor_args():
    sig = inspect.signature(simplefsm_SimpleFiniteStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplefsm_simplefinitestatemachine_has_name():
    assert hasattr(simplefsm_SimpleFiniteStateMachine, "name")
    descriptor = None
    for klass in simplefsm_SimpleFiniteStateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplefsm_transition_is_not_abstract():
    assert not inspect.isabstract(simplefsm_Transition)


def test_simplefsm_transition_constructor_exists():
    assert callable(simplefsm_Transition.__init__)


def test_simplefsm_transition_constructor_args():
    sig = inspect.signature(simplefsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplefsm_transition_has_event():
    assert hasattr(simplefsm_Transition, "event")
    descriptor = None
    for klass in simplefsm_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_simplefsm_transition_has_name():
    assert hasattr(simplefsm_Transition, "name")
    descriptor = None
    for klass in simplefsm_Transition.__mro__:
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
simplefsm_State_strategy = st.builds(
    simplefsm_State,
    action=
        safe_text,
    name=
        safe_text
)
simplefsm_SimpleFiniteStateMachine_strategy = st.builds(
    simplefsm_SimpleFiniteStateMachine,
    name=
        safe_text
)
simplefsm_Transition_strategy = st.builds(
    simplefsm_Transition,
    event=
        safe_text,
    name=
        safe_text
)

@given(instance=simplefsm_State_strategy)
@settings(max_examples=50)
def test_simplefsm_state_instantiation(instance):
    assert isinstance(instance, simplefsm_State)



@given(instance=simplefsm_State_strategy)
def test_simplefsm_state_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=simplefsm_State_strategy)
def test_simplefsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplefsm_SimpleFiniteStateMachine_strategy)
@settings(max_examples=50)
def test_simplefsm_simplefinitestatemachine_instantiation(instance):
    assert isinstance(instance, simplefsm_SimpleFiniteStateMachine)



@given(instance=simplefsm_SimpleFiniteStateMachine_strategy)
def test_simplefsm_simplefinitestatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplefsm_Transition_strategy)
@settings(max_examples=50)
def test_simplefsm_transition_instantiation(instance):
    assert isinstance(instance, simplefsm_Transition)



@given(instance=simplefsm_Transition_strategy)
def test_simplefsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=simplefsm_Transition_strategy)
def test_simplefsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
