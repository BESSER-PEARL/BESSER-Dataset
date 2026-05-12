import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sm2_Transition,
    sm2_State,
    sm2_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm2_transition_is_not_abstract():
    assert not inspect.isabstract(sm2_Transition)


def test_sm2_transition_constructor_exists():
    assert callable(sm2_Transition.__init__)


def test_sm2_transition_constructor_args():
    sig = inspect.signature(sm2_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_sm2_transition_has_event():
    assert hasattr(sm2_Transition, "event")
    descriptor = None
    for klass in sm2_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_sm2_state_is_not_abstract():
    assert not inspect.isabstract(sm2_State)


def test_sm2_state_constructor_exists():
    assert callable(sm2_State.__init__)


def test_sm2_state_constructor_args():
    sig = inspect.signature(sm2_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm2_state_has_name():
    assert hasattr(sm2_State, "name")
    descriptor = None
    for klass in sm2_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm2_statemachine_is_not_abstract():
    assert not inspect.isabstract(sm2_StateMachine)


def test_sm2_statemachine_constructor_exists():
    assert callable(sm2_StateMachine.__init__)


def test_sm2_statemachine_constructor_args():
    sig = inspect.signature(sm2_StateMachine.__init__)
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
sm2_Transition_strategy = st.builds(
    sm2_Transition,
    event=
        safe_text
)
sm2_State_strategy = st.builds(
    sm2_State,
    name=
        safe_text
)
sm2_StateMachine_strategy = st.builds(
    sm2_StateMachine,
)

@given(instance=sm2_Transition_strategy)
@settings(max_examples=50)
def test_sm2_transition_instantiation(instance):
    assert isinstance(instance, sm2_Transition)



@given(instance=sm2_Transition_strategy)
def test_sm2_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=sm2_State_strategy)
@settings(max_examples=50)
def test_sm2_state_instantiation(instance):
    assert isinstance(instance, sm2_State)



@given(instance=sm2_State_strategy)
def test_sm2_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm2_StateMachine_strategy)
@settings(max_examples=50)
def test_sm2_statemachine_instantiation(instance):
    assert isinstance(instance, sm2_StateMachine)
