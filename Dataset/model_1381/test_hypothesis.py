import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachine::Transition,
    statemachine::State,
    statemachine::FSM,
    State,
    statemachine::Final,
    statemachine::Initial,
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



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_statemachine::state_has_time():
    assert hasattr(statemachine::State, "time")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::fsm_is_not_abstract():
    assert not inspect.isabstract(statemachine::FSM)


def test_statemachine::fsm_constructor_exists():
    assert callable(statemachine::FSM.__init__)


def test_statemachine::fsm_constructor_args():
    sig = inspect.signature(statemachine::FSM.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::final_is_not_abstract():
    assert not inspect.isabstract(statemachine::Final)


def test_statemachine::final_constructor_exists():
    assert callable(statemachine::Final.__init__)


def test_statemachine::final_constructor_args():
    sig = inspect.signature(statemachine::Final.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::initial_is_not_abstract():
    assert not inspect.isabstract(statemachine::Initial)


def test_statemachine::initial_constructor_exists():
    assert callable(statemachine::Initial.__init__)


def test_statemachine::initial_constructor_args():
    sig = inspect.signature(statemachine::Initial.__init__)
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
)
statemachine::State_strategy = st.builds(
    statemachine::State,
    time=
        safe_text
)
statemachine::FSM_strategy = st.builds(
    statemachine::FSM,
)
State_strategy = st.builds(
    State,
)
statemachine::Final_strategy = st.builds(
    statemachine::Final,
)
statemachine::Initial_strategy = st.builds(
    statemachine::Initial,
)

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::State_strategy)
def test_statemachine::state_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=statemachine::FSM_strategy)
@settings(max_examples=50)
def test_statemachine::fsm_instantiation(instance):
    assert isinstance(instance, statemachine::FSM)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine::Final_strategy)
@settings(max_examples=50)
def test_statemachine::final_instantiation(instance):
    assert isinstance(instance, statemachine::Final)

@given(instance=statemachine::Initial_strategy)
@settings(max_examples=50)
def test_statemachine::initial_instantiation(instance):
    assert isinstance(instance, statemachine::Initial)
