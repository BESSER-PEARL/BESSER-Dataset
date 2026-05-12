import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sm6_State,
    sm6_StateMachine,
    sm6_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm6_state_is_not_abstract():
    assert not inspect.isabstract(sm6_State)


def test_sm6_state_constructor_exists():
    assert callable(sm6_State.__init__)


def test_sm6_state_constructor_args():
    sig = inspect.signature(sm6_State.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "name" in params, "Missing parameter 'name'"

def test_sm6_state_has_isFinal():
    assert hasattr(sm6_State, "isFinal")
    descriptor = None
    for klass in sm6_State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_sm6_state_has_name():
    assert hasattr(sm6_State, "name")
    descriptor = None
    for klass in sm6_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm6_statemachine_is_not_abstract():
    assert not inspect.isabstract(sm6_StateMachine)


def test_sm6_statemachine_constructor_exists():
    assert callable(sm6_StateMachine.__init__)


def test_sm6_statemachine_constructor_args():
    sig = inspect.signature(sm6_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_sm6_transition_is_not_abstract():
    assert not inspect.isabstract(sm6_Transition)


def test_sm6_transition_constructor_exists():
    assert callable(sm6_Transition.__init__)


def test_sm6_transition_constructor_args():
    sig = inspect.signature(sm6_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_sm6_transition_has_event():
    assert hasattr(sm6_Transition, "event")
    descriptor = None
    for klass in sm6_Transition.__mro__:
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
sm6_State_strategy = st.builds(
    sm6_State,
    isFinal=
        safe_text,
    name=
        safe_text
)
sm6_StateMachine_strategy = st.builds(
    sm6_StateMachine,
)
sm6_Transition_strategy = st.builds(
    sm6_Transition,
    event=
        safe_text
)

@given(instance=sm6_State_strategy)
@settings(max_examples=50)
def test_sm6_state_instantiation(instance):
    assert isinstance(instance, sm6_State)



@given(instance=sm6_State_strategy)
def test_sm6_state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=sm6_State_strategy)
def test_sm6_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm6_StateMachine_strategy)
@settings(max_examples=50)
def test_sm6_statemachine_instantiation(instance):
    assert isinstance(instance, sm6_StateMachine)

@given(instance=sm6_Transition_strategy)
@settings(max_examples=50)
def test_sm6_transition_instantiation(instance):
    assert isinstance(instance, sm6_Transition)



@given(instance=sm6_Transition_strategy)
def test_sm6_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original
