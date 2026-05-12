import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplefsm_Transition,
    simplefsm_State,
    simplefsm_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplefsm_transition_is_not_abstract():
    assert not inspect.isabstract(simplefsm_Transition)


def test_simplefsm_transition_constructor_exists():
    assert callable(simplefsm_Transition.__init__)


def test_simplefsm_transition_constructor_args():
    sig = inspect.signature(simplefsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_simplefsm_state_is_not_abstract():
    assert not inspect.isabstract(simplefsm_State)


def test_simplefsm_state_constructor_exists():
    assert callable(simplefsm_State.__init__)


def test_simplefsm_state_constructor_args():
    sig = inspect.signature(simplefsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplefsm_state_has_name():
    assert hasattr(simplefsm_State, "name")
    descriptor = None
    for klass in simplefsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplefsm_fsm_is_not_abstract():
    assert not inspect.isabstract(simplefsm_FSM)


def test_simplefsm_fsm_constructor_exists():
    assert callable(simplefsm_FSM.__init__)


def test_simplefsm_fsm_constructor_args():
    sig = inspect.signature(simplefsm_FSM.__init__)
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
simplefsm_Transition_strategy = st.builds(
    simplefsm_Transition,
)
simplefsm_State_strategy = st.builds(
    simplefsm_State,
    name=
        safe_text
)
simplefsm_FSM_strategy = st.builds(
    simplefsm_FSM,
)

@given(instance=simplefsm_Transition_strategy)
@settings(max_examples=50)
def test_simplefsm_transition_instantiation(instance):
    assert isinstance(instance, simplefsm_Transition)

@given(instance=simplefsm_State_strategy)
@settings(max_examples=50)
def test_simplefsm_state_instantiation(instance):
    assert isinstance(instance, simplefsm_State)



@given(instance=simplefsm_State_strategy)
def test_simplefsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplefsm_FSM_strategy)
@settings(max_examples=50)
def test_simplefsm_fsm_instantiation(instance):
    assert isinstance(instance, simplefsm_FSM)
