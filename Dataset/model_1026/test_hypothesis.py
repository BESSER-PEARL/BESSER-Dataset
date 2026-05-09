import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    tp01::FinalState,
    tp01::StartState,
    tp01::Transition,
    tp01::State,
    tp01::FSM,
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



def test_tp01::finalstate_is_not_abstract():
    assert not inspect.isabstract(tp01::FinalState)


def test_tp01::finalstate_constructor_exists():
    assert callable(tp01::FinalState.__init__)


def test_tp01::finalstate_constructor_args():
    sig = inspect.signature(tp01::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_tp01::startstate_is_not_abstract():
    assert not inspect.isabstract(tp01::StartState)


def test_tp01::startstate_constructor_exists():
    assert callable(tp01::StartState.__init__)


def test_tp01::startstate_constructor_args():
    sig = inspect.signature(tp01::StartState.__init__)
    params = list(sig.parameters.keys())



def test_tp01::transition_is_not_abstract():
    assert not inspect.isabstract(tp01::Transition)


def test_tp01::transition_constructor_exists():
    assert callable(tp01::Transition.__init__)


def test_tp01::transition_constructor_args():
    sig = inspect.signature(tp01::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp01::transition_has_name():
    assert hasattr(tp01::Transition, "name")
    descriptor = None
    for klass in tp01::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp01::state_is_not_abstract():
    assert not inspect.isabstract(tp01::State)


def test_tp01::state_constructor_exists():
    assert callable(tp01::State.__init__)


def test_tp01::state_constructor_args():
    sig = inspect.signature(tp01::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp01::state_has_name():
    assert hasattr(tp01::State, "name")
    descriptor = None
    for klass in tp01::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp01::fsm_is_not_abstract():
    assert not inspect.isabstract(tp01::FSM)


def test_tp01::fsm_constructor_exists():
    assert callable(tp01::FSM.__init__)


def test_tp01::fsm_constructor_args():
    sig = inspect.signature(tp01::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp01::fsm_has_name():
    assert hasattr(tp01::FSM, "name")
    descriptor = None
    for klass in tp01::FSM.__mro__:
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
tp01::FinalState_strategy = st.builds(
    tp01::FinalState,
)
tp01::StartState_strategy = st.builds(
    tp01::StartState,
)
tp01::Transition_strategy = st.builds(
    tp01::Transition,
    name=
        safe_text
)
tp01::State_strategy = st.builds(
    tp01::State,
    name=
        safe_text
)
tp01::FSM_strategy = st.builds(
    tp01::FSM,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=tp01::FinalState_strategy)
@settings(max_examples=50)
def test_tp01::finalstate_instantiation(instance):
    assert isinstance(instance, tp01::FinalState)

@given(instance=tp01::StartState_strategy)
@settings(max_examples=50)
def test_tp01::startstate_instantiation(instance):
    assert isinstance(instance, tp01::StartState)

@given(instance=tp01::Transition_strategy)
@settings(max_examples=50)
def test_tp01::transition_instantiation(instance):
    assert isinstance(instance, tp01::Transition)

@given(instance=tp01::Transition_strategy)
def test_tp01::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tp01::Transition_strategy)
def test_tp01::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tp01::State_strategy)
@settings(max_examples=50)
def test_tp01::state_instantiation(instance):
    assert isinstance(instance, tp01::State)

@given(instance=tp01::State_strategy)
def test_tp01::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tp01::State_strategy)
def test_tp01::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tp01::FSM_strategy)
@settings(max_examples=50)
def test_tp01::fsm_instantiation(instance):
    assert isinstance(instance, tp01::FSM)

@given(instance=tp01::FSM_strategy)
def test_tp01::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tp01::FSM_strategy)
def test_tp01::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
