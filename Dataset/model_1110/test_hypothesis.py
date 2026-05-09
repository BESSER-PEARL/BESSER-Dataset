import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateMachine::Transition,
    stateMachine::State,
    stateMachine::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(stateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(stateMachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::transition_has_action():
    assert hasattr(stateMachine::Transition, "action")
    descriptor = None
    for klass in stateMachine::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_trigger():
    assert hasattr(stateMachine::Transition, "trigger")
    descriptor = None
    for klass in stateMachine::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_name():
    assert hasattr(stateMachine::Transition, "name")
    descriptor = None
    for klass in stateMachine::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(stateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(stateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(stateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::state_has_status():
    assert hasattr(stateMachine::State, "status")
    descriptor = None
    for klass in stateMachine::State.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_name():
    assert hasattr(stateMachine::State, "name")
    descriptor = None
    for klass in stateMachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(stateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(stateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_name():
    assert hasattr(stateMachine::StateMachine, "name")
    descriptor = None
    for klass in stateMachine::StateMachine.__mro__:
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
stateMachine::Transition_strategy = st.builds(
    stateMachine::Transition,
    action=
        safe_text,
    trigger=
        safe_text,
    name=
        safe_text
)
stateMachine::State_strategy = st.builds(
    stateMachine::State,
    status=
        st.booleans(),
    name=
        safe_text
)
stateMachine::StateMachine_strategy = st.builds(
    stateMachine::StateMachine,
    name=
        safe_text
)

@given(instance=stateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, stateMachine::Transition)

@given(instance=stateMachine::Transition_strategy)
def test_statemachine::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=stateMachine::Transition_strategy)
def test_statemachine::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=stateMachine::Transition_strategy)
def test_statemachine::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=stateMachine::Transition_strategy)
def test_statemachine::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=stateMachine::Transition_strategy)
def test_statemachine::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::Transition_strategy)
def test_statemachine::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, stateMachine::State)

@given(instance=stateMachine::State_strategy)
def test_statemachine::state_status_type(instance):
    assert isinstance(instance.status, bool)


@given(instance=stateMachine::State_strategy)
def test_statemachine::state_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine::StateMachine)

@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
