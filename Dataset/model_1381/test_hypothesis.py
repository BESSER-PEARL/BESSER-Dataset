import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    statemachine_Final,
    statemachine_Initial,
    statemachine_Transition,
    statemachine_State,
    statemachine_FSM,
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



def test_statemachine_final_is_not_abstract():
    assert not inspect.isabstract(statemachine_Final)


def test_statemachine_final_constructor_exists():
    assert callable(statemachine_Final.__init__)


def test_statemachine_final_constructor_args():
    sig = inspect.signature(statemachine_Final.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_initial_is_not_abstract():
    assert not inspect.isabstract(statemachine_Initial)


def test_statemachine_initial_constructor_exists():
    assert callable(statemachine_Initial.__init__)


def test_statemachine_initial_constructor_args():
    sig = inspect.signature(statemachine_Initial.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_statemachine_state_has_time():
    assert hasattr(statemachine_State, "time")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_fsm_is_not_abstract():
    assert not inspect.isabstract(statemachine_FSM)


def test_statemachine_fsm_constructor_exists():
    assert callable(statemachine_FSM.__init__)


def test_statemachine_fsm_constructor_args():
    sig = inspect.signature(statemachine_FSM.__init__)
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
State_strategy = st.builds(
    State,
)
statemachine_Final_strategy = st.builds(
    statemachine_Final,
)
statemachine_Initial_strategy = st.builds(
    statemachine_Initial,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    time=
        safe_text
)
statemachine_FSM_strategy = st.builds(
    statemachine_FSM,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine_Final_strategy)
@settings(max_examples=50)
def test_statemachine_final_instantiation(instance):
    assert isinstance(instance, statemachine_Final)

@given(instance=statemachine_Initial_strategy)
@settings(max_examples=50)
def test_statemachine_initial_instantiation(instance):
    assert isinstance(instance, statemachine_Initial)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=statemachine_FSM_strategy)
@settings(max_examples=50)
def test_statemachine_fsm_instantiation(instance):
    assert isinstance(instance, statemachine_FSM)
