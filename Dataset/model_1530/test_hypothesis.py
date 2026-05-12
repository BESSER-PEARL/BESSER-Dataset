import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tP1_EM_State,
    tP1_EM_Transition,
    tP1_EM_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tp1_em_state_is_not_abstract():
    assert not inspect.isabstract(tP1_EM_State)


def test_tp1_em_state_constructor_exists():
    assert callable(tP1_EM_State.__init__)


def test_tp1_em_state_constructor_args():
    sig = inspect.signature(tP1_EM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1_em_state_has_name():
    assert hasattr(tP1_EM_State, "name")
    descriptor = None
    for klass in tP1_EM_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1_em_transition_is_not_abstract():
    assert not inspect.isabstract(tP1_EM_Transition)


def test_tp1_em_transition_constructor_exists():
    assert callable(tP1_EM_Transition.__init__)


def test_tp1_em_transition_constructor_args():
    sig = inspect.signature(tP1_EM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1_em_transition_has_name():
    assert hasattr(tP1_EM_Transition, "name")
    descriptor = None
    for klass in tP1_EM_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1_em_statemachine_is_not_abstract():
    assert not inspect.isabstract(tP1_EM_StateMachine)


def test_tp1_em_statemachine_constructor_exists():
    assert callable(tP1_EM_StateMachine.__init__)


def test_tp1_em_statemachine_constructor_args():
    sig = inspect.signature(tP1_EM_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1_em_statemachine_has_name():
    assert hasattr(tP1_EM_StateMachine, "name")
    descriptor = None
    for klass in tP1_EM_StateMachine.__mro__:
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
tP1_EM_State_strategy = st.builds(
    tP1_EM_State,
    name=
        safe_text
)
tP1_EM_Transition_strategy = st.builds(
    tP1_EM_Transition,
    name=
        safe_text
)
tP1_EM_StateMachine_strategy = st.builds(
    tP1_EM_StateMachine,
    name=
        safe_text
)

@given(instance=tP1_EM_State_strategy)
@settings(max_examples=50)
def test_tp1_em_state_instantiation(instance):
    assert isinstance(instance, tP1_EM_State)



@given(instance=tP1_EM_State_strategy)
def test_tp1_em_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tP1_EM_Transition_strategy)
@settings(max_examples=50)
def test_tp1_em_transition_instantiation(instance):
    assert isinstance(instance, tP1_EM_Transition)



@given(instance=tP1_EM_Transition_strategy)
def test_tp1_em_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tP1_EM_StateMachine_strategy)
@settings(max_examples=50)
def test_tp1_em_statemachine_instantiation(instance):
    assert isinstance(instance, tP1_EM_StateMachine)



@given(instance=tP1_EM_StateMachine_strategy)
def test_tp1_em_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
