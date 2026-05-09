import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FiniteStateMachines::Transition,
    FiniteStateMachines::State,
    FiniteStateMachines::FiniteStateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_finitestatemachines::transition_is_not_abstract():
    assert not inspect.isabstract(FiniteStateMachines::Transition)


def test_finitestatemachines::transition_constructor_exists():
    assert callable(FiniteStateMachines::Transition.__init__)


def test_finitestatemachines::transition_constructor_args():
    sig = inspect.signature(FiniteStateMachines::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_finitestatemachines::transition_has_input():
    assert hasattr(FiniteStateMachines::Transition, "input")
    descriptor = None
    for klass in FiniteStateMachines::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines::state_is_not_abstract():
    assert not inspect.isabstract(FiniteStateMachines::State)


def test_finitestatemachines::state_constructor_exists():
    assert callable(FiniteStateMachines::State.__init__)


def test_finitestatemachines::state_constructor_args():
    sig = inspect.signature(FiniteStateMachines::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isEndState" in params, "Missing parameter 'isEndState'"
    assert "isStartState" in params, "Missing parameter 'isStartState'"

def test_finitestatemachines::state_has_name():
    assert hasattr(FiniteStateMachines::State, "name")
    descriptor = None
    for klass in FiniteStateMachines::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_finitestatemachines::state_has_isEndState():
    assert hasattr(FiniteStateMachines::State, "isEndState")
    descriptor = None
    for klass in FiniteStateMachines::State.__mro__:
        if "isEndState" in klass.__dict__:
            descriptor = klass.__dict__["isEndState"]
            break
    assert isinstance(descriptor, property)

def test_finitestatemachines::state_has_isStartState():
    assert hasattr(FiniteStateMachines::State, "isStartState")
    descriptor = None
    for klass in FiniteStateMachines::State.__mro__:
        if "isStartState" in klass.__dict__:
            descriptor = klass.__dict__["isStartState"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines::finitestatemachine_is_not_abstract():
    assert not inspect.isabstract(FiniteStateMachines::FiniteStateMachine)


def test_finitestatemachines::finitestatemachine_constructor_exists():
    assert callable(FiniteStateMachines::FiniteStateMachine.__init__)


def test_finitestatemachines::finitestatemachine_constructor_args():
    sig = inspect.signature(FiniteStateMachines::FiniteStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_finitestatemachines::finitestatemachine_has_id():
    assert hasattr(FiniteStateMachines::FiniteStateMachine, "id")
    descriptor = None
    for klass in FiniteStateMachines::FiniteStateMachine.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
FiniteStateMachines::Transition_strategy = st.builds(
    FiniteStateMachines::Transition,
    input=
        safe_text
)
FiniteStateMachines::State_strategy = st.builds(
    FiniteStateMachines::State,
    name=
        safe_text,
    isEndState=
        st.booleans(),
    isStartState=
        st.booleans()
)
FiniteStateMachines::FiniteStateMachine_strategy = st.builds(
    FiniteStateMachines::FiniteStateMachine,
    id=
        safe_text
)

@given(instance=FiniteStateMachines::Transition_strategy)
@settings(max_examples=50)
def test_finitestatemachines::transition_instantiation(instance):
    assert isinstance(instance, FiniteStateMachines::Transition)

@given(instance=FiniteStateMachines::Transition_strategy)
def test_finitestatemachines::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=FiniteStateMachines::Transition_strategy)
def test_finitestatemachines::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=FiniteStateMachines::State_strategy)
@settings(max_examples=50)
def test_finitestatemachines::state_instantiation(instance):
    assert isinstance(instance, FiniteStateMachines::State)

@given(instance=FiniteStateMachines::State_strategy)
def test_finitestatemachines::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FiniteStateMachines::State_strategy)
def test_finitestatemachines::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FiniteStateMachines::State_strategy)
def test_finitestatemachines::state_isEndState_type(instance):
    assert isinstance(instance.isEndState, bool)


@given(instance=FiniteStateMachines::State_strategy)
def test_finitestatemachines::state_isEndState_setter(instance):
    original = instance.isEndState
    instance.isEndState = original
    assert instance.isEndState == original

@given(instance=FiniteStateMachines::State_strategy)
def test_finitestatemachines::state_isStartState_type(instance):
    assert isinstance(instance.isStartState, bool)


@given(instance=FiniteStateMachines::State_strategy)
def test_finitestatemachines::state_isStartState_setter(instance):
    original = instance.isStartState
    instance.isStartState = original
    assert instance.isStartState == original

@given(instance=FiniteStateMachines::FiniteStateMachine_strategy)
@settings(max_examples=50)
def test_finitestatemachines::finitestatemachine_instantiation(instance):
    assert isinstance(instance, FiniteStateMachines::FiniteStateMachine)

@given(instance=FiniteStateMachines::FiniteStateMachine_strategy)
def test_finitestatemachines::finitestatemachine_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=FiniteStateMachines::FiniteStateMachine_strategy)
def test_finitestatemachines::finitestatemachine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
