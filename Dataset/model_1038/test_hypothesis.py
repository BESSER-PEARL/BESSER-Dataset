import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    finalStateMachine_State,
    finalStateMachine_Transition,
    finalStateMachine_FSM,
    State,
    finalStateMachine_InitialState,
    finalStateMachine_FinalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_finalstatemachine_state_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine_State)


def test_finalstatemachine_state_constructor_exists():
    assert callable(finalStateMachine_State.__init__)


def test_finalstatemachine_state_constructor_args():
    sig = inspect.signature(finalStateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_finalstatemachine_state_has_name():
    assert hasattr(finalStateMachine_State, "name")
    descriptor = None
    for klass in finalStateMachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_finalstatemachine_transition_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine_Transition)


def test_finalstatemachine_transition_constructor_exists():
    assert callable(finalStateMachine_Transition.__init__)


def test_finalstatemachine_transition_constructor_args():
    sig = inspect.signature(finalStateMachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_finalstatemachine_transition_has_name():
    assert hasattr(finalStateMachine_Transition, "name")
    descriptor = None
    for klass in finalStateMachine_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_finalstatemachine_fsm_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine_FSM)


def test_finalstatemachine_fsm_constructor_exists():
    assert callable(finalStateMachine_FSM.__init__)


def test_finalstatemachine_fsm_constructor_args():
    sig = inspect.signature(finalStateMachine_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_finalstatemachine_fsm_has_name():
    assert hasattr(finalStateMachine_FSM, "name")
    descriptor = None
    for klass in finalStateMachine_FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_finalstatemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine_InitialState)


def test_finalstatemachine_initialstate_constructor_exists():
    assert callable(finalStateMachine_InitialState.__init__)


def test_finalstatemachine_initialstate_constructor_args():
    sig = inspect.signature(finalStateMachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_finalstatemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine_FinalState)


def test_finalstatemachine_finalstate_constructor_exists():
    assert callable(finalStateMachine_FinalState.__init__)


def test_finalstatemachine_finalstate_constructor_args():
    sig = inspect.signature(finalStateMachine_FinalState.__init__)
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
finalStateMachine_State_strategy = st.builds(
    finalStateMachine_State,
    name=
        safe_text
)
finalStateMachine_Transition_strategy = st.builds(
    finalStateMachine_Transition,
    name=
        safe_text
)
finalStateMachine_FSM_strategy = st.builds(
    finalStateMachine_FSM,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
finalStateMachine_InitialState_strategy = st.builds(
    finalStateMachine_InitialState,
)
finalStateMachine_FinalState_strategy = st.builds(
    finalStateMachine_FinalState,
)

@given(instance=finalStateMachine_State_strategy)
@settings(max_examples=50)
def test_finalstatemachine_state_instantiation(instance):
    assert isinstance(instance, finalStateMachine_State)



@given(instance=finalStateMachine_State_strategy)
def test_finalstatemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=finalStateMachine_Transition_strategy)
@settings(max_examples=50)
def test_finalstatemachine_transition_instantiation(instance):
    assert isinstance(instance, finalStateMachine_Transition)



@given(instance=finalStateMachine_Transition_strategy)
def test_finalstatemachine_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=finalStateMachine_FSM_strategy)
@settings(max_examples=50)
def test_finalstatemachine_fsm_instantiation(instance):
    assert isinstance(instance, finalStateMachine_FSM)



@given(instance=finalStateMachine_FSM_strategy)
def test_finalstatemachine_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=finalStateMachine_InitialState_strategy)
@settings(max_examples=50)
def test_finalstatemachine_initialstate_instantiation(instance):
    assert isinstance(instance, finalStateMachine_InitialState)

@given(instance=finalStateMachine_FinalState_strategy)
@settings(max_examples=50)
def test_finalstatemachine_finalstate_instantiation(instance):
    assert isinstance(instance, finalStateMachine_FinalState)
