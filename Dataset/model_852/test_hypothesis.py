import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FSM_StateMachine,
    FSM_Transition,
    FSM_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(FSM_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(FSM_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_statemachine_has_name():
    assert hasattr(FSM_StateMachine, "name")
    descriptor = None
    for klass in FSM_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(FSM_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(FSM_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(FSM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_fsm_transition_has_input():
    assert hasattr(FSM_Transition, "input")
    descriptor = None
    for klass in FSM_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(FSM_State)


def test_fsm_state_constructor_exists():
    assert callable(FSM_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(FSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isAccepting" in params, "Missing parameter 'isAccepting'"

def test_fsm_state_has_name():
    assert hasattr(FSM_State, "name")
    descriptor = None
    for klass in FSM_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm_state_has_isAccepting():
    assert hasattr(FSM_State, "isAccepting")
    descriptor = None
    for klass in FSM_State.__mro__:
        if "isAccepting" in klass.__dict__:
            descriptor = klass.__dict__["isAccepting"]
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
FSM_StateMachine_strategy = st.builds(
    FSM_StateMachine,
    name=
        safe_text
)
FSM_Transition_strategy = st.builds(
    FSM_Transition,
    input=
        safe_text
)
FSM_State_strategy = st.builds(
    FSM_State,
    name=
        safe_text,
    isAccepting=
        st.booleans()
)

@given(instance=FSM_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, FSM_StateMachine)



@given(instance=FSM_StateMachine_strategy)
def test_fsm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, FSM_Transition)



@given(instance=FSM_Transition_strategy)
def test_fsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=FSM_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, FSM_State)



@given(instance=FSM_State_strategy)
def test_fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=FSM_State_strategy)
def test_fsm_state_isAccepting_setter(instance):
    original = instance.isAccepting
    instance.isAccepting = original
    assert instance.isAccepting == original
