import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    StateMachine::UnNamedState,
    StateMachine::NamedState,
    StateMachine::Transition,
    StateMachine::State,
    StateMachine::WashingMachine,
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



def test_statemachine::unnamedstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine::UnNamedState)


def test_statemachine::unnamedstate_constructor_exists():
    assert callable(StateMachine::UnNamedState.__init__)


def test_statemachine::unnamedstate_constructor_args():
    sig = inspect.signature(StateMachine::UnNamedState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::unnamedstate_has_name():
    assert hasattr(StateMachine::UnNamedState, "name")
    descriptor = None
    for klass in StateMachine::UnNamedState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::namedstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine::NamedState)


def test_statemachine::namedstate_constructor_exists():
    assert callable(StateMachine::NamedState.__init__)


def test_statemachine::namedstate_constructor_args():
    sig = inspect.signature(StateMachine::NamedState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::namedstate_has_name():
    assert hasattr(StateMachine::NamedState, "name")
    descriptor = None
    for klass in StateMachine::NamedState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(StateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(StateMachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "action" in params, "Missing parameter 'action'"

def test_statemachine::transition_has_id():
    assert hasattr(StateMachine::Transition, "id")
    descriptor = None
    for klass in StateMachine::Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_name():
    assert hasattr(StateMachine::Transition, "name")
    descriptor = None
    for klass in StateMachine::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_trigger():
    assert hasattr(StateMachine::Transition, "trigger")
    descriptor = None
    for klass in StateMachine::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_action():
    assert hasattr(StateMachine::Transition, "action")
    descriptor = None
    for klass in StateMachine::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(StateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(StateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(StateMachine::State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::washingmachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine::WashingMachine)


def test_statemachine::washingmachine_constructor_exists():
    assert callable(StateMachine::WashingMachine.__init__)


def test_statemachine::washingmachine_constructor_args():
    sig = inspect.signature(StateMachine::WashingMachine.__init__)
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
StateMachine::UnNamedState_strategy = st.builds(
    StateMachine::UnNamedState,
    name=
        safe_text
)
StateMachine::NamedState_strategy = st.builds(
    StateMachine::NamedState,
    name=
        safe_text
)
StateMachine::Transition_strategy = st.builds(
    StateMachine::Transition,
    id=
        st.integers(),
    name=
        safe_text,
    trigger=
        safe_text,
    action=
        safe_text
)
StateMachine::State_strategy = st.builds(
    StateMachine::State,
)
StateMachine::WashingMachine_strategy = st.builds(
    StateMachine::WashingMachine,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachine::UnNamedState_strategy)
@settings(max_examples=50)
def test_statemachine::unnamedstate_instantiation(instance):
    assert isinstance(instance, StateMachine::UnNamedState)

@given(instance=StateMachine::UnNamedState_strategy)
def test_statemachine::unnamedstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::UnNamedState_strategy)
def test_statemachine::unnamedstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine::NamedState_strategy)
@settings(max_examples=50)
def test_statemachine::namedstate_instantiation(instance):
    assert isinstance(instance, StateMachine::NamedState)

@given(instance=StateMachine::NamedState_strategy)
def test_statemachine::namedstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::NamedState_strategy)
def test_statemachine::namedstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, StateMachine::Transition)

@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=StateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, StateMachine::State)

@given(instance=StateMachine::WashingMachine_strategy)
@settings(max_examples=50)
def test_statemachine::washingmachine_instantiation(instance):
    assert isinstance(instance, StateMachine::WashingMachine)
