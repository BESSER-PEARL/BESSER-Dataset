import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StateMachineHyperedges::Transition,
    StateMachineHyperedges::StateVertex,
    StateMachineHyperedges::StateMachine,
    StateVertex,
    StateMachineHyperedges::FinalState,
    StateMachineHyperedges::SimpleState,
    StateMachineHyperedges::InitialState,
    StateMachineHyperedges::Event,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachinehyperedges::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachineHyperedges::Transition)


def test_statemachinehyperedges::transition_constructor_exists():
    assert callable(StateMachineHyperedges::Transition.__init__)


def test_statemachinehyperedges::transition_constructor_args():
    sig = inspect.signature(StateMachineHyperedges::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinehyperedges::transition_has_name():
    assert hasattr(StateMachineHyperedges::Transition, "name")
    descriptor = None
    for klass in StateMachineHyperedges::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinehyperedges::statevertex_is_not_abstract():
    assert not inspect.isabstract(StateMachineHyperedges::StateVertex)


def test_statemachinehyperedges::statevertex_constructor_exists():
    assert callable(StateMachineHyperedges::StateVertex.__init__)


def test_statemachinehyperedges::statevertex_constructor_args():
    sig = inspect.signature(StateMachineHyperedges::StateVertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinehyperedges::statevertex_has_name():
    assert hasattr(StateMachineHyperedges::StateVertex, "name")
    descriptor = None
    for klass in StateMachineHyperedges::StateVertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinehyperedges::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachineHyperedges::StateMachine)


def test_statemachinehyperedges::statemachine_constructor_exists():
    assert callable(StateMachineHyperedges::StateMachine.__init__)


def test_statemachinehyperedges::statemachine_constructor_args():
    sig = inspect.signature(StateMachineHyperedges::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachinehyperedges::finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachineHyperedges::FinalState)


def test_statemachinehyperedges::finalstate_constructor_exists():
    assert callable(StateMachineHyperedges::FinalState.__init__)


def test_statemachinehyperedges::finalstate_constructor_args():
    sig = inspect.signature(StateMachineHyperedges::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachinehyperedges::simplestate_is_not_abstract():
    assert not inspect.isabstract(StateMachineHyperedges::SimpleState)


def test_statemachinehyperedges::simplestate_constructor_exists():
    assert callable(StateMachineHyperedges::SimpleState.__init__)


def test_statemachinehyperedges::simplestate_constructor_args():
    sig = inspect.signature(StateMachineHyperedges::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_statemachinehyperedges::initialstate_is_not_abstract():
    assert not inspect.isabstract(StateMachineHyperedges::InitialState)


def test_statemachinehyperedges::initialstate_constructor_exists():
    assert callable(StateMachineHyperedges::InitialState.__init__)


def test_statemachinehyperedges::initialstate_constructor_args():
    sig = inspect.signature(StateMachineHyperedges::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachinehyperedges::event_is_not_abstract():
    assert not inspect.isabstract(StateMachineHyperedges::Event)


def test_statemachinehyperedges::event_constructor_exists():
    assert callable(StateMachineHyperedges::Event.__init__)


def test_statemachinehyperedges::event_constructor_args():
    sig = inspect.signature(StateMachineHyperedges::Event.__init__)
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
StateMachineHyperedges::Transition_strategy = st.builds(
    StateMachineHyperedges::Transition,
    name=
        safe_text
)
StateMachineHyperedges::StateVertex_strategy = st.builds(
    StateMachineHyperedges::StateVertex,
    name=
        safe_text
)
StateMachineHyperedges::StateMachine_strategy = st.builds(
    StateMachineHyperedges::StateMachine,
)
StateVertex_strategy = st.builds(
    StateVertex,
)
StateMachineHyperedges::FinalState_strategy = st.builds(
    StateMachineHyperedges::FinalState,
)
StateMachineHyperedges::SimpleState_strategy = st.builds(
    StateMachineHyperedges::SimpleState,
)
StateMachineHyperedges::InitialState_strategy = st.builds(
    StateMachineHyperedges::InitialState,
)
StateMachineHyperedges::Event_strategy = st.builds(
    StateMachineHyperedges::Event,
)

@given(instance=StateMachineHyperedges::Transition_strategy)
@settings(max_examples=50)
def test_statemachinehyperedges::transition_instantiation(instance):
    assert isinstance(instance, StateMachineHyperedges::Transition)

@given(instance=StateMachineHyperedges::Transition_strategy)
def test_statemachinehyperedges::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineHyperedges::Transition_strategy)
def test_statemachinehyperedges::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineHyperedges::StateVertex_strategy)
@settings(max_examples=50)
def test_statemachinehyperedges::statevertex_instantiation(instance):
    assert isinstance(instance, StateMachineHyperedges::StateVertex)

@given(instance=StateMachineHyperedges::StateVertex_strategy)
def test_statemachinehyperedges::statevertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineHyperedges::StateVertex_strategy)
def test_statemachinehyperedges::statevertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineHyperedges::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachinehyperedges::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachineHyperedges::StateMachine)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=StateMachineHyperedges::FinalState_strategy)
@settings(max_examples=50)
def test_statemachinehyperedges::finalstate_instantiation(instance):
    assert isinstance(instance, StateMachineHyperedges::FinalState)

@given(instance=StateMachineHyperedges::SimpleState_strategy)
@settings(max_examples=50)
def test_statemachinehyperedges::simplestate_instantiation(instance):
    assert isinstance(instance, StateMachineHyperedges::SimpleState)

@given(instance=StateMachineHyperedges::InitialState_strategy)
@settings(max_examples=50)
def test_statemachinehyperedges::initialstate_instantiation(instance):
    assert isinstance(instance, StateMachineHyperedges::InitialState)

@given(instance=StateMachineHyperedges::Event_strategy)
@settings(max_examples=50)
def test_statemachinehyperedges::event_instantiation(instance):
    assert isinstance(instance, StateMachineHyperedges::Event)
