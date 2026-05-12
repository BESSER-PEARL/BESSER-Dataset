import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_Event,
    statemachine_Transition,
    statemachine_State,
    statemachine_SM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(statemachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(statemachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(statemachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine_event_has_id():
    assert hasattr(statemachine_Event, "id")
    descriptor = None
    for klass in statemachine_Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine_state_has_id():
    assert hasattr(statemachine_State, "id")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_sm_is_not_abstract():
    assert not inspect.isabstract(statemachine_SM)


def test_statemachine_sm_constructor_exists():
    assert callable(statemachine_SM.__init__)


def test_statemachine_sm_constructor_args():
    sig = inspect.signature(statemachine_SM.__init__)
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
statemachine_Event_strategy = st.builds(
    statemachine_Event,
    id=
        safe_text
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    id=
        safe_text
)
statemachine_SM_strategy = st.builds(
    statemachine_SM,
)

@given(instance=statemachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, statemachine_Event)



@given(instance=statemachine_Event_strategy)
def test_statemachine_event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine_SM_strategy)
@settings(max_examples=50)
def test_statemachine_sm_instantiation(instance):
    assert isinstance(instance, statemachine_SM)
