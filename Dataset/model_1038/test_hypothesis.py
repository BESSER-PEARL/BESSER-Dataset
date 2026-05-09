import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    finalStateMachine::State,
    finalStateMachine::Transition,
    finalStateMachine::FSM,
    State,
    finalStateMachine::InitialState,
    finalStateMachine::FinalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_finalstatemachine::state_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine::State)


def test_finalstatemachine::state_constructor_exists():
    assert callable(finalStateMachine::State.__init__)


def test_finalstatemachine::state_constructor_args():
    sig = inspect.signature(finalStateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_finalstatemachine::state_has_name():
    assert hasattr(finalStateMachine::State, "name")
    descriptor = None
    for klass in finalStateMachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_finalstatemachine::transition_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine::Transition)


def test_finalstatemachine::transition_constructor_exists():
    assert callable(finalStateMachine::Transition.__init__)


def test_finalstatemachine::transition_constructor_args():
    sig = inspect.signature(finalStateMachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_finalstatemachine::transition_has_name():
    assert hasattr(finalStateMachine::Transition, "name")
    descriptor = None
    for klass in finalStateMachine::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_finalstatemachine::fsm_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine::FSM)


def test_finalstatemachine::fsm_constructor_exists():
    assert callable(finalStateMachine::FSM.__init__)


def test_finalstatemachine::fsm_constructor_args():
    sig = inspect.signature(finalStateMachine::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_finalstatemachine::fsm_has_name():
    assert hasattr(finalStateMachine::FSM, "name")
    descriptor = None
    for klass in finalStateMachine::FSM.__mro__:
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



def test_finalstatemachine::initialstate_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine::InitialState)


def test_finalstatemachine::initialstate_constructor_exists():
    assert callable(finalStateMachine::InitialState.__init__)


def test_finalstatemachine::initialstate_constructor_args():
    sig = inspect.signature(finalStateMachine::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_finalstatemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(finalStateMachine::FinalState)


def test_finalstatemachine::finalstate_constructor_exists():
    assert callable(finalStateMachine::FinalState.__init__)


def test_finalstatemachine::finalstate_constructor_args():
    sig = inspect.signature(finalStateMachine::FinalState.__init__)
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
finalStateMachine::State_strategy = st.builds(
    finalStateMachine::State,
    name=
        safe_text
)
finalStateMachine::Transition_strategy = st.builds(
    finalStateMachine::Transition,
    name=
        safe_text
)
finalStateMachine::FSM_strategy = st.builds(
    finalStateMachine::FSM,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
finalStateMachine::InitialState_strategy = st.builds(
    finalStateMachine::InitialState,
)
finalStateMachine::FinalState_strategy = st.builds(
    finalStateMachine::FinalState,
)

@given(instance=finalStateMachine::State_strategy)
@settings(max_examples=50)
def test_finalstatemachine::state_instantiation(instance):
    assert isinstance(instance, finalStateMachine::State)

@given(instance=finalStateMachine::State_strategy)
def test_finalstatemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=finalStateMachine::State_strategy)
def test_finalstatemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=finalStateMachine::Transition_strategy)
@settings(max_examples=50)
def test_finalstatemachine::transition_instantiation(instance):
    assert isinstance(instance, finalStateMachine::Transition)

@given(instance=finalStateMachine::Transition_strategy)
def test_finalstatemachine::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=finalStateMachine::Transition_strategy)
def test_finalstatemachine::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=finalStateMachine::FSM_strategy)
@settings(max_examples=50)
def test_finalstatemachine::fsm_instantiation(instance):
    assert isinstance(instance, finalStateMachine::FSM)

@given(instance=finalStateMachine::FSM_strategy)
def test_finalstatemachine::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=finalStateMachine::FSM_strategy)
def test_finalstatemachine::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=finalStateMachine::InitialState_strategy)
@settings(max_examples=50)
def test_finalstatemachine::initialstate_instantiation(instance):
    assert isinstance(instance, finalStateMachine::InitialState)

@given(instance=finalStateMachine::FinalState_strategy)
@settings(max_examples=50)
def test_finalstatemachine::finalstate_instantiation(instance):
    assert isinstance(instance, finalStateMachine::FinalState)
