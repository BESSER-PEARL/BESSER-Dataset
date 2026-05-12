import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    iDM_Test_Transition,
    iDM_Test_State,
    iDM_Test_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_idm_test_transition_is_not_abstract():
    assert not inspect.isabstract(iDM_Test_Transition)


def test_idm_test_transition_constructor_exists():
    assert callable(iDM_Test_Transition.__init__)


def test_idm_test_transition_constructor_args():
    sig = inspect.signature(iDM_Test_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm_test_transition_has_name():
    assert hasattr(iDM_Test_Transition, "name")
    descriptor = None
    for klass in iDM_Test_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idm_test_state_is_not_abstract():
    assert not inspect.isabstract(iDM_Test_State)


def test_idm_test_state_constructor_exists():
    assert callable(iDM_Test_State.__init__)


def test_idm_test_state_constructor_args():
    sig = inspect.signature(iDM_Test_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm_test_state_has_name():
    assert hasattr(iDM_Test_State, "name")
    descriptor = None
    for klass in iDM_Test_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idm_test_statemachine_is_not_abstract():
    assert not inspect.isabstract(iDM_Test_StateMachine)


def test_idm_test_statemachine_constructor_exists():
    assert callable(iDM_Test_StateMachine.__init__)


def test_idm_test_statemachine_constructor_args():
    sig = inspect.signature(iDM_Test_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm_test_statemachine_has_name():
    assert hasattr(iDM_Test_StateMachine, "name")
    descriptor = None
    for klass in iDM_Test_StateMachine.__mro__:
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
iDM_Test_Transition_strategy = st.builds(
    iDM_Test_Transition,
    name=
        safe_text
)
iDM_Test_State_strategy = st.builds(
    iDM_Test_State,
    name=
        safe_text
)
iDM_Test_StateMachine_strategy = st.builds(
    iDM_Test_StateMachine,
    name=
        safe_text
)

@given(instance=iDM_Test_Transition_strategy)
@settings(max_examples=50)
def test_idm_test_transition_instantiation(instance):
    assert isinstance(instance, iDM_Test_Transition)



@given(instance=iDM_Test_Transition_strategy)
def test_idm_test_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iDM_Test_State_strategy)
@settings(max_examples=50)
def test_idm_test_state_instantiation(instance):
    assert isinstance(instance, iDM_Test_State)



@given(instance=iDM_Test_State_strategy)
def test_idm_test_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iDM_Test_StateMachine_strategy)
@settings(max_examples=50)
def test_idm_test_statemachine_instantiation(instance):
    assert isinstance(instance, iDM_Test_StateMachine)



@given(instance=iDM_Test_StateMachine_strategy)
def test_idm_test_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
