import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StateMachine::StateMachine,
    StateVertex,
    StateMachine::SimpleState,
    StateMachine::FinalState,
    StateMachine::InitialState,
    StateMachine::Event,
    StateMachine::Transition,
    StateMachine::StateVertex,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(StateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(StateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::simplestate_is_not_abstract():
    assert not inspect.isabstract(StateMachine::SimpleState)


def test_statemachine::simplestate_constructor_exists():
    assert callable(StateMachine::SimpleState.__init__)


def test_statemachine::simplestate_constructor_args():
    sig = inspect.signature(StateMachine::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine::FinalState)


def test_statemachine::finalstate_constructor_exists():
    assert callable(StateMachine::FinalState.__init__)


def test_statemachine::finalstate_constructor_args():
    sig = inspect.signature(StateMachine::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::initialstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine::InitialState)


def test_statemachine::initialstate_constructor_exists():
    assert callable(StateMachine::InitialState.__init__)


def test_statemachine::initialstate_constructor_args():
    sig = inspect.signature(StateMachine::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(StateMachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(StateMachine::Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(StateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(StateMachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::transition_has_name():
    assert hasattr(StateMachine::Transition, "name")
    descriptor = None
    for klass in StateMachine::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statevertex_is_not_abstract():
    assert not inspect.isabstract(StateMachine::StateVertex)


def test_statemachine::statevertex_constructor_exists():
    assert callable(StateMachine::StateVertex.__init__)


def test_statemachine::statevertex_constructor_args():
    sig = inspect.signature(StateMachine::StateVertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statevertex_has_name():
    assert hasattr(StateMachine::StateVertex, "name")
    descriptor = None
    for klass in StateMachine::StateVertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
StateMachine::StateMachine_strategy = st.builds(
    StateMachine::StateMachine,
)
StateVertex_strategy = st.builds(
    StateVertex,
)
StateMachine::SimpleState_strategy = st.builds(
    StateMachine::SimpleState,
)
StateMachine::FinalState_strategy = st.builds(
    StateMachine::FinalState,
)
StateMachine::InitialState_strategy = st.builds(
    StateMachine::InitialState,
)
StateMachine::Event_strategy = st.builds(
    StateMachine::Event,
)
StateMachine::Transition_strategy = st.builds(
    StateMachine::Transition,
    name=
        safe_text
)
StateMachine::StateVertex_strategy = st.builds(
    StateMachine::StateVertex,
    name=
        safe_text
)

@given(instance=StateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine::StateMachine)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=StateMachine::SimpleState_strategy)
@settings(max_examples=50)
def test_statemachine::simplestate_instantiation(instance):
    assert isinstance(instance, StateMachine::SimpleState)

@given(instance=StateMachine::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine::finalstate_instantiation(instance):
    assert isinstance(instance, StateMachine::FinalState)

@given(instance=StateMachine::InitialState_strategy)
@settings(max_examples=50)
def test_statemachine::initialstate_instantiation(instance):
    assert isinstance(instance, StateMachine::InitialState)

@given(instance=StateMachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, StateMachine::Event)

@given(instance=StateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, StateMachine::Transition)

@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine::StateVertex_strategy)
@settings(max_examples=50)
def test_statemachine::statevertex_instantiation(instance):
    assert isinstance(instance, StateMachine::StateVertex)

@given(instance=StateMachine::StateVertex_strategy)
def test_statemachine::statevertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::StateVertex_strategy)
def test_statemachine::statevertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
