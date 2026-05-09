import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachine::Transition,
    statemachine::State,
    statemachine::MyFSM,
    State,
    statemachine::FinalState,
    statemachine::InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::transition_has_name():
    assert hasattr(statemachine::Transition, "name")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
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



def test_statemachine::myfsm_is_not_abstract():
    assert not inspect.isabstract(statemachine::MyFSM)


def test_statemachine::myfsm_constructor_exists():
    assert callable(statemachine::MyFSM.__init__)


def test_statemachine::myfsm_constructor_args():
    sig = inspect.signature(statemachine::MyFSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::myfsm_has_name():
    assert hasattr(statemachine::MyFSM, "name")
    descriptor = None
    for klass in statemachine::MyFSM.__mro__:
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



def test_statemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::FinalState)


def test_statemachine::finalstate_constructor_exists():
    assert callable(statemachine::FinalState.__init__)


def test_statemachine::finalstate_constructor_args():
    sig = inspect.signature(statemachine::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::InitialState)


def test_statemachine::initialstate_constructor_exists():
    assert callable(statemachine::InitialState.__init__)


def test_statemachine::initialstate_constructor_args():
    sig = inspect.signature(statemachine::InitialState.__init__)
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
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
    name=
        safe_text
)
statemachine::State_strategy = st.builds(
    statemachine::State,
    name=
        safe_text
)
statemachine::MyFSM_strategy = st.builds(
    statemachine::MyFSM,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
statemachine::FinalState_strategy = st.builds(
    statemachine::FinalState,
)
statemachine::InitialState_strategy = st.builds(
    statemachine::InitialState,
)

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_name_setter(instance):
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

@given(instance=statemachine::MyFSM_strategy)
@settings(max_examples=50)
def test_statemachine::myfsm_instantiation(instance):
    assert isinstance(instance, statemachine::MyFSM)

@given(instance=statemachine::MyFSM_strategy)
def test_statemachine::myfsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::MyFSM_strategy)
def test_statemachine::myfsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine::finalstate_instantiation(instance):
    assert isinstance(instance, statemachine::FinalState)

@given(instance=statemachine::InitialState_strategy)
@settings(max_examples=50)
def test_statemachine::initialstate_instantiation(instance):
    assert isinstance(instance, statemachine::InitialState)
