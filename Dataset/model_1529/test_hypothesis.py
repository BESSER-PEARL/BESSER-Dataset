import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    minifsm_FinalState,
    minifsm_Transition,
    minifsm_State,
    minifsm_Machine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_minifsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(minifsm_FinalState)


def test_minifsm_finalstate_constructor_exists():
    assert callable(minifsm_FinalState.__init__)


def test_minifsm_finalstate_constructor_args():
    sig = inspect.signature(minifsm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_minifsm_transition_is_not_abstract():
    assert not inspect.isabstract(minifsm_Transition)


def test_minifsm_transition_constructor_exists():
    assert callable(minifsm_Transition.__init__)


def test_minifsm_transition_constructor_args():
    sig = inspect.signature(minifsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_minifsm_transition_has_event():
    assert hasattr(minifsm_Transition, "event")
    descriptor = None
    for klass in minifsm_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_minifsm_state_is_not_abstract():
    assert not inspect.isabstract(minifsm_State)


def test_minifsm_state_constructor_exists():
    assert callable(minifsm_State.__init__)


def test_minifsm_state_constructor_args():
    sig = inspect.signature(minifsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minifsm_state_has_name():
    assert hasattr(minifsm_State, "name")
    descriptor = None
    for klass in minifsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minifsm_machine_is_not_abstract():
    assert not inspect.isabstract(minifsm_Machine)


def test_minifsm_machine_constructor_exists():
    assert callable(minifsm_Machine.__init__)


def test_minifsm_machine_constructor_args():
    sig = inspect.signature(minifsm_Machine.__init__)
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
State_strategy = st.builds(
    State,
)
minifsm_FinalState_strategy = st.builds(
    minifsm_FinalState,
)
minifsm_Transition_strategy = st.builds(
    minifsm_Transition,
    event=
        safe_text
)
minifsm_State_strategy = st.builds(
    minifsm_State,
    name=
        safe_text
)
minifsm_Machine_strategy = st.builds(
    minifsm_Machine,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=minifsm_FinalState_strategy)
@settings(max_examples=50)
def test_minifsm_finalstate_instantiation(instance):
    assert isinstance(instance, minifsm_FinalState)

@given(instance=minifsm_Transition_strategy)
@settings(max_examples=50)
def test_minifsm_transition_instantiation(instance):
    assert isinstance(instance, minifsm_Transition)



@given(instance=minifsm_Transition_strategy)
def test_minifsm_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=minifsm_State_strategy)
@settings(max_examples=50)
def test_minifsm_state_instantiation(instance):
    assert isinstance(instance, minifsm_State)



@given(instance=minifsm_State_strategy)
def test_minifsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minifsm_Machine_strategy)
@settings(max_examples=50)
def test_minifsm_machine_instantiation(instance):
    assert isinstance(instance, minifsm_Machine)
