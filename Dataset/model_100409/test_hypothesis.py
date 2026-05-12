import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simplefsm::State,
    simplefsm::SimpleFiniteStateMachine,
    simplefsm::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplefsm::state_is_not_abstract():
    assert not inspect.isabstract(simplefsm::State)


def test_simplefsm::state_constructor_exists():
    assert callable(simplefsm::State.__init__)


def test_simplefsm::state_constructor_args():
    sig = inspect.signature(simplefsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "action" in params, "Missing parameter 'action'"

def test_simplefsm::state_has_name():
    assert hasattr(simplefsm::State, "name")
    descriptor = None
    for klass in simplefsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplefsm::state_has_action():
    assert hasattr(simplefsm::State, "action")
    descriptor = None
    for klass in simplefsm::State.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_simplefsm::simplefinitestatemachine_is_not_abstract():
    assert not inspect.isabstract(simplefsm::SimpleFiniteStateMachine)


def test_simplefsm::simplefinitestatemachine_constructor_exists():
    assert callable(simplefsm::SimpleFiniteStateMachine.__init__)


def test_simplefsm::simplefinitestatemachine_constructor_args():
    sig = inspect.signature(simplefsm::SimpleFiniteStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplefsm::simplefinitestatemachine_has_name():
    assert hasattr(simplefsm::SimpleFiniteStateMachine, "name")
    descriptor = None
    for klass in simplefsm::SimpleFiniteStateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplefsm::transition_is_not_abstract():
    assert not inspect.isabstract(simplefsm::Transition)


def test_simplefsm::transition_constructor_exists():
    assert callable(simplefsm::Transition.__init__)


def test_simplefsm::transition_constructor_args():
    sig = inspect.signature(simplefsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "event" in params, "Missing parameter 'event'"

def test_simplefsm::transition_has_name():
    assert hasattr(simplefsm::Transition, "name")
    descriptor = None
    for klass in simplefsm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplefsm::transition_has_event():
    assert hasattr(simplefsm::Transition, "event")
    descriptor = None
    for klass in simplefsm::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
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
simplefsm::State_strategy = st.builds(
    simplefsm::State,
    name=
        safe_text,
    action=
        safe_text
)
simplefsm::SimpleFiniteStateMachine_strategy = st.builds(
    simplefsm::SimpleFiniteStateMachine,
    name=
        safe_text
)
simplefsm::Transition_strategy = st.builds(
    simplefsm::Transition,
    name=
        safe_text,
    event=
        safe_text
)

@given(instance=simplefsm::State_strategy)
@settings(max_examples=50)
def test_simplefsm::state_instantiation(instance):
    assert isinstance(instance, simplefsm::State)

@given(instance=simplefsm::State_strategy)
def test_simplefsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplefsm::State_strategy)
def test_simplefsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplefsm::State_strategy)
def test_simplefsm::state_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=simplefsm::State_strategy)
def test_simplefsm::state_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=simplefsm::SimpleFiniteStateMachine_strategy)
@settings(max_examples=50)
def test_simplefsm::simplefinitestatemachine_instantiation(instance):
    assert isinstance(instance, simplefsm::SimpleFiniteStateMachine)

@given(instance=simplefsm::SimpleFiniteStateMachine_strategy)
def test_simplefsm::simplefinitestatemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplefsm::SimpleFiniteStateMachine_strategy)
def test_simplefsm::simplefinitestatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplefsm::Transition_strategy)
@settings(max_examples=50)
def test_simplefsm::transition_instantiation(instance):
    assert isinstance(instance, simplefsm::Transition)

@given(instance=simplefsm::Transition_strategy)
def test_simplefsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplefsm::Transition_strategy)
def test_simplefsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplefsm::Transition_strategy)
def test_simplefsm::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=simplefsm::Transition_strategy)
def test_simplefsm::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original
