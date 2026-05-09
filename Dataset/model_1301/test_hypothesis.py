import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleHierarchicalStateMachine::StateMachine,
    SimpleHierarchicalStateMachine::Transition,
    SimpleHierarchicalStateMachine::State,
    State,
    SimpleHierarchicalStateMachine::CompositeState,
    SimpleHierarchicalStateMachine::InitialState,
    SimpleHierarchicalStateMachine::FinalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplehierarchicalstatemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine::StateMachine)


def test_simplehierarchicalstatemachine::statemachine_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine::StateMachine.__init__)


def test_simplehierarchicalstatemachine::statemachine_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_simplehierarchicalstatemachine::transition_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine::Transition)


def test_simplehierarchicalstatemachine::transition_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine::Transition.__init__)


def test_simplehierarchicalstatemachine::transition_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "effect" in params, "Missing parameter 'effect'"

def test_simplehierarchicalstatemachine::transition_has_trigger():
    assert hasattr(SimpleHierarchicalStateMachine::Transition, "trigger")
    descriptor = None
    for klass in SimpleHierarchicalStateMachine::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_simplehierarchicalstatemachine::transition_has_effect():
    assert hasattr(SimpleHierarchicalStateMachine::Transition, "effect")
    descriptor = None
    for klass in SimpleHierarchicalStateMachine::Transition.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)



def test_simplehierarchicalstatemachine::state_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine::State)


def test_simplehierarchicalstatemachine::state_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine::State.__init__)


def test_simplehierarchicalstatemachine::state_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplehierarchicalstatemachine::state_has_name():
    assert hasattr(SimpleHierarchicalStateMachine::State, "name")
    descriptor = None
    for klass in SimpleHierarchicalStateMachine::State.__mro__:
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



def test_simplehierarchicalstatemachine::compositestate_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine::CompositeState)


def test_simplehierarchicalstatemachine::compositestate_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine::CompositeState.__init__)


def test_simplehierarchicalstatemachine::compositestate_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_simplehierarchicalstatemachine::initialstate_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine::InitialState)


def test_simplehierarchicalstatemachine::initialstate_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine::InitialState.__init__)


def test_simplehierarchicalstatemachine::initialstate_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_simplehierarchicalstatemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(SimpleHierarchicalStateMachine::FinalState)


def test_simplehierarchicalstatemachine::finalstate_constructor_exists():
    assert callable(SimpleHierarchicalStateMachine::FinalState.__init__)


def test_simplehierarchicalstatemachine::finalstate_constructor_args():
    sig = inspect.signature(SimpleHierarchicalStateMachine::FinalState.__init__)
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
SimpleHierarchicalStateMachine::StateMachine_strategy = st.builds(
    SimpleHierarchicalStateMachine::StateMachine,
)
SimpleHierarchicalStateMachine::Transition_strategy = st.builds(
    SimpleHierarchicalStateMachine::Transition,
    trigger=
        safe_text,
    effect=
        safe_text
)
SimpleHierarchicalStateMachine::State_strategy = st.builds(
    SimpleHierarchicalStateMachine::State,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
SimpleHierarchicalStateMachine::CompositeState_strategy = st.builds(
    SimpleHierarchicalStateMachine::CompositeState,
)
SimpleHierarchicalStateMachine::InitialState_strategy = st.builds(
    SimpleHierarchicalStateMachine::InitialState,
)
SimpleHierarchicalStateMachine::FinalState_strategy = st.builds(
    SimpleHierarchicalStateMachine::FinalState,
)

@given(instance=SimpleHierarchicalStateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine::statemachine_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine::StateMachine)

@given(instance=SimpleHierarchicalStateMachine::Transition_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine::transition_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine::Transition)

@given(instance=SimpleHierarchicalStateMachine::Transition_strategy)
def test_simplehierarchicalstatemachine::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=SimpleHierarchicalStateMachine::Transition_strategy)
def test_simplehierarchicalstatemachine::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=SimpleHierarchicalStateMachine::Transition_strategy)
def test_simplehierarchicalstatemachine::transition_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=SimpleHierarchicalStateMachine::Transition_strategy)
def test_simplehierarchicalstatemachine::transition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=SimpleHierarchicalStateMachine::State_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine::state_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine::State)

@given(instance=SimpleHierarchicalStateMachine::State_strategy)
def test_simplehierarchicalstatemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleHierarchicalStateMachine::State_strategy)
def test_simplehierarchicalstatemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=SimpleHierarchicalStateMachine::CompositeState_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine::compositestate_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine::CompositeState)

@given(instance=SimpleHierarchicalStateMachine::InitialState_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine::initialstate_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine::InitialState)

@given(instance=SimpleHierarchicalStateMachine::FinalState_strategy)
@settings(max_examples=50)
def test_simplehierarchicalstatemachine::finalstate_instantiation(instance):
    assert isinstance(instance, SimpleHierarchicalStateMachine::FinalState)
