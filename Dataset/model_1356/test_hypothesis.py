import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    statemachine::Composite,
    statemachine::Simple,
    statemachine::Initial,
    statemachine::StateMachine,
    statemachine::Resource,
    statemachine::State,
    statemachine::Transition,
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



def test_statemachine::composite_is_not_abstract():
    assert not inspect.isabstract(statemachine::Composite)


def test_statemachine::composite_constructor_exists():
    assert callable(statemachine::Composite.__init__)


def test_statemachine::composite_constructor_args():
    sig = inspect.signature(statemachine::Composite.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::simple_is_not_abstract():
    assert not inspect.isabstract(statemachine::Simple)


def test_statemachine::simple_constructor_exists():
    assert callable(statemachine::Simple.__init__)


def test_statemachine::simple_constructor_args():
    sig = inspect.signature(statemachine::Simple.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::initial_is_not_abstract():
    assert not inspect.isabstract(statemachine::Initial)


def test_statemachine::initial_constructor_exists():
    assert callable(statemachine::Initial.__init__)


def test_statemachine::initial_constructor_args():
    sig = inspect.signature(statemachine::Initial.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_name():
    assert hasattr(statemachine::StateMachine, "name")
    descriptor = None
    for klass in statemachine::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::resource_is_not_abstract():
    assert not inspect.isabstract(statemachine::Resource)


def test_statemachine::resource_constructor_exists():
    assert callable(statemachine::Resource.__init__)


def test_statemachine::resource_constructor_args():
    sig = inspect.signature(statemachine::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::resource_has_name():
    assert hasattr(statemachine::Resource, "name")
    descriptor = None
    for klass in statemachine::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::state_has_name():
    assert hasattr(statemachine::State, "name")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_statemachine::transition_has_duration():
    assert hasattr(statemachine::Transition, "duration")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_Id():
    assert hasattr(statemachine::Transition, "Id")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
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
State_strategy = st.builds(
    State,
)
statemachine::Composite_strategy = st.builds(
    statemachine::Composite,
)
statemachine::Simple_strategy = st.builds(
    statemachine::Simple,
)
statemachine::Initial_strategy = st.builds(
    statemachine::Initial,
)
statemachine::StateMachine_strategy = st.builds(
    statemachine::StateMachine,
    name=
        safe_text
)
statemachine::Resource_strategy = st.builds(
    statemachine::Resource,
    name=
        safe_text
)
statemachine::State_strategy = st.builds(
    statemachine::State,
    name=
        safe_text
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
    duration=
        st.integers(),
    Id=
        st.integers()
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine::Composite_strategy)
@settings(max_examples=50)
def test_statemachine::composite_instantiation(instance):
    assert isinstance(instance, statemachine::Composite)

@given(instance=statemachine::Simple_strategy)
@settings(max_examples=50)
def test_statemachine::simple_instantiation(instance):
    assert isinstance(instance, statemachine::Simple)

@given(instance=statemachine::Initial_strategy)
@settings(max_examples=50)
def test_statemachine::initial_instantiation(instance):
    assert isinstance(instance, statemachine::Initial)

@given(instance=statemachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::StateMachine)

@given(instance=statemachine::StateMachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::StateMachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Resource_strategy)
@settings(max_examples=50)
def test_statemachine::resource_instantiation(instance):
    assert isinstance(instance, statemachine::Resource)

@given(instance=statemachine::Resource_strategy)
def test_statemachine::resource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Resource_strategy)
def test_statemachine::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_Id_type(instance):
    assert isinstance(instance.Id, int)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original
