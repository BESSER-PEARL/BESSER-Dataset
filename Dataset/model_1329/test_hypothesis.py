import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_mk2_Event,
    statemachine_mk2_Transition,
    statemachine_mk2_State,
    State,
    statemachine_mk2_Composite_state,
    statemachine_mk2_SimpleState,
    statemachine_mk2_Final_state,
    statemachine_mk2_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_mk2_event_is_not_abstract():
    assert not inspect.isabstract(statemachine_mk2_Event)


def test_statemachine_mk2_event_constructor_exists():
    assert callable(statemachine_mk2_Event.__init__)


def test_statemachine_mk2_event_constructor_args():
    sig = inspect.signature(statemachine_mk2_Event.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_statemachine_mk2_event_has_description():
    assert hasattr(statemachine_mk2_Event, "description")
    descriptor = None
    for klass in statemachine_mk2_Event.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_mk2_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_mk2_Transition)


def test_statemachine_mk2_transition_constructor_exists():
    assert callable(statemachine_mk2_Transition.__init__)


def test_statemachine_mk2_transition_constructor_args():
    sig = inspect.signature(statemachine_mk2_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_mk2_transition_has_name():
    assert hasattr(statemachine_mk2_Transition, "name")
    descriptor = None
    for klass in statemachine_mk2_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_mk2_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_mk2_State)


def test_statemachine_mk2_state_constructor_exists():
    assert callable(statemachine_mk2_State.__init__)


def test_statemachine_mk2_state_constructor_args():
    sig = inspect.signature(statemachine_mk2_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_mk2_state_has_name():
    assert hasattr(statemachine_mk2_State, "name")
    descriptor = None
    for klass in statemachine_mk2_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_mk2_composite_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_mk2_Composite_state)


def test_statemachine_mk2_composite_state_constructor_exists():
    assert callable(statemachine_mk2_Composite_state.__init__)


def test_statemachine_mk2_composite_state_constructor_args():
    sig = inspect.signature(statemachine_mk2_Composite_state.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_mk2_simplestate_is_not_abstract():
    assert not inspect.isabstract(statemachine_mk2_SimpleState)


def test_statemachine_mk2_simplestate_constructor_exists():
    assert callable(statemachine_mk2_SimpleState.__init__)


def test_statemachine_mk2_simplestate_constructor_args():
    sig = inspect.signature(statemachine_mk2_SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_mk2_final_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_mk2_Final_state)


def test_statemachine_mk2_final_state_constructor_exists():
    assert callable(statemachine_mk2_Final_state.__init__)


def test_statemachine_mk2_final_state_constructor_args():
    sig = inspect.signature(statemachine_mk2_Final_state.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_mk2_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_mk2_StateMachine)


def test_statemachine_mk2_statemachine_constructor_exists():
    assert callable(statemachine_mk2_StateMachine.__init__)


def test_statemachine_mk2_statemachine_constructor_args():
    sig = inspect.signature(statemachine_mk2_StateMachine.__init__)
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
statemachine_mk2_Event_strategy = st.builds(
    statemachine_mk2_Event,
    description=
        safe_text
)
statemachine_mk2_Transition_strategy = st.builds(
    statemachine_mk2_Transition,
    name=
        safe_text
)
statemachine_mk2_State_strategy = st.builds(
    statemachine_mk2_State,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
statemachine_mk2_Composite_state_strategy = st.builds(
    statemachine_mk2_Composite_state,
)
statemachine_mk2_SimpleState_strategy = st.builds(
    statemachine_mk2_SimpleState,
)
statemachine_mk2_Final_state_strategy = st.builds(
    statemachine_mk2_Final_state,
)
statemachine_mk2_StateMachine_strategy = st.builds(
    statemachine_mk2_StateMachine,
)

@given(instance=statemachine_mk2_Event_strategy)
@settings(max_examples=50)
def test_statemachine_mk2_event_instantiation(instance):
    assert isinstance(instance, statemachine_mk2_Event)



@given(instance=statemachine_mk2_Event_strategy)
def test_statemachine_mk2_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=statemachine_mk2_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_mk2_transition_instantiation(instance):
    assert isinstance(instance, statemachine_mk2_Transition)



@given(instance=statemachine_mk2_Transition_strategy)
def test_statemachine_mk2_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_mk2_State_strategy)
@settings(max_examples=50)
def test_statemachine_mk2_state_instantiation(instance):
    assert isinstance(instance, statemachine_mk2_State)



@given(instance=statemachine_mk2_State_strategy)
def test_statemachine_mk2_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine_mk2_Composite_state_strategy)
@settings(max_examples=50)
def test_statemachine_mk2_composite_state_instantiation(instance):
    assert isinstance(instance, statemachine_mk2_Composite_state)

@given(instance=statemachine_mk2_SimpleState_strategy)
@settings(max_examples=50)
def test_statemachine_mk2_simplestate_instantiation(instance):
    assert isinstance(instance, statemachine_mk2_SimpleState)

@given(instance=statemachine_mk2_Final_state_strategy)
@settings(max_examples=50)
def test_statemachine_mk2_final_state_instantiation(instance):
    assert isinstance(instance, statemachine_mk2_Final_state)

@given(instance=statemachine_mk2_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_mk2_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_mk2_StateMachine)
