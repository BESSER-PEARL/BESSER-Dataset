import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sm1_State,
    sm1_StateMachine,
    sm1_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm1_state_is_not_abstract():
    assert not inspect.isabstract(sm1_State)


def test_sm1_state_constructor_exists():
    assert callable(sm1_State.__init__)


def test_sm1_state_constructor_args():
    sig = inspect.signature(sm1_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm1_state_has_name():
    assert hasattr(sm1_State, "name")
    descriptor = None
    for klass in sm1_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm1_statemachine_is_not_abstract():
    assert not inspect.isabstract(sm1_StateMachine)


def test_sm1_statemachine_constructor_exists():
    assert callable(sm1_StateMachine.__init__)


def test_sm1_statemachine_constructor_args():
    sig = inspect.signature(sm1_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_sm1_transition_is_not_abstract():
    assert not inspect.isabstract(sm1_Transition)


def test_sm1_transition_constructor_exists():
    assert callable(sm1_Transition.__init__)


def test_sm1_transition_constructor_args():
    sig = inspect.signature(sm1_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_sm1_transition_has_event():
    assert hasattr(sm1_Transition, "event")
    descriptor = None
    for klass in sm1_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
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
sm1_State_strategy = st.builds(
    sm1_State,
    name=
        safe_text
)
sm1_StateMachine_strategy = st.builds(
    sm1_StateMachine,
)
sm1_Transition_strategy = st.builds(
    sm1_Transition,
    event=
        safe_text
)

@given(instance=sm1_State_strategy)
@settings(max_examples=50)
def test_sm1_state_instantiation(instance):
    assert isinstance(instance, sm1_State)



@given(instance=sm1_State_strategy)
def test_sm1_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm1_StateMachine_strategy)
@settings(max_examples=50)
def test_sm1_statemachine_instantiation(instance):
    assert isinstance(instance, sm1_StateMachine)

@given(instance=sm1_Transition_strategy)
@settings(max_examples=50)
def test_sm1_transition_instantiation(instance):
    assert isinstance(instance, sm1_Transition)



@given(instance=sm1_Transition_strategy)
def test_sm1_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original
