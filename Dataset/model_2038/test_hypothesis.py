import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    etatma_State,
    etatma_Transition,
    etatma_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_etatma_state_is_not_abstract():
    assert not inspect.isabstract(etatma_State)


def test_etatma_state_constructor_exists():
    assert callable(etatma_State.__init__)


def test_etatma_state_constructor_args():
    sig = inspect.signature(etatma_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_etatma_state_has_name():
    assert hasattr(etatma_State, "name")
    descriptor = None
    for klass in etatma_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etatma_transition_is_not_abstract():
    assert not inspect.isabstract(etatma_Transition)


def test_etatma_transition_constructor_exists():
    assert callable(etatma_Transition.__init__)


def test_etatma_transition_constructor_args():
    sig = inspect.signature(etatma_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_etatma_transition_has_name():
    assert hasattr(etatma_Transition, "name")
    descriptor = None
    for klass in etatma_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etatma_statemachine_is_not_abstract():
    assert not inspect.isabstract(etatma_StateMachine)


def test_etatma_statemachine_constructor_exists():
    assert callable(etatma_StateMachine.__init__)


def test_etatma_statemachine_constructor_args():
    sig = inspect.signature(etatma_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_etatma_statemachine_has_name():
    assert hasattr(etatma_StateMachine, "name")
    descriptor = None
    for klass in etatma_StateMachine.__mro__:
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
etatma_State_strategy = st.builds(
    etatma_State,
    name=
        safe_text
)
etatma_Transition_strategy = st.builds(
    etatma_Transition,
    name=
        safe_text
)
etatma_StateMachine_strategy = st.builds(
    etatma_StateMachine,
    name=
        safe_text
)

@given(instance=etatma_State_strategy)
@settings(max_examples=50)
def test_etatma_state_instantiation(instance):
    assert isinstance(instance, etatma_State)



@given(instance=etatma_State_strategy)
def test_etatma_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=etatma_Transition_strategy)
@settings(max_examples=50)
def test_etatma_transition_instantiation(instance):
    assert isinstance(instance, etatma_Transition)



@given(instance=etatma_Transition_strategy)
def test_etatma_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=etatma_StateMachine_strategy)
@settings(max_examples=50)
def test_etatma_statemachine_instantiation(instance):
    assert isinstance(instance, etatma_StateMachine)



@given(instance=etatma_StateMachine_strategy)
def test_etatma_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
