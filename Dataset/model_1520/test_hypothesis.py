import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sm4_Transition,
    sm4_State,
    State,
    sm4_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm4_transition_is_not_abstract():
    assert not inspect.isabstract(sm4_Transition)


def test_sm4_transition_constructor_exists():
    assert callable(sm4_Transition.__init__)


def test_sm4_transition_constructor_args():
    sig = inspect.signature(sm4_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_sm4_transition_has_event():
    assert hasattr(sm4_Transition, "event")
    descriptor = None
    for klass in sm4_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_sm4_state_is_not_abstract():
    assert not inspect.isabstract(sm4_State)


def test_sm4_state_constructor_exists():
    assert callable(sm4_State.__init__)


def test_sm4_state_constructor_args():
    sig = inspect.signature(sm4_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm4_state_has_name():
    assert hasattr(sm4_State, "name")
    descriptor = None
    for klass in sm4_State.__mro__:
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



def test_sm4_statemachine_is_not_abstract():
    assert not inspect.isabstract(sm4_StateMachine)


def test_sm4_statemachine_constructor_exists():
    assert callable(sm4_StateMachine.__init__)


def test_sm4_statemachine_constructor_args():
    sig = inspect.signature(sm4_StateMachine.__init__)
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
sm4_Transition_strategy = st.builds(
    sm4_Transition,
    event=
        safe_text
)
sm4_State_strategy = st.builds(
    sm4_State,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
sm4_StateMachine_strategy = st.builds(
    sm4_StateMachine,
)

@given(instance=sm4_Transition_strategy)
@settings(max_examples=50)
def test_sm4_transition_instantiation(instance):
    assert isinstance(instance, sm4_Transition)



@given(instance=sm4_Transition_strategy)
def test_sm4_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=sm4_State_strategy)
@settings(max_examples=50)
def test_sm4_state_instantiation(instance):
    assert isinstance(instance, sm4_State)



@given(instance=sm4_State_strategy)
def test_sm4_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=sm4_StateMachine_strategy)
@settings(max_examples=50)
def test_sm4_statemachine_instantiation(instance):
    assert isinstance(instance, sm4_StateMachine)
