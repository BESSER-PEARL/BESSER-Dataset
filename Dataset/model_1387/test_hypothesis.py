import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    SM_FinalState,
    SM_InitialState,
    SM_Transition,
    SM_StateMachine,
    SM_State,
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



def test_sm_finalstate_is_not_abstract():
    assert not inspect.isabstract(SM_FinalState)


def test_sm_finalstate_constructor_exists():
    assert callable(SM_FinalState.__init__)


def test_sm_finalstate_constructor_args():
    sig = inspect.signature(SM_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_sm_initialstate_is_not_abstract():
    assert not inspect.isabstract(SM_InitialState)


def test_sm_initialstate_constructor_exists():
    assert callable(SM_InitialState.__init__)


def test_sm_initialstate_constructor_args():
    sig = inspect.signature(SM_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_sm_transition_is_not_abstract():
    assert not inspect.isabstract(SM_Transition)


def test_sm_transition_constructor_exists():
    assert callable(SM_Transition.__init__)


def test_sm_transition_constructor_args():
    sig = inspect.signature(SM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "effect" in params, "Missing parameter 'effect'"

def test_sm_transition_has_trigger():
    assert hasattr(SM_Transition, "trigger")
    descriptor = None
    for klass in SM_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_sm_transition_has_effect():
    assert hasattr(SM_Transition, "effect")
    descriptor = None
    for klass in SM_Transition.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)



def test_sm_statemachine_is_not_abstract():
    assert not inspect.isabstract(SM_StateMachine)


def test_sm_statemachine_constructor_exists():
    assert callable(SM_StateMachine.__init__)


def test_sm_statemachine_constructor_args():
    sig = inspect.signature(SM_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_sm_state_is_not_abstract():
    assert not inspect.isabstract(SM_State)


def test_sm_state_constructor_exists():
    assert callable(SM_State.__init__)


def test_sm_state_constructor_args():
    sig = inspect.signature(SM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm_state_has_name():
    assert hasattr(SM_State, "name")
    descriptor = None
    for klass in SM_State.__mro__:
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
State_strategy = st.builds(
    State,
)
SM_FinalState_strategy = st.builds(
    SM_FinalState,
)
SM_InitialState_strategy = st.builds(
    SM_InitialState,
)
SM_Transition_strategy = st.builds(
    SM_Transition,
    trigger=
        safe_text,
    effect=
        safe_text
)
SM_StateMachine_strategy = st.builds(
    SM_StateMachine,
)
SM_State_strategy = st.builds(
    SM_State,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=SM_FinalState_strategy)
@settings(max_examples=50)
def test_sm_finalstate_instantiation(instance):
    assert isinstance(instance, SM_FinalState)

@given(instance=SM_InitialState_strategy)
@settings(max_examples=50)
def test_sm_initialstate_instantiation(instance):
    assert isinstance(instance, SM_InitialState)

@given(instance=SM_Transition_strategy)
@settings(max_examples=50)
def test_sm_transition_instantiation(instance):
    assert isinstance(instance, SM_Transition)



@given(instance=SM_Transition_strategy)
def test_sm_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=SM_Transition_strategy)
def test_sm_transition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=SM_StateMachine_strategy)
@settings(max_examples=50)
def test_sm_statemachine_instantiation(instance):
    assert isinstance(instance, SM_StateMachine)

@given(instance=SM_State_strategy)
@settings(max_examples=50)
def test_sm_state_instantiation(instance):
    assert isinstance(instance, SM_State)



@given(instance=SM_State_strategy)
def test_sm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
