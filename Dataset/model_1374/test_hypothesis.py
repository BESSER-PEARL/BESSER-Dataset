import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachines_Transition,
    statemachines_Event,
    statemachines_State,
    statemachines_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachines_transition_is_not_abstract():
    assert not inspect.isabstract(statemachines_Transition)


def test_statemachines_transition_constructor_exists():
    assert callable(statemachines_Transition.__init__)


def test_statemachines_transition_constructor_args():
    sig = inspect.signature(statemachines_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachines_event_is_not_abstract():
    assert not inspect.isabstract(statemachines_Event)


def test_statemachines_event_constructor_exists():
    assert callable(statemachines_Event.__init__)


def test_statemachines_event_constructor_args():
    sig = inspect.signature(statemachines_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_statemachines_event_has_name():
    assert hasattr(statemachines_Event, "name")
    descriptor = None
    for klass in statemachines_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachines_event_has_code():
    assert hasattr(statemachines_Event, "code")
    descriptor = None
    for klass in statemachines_Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_state_is_not_abstract():
    assert not inspect.isabstract(statemachines_State)


def test_statemachines_state_constructor_exists():
    assert callable(statemachines_State.__init__)


def test_statemachines_state_constructor_args():
    sig = inspect.signature(statemachines_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachines_state_has_name():
    assert hasattr(statemachines_State, "name")
    descriptor = None
    for klass in statemachines_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachines_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachines_StateMachine)


def test_statemachines_statemachine_constructor_exists():
    assert callable(statemachines_StateMachine.__init__)


def test_statemachines_statemachine_constructor_args():
    sig = inspect.signature(statemachines_StateMachine.__init__)
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
statemachines_Transition_strategy = st.builds(
    statemachines_Transition,
)
statemachines_Event_strategy = st.builds(
    statemachines_Event,
    name=
        safe_text,
    code=
        safe_text
)
statemachines_State_strategy = st.builds(
    statemachines_State,
    name=
        safe_text
)
statemachines_StateMachine_strategy = st.builds(
    statemachines_StateMachine,
)

@given(instance=statemachines_Transition_strategy)
@settings(max_examples=50)
def test_statemachines_transition_instantiation(instance):
    assert isinstance(instance, statemachines_Transition)

@given(instance=statemachines_Event_strategy)
@settings(max_examples=50)
def test_statemachines_event_instantiation(instance):
    assert isinstance(instance, statemachines_Event)



@given(instance=statemachines_Event_strategy)
def test_statemachines_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statemachines_Event_strategy)
def test_statemachines_event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachines_State_strategy)
@settings(max_examples=50)
def test_statemachines_state_instantiation(instance):
    assert isinstance(instance, statemachines_State)



@given(instance=statemachines_State_strategy)
def test_statemachines_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachines_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachines_statemachine_instantiation(instance):
    assert isinstance(instance, statemachines_StateMachine)
