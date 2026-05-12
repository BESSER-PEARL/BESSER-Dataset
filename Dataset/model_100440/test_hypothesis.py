import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    statemachine::mk2::Composite::state,
    statemachine::mk2::Final::state,
    statemachine::mk2::Event,
    statemachine::mk2::Transition,
    statemachine::mk2::State,
    statemachine::mk2::StateMachine,
    statemachine::mk2::SimpleState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::mk2::composite::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::mk2::Composite::state)


def test_statemachine::mk2::composite::state_constructor_exists():
    assert callable(statemachine::mk2::Composite::state.__init__)


def test_statemachine::mk2::composite::state_constructor_args():
    sig = inspect.signature(statemachine::mk2::Composite::state.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::mk2::final::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::mk2::Final::state)


def test_statemachine::mk2::final::state_constructor_exists():
    assert callable(statemachine::mk2::Final::state.__init__)


def test_statemachine::mk2::final::state_constructor_args():
    sig = inspect.signature(statemachine::mk2::Final::state.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::mk2::event_is_not_abstract():
    assert not inspect.isabstract(statemachine::mk2::Event)


def test_statemachine::mk2::event_constructor_exists():
    assert callable(statemachine::mk2::Event.__init__)


def test_statemachine::mk2::event_constructor_args():
    sig = inspect.signature(statemachine::mk2::Event.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_statemachine::mk2::event_has_description():
    assert hasattr(statemachine::mk2::Event, "description")
    descriptor = None
    for klass in statemachine::mk2::Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::mk2::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::mk2::Transition)


def test_statemachine::mk2::transition_constructor_exists():
    assert callable(statemachine::mk2::Transition.__init__)


def test_statemachine::mk2::transition_constructor_args():
    sig = inspect.signature(statemachine::mk2::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::mk2::transition_has_name():
    assert hasattr(statemachine::mk2::Transition, "name")
    descriptor = None
    for klass in statemachine::mk2::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::mk2::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::mk2::State)


def test_statemachine::mk2::state_constructor_exists():
    assert callable(statemachine::mk2::State.__init__)


def test_statemachine::mk2::state_constructor_args():
    sig = inspect.signature(statemachine::mk2::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::mk2::state_has_name():
    assert hasattr(statemachine::mk2::State, "name")
    descriptor = None
    for klass in statemachine::mk2::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::mk2::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::mk2::StateMachine)


def test_statemachine::mk2::statemachine_constructor_exists():
    assert callable(statemachine::mk2::StateMachine.__init__)


def test_statemachine::mk2::statemachine_constructor_args():
    sig = inspect.signature(statemachine::mk2::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::mk2::simplestate_is_not_abstract():
    assert not inspect.isabstract(statemachine::mk2::SimpleState)


def test_statemachine::mk2::simplestate_constructor_exists():
    assert callable(statemachine::mk2::SimpleState.__init__)


def test_statemachine::mk2::simplestate_constructor_args():
    sig = inspect.signature(statemachine::mk2::SimpleState.__init__)
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
State_strategy = st.builds(
    State,
)
statemachine::mk2::Composite::state_strategy = st.builds(
    statemachine::mk2::Composite::state,
)
statemachine::mk2::Final::state_strategy = st.builds(
    statemachine::mk2::Final::state,
)
statemachine::mk2::Event_strategy = st.builds(
    statemachine::mk2::Event,
    description=
        safe_text
)
statemachine::mk2::Transition_strategy = st.builds(
    statemachine::mk2::Transition,
    name=
        safe_text
)
statemachine::mk2::State_strategy = st.builds(
    statemachine::mk2::State,
    name=
        safe_text
)
statemachine::mk2::StateMachine_strategy = st.builds(
    statemachine::mk2::StateMachine,
)
statemachine::mk2::SimpleState_strategy = st.builds(
    statemachine::mk2::SimpleState,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine::mk2::Composite::state_strategy)
@settings(max_examples=50)
def test_statemachine::mk2::composite::state_instantiation(instance):
    assert isinstance(instance, statemachine::mk2::Composite::state)

@given(instance=statemachine::mk2::Final::state_strategy)
@settings(max_examples=50)
def test_statemachine::mk2::final::state_instantiation(instance):
    assert isinstance(instance, statemachine::mk2::Final::state)

@given(instance=statemachine::mk2::Event_strategy)
@settings(max_examples=50)
def test_statemachine::mk2::event_instantiation(instance):
    assert isinstance(instance, statemachine::mk2::Event)

@given(instance=statemachine::mk2::Event_strategy)
def test_statemachine::mk2::event_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=statemachine::mk2::Event_strategy)
def test_statemachine::mk2::event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=statemachine::mk2::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::mk2::transition_instantiation(instance):
    assert isinstance(instance, statemachine::mk2::Transition)

@given(instance=statemachine::mk2::Transition_strategy)
def test_statemachine::mk2::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::mk2::Transition_strategy)
def test_statemachine::mk2::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::mk2::State_strategy)
@settings(max_examples=50)
def test_statemachine::mk2::state_instantiation(instance):
    assert isinstance(instance, statemachine::mk2::State)

@given(instance=statemachine::mk2::State_strategy)
def test_statemachine::mk2::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::mk2::State_strategy)
def test_statemachine::mk2::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::mk2::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::mk2::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::mk2::StateMachine)

@given(instance=statemachine::mk2::SimpleState_strategy)
@settings(max_examples=50)
def test_statemachine::mk2::simplestate_instantiation(instance):
    assert isinstance(instance, statemachine::mk2::SimpleState)
