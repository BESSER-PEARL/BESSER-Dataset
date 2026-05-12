import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stateMachine_Condition,
    stateMachine_Transition,
    stateMachine_State,
    stateMachine_Event,
    stateMachine_StateMachine,
    stateMachine_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_condition_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Condition)


def test_statemachine_condition_constructor_exists():
    assert callable(stateMachine_Condition.__init__)


def test_statemachine_condition_constructor_args():
    sig = inspect.signature(stateMachine_Condition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(stateMachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(stateMachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(stateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(stateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(stateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_state_has_name():
    assert hasattr(stateMachine_State, "name")
    descriptor = None
    for klass in stateMachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(stateMachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(stateMachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_event_has_name():
    assert hasattr(stateMachine_Event, "name")
    descriptor = None
    for klass in stateMachine_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(stateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(stateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statemachine_has_name():
    assert hasattr(stateMachine_StateMachine, "name")
    descriptor = None
    for klass in stateMachine_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_model_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Model)


def test_statemachine_model_constructor_exists():
    assert callable(stateMachine_Model.__init__)


def test_statemachine_model_constructor_args():
    sig = inspect.signature(stateMachine_Model.__init__)
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
stateMachine_Condition_strategy = st.builds(
    stateMachine_Condition,
)
stateMachine_Transition_strategy = st.builds(
    stateMachine_Transition,
)
stateMachine_State_strategy = st.builds(
    stateMachine_State,
    name=
        safe_text
)
stateMachine_Event_strategy = st.builds(
    stateMachine_Event,
    name=
        safe_text
)
stateMachine_StateMachine_strategy = st.builds(
    stateMachine_StateMachine,
    name=
        safe_text
)
stateMachine_Model_strategy = st.builds(
    stateMachine_Model,
)

@given(instance=stateMachine_Condition_strategy)
@settings(max_examples=50)
def test_statemachine_condition_instantiation(instance):
    assert isinstance(instance, stateMachine_Condition)

@given(instance=stateMachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, stateMachine_Transition)

@given(instance=stateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, stateMachine_State)



@given(instance=stateMachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, stateMachine_Event)



@given(instance=stateMachine_Event_strategy)
def test_statemachine_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine_StateMachine)



@given(instance=stateMachine_StateMachine_strategy)
def test_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_Model_strategy)
@settings(max_examples=50)
def test_statemachine_model_instantiation(instance):
    assert isinstance(instance, stateMachine_Model)
