import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sm1::State,
    sm1::StateMachine,
    sm1::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm1::state_is_not_abstract():
    assert not inspect.isabstract(sm1::State)


def test_sm1::state_constructor_exists():
    assert callable(sm1::State.__init__)


def test_sm1::state_constructor_args():
    sig = inspect.signature(sm1::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm1::state_has_name():
    assert hasattr(sm1::State, "name")
    descriptor = None
    for klass in sm1::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm1::statemachine_is_not_abstract():
    assert not inspect.isabstract(sm1::StateMachine)


def test_sm1::statemachine_constructor_exists():
    assert callable(sm1::StateMachine.__init__)


def test_sm1::statemachine_constructor_args():
    sig = inspect.signature(sm1::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_sm1::transition_is_not_abstract():
    assert not inspect.isabstract(sm1::Transition)


def test_sm1::transition_constructor_exists():
    assert callable(sm1::Transition.__init__)


def test_sm1::transition_constructor_args():
    sig = inspect.signature(sm1::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_sm1::transition_has_event():
    assert hasattr(sm1::Transition, "event")
    descriptor = None
    for klass in sm1::Transition.__mro__:
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
sm1::State_strategy = st.builds(
    sm1::State,
    name=
        safe_text
)
sm1::StateMachine_strategy = st.builds(
    sm1::StateMachine,
)
sm1::Transition_strategy = st.builds(
    sm1::Transition,
    event=
        safe_text
)

@given(instance=sm1::State_strategy)
@settings(max_examples=50)
def test_sm1::state_instantiation(instance):
    assert isinstance(instance, sm1::State)

@given(instance=sm1::State_strategy)
def test_sm1::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm1::State_strategy)
def test_sm1::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm1::StateMachine_strategy)
@settings(max_examples=50)
def test_sm1::statemachine_instantiation(instance):
    assert isinstance(instance, sm1::StateMachine)

@given(instance=sm1::Transition_strategy)
@settings(max_examples=50)
def test_sm1::transition_instantiation(instance):
    assert isinstance(instance, sm1::Transition)

@given(instance=sm1::Transition_strategy)
def test_sm1::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=sm1::Transition_strategy)
def test_sm1::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original
