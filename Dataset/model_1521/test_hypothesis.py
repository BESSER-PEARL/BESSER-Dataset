import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sm6::State,
    sm6::StateMachine,
    sm6::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm6::state_is_not_abstract():
    assert not inspect.isabstract(sm6::State)


def test_sm6::state_constructor_exists():
    assert callable(sm6::State.__init__)


def test_sm6::state_constructor_args():
    sig = inspect.signature(sm6::State.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "name" in params, "Missing parameter 'name'"

def test_sm6::state_has_isFinal():
    assert hasattr(sm6::State, "isFinal")
    descriptor = None
    for klass in sm6::State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_sm6::state_has_name():
    assert hasattr(sm6::State, "name")
    descriptor = None
    for klass in sm6::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm6::statemachine_is_not_abstract():
    assert not inspect.isabstract(sm6::StateMachine)


def test_sm6::statemachine_constructor_exists():
    assert callable(sm6::StateMachine.__init__)


def test_sm6::statemachine_constructor_args():
    sig = inspect.signature(sm6::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_sm6::transition_is_not_abstract():
    assert not inspect.isabstract(sm6::Transition)


def test_sm6::transition_constructor_exists():
    assert callable(sm6::Transition.__init__)


def test_sm6::transition_constructor_args():
    sig = inspect.signature(sm6::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_sm6::transition_has_event():
    assert hasattr(sm6::Transition, "event")
    descriptor = None
    for klass in sm6::Transition.__mro__:
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
sm6::State_strategy = st.builds(
    sm6::State,
    isFinal=
        safe_text,
    name=
        safe_text
)
sm6::StateMachine_strategy = st.builds(
    sm6::StateMachine,
)
sm6::Transition_strategy = st.builds(
    sm6::Transition,
    event=
        safe_text
)

@given(instance=sm6::State_strategy)
@settings(max_examples=50)
def test_sm6::state_instantiation(instance):
    assert isinstance(instance, sm6::State)

@given(instance=sm6::State_strategy)
def test_sm6::state_isFinal_type(instance):
    assert isinstance(instance.isFinal, str)


@given(instance=sm6::State_strategy)
def test_sm6::state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=sm6::State_strategy)
def test_sm6::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm6::State_strategy)
def test_sm6::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm6::StateMachine_strategy)
@settings(max_examples=50)
def test_sm6::statemachine_instantiation(instance):
    assert isinstance(instance, sm6::StateMachine)

@given(instance=sm6::Transition_strategy)
@settings(max_examples=50)
def test_sm6::transition_instantiation(instance):
    assert isinstance(instance, sm6::Transition)

@given(instance=sm6::Transition_strategy)
def test_sm6::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=sm6::Transition_strategy)
def test_sm6::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original
