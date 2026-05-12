import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FiniteStateMachines_Transition,
    FiniteStateMachines_State,
    FiniteStateMachines_FiniteStateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_finitestatemachines_transition_is_not_abstract():
    assert not inspect.isabstract(FiniteStateMachines_Transition)


def test_finitestatemachines_transition_constructor_exists():
    assert callable(FiniteStateMachines_Transition.__init__)


def test_finitestatemachines_transition_constructor_args():
    sig = inspect.signature(FiniteStateMachines_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_finitestatemachines_transition_has_input():
    assert hasattr(FiniteStateMachines_Transition, "input")
    descriptor = None
    for klass in FiniteStateMachines_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines_state_is_not_abstract():
    assert not inspect.isabstract(FiniteStateMachines_State)


def test_finitestatemachines_state_constructor_exists():
    assert callable(FiniteStateMachines_State.__init__)


def test_finitestatemachines_state_constructor_args():
    sig = inspect.signature(FiniteStateMachines_State.__init__)
    params = list(sig.parameters.keys())
    assert "isEndState" in params, "Missing parameter 'isEndState'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isStartState" in params, "Missing parameter 'isStartState'"

def test_finitestatemachines_state_has_isEndState():
    assert hasattr(FiniteStateMachines_State, "isEndState")
    descriptor = None
    for klass in FiniteStateMachines_State.__mro__:
        if "isEndState" in klass.__dict__:
            descriptor = klass.__dict__["isEndState"]
            break
    assert isinstance(descriptor, property)

def test_finitestatemachines_state_has_name():
    assert hasattr(FiniteStateMachines_State, "name")
    descriptor = None
    for klass in FiniteStateMachines_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_finitestatemachines_state_has_isStartState():
    assert hasattr(FiniteStateMachines_State, "isStartState")
    descriptor = None
    for klass in FiniteStateMachines_State.__mro__:
        if "isStartState" in klass.__dict__:
            descriptor = klass.__dict__["isStartState"]
            break
    assert isinstance(descriptor, property)



def test_finitestatemachines_finitestatemachine_is_not_abstract():
    assert not inspect.isabstract(FiniteStateMachines_FiniteStateMachine)


def test_finitestatemachines_finitestatemachine_constructor_exists():
    assert callable(FiniteStateMachines_FiniteStateMachine.__init__)


def test_finitestatemachines_finitestatemachine_constructor_args():
    sig = inspect.signature(FiniteStateMachines_FiniteStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_finitestatemachines_finitestatemachine_has_id():
    assert hasattr(FiniteStateMachines_FiniteStateMachine, "id")
    descriptor = None
    for klass in FiniteStateMachines_FiniteStateMachine.__mro__:
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
FiniteStateMachines_Transition_strategy = st.builds(
    FiniteStateMachines_Transition,
    input=
        safe_text
)
FiniteStateMachines_State_strategy = st.builds(
    FiniteStateMachines_State,
    isEndState=
        st.booleans(),
    name=
        safe_text,
    isStartState=
        st.booleans()
)
FiniteStateMachines_FiniteStateMachine_strategy = st.builds(
    FiniteStateMachines_FiniteStateMachine,
    id=
        safe_text
)

@given(instance=FiniteStateMachines_Transition_strategy)
@settings(max_examples=50)
def test_finitestatemachines_transition_instantiation(instance):
    assert isinstance(instance, FiniteStateMachines_Transition)



@given(instance=FiniteStateMachines_Transition_strategy)
def test_finitestatemachines_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=FiniteStateMachines_State_strategy)
@settings(max_examples=50)
def test_finitestatemachines_state_instantiation(instance):
    assert isinstance(instance, FiniteStateMachines_State)



@given(instance=FiniteStateMachines_State_strategy)
def test_finitestatemachines_state_isEndState_setter(instance):
    original = instance.isEndState
    instance.isEndState = original
    assert instance.isEndState == original



@given(instance=FiniteStateMachines_State_strategy)
def test_finitestatemachines_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=FiniteStateMachines_State_strategy)
def test_finitestatemachines_state_isStartState_setter(instance):
    original = instance.isStartState
    instance.isStartState = original
    assert instance.isStartState == original

@given(instance=FiniteStateMachines_FiniteStateMachine_strategy)
@settings(max_examples=50)
def test_finitestatemachines_finitestatemachine_instantiation(instance):
    assert isinstance(instance, FiniteStateMachines_FiniteStateMachine)



@given(instance=FiniteStateMachines_FiniteStateMachine_strategy)
def test_finitestatemachines_finitestatemachine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
