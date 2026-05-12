import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myStateMachines_State,
    myStateMachines_Transition,
    myStateMachines_Event,
    myStateMachines_Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mystatemachines_state_is_not_abstract():
    assert not inspect.isabstract(myStateMachines_State)


def test_mystatemachines_state_constructor_exists():
    assert callable(myStateMachines_State.__init__)


def test_mystatemachines_state_constructor_args():
    sig = inspect.signature(myStateMachines_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "actions" in params, "Missing parameter 'actions'"

def test_mystatemachines_state_has_name():
    assert hasattr(myStateMachines_State, "name")
    descriptor = None
    for klass in myStateMachines_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mystatemachines_state_has_actions():
    assert hasattr(myStateMachines_State, "actions")
    descriptor = None
    for klass in myStateMachines_State.__mro__:
        if "actions" in klass.__dict__:
            descriptor = klass.__dict__["actions"]
            break
    assert isinstance(descriptor, property)



def test_mystatemachines_transition_is_not_abstract():
    assert not inspect.isabstract(myStateMachines_Transition)


def test_mystatemachines_transition_constructor_exists():
    assert callable(myStateMachines_Transition.__init__)


def test_mystatemachines_transition_constructor_args():
    sig = inspect.signature(myStateMachines_Transition.__init__)
    params = list(sig.parameters.keys())



def test_mystatemachines_event_is_not_abstract():
    assert not inspect.isabstract(myStateMachines_Event)


def test_mystatemachines_event_constructor_exists():
    assert callable(myStateMachines_Event.__init__)


def test_mystatemachines_event_constructor_args():
    sig = inspect.signature(myStateMachines_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mystatemachines_event_has_name():
    assert hasattr(myStateMachines_Event, "name")
    descriptor = None
    for klass in myStateMachines_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mystatemachines_statemachine_is_not_abstract():
    assert not inspect.isabstract(myStateMachines_Statemachine)


def test_mystatemachines_statemachine_constructor_exists():
    assert callable(myStateMachines_Statemachine.__init__)


def test_mystatemachines_statemachine_constructor_args():
    sig = inspect.signature(myStateMachines_Statemachine.__init__)
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
myStateMachines_State_strategy = st.builds(
    myStateMachines_State,
    name=
        safe_text,
    actions=
        safe_text
)
myStateMachines_Transition_strategy = st.builds(
    myStateMachines_Transition,
)
myStateMachines_Event_strategy = st.builds(
    myStateMachines_Event,
    name=
        safe_text
)
myStateMachines_Statemachine_strategy = st.builds(
    myStateMachines_Statemachine,
)

@given(instance=myStateMachines_State_strategy)
@settings(max_examples=50)
def test_mystatemachines_state_instantiation(instance):
    assert isinstance(instance, myStateMachines_State)



@given(instance=myStateMachines_State_strategy)
def test_mystatemachines_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myStateMachines_State_strategy)
def test_mystatemachines_state_actions_setter(instance):
    original = instance.actions
    instance.actions = original
    assert instance.actions == original

@given(instance=myStateMachines_Transition_strategy)
@settings(max_examples=50)
def test_mystatemachines_transition_instantiation(instance):
    assert isinstance(instance, myStateMachines_Transition)

@given(instance=myStateMachines_Event_strategy)
@settings(max_examples=50)
def test_mystatemachines_event_instantiation(instance):
    assert isinstance(instance, myStateMachines_Event)



@given(instance=myStateMachines_Event_strategy)
def test_mystatemachines_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myStateMachines_Statemachine_strategy)
@settings(max_examples=50)
def test_mystatemachines_statemachine_instantiation(instance):
    assert isinstance(instance, myStateMachines_Statemachine)
