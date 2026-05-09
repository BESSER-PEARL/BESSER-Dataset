import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myStateMachines::State,
    myStateMachines::Transition,
    myStateMachines::Event,
    myStateMachines::Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mystatemachines::state_is_not_abstract():
    assert not inspect.isabstract(myStateMachines::State)


def test_mystatemachines::state_constructor_exists():
    assert callable(myStateMachines::State.__init__)


def test_mystatemachines::state_constructor_args():
    sig = inspect.signature(myStateMachines::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "actions" in params, "Missing parameter 'actions'"

def test_mystatemachines::state_has_name():
    assert hasattr(myStateMachines::State, "name")
    descriptor = None
    for klass in myStateMachines::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mystatemachines::state_has_actions():
    assert hasattr(myStateMachines::State, "actions")
    descriptor = None
    for klass in myStateMachines::State.__mro__:
        if "actions" in klass.__dict__:
            descriptor = klass.__dict__["actions"]
            break
    assert isinstance(descriptor, property)



def test_mystatemachines::transition_is_not_abstract():
    assert not inspect.isabstract(myStateMachines::Transition)


def test_mystatemachines::transition_constructor_exists():
    assert callable(myStateMachines::Transition.__init__)


def test_mystatemachines::transition_constructor_args():
    sig = inspect.signature(myStateMachines::Transition.__init__)
    params = list(sig.parameters.keys())



def test_mystatemachines::event_is_not_abstract():
    assert not inspect.isabstract(myStateMachines::Event)


def test_mystatemachines::event_constructor_exists():
    assert callable(myStateMachines::Event.__init__)


def test_mystatemachines::event_constructor_args():
    sig = inspect.signature(myStateMachines::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mystatemachines::event_has_name():
    assert hasattr(myStateMachines::Event, "name")
    descriptor = None
    for klass in myStateMachines::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mystatemachines::statemachine_is_not_abstract():
    assert not inspect.isabstract(myStateMachines::Statemachine)


def test_mystatemachines::statemachine_constructor_exists():
    assert callable(myStateMachines::Statemachine.__init__)


def test_mystatemachines::statemachine_constructor_args():
    sig = inspect.signature(myStateMachines::Statemachine.__init__)
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
myStateMachines::State_strategy = st.builds(
    myStateMachines::State,
    name=
        safe_text,
    actions=
        safe_text
)
myStateMachines::Transition_strategy = st.builds(
    myStateMachines::Transition,
)
myStateMachines::Event_strategy = st.builds(
    myStateMachines::Event,
    name=
        safe_text
)
myStateMachines::Statemachine_strategy = st.builds(
    myStateMachines::Statemachine,
)

@given(instance=myStateMachines::State_strategy)
@settings(max_examples=50)
def test_mystatemachines::state_instantiation(instance):
    assert isinstance(instance, myStateMachines::State)

@given(instance=myStateMachines::State_strategy)
def test_mystatemachines::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myStateMachines::State_strategy)
def test_mystatemachines::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myStateMachines::State_strategy)
def test_mystatemachines::state_actions_type(instance):
    assert isinstance(instance.actions, str)


@given(instance=myStateMachines::State_strategy)
def test_mystatemachines::state_actions_setter(instance):
    original = instance.actions
    instance.actions = original
    assert instance.actions == original

@given(instance=myStateMachines::Transition_strategy)
@settings(max_examples=50)
def test_mystatemachines::transition_instantiation(instance):
    assert isinstance(instance, myStateMachines::Transition)

@given(instance=myStateMachines::Event_strategy)
@settings(max_examples=50)
def test_mystatemachines::event_instantiation(instance):
    assert isinstance(instance, myStateMachines::Event)

@given(instance=myStateMachines::Event_strategy)
def test_mystatemachines::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myStateMachines::Event_strategy)
def test_mystatemachines::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myStateMachines::Statemachine_strategy)
@settings(max_examples=50)
def test_mystatemachines::statemachine_instantiation(instance):
    assert isinstance(instance, myStateMachines::Statemachine)
