import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StateVertex,
    StateMachine_SimpleState,
    StateMachine_FinalState,
    StateMachine_InitialState,
    StateMachine_Event,
    StateMachine_Transition,
    StateMachine_StateVertex,
    StateMachine_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateVertex)


def test_statevertex_constructor_exists():
    assert callable(StateVertex.__init__)


def test_statevertex_constructor_args():
    sig = inspect.signature(StateVertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_simplestate_is_not_abstract():
    assert not inspect.isabstract(StateMachine_SimpleState)


def test_statemachine_simplestate_constructor_exists():
    assert callable(StateMachine_SimpleState.__init__)


def test_statemachine_simplestate_constructor_args():
    sig = inspect.signature(StateMachine_SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine_FinalState)


def test_statemachine_finalstate_constructor_exists():
    assert callable(StateMachine_FinalState.__init__)


def test_statemachine_finalstate_constructor_args():
    sig = inspect.signature(StateMachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(StateMachine_InitialState)


def test_statemachine_initialstate_constructor_exists():
    assert callable(StateMachine_InitialState.__init__)


def test_statemachine_initialstate_constructor_args():
    sig = inspect.signature(StateMachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(StateMachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(StateMachine_Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(StateMachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(StateMachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_transition_has_name():
    assert hasattr(StateMachine_Transition, "name")
    descriptor = None
    for klass in StateMachine_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateMachine_StateVertex)


def test_statemachine_statevertex_constructor_exists():
    assert callable(StateMachine_StateVertex.__init__)


def test_statemachine_statevertex_constructor_args():
    sig = inspect.signature(StateMachine_StateVertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statevertex_has_name():
    assert hasattr(StateMachine_StateVertex, "name")
    descriptor = None
    for klass in StateMachine_StateVertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(StateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(StateMachine_StateMachine.__init__)
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
StateVertex_strategy = st.builds(
    StateVertex,
)
StateMachine_SimpleState_strategy = st.builds(
    StateMachine_SimpleState,
)
StateMachine_FinalState_strategy = st.builds(
    StateMachine_FinalState,
)
StateMachine_InitialState_strategy = st.builds(
    StateMachine_InitialState,
)
StateMachine_Event_strategy = st.builds(
    StateMachine_Event,
)
StateMachine_Transition_strategy = st.builds(
    StateMachine_Transition,
    name=
        safe_text
)
StateMachine_StateVertex_strategy = st.builds(
    StateMachine_StateVertex,
    name=
        safe_text
)
StateMachine_StateMachine_strategy = st.builds(
    StateMachine_StateMachine,
)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=StateMachine_SimpleState_strategy)
@settings(max_examples=50)
def test_statemachine_simplestate_instantiation(instance):
    assert isinstance(instance, StateMachine_SimpleState)

@given(instance=StateMachine_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine_finalstate_instantiation(instance):
    assert isinstance(instance, StateMachine_FinalState)

@given(instance=StateMachine_InitialState_strategy)
@settings(max_examples=50)
def test_statemachine_initialstate_instantiation(instance):
    assert isinstance(instance, StateMachine_InitialState)

@given(instance=StateMachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, StateMachine_Event)

@given(instance=StateMachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, StateMachine_Transition)



@given(instance=StateMachine_Transition_strategy)
def test_statemachine_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine_StateVertex_strategy)
@settings(max_examples=50)
def test_statemachine_statevertex_instantiation(instance):
    assert isinstance(instance, StateMachine_StateVertex)



@given(instance=StateMachine_StateVertex_strategy)
def test_statemachine_statevertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine_StateMachine)
