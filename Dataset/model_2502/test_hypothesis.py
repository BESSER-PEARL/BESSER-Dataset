import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tfsm_Guard,
    Transition,
    tfsm_Transition,
    State,
    tfsm_State,
    FSM,
    tfsm_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tfsm_guard_is_not_abstract():
    assert not inspect.isabstract(tfsm_Guard)


def test_tfsm_guard_constructor_exists():
    assert callable(tfsm_Guard.__init__)


def test_tfsm_guard_constructor_args():
    sig = inspect.signature(tfsm_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_tfsm_guard_has_time():
    assert hasattr(tfsm_Guard, "time")
    descriptor = None
    for klass in tfsm_Guard.__mro__:
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



def test_tfsm_transition_is_not_abstract():
    assert not inspect.isabstract(tfsm_Transition)


def test_tfsm_transition_constructor_exists():
    assert callable(tfsm_Transition.__init__)


def test_tfsm_transition_constructor_args():
    sig = inspect.signature(tfsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_state_is_not_abstract():
    assert not inspect.isabstract(tfsm_State)


def test_tfsm_state_constructor_exists():
    assert callable(tfsm_State.__init__)


def test_tfsm_state_constructor_args():
    sig = inspect.signature(tfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_tfsm_state_has_time():
    assert hasattr(tfsm_State, "time")
    descriptor = None
    for klass in tfsm_State.__mro__:
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



def test_tfsm_fsm_is_not_abstract():
    assert not inspect.isabstract(tfsm_FSM)


def test_tfsm_fsm_constructor_exists():
    assert callable(tfsm_FSM.__init__)


def test_tfsm_fsm_constructor_args():
    sig = inspect.signature(tfsm_FSM.__init__)
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
tfsm_Guard_strategy = st.builds(
    tfsm_Guard,
    time=
        st.integers()
)
Transition_strategy = st.builds(
    Transition,
)
tfsm_Transition_strategy = st.builds(
    tfsm_Transition,
)
State_strategy = st.builds(
    State,
)
tfsm_State_strategy = st.builds(
    tfsm_State,
    time=
        st.integers()
)
FSM_strategy = st.builds(
    FSM,
)
tfsm_FSM_strategy = st.builds(
    tfsm_FSM,
)

@given(instance=tfsm_Guard_strategy)
@settings(max_examples=50)
def test_tfsm_guard_instantiation(instance):
    assert isinstance(instance, tfsm_Guard)



@given(instance=tfsm_Guard_strategy)
def test_tfsm_guard_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=tfsm_Transition_strategy)
@settings(max_examples=50)
def test_tfsm_transition_instantiation(instance):
    assert isinstance(instance, tfsm_Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=tfsm_State_strategy)
@settings(max_examples=50)
def test_tfsm_state_instantiation(instance):
    assert isinstance(instance, tfsm_State)



@given(instance=tfsm_State_strategy)
def test_tfsm_state_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=tfsm_FSM_strategy)
@settings(max_examples=50)
def test_tfsm_fsm_instantiation(instance):
    assert isinstance(instance, tfsm_FSM)
