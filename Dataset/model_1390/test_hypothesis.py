import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_Transition,
    statemachine_State,
    statemachine_MyFSM,
    State,
    statemachine_InitialState,
    statemachine_FinalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_transition_has_name():
    assert hasattr(statemachine_Transition, "name")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_statemachine_myfsm_is_not_abstract():
    assert not inspect.isabstract(statemachine_MyFSM)


def test_statemachine_myfsm_constructor_exists():
    assert callable(statemachine_MyFSM.__init__)


def test_statemachine_myfsm_constructor_args():
    sig = inspect.signature(statemachine_MyFSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_myfsm_has_name():
    assert hasattr(statemachine_MyFSM, "name")
    descriptor = None
    for klass in statemachine_MyFSM.__mro__:
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



def test_statemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_InitialState)


def test_statemachine_initialstate_constructor_exists():
    assert callable(statemachine_InitialState.__init__)


def test_statemachine_initialstate_constructor_args():
    sig = inspect.signature(statemachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_FinalState)


def test_statemachine_finalstate_constructor_exists():
    assert callable(statemachine_FinalState.__init__)


def test_statemachine_finalstate_constructor_args():
    sig = inspect.signature(statemachine_FinalState.__init__)
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
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    name=
        safe_text
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    name=
        safe_text
)
statemachine_MyFSM_strategy = st.builds(
    statemachine_MyFSM,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
statemachine_InitialState_strategy = st.builds(
    statemachine_InitialState,
)
statemachine_FinalState_strategy = st.builds(
    statemachine_FinalState,
)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_MyFSM_strategy)
@settings(max_examples=50)
def test_statemachine_myfsm_instantiation(instance):
    assert isinstance(instance, statemachine_MyFSM)



@given(instance=statemachine_MyFSM_strategy)
def test_statemachine_myfsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine_InitialState_strategy)
@settings(max_examples=50)
def test_statemachine_initialstate_instantiation(instance):
    assert isinstance(instance, statemachine_InitialState)

@given(instance=statemachine_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine_finalstate_instantiation(instance):
    assert isinstance(instance, statemachine_FinalState)
