import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tfsm::Guard,
    Transition,
    tfsm::Transition,
    State,
    tfsm::State,
    FSM,
    tfsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tfsm::guard_is_not_abstract():
    assert not inspect.isabstract(tfsm::Guard)


def test_tfsm::guard_constructor_exists():
    assert callable(tfsm::Guard.__init__)


def test_tfsm::guard_constructor_args():
    sig = inspect.signature(tfsm::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_tfsm::guard_has_time():
    assert hasattr(tfsm::Guard, "time")
    descriptor = None
    for klass in tfsm::Guard.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::transition_is_not_abstract():
    assert not inspect.isabstract(tfsm::Transition)


def test_tfsm::transition_constructor_exists():
    assert callable(tfsm::Transition.__init__)


def test_tfsm::transition_constructor_args():
    sig = inspect.signature(tfsm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::state_is_not_abstract():
    assert not inspect.isabstract(tfsm::State)


def test_tfsm::state_constructor_exists():
    assert callable(tfsm::State.__init__)


def test_tfsm::state_constructor_args():
    sig = inspect.signature(tfsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_tfsm::state_has_time():
    assert hasattr(tfsm::State, "time")
    descriptor = None
    for klass in tfsm::State.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::fsm_is_not_abstract():
    assert not inspect.isabstract(tfsm::FSM)


def test_tfsm::fsm_constructor_exists():
    assert callable(tfsm::FSM.__init__)


def test_tfsm::fsm_constructor_args():
    sig = inspect.signature(tfsm::FSM.__init__)
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
tfsm::Guard_strategy = st.builds(
    tfsm::Guard,
    time=
        st.integers()
)
Transition_strategy = st.builds(
    Transition,
)
tfsm::Transition_strategy = st.builds(
    tfsm::Transition,
)
State_strategy = st.builds(
    State,
)
tfsm::State_strategy = st.builds(
    tfsm::State,
    time=
        st.integers()
)
FSM_strategy = st.builds(
    FSM,
)
tfsm::FSM_strategy = st.builds(
    tfsm::FSM,
)

@given(instance=tfsm::Guard_strategy)
@settings(max_examples=50)
def test_tfsm::guard_instantiation(instance):
    assert isinstance(instance, tfsm::Guard)

@given(instance=tfsm::Guard_strategy)
def test_tfsm::guard_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=tfsm::Guard_strategy)
def test_tfsm::guard_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=tfsm::Transition_strategy)
@settings(max_examples=50)
def test_tfsm::transition_instantiation(instance):
    assert isinstance(instance, tfsm::Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=tfsm::State_strategy)
@settings(max_examples=50)
def test_tfsm::state_instantiation(instance):
    assert isinstance(instance, tfsm::State)

@given(instance=tfsm::State_strategy)
def test_tfsm::state_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=tfsm::State_strategy)
def test_tfsm::state_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=tfsm::FSM_strategy)
@settings(max_examples=50)
def test_tfsm::fsm_instantiation(instance):
    assert isinstance(instance, tfsm::FSM)
