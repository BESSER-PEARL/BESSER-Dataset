import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    idm_Transition,
    idm_State,
    idm_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_idm_transition_is_not_abstract():
    assert not inspect.isabstract(idm_Transition)


def test_idm_transition_constructor_exists():
    assert callable(idm_Transition.__init__)


def test_idm_transition_constructor_args():
    sig = inspect.signature(idm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm_transition_has_name():
    assert hasattr(idm_Transition, "name")
    descriptor = None
    for klass in idm_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idm_state_is_not_abstract():
    assert not inspect.isabstract(idm_State)


def test_idm_state_constructor_exists():
    assert callable(idm_State.__init__)


def test_idm_state_constructor_args():
    sig = inspect.signature(idm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm_state_has_name():
    assert hasattr(idm_State, "name")
    descriptor = None
    for klass in idm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idm_statemachine_is_not_abstract():
    assert not inspect.isabstract(idm_StateMachine)


def test_idm_statemachine_constructor_exists():
    assert callable(idm_StateMachine.__init__)


def test_idm_statemachine_constructor_args():
    sig = inspect.signature(idm_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm_statemachine_has_name():
    assert hasattr(idm_StateMachine, "name")
    descriptor = None
    for klass in idm_StateMachine.__mro__:
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
idm_Transition_strategy = st.builds(
    idm_Transition,
    name=
        safe_text
)
idm_State_strategy = st.builds(
    idm_State,
    name=
        safe_text
)
idm_StateMachine_strategy = st.builds(
    idm_StateMachine,
    name=
        safe_text
)

@given(instance=idm_Transition_strategy)
@settings(max_examples=50)
def test_idm_transition_instantiation(instance):
    assert isinstance(instance, idm_Transition)



@given(instance=idm_Transition_strategy)
def test_idm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idm_State_strategy)
@settings(max_examples=50)
def test_idm_state_instantiation(instance):
    assert isinstance(instance, idm_State)



@given(instance=idm_State_strategy)
def test_idm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idm_StateMachine_strategy)
@settings(max_examples=50)
def test_idm_statemachine_instantiation(instance):
    assert isinstance(instance, idm_StateMachine)



@given(instance=idm_StateMachine_strategy)
def test_idm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
