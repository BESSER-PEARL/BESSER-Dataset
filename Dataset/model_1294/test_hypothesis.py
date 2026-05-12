import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StateVertex,
    StateMachineUnnamed_SimpleState,
    StateMachineUnnamed_FinalState,
    StateMachineUnnamed_InitialState,
    StateMachineUnnamed_Event,
    StateMachineUnnamed_Transition,
    StateMachineUnnamed_StateVertex,
    StateMachineUnnamed_StateMachine,
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



def test_statemachineunnamed_simplestate_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed_SimpleState)


def test_statemachineunnamed_simplestate_constructor_exists():
    assert callable(StateMachineUnnamed_SimpleState.__init__)


def test_statemachineunnamed_simplestate_constructor_args():
    sig = inspect.signature(StateMachineUnnamed_SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_statemachineunnamed_finalstate_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed_FinalState)


def test_statemachineunnamed_finalstate_constructor_exists():
    assert callable(StateMachineUnnamed_FinalState.__init__)


def test_statemachineunnamed_finalstate_constructor_args():
    sig = inspect.signature(StateMachineUnnamed_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachineunnamed_initialstate_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed_InitialState)


def test_statemachineunnamed_initialstate_constructor_exists():
    assert callable(StateMachineUnnamed_InitialState.__init__)


def test_statemachineunnamed_initialstate_constructor_args():
    sig = inspect.signature(StateMachineUnnamed_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachineunnamed_event_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed_Event)


def test_statemachineunnamed_event_constructor_exists():
    assert callable(StateMachineUnnamed_Event.__init__)


def test_statemachineunnamed_event_constructor_args():
    sig = inspect.signature(StateMachineUnnamed_Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachineunnamed_transition_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed_Transition)


def test_statemachineunnamed_transition_constructor_exists():
    assert callable(StateMachineUnnamed_Transition.__init__)


def test_statemachineunnamed_transition_constructor_args():
    sig = inspect.signature(StateMachineUnnamed_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachineunnamed_transition_has_name():
    assert hasattr(StateMachineUnnamed_Transition, "name")
    descriptor = None
    for klass in StateMachineUnnamed_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachineunnamed_statevertex_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed_StateVertex)


def test_statemachineunnamed_statevertex_constructor_exists():
    assert callable(StateMachineUnnamed_StateVertex.__init__)


def test_statemachineunnamed_statevertex_constructor_args():
    sig = inspect.signature(StateMachineUnnamed_StateVertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachineunnamed_statevertex_has_name():
    assert hasattr(StateMachineUnnamed_StateVertex, "name")
    descriptor = None
    for klass in StateMachineUnnamed_StateVertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachineunnamed_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachineUnnamed_StateMachine)


def test_statemachineunnamed_statemachine_constructor_exists():
    assert callable(StateMachineUnnamed_StateMachine.__init__)


def test_statemachineunnamed_statemachine_constructor_args():
    sig = inspect.signature(StateMachineUnnamed_StateMachine.__init__)
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
StateMachineUnnamed_SimpleState_strategy = st.builds(
    StateMachineUnnamed_SimpleState,
)
StateMachineUnnamed_FinalState_strategy = st.builds(
    StateMachineUnnamed_FinalState,
)
StateMachineUnnamed_InitialState_strategy = st.builds(
    StateMachineUnnamed_InitialState,
)
StateMachineUnnamed_Event_strategy = st.builds(
    StateMachineUnnamed_Event,
)
StateMachineUnnamed_Transition_strategy = st.builds(
    StateMachineUnnamed_Transition,
    name=
        safe_text
)
StateMachineUnnamed_StateVertex_strategy = st.builds(
    StateMachineUnnamed_StateVertex,
    name=
        safe_text
)
StateMachineUnnamed_StateMachine_strategy = st.builds(
    StateMachineUnnamed_StateMachine,
)

@given(instance=StateVertex_strategy)
@settings(max_examples=50)
def test_statevertex_instantiation(instance):
    assert isinstance(instance, StateVertex)

@given(instance=StateMachineUnnamed_SimpleState_strategy)
@settings(max_examples=50)
def test_statemachineunnamed_simplestate_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed_SimpleState)

@given(instance=StateMachineUnnamed_FinalState_strategy)
@settings(max_examples=50)
def test_statemachineunnamed_finalstate_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed_FinalState)

@given(instance=StateMachineUnnamed_InitialState_strategy)
@settings(max_examples=50)
def test_statemachineunnamed_initialstate_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed_InitialState)

@given(instance=StateMachineUnnamed_Event_strategy)
@settings(max_examples=50)
def test_statemachineunnamed_event_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed_Event)

@given(instance=StateMachineUnnamed_Transition_strategy)
@settings(max_examples=50)
def test_statemachineunnamed_transition_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed_Transition)



@given(instance=StateMachineUnnamed_Transition_strategy)
def test_statemachineunnamed_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineUnnamed_StateVertex_strategy)
@settings(max_examples=50)
def test_statemachineunnamed_statevertex_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed_StateVertex)



@given(instance=StateMachineUnnamed_StateVertex_strategy)
def test_statemachineunnamed_statevertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineUnnamed_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachineunnamed_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachineUnnamed_StateMachine)
