import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    tp01_FinalState,
    tp01_StartState,
    tp01_Transition,
    tp01_State,
    tp01_FSM,
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



def test_tp01_finalstate_is_not_abstract():
    assert not inspect.isabstract(tp01_FinalState)


def test_tp01_finalstate_constructor_exists():
    assert callable(tp01_FinalState.__init__)


def test_tp01_finalstate_constructor_args():
    sig = inspect.signature(tp01_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_tp01_startstate_is_not_abstract():
    assert not inspect.isabstract(tp01_StartState)


def test_tp01_startstate_constructor_exists():
    assert callable(tp01_StartState.__init__)


def test_tp01_startstate_constructor_args():
    sig = inspect.signature(tp01_StartState.__init__)
    params = list(sig.parameters.keys())



def test_tp01_transition_is_not_abstract():
    assert not inspect.isabstract(tp01_Transition)


def test_tp01_transition_constructor_exists():
    assert callable(tp01_Transition.__init__)


def test_tp01_transition_constructor_args():
    sig = inspect.signature(tp01_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp01_transition_has_name():
    assert hasattr(tp01_Transition, "name")
    descriptor = None
    for klass in tp01_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp01_state_is_not_abstract():
    assert not inspect.isabstract(tp01_State)


def test_tp01_state_constructor_exists():
    assert callable(tp01_State.__init__)


def test_tp01_state_constructor_args():
    sig = inspect.signature(tp01_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp01_state_has_name():
    assert hasattr(tp01_State, "name")
    descriptor = None
    for klass in tp01_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp01_fsm_is_not_abstract():
    assert not inspect.isabstract(tp01_FSM)


def test_tp01_fsm_constructor_exists():
    assert callable(tp01_FSM.__init__)


def test_tp01_fsm_constructor_args():
    sig = inspect.signature(tp01_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp01_fsm_has_name():
    assert hasattr(tp01_FSM, "name")
    descriptor = None
    for klass in tp01_FSM.__mro__:
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
tp01_FinalState_strategy = st.builds(
    tp01_FinalState,
)
tp01_StartState_strategy = st.builds(
    tp01_StartState,
)
tp01_Transition_strategy = st.builds(
    tp01_Transition,
    name=
        safe_text
)
tp01_State_strategy = st.builds(
    tp01_State,
    name=
        safe_text
)
tp01_FSM_strategy = st.builds(
    tp01_FSM,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=tp01_FinalState_strategy)
@settings(max_examples=50)
def test_tp01_finalstate_instantiation(instance):
    assert isinstance(instance, tp01_FinalState)

@given(instance=tp01_StartState_strategy)
@settings(max_examples=50)
def test_tp01_startstate_instantiation(instance):
    assert isinstance(instance, tp01_StartState)

@given(instance=tp01_Transition_strategy)
@settings(max_examples=50)
def test_tp01_transition_instantiation(instance):
    assert isinstance(instance, tp01_Transition)



@given(instance=tp01_Transition_strategy)
def test_tp01_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tp01_State_strategy)
@settings(max_examples=50)
def test_tp01_state_instantiation(instance):
    assert isinstance(instance, tp01_State)



@given(instance=tp01_State_strategy)
def test_tp01_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tp01_FSM_strategy)
@settings(max_examples=50)
def test_tp01_fsm_instantiation(instance):
    assert isinstance(instance, tp01_FSM)



@given(instance=tp01_FSM_strategy)
def test_tp01_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
