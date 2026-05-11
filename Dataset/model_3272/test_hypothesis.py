import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sm::Transition,
    sm::State,
    Transition,
    sm::sm::Transition,
    State,
    sm::sm::State,
    StateMachine,
    sm::StateMachine,
    sm::Event,
    sm::sm::StateMachine,
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
    assert "name" in params, "Missing parameter 'name'"

def test_sm::transition_has_name():
    assert hasattr(sm::Transition, "name")
    descriptor = None
    for klass in sm::Transition.__mro__:
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



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_sm::sm::transition_is_not_abstract():
    assert not inspect.isabstract(sm::sm::Transition)


def test_sm::sm::transition_constructor_exists():
    assert callable(sm::sm::Transition.__init__)


def test_sm::sm::transition_constructor_args():
    sig = inspect.signature(sm::sm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_sm::sm::state_is_not_abstract():
    assert not inspect.isabstract(sm::sm::State)


def test_sm::sm::state_constructor_exists():
    assert callable(sm::sm::State.__init__)


def test_sm::sm::state_constructor_args():
    sig = inspect.signature(sm::sm::State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



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



def test_sm::event_is_not_abstract():
    assert not inspect.isabstract(sm::Event)


def test_sm::event_constructor_exists():
    assert callable(sm::Event.__init__)


def test_sm::event_constructor_args():
    sig = inspect.signature(sm::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm::event_has_name():
    assert hasattr(sm::Event, "name")
    descriptor = None
    for klass in sm::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sm::sm::statemachine_is_not_abstract():
    assert not inspect.isabstract(sm::sm::StateMachine)


def test_sm::sm::statemachine_constructor_exists():
    assert callable(sm::sm::StateMachine.__init__)


def test_sm::sm::statemachine_constructor_args():
    sig = inspect.signature(sm::sm::StateMachine.__init__)
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
sm::Transition_strategy = st.builds(
    sm::Transition,
    name=
        safe_text
)
sm::State_strategy = st.builds(
    sm::State,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
sm::sm::Transition_strategy = st.builds(
    sm::sm::Transition,
)
State_strategy = st.builds(
    State,
)
sm::sm::State_strategy = st.builds(
    sm::sm::State,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
sm::StateMachine_strategy = st.builds(
    sm::StateMachine,
    name=
        safe_text
)
sm::Event_strategy = st.builds(
    sm::Event,
    name=
        safe_text
)
sm::sm::StateMachine_strategy = st.builds(
    sm::sm::StateMachine,
)

@given(instance=sm::Transition_strategy)
@settings(max_examples=50)
def test_sm::transition_instantiation(instance):
    assert isinstance(instance, sm::Transition)

@given(instance=sm::Transition_strategy)
def test_sm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm::Transition_strategy)
def test_sm::transition_name_setter(instance):
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

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=sm::sm::Transition_strategy)
@settings(max_examples=50)
def test_sm::sm::transition_instantiation(instance):
    assert isinstance(instance, sm::sm::Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=sm::sm::State_strategy)
@settings(max_examples=50)
def test_sm::sm::state_instantiation(instance):
    assert isinstance(instance, sm::sm::State)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

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

@given(instance=sm::Event_strategy)
@settings(max_examples=50)
def test_sm::event_instantiation(instance):
    assert isinstance(instance, sm::Event)

@given(instance=sm::Event_strategy)
def test_sm::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sm::Event_strategy)
def test_sm::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sm::sm::StateMachine_strategy)
@settings(max_examples=50)
def test_sm::sm::statemachine_instantiation(instance):
    assert isinstance(instance, sm::sm::StateMachine)
