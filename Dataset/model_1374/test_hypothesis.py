import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachines::Transition,
    statemachines::Event,
    statemachines::State,
    statemachines::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachines::transition_is_not_abstract():
    assert not inspect.isabstract(statemachines::Transition)


def test_statemachines::transition_constructor_exists():
    assert callable(statemachines::Transition.__init__)


def test_statemachines::transition_constructor_args():
    sig = inspect.signature(statemachines::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::event_is_not_abstract():
    assert not inspect.isabstract(statemachines::Event)


def test_statemachines::event_constructor_exists():
    assert callable(statemachines::Event.__init__)


def test_statemachines::event_constructor_args():
    sig = inspect.signature(statemachines::Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachines::event_has_code():
    assert hasattr(statemachines::Event, "code")
    descriptor = None
    for klass in statemachines::Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_statemachines::event_has_name():
    assert hasattr(statemachines::Event, "name")
    descriptor = None
    for klass in statemachines::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachines::state_is_not_abstract():
    assert not inspect.isabstract(statemachines::State)


def test_statemachines::state_constructor_exists():
    assert callable(statemachines::State.__init__)


def test_statemachines::state_constructor_args():
    sig = inspect.signature(statemachines::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachines::state_has_name():
    assert hasattr(statemachines::State, "name")
    descriptor = None
    for klass in statemachines::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachines::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachines::StateMachine)


def test_statemachines::statemachine_constructor_exists():
    assert callable(statemachines::StateMachine.__init__)


def test_statemachines::statemachine_constructor_args():
    sig = inspect.signature(statemachines::StateMachine.__init__)
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
statemachines::Transition_strategy = st.builds(
    statemachines::Transition,
)
statemachines::Event_strategy = st.builds(
    statemachines::Event,
    code=
        safe_text,
    name=
        safe_text
)
statemachines::State_strategy = st.builds(
    statemachines::State,
    name=
        safe_text
)
statemachines::StateMachine_strategy = st.builds(
    statemachines::StateMachine,
)

@given(instance=statemachines::Transition_strategy)
@settings(max_examples=50)
def test_statemachines::transition_instantiation(instance):
    assert isinstance(instance, statemachines::Transition)

@given(instance=statemachines::Event_strategy)
@settings(max_examples=50)
def test_statemachines::event_instantiation(instance):
    assert isinstance(instance, statemachines::Event)

@given(instance=statemachines::Event_strategy)
def test_statemachines::event_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=statemachines::Event_strategy)
def test_statemachines::event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachines::Event_strategy)
def test_statemachines::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachines::Event_strategy)
def test_statemachines::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachines::State_strategy)
@settings(max_examples=50)
def test_statemachines::state_instantiation(instance):
    assert isinstance(instance, statemachines::State)

@given(instance=statemachines::State_strategy)
def test_statemachines::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachines::State_strategy)
def test_statemachines::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachines::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachines::statemachine_instantiation(instance):
    assert isinstance(instance, statemachines::StateMachine)
