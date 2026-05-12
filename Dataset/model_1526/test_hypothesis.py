import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lab1_Transition,
    lab1_State,
    lab1_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lab1_transition_is_not_abstract():
    assert not inspect.isabstract(lab1_Transition)


def test_lab1_transition_constructor_exists():
    assert callable(lab1_Transition.__init__)


def test_lab1_transition_constructor_args():
    sig = inspect.signature(lab1_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lab1_transition_has_name():
    assert hasattr(lab1_Transition, "name")
    descriptor = None
    for klass in lab1_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lab1_state_is_not_abstract():
    assert not inspect.isabstract(lab1_State)


def test_lab1_state_constructor_exists():
    assert callable(lab1_State.__init__)


def test_lab1_state_constructor_args():
    sig = inspect.signature(lab1_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "init" in params, "Missing parameter 'init'"

def test_lab1_state_has_name():
    assert hasattr(lab1_State, "name")
    descriptor = None
    for klass in lab1_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_lab1_state_has_init():
    assert hasattr(lab1_State, "init")
    descriptor = None
    for klass in lab1_State.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)



def test_lab1_statemachine_is_not_abstract():
    assert not inspect.isabstract(lab1_StateMachine)


def test_lab1_statemachine_constructor_exists():
    assert callable(lab1_StateMachine.__init__)


def test_lab1_statemachine_constructor_args():
    sig = inspect.signature(lab1_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lab1_statemachine_has_name():
    assert hasattr(lab1_StateMachine, "name")
    descriptor = None
    for klass in lab1_StateMachine.__mro__:
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
lab1_Transition_strategy = st.builds(
    lab1_Transition,
    name=
        safe_text
)
lab1_State_strategy = st.builds(
    lab1_State,
    name=
        safe_text,
    init=
        st.booleans()
)
lab1_StateMachine_strategy = st.builds(
    lab1_StateMachine,
    name=
        safe_text
)

@given(instance=lab1_Transition_strategy)
@settings(max_examples=50)
def test_lab1_transition_instantiation(instance):
    assert isinstance(instance, lab1_Transition)



@given(instance=lab1_Transition_strategy)
def test_lab1_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lab1_State_strategy)
@settings(max_examples=50)
def test_lab1_state_instantiation(instance):
    assert isinstance(instance, lab1_State)



@given(instance=lab1_State_strategy)
def test_lab1_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=lab1_State_strategy)
def test_lab1_state_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original

@given(instance=lab1_StateMachine_strategy)
@settings(max_examples=50)
def test_lab1_statemachine_instantiation(instance):
    assert isinstance(instance, lab1_StateMachine)



@given(instance=lab1_StateMachine_strategy)
def test_lab1_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
