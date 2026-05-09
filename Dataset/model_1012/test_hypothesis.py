import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Transition,
    fsm::State,
    fsm::FSM,
    State,
    fsm::InitialState,
    fsm::FinalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::state_has_name():
    assert hasattr(fsm::State, "name")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fsm::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fsm::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::fsm_has_name():
    assert hasattr(fsm::FSM, "name")
    descriptor = None
    for klass in fsm::FSM.__mro__:
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



def test_fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm::InitialState)


def test_fsm::initialstate_constructor_exists():
    assert callable(fsm::InitialState.__init__)


def test_fsm::initialstate_constructor_args():
    sig = inspect.signature(fsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm::FinalState)


def test_fsm::finalstate_constructor_exists():
    assert callable(fsm::FinalState.__init__)


def test_fsm::finalstate_constructor_args():
    sig = inspect.signature(fsm::FinalState.__init__)
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
fsm::Transition_strategy = st.builds(
    fsm::Transition,
)
fsm::State_strategy = st.builds(
    fsm::State,
    name=
        safe_text
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm::InitialState_strategy = st.builds(
    fsm::InitialState,
)
fsm::FinalState_strategy = st.builds(
    fsm::FinalState,
)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fsm::FSM)

@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::initialstate_instantiation(instance):
    assert isinstance(instance, fsm::InitialState)

@given(instance=fsm::FinalState_strategy)
@settings(max_examples=50)
def test_fsm::finalstate_instantiation(instance):
    assert isinstance(instance, fsm::FinalState)
