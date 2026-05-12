import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    NHSM_FinalState,
    NHSM_InitialState,
    NHSM_StateMachine,
    NHSM_State,
    NHSM_Transition,
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



def test_nhsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(NHSM_FinalState)


def test_nhsm_finalstate_constructor_exists():
    assert callable(NHSM_FinalState.__init__)


def test_nhsm_finalstate_constructor_args():
    sig = inspect.signature(NHSM_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_nhsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(NHSM_InitialState)


def test_nhsm_initialstate_constructor_exists():
    assert callable(NHSM_InitialState.__init__)


def test_nhsm_initialstate_constructor_args():
    sig = inspect.signature(NHSM_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_nhsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(NHSM_StateMachine)


def test_nhsm_statemachine_constructor_exists():
    assert callable(NHSM_StateMachine.__init__)


def test_nhsm_statemachine_constructor_args():
    sig = inspect.signature(NHSM_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nhsm_statemachine_has_name():
    assert hasattr(NHSM_StateMachine, "name")
    descriptor = None
    for klass in NHSM_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nhsm_state_is_not_abstract():
    assert not inspect.isabstract(NHSM_State)


def test_nhsm_state_constructor_exists():
    assert callable(NHSM_State.__init__)


def test_nhsm_state_constructor_args():
    sig = inspect.signature(NHSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nhsm_state_has_name():
    assert hasattr(NHSM_State, "name")
    descriptor = None
    for klass in NHSM_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nhsm_transition_is_not_abstract():
    assert not inspect.isabstract(NHSM_Transition)


def test_nhsm_transition_constructor_exists():
    assert callable(NHSM_Transition.__init__)


def test_nhsm_transition_constructor_args():
    sig = inspect.signature(NHSM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_nhsm_transition_has_effect():
    assert hasattr(NHSM_Transition, "effect")
    descriptor = None
    for klass in NHSM_Transition.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_nhsm_transition_has_trigger():
    assert hasattr(NHSM_Transition, "trigger")
    descriptor = None
    for klass in NHSM_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
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
NHSM_FinalState_strategy = st.builds(
    NHSM_FinalState,
)
NHSM_InitialState_strategy = st.builds(
    NHSM_InitialState,
)
NHSM_StateMachine_strategy = st.builds(
    NHSM_StateMachine,
    name=
        safe_text
)
NHSM_State_strategy = st.builds(
    NHSM_State,
    name=
        safe_text
)
NHSM_Transition_strategy = st.builds(
    NHSM_Transition,
    effect=
        safe_text,
    trigger=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=NHSM_FinalState_strategy)
@settings(max_examples=50)
def test_nhsm_finalstate_instantiation(instance):
    assert isinstance(instance, NHSM_FinalState)

@given(instance=NHSM_InitialState_strategy)
@settings(max_examples=50)
def test_nhsm_initialstate_instantiation(instance):
    assert isinstance(instance, NHSM_InitialState)

@given(instance=NHSM_StateMachine_strategy)
@settings(max_examples=50)
def test_nhsm_statemachine_instantiation(instance):
    assert isinstance(instance, NHSM_StateMachine)



@given(instance=NHSM_StateMachine_strategy)
def test_nhsm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NHSM_State_strategy)
@settings(max_examples=50)
def test_nhsm_state_instantiation(instance):
    assert isinstance(instance, NHSM_State)



@given(instance=NHSM_State_strategy)
def test_nhsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NHSM_Transition_strategy)
@settings(max_examples=50)
def test_nhsm_transition_instantiation(instance):
    assert isinstance(instance, NHSM_Transition)



@given(instance=NHSM_Transition_strategy)
def test_nhsm_transition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=NHSM_Transition_strategy)
def test_nhsm_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original
