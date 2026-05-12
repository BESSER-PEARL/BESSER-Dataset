import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stateMachine_Transition,
    stateMachine_State,
    stateMachine_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(stateMachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(stateMachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_transition_has_action():
    assert hasattr(stateMachine_Transition, "action")
    descriptor = None
    for klass in stateMachine_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_trigger():
    assert hasattr(stateMachine_Transition, "trigger")
    descriptor = None
    for klass in stateMachine_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_name():
    assert hasattr(stateMachine_Transition, "name")
    descriptor = None
    for klass in stateMachine_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(stateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(stateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(stateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "status" in params, "Missing parameter 'status'"

def test_statemachine_state_has_name():
    assert hasattr(stateMachine_State, "name")
    descriptor = None
    for klass in stateMachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_status():
    assert hasattr(stateMachine_State, "status")
    descriptor = None
    for klass in stateMachine_State.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(stateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(stateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statemachine_has_name():
    assert hasattr(stateMachine_StateMachine, "name")
    descriptor = None
    for klass in stateMachine_StateMachine.__mro__:
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
stateMachine_Transition_strategy = st.builds(
    stateMachine_Transition,
    action=
        safe_text,
    trigger=
        safe_text,
    name=
        safe_text
)
stateMachine_State_strategy = st.builds(
    stateMachine_State,
    name=
        safe_text,
    status=
        st.booleans()
)
stateMachine_StateMachine_strategy = st.builds(
    stateMachine_StateMachine,
    name=
        safe_text
)

@given(instance=stateMachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, stateMachine_Transition)



@given(instance=stateMachine_Transition_strategy)
def test_statemachine_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=stateMachine_Transition_strategy)
def test_statemachine_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=stateMachine_Transition_strategy)
def test_statemachine_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, stateMachine_State)



@given(instance=stateMachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=stateMachine_State_strategy)
def test_statemachine_state_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=stateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine_StateMachine)



@given(instance=stateMachine_StateMachine_strategy)
def test_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
