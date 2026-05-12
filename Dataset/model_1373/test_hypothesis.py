import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_StateMachine,
    statemachine_Transition,
    statemachine_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "action" in params, "Missing parameter 'action'"

def test_statemachine_transition_has_trigger():
    assert hasattr(statemachine_Transition, "trigger")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_action():
    assert hasattr(statemachine_Transition, "action")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_state_has_name():
    assert hasattr(statemachine_State, "name")
    descriptor = None
    for klass in statemachine_State.__mro__:
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
statemachine_StateMachine_strategy = st.builds(
    statemachine_StateMachine,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    trigger=
        safe_text,
    action=
        safe_text
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    name=
        safe_text
)

@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachine)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
