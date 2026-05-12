import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    StateMachine_UnNamedState,
    StateMachine_NamedState,
    StateMachine_Transition,
    StateMachine_State,
    StateMachine_WashingMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_unnamedstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine_UnNamedState)


def test_statemachine_unnamedstate_constructor_exists():
    assert callable(StateMachine_UnNamedState.__init__)


def test_statemachine_unnamedstate_constructor_args():
    sig = inspect.signature(StateMachine_UnNamedState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_unnamedstate_has_name():
    assert hasattr(StateMachine_UnNamedState, "name")
    descriptor = None
    for klass in StateMachine_UnNamedState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_namedstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine_NamedState)


def test_statemachine_namedstate_constructor_exists():
    assert callable(StateMachine_NamedState.__init__)


def test_statemachine_namedstate_constructor_args():
    sig = inspect.signature(StateMachine_NamedState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_namedstate_has_name():
    assert hasattr(StateMachine_NamedState, "name")
    descriptor = None
    for klass in StateMachine_NamedState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(StateMachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(StateMachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_transition_has_id():
    assert hasattr(StateMachine_Transition, "id")
    descriptor = None
    for klass in StateMachine_Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_trigger():
    assert hasattr(StateMachine_Transition, "trigger")
    descriptor = None
    for klass in StateMachine_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_action():
    assert hasattr(StateMachine_Transition, "action")
    descriptor = None
    for klass in StateMachine_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_name():
    assert hasattr(StateMachine_Transition, "name")
    descriptor = None
    for klass in StateMachine_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(StateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(StateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(StateMachine_State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_washingmachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine_WashingMachine)


def test_statemachine_washingmachine_constructor_exists():
    assert callable(StateMachine_WashingMachine.__init__)


def test_statemachine_washingmachine_constructor_args():
    sig = inspect.signature(StateMachine_WashingMachine.__init__)
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
State_strategy = st.builds(
    State,
)
StateMachine_UnNamedState_strategy = st.builds(
    StateMachine_UnNamedState,
    name=
        safe_text
)
StateMachine_NamedState_strategy = st.builds(
    StateMachine_NamedState,
    name=
        safe_text
)
StateMachine_Transition_strategy = st.builds(
    StateMachine_Transition,
    id=
        st.integers(),
    trigger=
        safe_text,
    action=
        safe_text,
    name=
        safe_text
)
StateMachine_State_strategy = st.builds(
    StateMachine_State,
)
StateMachine_WashingMachine_strategy = st.builds(
    StateMachine_WashingMachine,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachine_UnNamedState_strategy)
@settings(max_examples=50)
def test_statemachine_unnamedstate_instantiation(instance):
    assert isinstance(instance, StateMachine_UnNamedState)



@given(instance=StateMachine_UnNamedState_strategy)
def test_statemachine_unnamedstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine_NamedState_strategy)
@settings(max_examples=50)
def test_statemachine_namedstate_instantiation(instance):
    assert isinstance(instance, StateMachine_NamedState)



@given(instance=StateMachine_NamedState_strategy)
def test_statemachine_namedstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, StateMachine_Transition)



@given(instance=StateMachine_Transition_strategy)
def test_statemachine_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=StateMachine_Transition_strategy)
def test_statemachine_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=StateMachine_Transition_strategy)
def test_statemachine_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=StateMachine_Transition_strategy)
def test_statemachine_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, StateMachine_State)

@given(instance=StateMachine_WashingMachine_strategy)
@settings(max_examples=50)
def test_statemachine_washingmachine_instantiation(instance):
    assert isinstance(instance, StateMachine_WashingMachine)
