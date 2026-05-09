import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachine::Event,
    statemachine::Transition,
    statemachine::State,
    statemachine::SM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(statemachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(statemachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(statemachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine::event_has_id():
    assert hasattr(statemachine::Event, "id")
    descriptor = None
    for klass in statemachine::Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine::state_has_id():
    assert hasattr(statemachine::State, "id")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::sm_is_not_abstract():
    assert not inspect.isabstract(statemachine::SM)


def test_statemachine::sm_constructor_exists():
    assert callable(statemachine::SM.__init__)


def test_statemachine::sm_constructor_args():
    sig = inspect.signature(statemachine::SM.__init__)
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
statemachine::Event_strategy = st.builds(
    statemachine::Event,
    id=
        safe_text
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
)
statemachine::State_strategy = st.builds(
    statemachine::State,
    id=
        safe_text
)
statemachine::SM_strategy = st.builds(
    statemachine::SM,
)

@given(instance=statemachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, statemachine::Event)

@given(instance=statemachine::Event_strategy)
def test_statemachine::event_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=statemachine::Event_strategy)
def test_statemachine::event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::State_strategy)
def test_statemachine::state_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine::SM_strategy)
@settings(max_examples=50)
def test_statemachine::sm_instantiation(instance):
    assert isinstance(instance, statemachine::SM)
