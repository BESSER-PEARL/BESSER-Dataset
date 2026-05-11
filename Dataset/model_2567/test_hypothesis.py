import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dsl::Transition,
    dsl::State,
    dsl::Event,
    dsl::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl::transition_is_not_abstract():
    assert not inspect.isabstract(dsl::Transition)


def test_dsl::transition_constructor_exists():
    assert callable(dsl::Transition.__init__)


def test_dsl::transition_constructor_args():
    sig = inspect.signature(dsl::Transition.__init__)
    params = list(sig.parameters.keys())



def test_dsl::state_is_not_abstract():
    assert not inspect.isabstract(dsl::State)


def test_dsl::state_constructor_exists():
    assert callable(dsl::State.__init__)


def test_dsl::state_constructor_args():
    sig = inspect.signature(dsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::state_has_name():
    assert hasattr(dsl::State, "name")
    descriptor = None
    for klass in dsl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::event_is_not_abstract():
    assert not inspect.isabstract(dsl::Event)


def test_dsl::event_constructor_exists():
    assert callable(dsl::Event.__init__)


def test_dsl::event_constructor_args():
    sig = inspect.signature(dsl::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::event_has_name():
    assert hasattr(dsl::Event, "name")
    descriptor = None
    for klass in dsl::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::statemachine_is_not_abstract():
    assert not inspect.isabstract(dsl::StateMachine)


def test_dsl::statemachine_constructor_exists():
    assert callable(dsl::StateMachine.__init__)


def test_dsl::statemachine_constructor_args():
    sig = inspect.signature(dsl::StateMachine.__init__)
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
dsl::Transition_strategy = st.builds(
    dsl::Transition,
)
dsl::State_strategy = st.builds(
    dsl::State,
    name=
        safe_text
)
dsl::Event_strategy = st.builds(
    dsl::Event,
    name=
        safe_text
)
dsl::StateMachine_strategy = st.builds(
    dsl::StateMachine,
)

@given(instance=dsl::Transition_strategy)
@settings(max_examples=50)
def test_dsl::transition_instantiation(instance):
    assert isinstance(instance, dsl::Transition)

@given(instance=dsl::State_strategy)
@settings(max_examples=50)
def test_dsl::state_instantiation(instance):
    assert isinstance(instance, dsl::State)

@given(instance=dsl::State_strategy)
def test_dsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::State_strategy)
def test_dsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Event_strategy)
@settings(max_examples=50)
def test_dsl::event_instantiation(instance):
    assert isinstance(instance, dsl::Event)

@given(instance=dsl::Event_strategy)
def test_dsl::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Event_strategy)
def test_dsl::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::StateMachine_strategy)
@settings(max_examples=50)
def test_dsl::statemachine_instantiation(instance):
    assert isinstance(instance, dsl::StateMachine)
