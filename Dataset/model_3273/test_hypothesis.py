import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sm_Transition,
    sm_State,
    sm_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm_transition_is_not_abstract():
    assert not inspect.isabstract(sm_Transition)


def test_sm_transition_constructor_exists():
    assert callable(sm_Transition.__init__)


def test_sm_transition_constructor_args():
    sig = inspect.signature(sm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm_transition_has_name():
    assert hasattr(sm_Transition, "name")
    descriptor = None
    for klass in sm_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm_state_is_not_abstract():
    assert not inspect.isabstract(sm_State)


def test_sm_state_constructor_exists():
    assert callable(sm_State.__init__)


def test_sm_state_constructor_args():
    sig = inspect.signature(sm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm_state_has_name():
    assert hasattr(sm_State, "name")
    descriptor = None
    for klass in sm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm_statemachine_is_not_abstract():
    assert not inspect.isabstract(sm_StateMachine)


def test_sm_statemachine_constructor_exists():
    assert callable(sm_StateMachine.__init__)


def test_sm_statemachine_constructor_args():
    sig = inspect.signature(sm_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm_statemachine_has_name():
    assert hasattr(sm_StateMachine, "name")
    descriptor = None
    for klass in sm_StateMachine.__mro__:
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
sm_Transition_strategy = st.builds(
    sm_Transition,
    name=
        safe_text
)
sm_State_strategy = st.builds(
    sm_State,
    name=
        safe_text
)
sm_StateMachine_strategy = st.builds(
    sm_StateMachine,
    name=
        safe_text
)

@given(instance=sm_Transition_strategy)
@settings(max_examples=50)
def test_sm_transition_instantiation(instance):
    assert isinstance(instance, sm_Transition)



@given(instance=sm_Transition_strategy)
def test_sm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm_State_strategy)
@settings(max_examples=50)
def test_sm_state_instantiation(instance):
    assert isinstance(instance, sm_State)



@given(instance=sm_State_strategy)
def test_sm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm_StateMachine_strategy)
@settings(max_examples=50)
def test_sm_statemachine_instantiation(instance):
    assert isinstance(instance, sm_StateMachine)



@given(instance=sm_StateMachine_strategy)
def test_sm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
