import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateMachine::Condition,
    stateMachine::Transition,
    stateMachine::State,
    stateMachine::Event,
    stateMachine::StateMachine,
    stateMachine::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::condition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Condition)


def test_statemachine::condition_constructor_exists():
    assert callable(stateMachine::Condition.__init__)


def test_statemachine::condition_constructor_args():
    sig = inspect.signature(stateMachine::Condition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(stateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(stateMachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(stateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(stateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(stateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::state_has_name():
    assert hasattr(stateMachine::State, "name")
    descriptor = None
    for klass in stateMachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(stateMachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(stateMachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::event_has_name():
    assert hasattr(stateMachine::Event, "name")
    descriptor = None
    for klass in stateMachine::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(stateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(stateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_name():
    assert hasattr(stateMachine::StateMachine, "name")
    descriptor = None
    for klass in stateMachine::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::model_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Model)


def test_statemachine::model_constructor_exists():
    assert callable(stateMachine::Model.__init__)


def test_statemachine::model_constructor_args():
    sig = inspect.signature(stateMachine::Model.__init__)
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
stateMachine::Condition_strategy = st.builds(
    stateMachine::Condition,
)
stateMachine::Transition_strategy = st.builds(
    stateMachine::Transition,
)
stateMachine::State_strategy = st.builds(
    stateMachine::State,
    name=
        safe_text
)
stateMachine::Event_strategy = st.builds(
    stateMachine::Event,
    name=
        safe_text
)
stateMachine::StateMachine_strategy = st.builds(
    stateMachine::StateMachine,
    name=
        safe_text
)
stateMachine::Model_strategy = st.builds(
    stateMachine::Model,
)

@given(instance=stateMachine::Condition_strategy)
@settings(max_examples=50)
def test_statemachine::condition_instantiation(instance):
    assert isinstance(instance, stateMachine::Condition)

@given(instance=stateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, stateMachine::Transition)

@given(instance=stateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, stateMachine::State)

@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, stateMachine::Event)

@given(instance=stateMachine::Event_strategy)
def test_statemachine::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::Event_strategy)
def test_statemachine::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine::StateMachine)

@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::Model_strategy)
@settings(max_examples=50)
def test_statemachine::model_instantiation(instance):
    assert isinstance(instance, stateMachine::Model)
