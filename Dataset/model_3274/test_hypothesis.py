import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sm::Transition,
    sm::StateMachine,
    sm::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm::transition_is_not_abstract():
    assert not inspect.isabstract(sm::Transition)


def test_sm::transition_constructor_exists():
    assert callable(sm::Transition.__init__)


def test_sm::transition_constructor_args():
    sig = inspect.signature(sm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "isCompletion" in params, "Missing parameter 'isCompletion'"
    assert "name" in params, "Missing parameter 'name'"

def test_sm::transition_has_isCompletion():
    assert hasattr(sm::Transition, "isCompletion")
    descriptor = None
    for klass in sm::Transition.__mro__:
        if "isCompletion" in klass.__dict__:
            descriptor = klass.__dict__["isCompletion"]
            break
    assert isinstance(descriptor, property)

def test_sm::transition_has_name():
    assert hasattr(sm::Transition, "name")
    descriptor = None
    for klass in sm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm::statemachine_is_not_abstract():
    assert not inspect.isabstract(sm::StateMachine)


def test_sm::statemachine_constructor_exists():
    assert callable(sm::StateMachine.__init__)


def test_sm::statemachine_constructor_args():
    sig = inspect.signature(sm::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm::statemachine_has_name():
    assert hasattr(sm::StateMachine, "name")
    descriptor = None
    for klass in sm::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm::state_is_not_abstract():
    assert not inspect.isabstract(sm::State)


def test_sm::state_constructor_exists():
    assert callable(sm::State.__init__)


def test_sm::state_constructor_args():
    sig = inspect.signature(sm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm::state_has_name():
    assert hasattr(sm::State, "name")
    descriptor = None
    for klass in sm::State.__mro__:
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
sm::Transition_strategy = st.builds(
    sm::Transition,
    isCompletion=
        safe_text,
    name=
        safe_text
)
sm::StateMachine_strategy = st.builds(
    sm::StateMachine,
    name=
        safe_text
)
sm::State_strategy = st.builds(
    sm::State,
    name=
        safe_text
)

@given(instance=sm::Transition_strategy)
@settings(max_examples=50)
def test_sm::transition_instantiation(instance):
    assert isinstance(instance, sm::Transition)

@given(instance=sm::Transition_strategy)
def test_sm::transition_isCompletion_type(instance):
    assert isinstance(instance.isCompletion, str)


@given(instance=sm::Transition_strategy)
def test_sm::transition_isCompletion_setter(instance):
    original = instance.isCompletion
    instance.isCompletion = original
    assert instance.isCompletion == original

@given(instance=sm::Transition_strategy)
def test_sm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm::Transition_strategy)
def test_sm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm::StateMachine_strategy)
@settings(max_examples=50)
def test_sm::statemachine_instantiation(instance):
    assert isinstance(instance, sm::StateMachine)

@given(instance=sm::StateMachine_strategy)
def test_sm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm::StateMachine_strategy)
def test_sm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm::State_strategy)
@settings(max_examples=50)
def test_sm::state_instantiation(instance):
    assert isinstance(instance, sm::State)

@given(instance=sm::State_strategy)
def test_sm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm::State_strategy)
def test_sm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
