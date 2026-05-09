import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    fMS::FinalState,
    fMS::InitState,
    fMS::Transition,
    fMS::State,
    fMS::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fms::finalstate_is_not_abstract():
    assert not inspect.isabstract(fMS::FinalState)


def test_fms::finalstate_constructor_exists():
    assert callable(fMS::FinalState.__init__)


def test_fms::finalstate_constructor_args():
    sig = inspect.signature(fMS::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_fms::initstate_is_not_abstract():
    assert not inspect.isabstract(fMS::InitState)


def test_fms::initstate_constructor_exists():
    assert callable(fMS::InitState.__init__)


def test_fms::initstate_constructor_args():
    sig = inspect.signature(fMS::InitState.__init__)
    params = list(sig.parameters.keys())



def test_fms::transition_is_not_abstract():
    assert not inspect.isabstract(fMS::Transition)


def test_fms::transition_constructor_exists():
    assert callable(fMS::Transition.__init__)


def test_fms::transition_constructor_args():
    sig = inspect.signature(fMS::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fms::transition_has_name():
    assert hasattr(fMS::Transition, "name")
    descriptor = None
    for klass in fMS::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fms::state_is_not_abstract():
    assert not inspect.isabstract(fMS::State)


def test_fms::state_constructor_exists():
    assert callable(fMS::State.__init__)


def test_fms::state_constructor_args():
    sig = inspect.signature(fMS::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fms::state_has_name():
    assert hasattr(fMS::State, "name")
    descriptor = None
    for klass in fMS::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fms::fsm_is_not_abstract():
    assert not inspect.isabstract(fMS::FSM)


def test_fms::fsm_constructor_exists():
    assert callable(fMS::FSM.__init__)


def test_fms::fsm_constructor_args():
    sig = inspect.signature(fMS::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fms::fsm_has_name():
    assert hasattr(fMS::FSM, "name")
    descriptor = None
    for klass in fMS::FSM.__mro__:
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
State_strategy = st.builds(
    State,
)
fMS::FinalState_strategy = st.builds(
    fMS::FinalState,
)
fMS::InitState_strategy = st.builds(
    fMS::InitState,
)
fMS::Transition_strategy = st.builds(
    fMS::Transition,
    name=
        safe_text
)
fMS::State_strategy = st.builds(
    fMS::State,
    name=
        safe_text
)
fMS::FSM_strategy = st.builds(
    fMS::FSM,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fMS::FinalState_strategy)
@settings(max_examples=50)
def test_fms::finalstate_instantiation(instance):
    assert isinstance(instance, fMS::FinalState)

@given(instance=fMS::InitState_strategy)
@settings(max_examples=50)
def test_fms::initstate_instantiation(instance):
    assert isinstance(instance, fMS::InitState)

@given(instance=fMS::Transition_strategy)
@settings(max_examples=50)
def test_fms::transition_instantiation(instance):
    assert isinstance(instance, fMS::Transition)

@given(instance=fMS::Transition_strategy)
def test_fms::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fMS::Transition_strategy)
def test_fms::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fMS::State_strategy)
@settings(max_examples=50)
def test_fms::state_instantiation(instance):
    assert isinstance(instance, fMS::State)

@given(instance=fMS::State_strategy)
def test_fms::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fMS::State_strategy)
def test_fms::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fMS::FSM_strategy)
@settings(max_examples=50)
def test_fms::fsm_instantiation(instance):
    assert isinstance(instance, fMS::FSM)

@given(instance=fMS::FSM_strategy)
def test_fms::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fMS::FSM_strategy)
def test_fms::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
