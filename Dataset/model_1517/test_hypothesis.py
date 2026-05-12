import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sm3_Transition,
    sm3_State,
    sm3_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm3_transition_is_not_abstract():
    assert not inspect.isabstract(sm3_Transition)


def test_sm3_transition_constructor_exists():
    assert callable(sm3_Transition.__init__)


def test_sm3_transition_constructor_args():
    sig = inspect.signature(sm3_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_sm3_transition_has_event():
    assert hasattr(sm3_Transition, "event")
    descriptor = None
    for klass in sm3_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_sm3_state_is_not_abstract():
    assert not inspect.isabstract(sm3_State)


def test_sm3_state_constructor_exists():
    assert callable(sm3_State.__init__)


def test_sm3_state_constructor_args():
    sig = inspect.signature(sm3_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm3_state_has_name():
    assert hasattr(sm3_State, "name")
    descriptor = None
    for klass in sm3_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm3_statemachine_is_not_abstract():
    assert not inspect.isabstract(sm3_StateMachine)


def test_sm3_statemachine_constructor_exists():
    assert callable(sm3_StateMachine.__init__)


def test_sm3_statemachine_constructor_args():
    sig = inspect.signature(sm3_StateMachine.__init__)
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
sm3_Transition_strategy = st.builds(
    sm3_Transition,
    event=
        safe_text
)
sm3_State_strategy = st.builds(
    sm3_State,
    name=
        safe_text
)
sm3_StateMachine_strategy = st.builds(
    sm3_StateMachine,
)

@given(instance=sm3_Transition_strategy)
@settings(max_examples=50)
def test_sm3_transition_instantiation(instance):
    assert isinstance(instance, sm3_Transition)



@given(instance=sm3_Transition_strategy)
def test_sm3_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=sm3_State_strategy)
@settings(max_examples=50)
def test_sm3_state_instantiation(instance):
    assert isinstance(instance, sm3_State)



@given(instance=sm3_State_strategy)
def test_sm3_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm3_StateMachine_strategy)
@settings(max_examples=50)
def test_sm3_statemachine_instantiation(instance):
    assert isinstance(instance, sm3_StateMachine)
