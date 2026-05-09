import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StateVertex,
    StateMachineUnnamed::SimpleState,
    StateMachineUnnamed::FinalState,
    StateMachineUnnamed::InitialState,
    StateMachineUnnamed::Event,
    StateMachineUnnamed::Transition,
    StateMachineUnnamed::StateVertex,
    StateMachineUnnamed::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachineunnamed::simplestate_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed::SimpleState)


def test_statemachineunnamed::simplestate_constructor_exists():
    assert callable(StateMachineUnnamed::SimpleState.__init__)


def test_statemachineunnamed::simplestate_constructor_args():
    sig = inspect.signature(StateMachineUnnamed::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_statemachineunnamed::finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed::FinalState)


def test_statemachineunnamed::finalstate_constructor_exists():
    assert callable(StateMachineUnnamed::FinalState.__init__)


def test_statemachineunnamed::finalstate_constructor_args():
    sig = inspect.signature(StateMachineUnnamed::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachineunnamed::initialstate_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed::InitialState)


def test_statemachineunnamed::initialstate_constructor_exists():
    assert callable(StateMachineUnnamed::InitialState.__init__)


def test_statemachineunnamed::initialstate_constructor_args():
    sig = inspect.signature(StateMachineUnnamed::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachineunnamed::event_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed::Event)


def test_statemachineunnamed::event_constructor_exists():
    assert callable(StateMachineUnnamed::Event.__init__)


def test_statemachineunnamed::event_constructor_args():
    sig = inspect.signature(StateMachineUnnamed::Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachineunnamed::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed::Transition)


def test_statemachineunnamed::transition_constructor_exists():
    assert callable(StateMachineUnnamed::Transition.__init__)


def test_statemachineunnamed::transition_constructor_args():
    sig = inspect.signature(StateMachineUnnamed::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachineunnamed::transition_has_name():
    assert hasattr(StateMachineUnnamed::Transition, "name")
    descriptor = None
    for klass in StateMachineUnnamed::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachineunnamed::statevertex_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed::StateVertex)


def test_statemachineunnamed::statevertex_constructor_exists():
    assert callable(StateMachineUnnamed::StateVertex.__init__)


def test_statemachineunnamed::statevertex_constructor_args():
    sig = inspect.signature(StateMachineUnnamed::StateVertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachineunnamed::statevertex_has_name():
    assert hasattr(StateMachineUnnamed::StateVertex, "name")
    descriptor = None
    for klass in StateMachineUnnamed::StateVertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachineunnamed::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed::StateMachine)


def test_statemachineunnamed::statemachine_constructor_exists():
    assert callable(StateMachineUnnamed::StateMachine.__init__)


def test_statemachineunnamed::statemachine_constructor_args():
    sig = inspect.signature(StateMachineUnnamed::StateMachine.__init__)
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
StateVertex_strategy = st.builds(
    StateVertex,
)
StateMachineUnnamed::SimpleState_strategy = st.builds(
    StateMachineUnnamed::SimpleState,
)
StateMachineUnnamed::FinalState_strategy = st.builds(
    StateMachineUnnamed::FinalState,
)
StateMachineUnnamed::InitialState_strategy = st.builds(
    StateMachineUnnamed::InitialState,
)
StateMachineUnnamed::Event_strategy = st.builds(
    StateMachineUnnamed::Event,
)
StateMachineUnnamed::Transition_strategy = st.builds(
    StateMachineUnnamed::Transition,
    name=
        safe_text
)
StateMachineUnnamed::StateVertex_strategy = st.builds(
    StateMachineUnnamed::StateVertex,
    name=
        safe_text
)
StateMachineUnnamed::StateMachine_strategy = st.builds(
    StateMachineUnnamed::StateMachine,
)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=StateMachineUnnamed::SimpleState_strategy)
@settings(max_examples=50)
def test_statemachineunnamed::simplestate_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed::SimpleState)

@given(instance=StateMachineUnnamed::FinalState_strategy)
@settings(max_examples=50)
def test_statemachineunnamed::finalstate_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed::FinalState)

@given(instance=StateMachineUnnamed::InitialState_strategy)
@settings(max_examples=50)
def test_statemachineunnamed::initialstate_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed::InitialState)

@given(instance=StateMachineUnnamed::Event_strategy)
@settings(max_examples=50)
def test_statemachineunnamed::event_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed::Event)

@given(instance=StateMachineUnnamed::Transition_strategy)
@settings(max_examples=50)
def test_statemachineunnamed::transition_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed::Transition)

@given(instance=StateMachineUnnamed::Transition_strategy)
def test_statemachineunnamed::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineUnnamed::Transition_strategy)
def test_statemachineunnamed::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineUnnamed::StateVertex_strategy)
@settings(max_examples=50)
def test_statemachineunnamed::statevertex_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed::StateVertex)

@given(instance=StateMachineUnnamed::StateVertex_strategy)
def test_statemachineunnamed::statevertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineUnnamed::StateVertex_strategy)
def test_statemachineunnamed::statevertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineUnnamed::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachineunnamed::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed::StateMachine)
