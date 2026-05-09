import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    minifsm::Transition,
    minifsm::State,
    State,
    minifsm::FinalState,
    minifsm::Machine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minifsm::transition_is_not_abstract():
    assert not inspect.isabstract(minifsm::Transition)


def test_minifsm::transition_constructor_exists():
    assert callable(minifsm::Transition.__init__)


def test_minifsm::transition_constructor_args():
    sig = inspect.signature(minifsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_minifsm::transition_has_event():
    assert hasattr(minifsm::Transition, "event")
    descriptor = None
    for klass in minifsm::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_minifsm::state_is_not_abstract():
    assert not inspect.isabstract(minifsm::State)


def test_minifsm::state_constructor_exists():
    assert callable(minifsm::State.__init__)


def test_minifsm::state_constructor_args():
    sig = inspect.signature(minifsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minifsm::state_has_name():
    assert hasattr(minifsm::State, "name")
    descriptor = None
    for klass in minifsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_minifsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(minifsm::FinalState)


def test_minifsm::finalstate_constructor_exists():
    assert callable(minifsm::FinalState.__init__)


def test_minifsm::finalstate_constructor_args():
    sig = inspect.signature(minifsm::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_minifsm::machine_is_not_abstract():
    assert not inspect.isabstract(minifsm::Machine)


def test_minifsm::machine_constructor_exists():
    assert callable(minifsm::Machine.__init__)


def test_minifsm::machine_constructor_args():
    sig = inspect.signature(minifsm::Machine.__init__)
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
minifsm::Transition_strategy = st.builds(
    minifsm::Transition,
    event=
        safe_text
)
minifsm::State_strategy = st.builds(
    minifsm::State,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
minifsm::FinalState_strategy = st.builds(
    minifsm::FinalState,
)
minifsm::Machine_strategy = st.builds(
    minifsm::Machine,
)

@given(instance=minifsm::Transition_strategy)
@settings(max_examples=50)
def test_minifsm::transition_instantiation(instance):
    assert isinstance(instance, minifsm::Transition)

@given(instance=minifsm::Transition_strategy)
def test_minifsm::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=minifsm::Transition_strategy)
def test_minifsm::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=minifsm::State_strategy)
@settings(max_examples=50)
def test_minifsm::state_instantiation(instance):
    assert isinstance(instance, minifsm::State)

@given(instance=minifsm::State_strategy)
def test_minifsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minifsm::State_strategy)
def test_minifsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=minifsm::FinalState_strategy)
@settings(max_examples=50)
def test_minifsm::finalstate_instantiation(instance):
    assert isinstance(instance, minifsm::FinalState)

@given(instance=minifsm::Machine_strategy)
@settings(max_examples=50)
def test_minifsm::machine_instantiation(instance):
    assert isinstance(instance, minifsm::Machine)
