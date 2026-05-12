import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleHierarchicalStateMachine_StateMachine,
    SimpleHierarchicalStateMachine_Transition,
    SimpleHierarchicalStateMachine_State,
    State,
    SimpleHierarchicalStateMachine_InitialState,
    SimpleHierarchicalStateMachine_FinalState,
    SimpleHierarchicalStateMachine_CompositeState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplehierarchicalstatemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine_StateMachine)


def test_simplehierarchicalstatemachine_statemachine_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine_StateMachine.__init__)


def test_simplehierarchicalstatemachine_statemachine_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_simplehierarchicalstatemachine_transition_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine_Transition)


def test_simplehierarchicalstatemachine_transition_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine_Transition.__init__)


def test_simplehierarchicalstatemachine_transition_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "effect" in params, "Missing parameter 'effect'"

def test_simplehierarchicalstatemachine_transition_has_trigger():
    assert hasattr(SimpleHierarchicalStateMachine_Transition, "trigger")
    descriptor = None
    for klass in SimpleHierarchicalStateMachine_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_simplehierarchicalstatemachine_transition_has_effect():
    assert hasattr(SimpleHierarchicalStateMachine_Transition, "effect")
    descriptor = None
    for klass in SimpleHierarchicalStateMachine_Transition.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)



def test_simplehierarchicalstatemachine_state_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine_State)


def test_simplehierarchicalstatemachine_state_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine_State.__init__)


def test_simplehierarchicalstatemachine_state_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplehierarchicalstatemachine_state_has_name():
    assert hasattr(SimpleHierarchicalStateMachine_State, "name")
    descriptor = None
    for klass in SimpleHierarchicalStateMachine_State.__mro__:
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



def test_simplehierarchicalstatemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine_InitialState)


def test_simplehierarchicalstatemachine_initialstate_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine_InitialState.__init__)


def test_simplehierarchicalstatemachine_initialstate_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_simplehierarchicalstatemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine_FinalState)


def test_simplehierarchicalstatemachine_finalstate_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine_FinalState.__init__)


def test_simplehierarchicalstatemachine_finalstate_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_simplehierarchicalstatemachine_compositestate_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine_CompositeState)


def test_simplehierarchicalstatemachine_compositestate_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine_CompositeState.__init__)


def test_simplehierarchicalstatemachine_compositestate_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine_CompositeState.__init__)
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
SimpleHierarchicalStateMachine_StateMachine_strategy = st.builds(
    SimpleHierarchicalStateMachine_StateMachine,
)
SimpleHierarchicalStateMachine_Transition_strategy = st.builds(
    SimpleHierarchicalStateMachine_Transition,
    trigger=
        safe_text,
    effect=
        safe_text
)
SimpleHierarchicalStateMachine_State_strategy = st.builds(
    SimpleHierarchicalStateMachine_State,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
SimpleHierarchicalStateMachine_InitialState_strategy = st.builds(
    SimpleHierarchicalStateMachine_InitialState,
)
SimpleHierarchicalStateMachine_FinalState_strategy = st.builds(
    SimpleHierarchicalStateMachine_FinalState,
)
SimpleHierarchicalStateMachine_CompositeState_strategy = st.builds(
    SimpleHierarchicalStateMachine_CompositeState,
)

@given(instance=SimpleHierarchicalStateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine_statemachine_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine_StateMachine)

@given(instance=SimpleHierarchicalStateMachine_Transition_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine_transition_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine_Transition)



@given(instance=SimpleHierarchicalStateMachine_Transition_strategy)
def test_simplehierarchicalstatemachine_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=SimpleHierarchicalStateMachine_Transition_strategy)
def test_simplehierarchicalstatemachine_transition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=SimpleHierarchicalStateMachine_State_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine_state_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine_State)



@given(instance=SimpleHierarchicalStateMachine_State_strategy)
def test_simplehierarchicalstatemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=SimpleHierarchicalStateMachine_InitialState_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine_initialstate_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine_InitialState)

@given(instance=SimpleHierarchicalStateMachine_FinalState_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine_finalstate_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine_FinalState)

@given(instance=SimpleHierarchicalStateMachine_CompositeState_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine_compositestate_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine_CompositeState)
