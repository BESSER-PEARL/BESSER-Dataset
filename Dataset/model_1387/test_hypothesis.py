import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    SM::FinalState,
    SM::InitialState,
    SM::Transition,
    SM::StateMachine,
    SM::State,
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



def test_sm::finalstate_is_not_abstract():
    assert not inspect.isabstract(SM::FinalState)


def test_sm::finalstate_constructor_exists():
    assert callable(SM::FinalState.__init__)


def test_sm::finalstate_constructor_args():
    sig = inspect.signature(SM::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_sm::initialstate_is_not_abstract():
    assert not inspect.isabstract(SM::InitialState)


def test_sm::initialstate_constructor_exists():
    assert callable(SM::InitialState.__init__)


def test_sm::initialstate_constructor_args():
    sig = inspect.signature(SM::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_sm::transition_is_not_abstract():
    assert not inspect.isabstract(SM::Transition)


def test_sm::transition_constructor_exists():
    assert callable(SM::Transition.__init__)


def test_sm::transition_constructor_args():
    sig = inspect.signature(SM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_sm::transition_has_effect():
    assert hasattr(SM::Transition, "effect")
    descriptor = None
    for klass in SM::Transition.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_sm::transition_has_trigger():
    assert hasattr(SM::Transition, "trigger")
    descriptor = None
    for klass in SM::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_sm::statemachine_is_not_abstract():
    assert not inspect.isabstract(SM::StateMachine)


def test_sm::statemachine_constructor_exists():
    assert callable(SM::StateMachine.__init__)


def test_sm::statemachine_constructor_args():
    sig = inspect.signature(SM::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_sm::state_is_not_abstract():
    assert not inspect.isabstract(SM::State)


def test_sm::state_constructor_exists():
    assert callable(SM::State.__init__)


def test_sm::state_constructor_args():
    sig = inspect.signature(SM::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sm::state_has_name():
    assert hasattr(SM::State, "name")
    descriptor = None
    for klass in SM::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
SM::FinalState_strategy = st.builds(
    SM::FinalState,
)
SM::InitialState_strategy = st.builds(
    SM::InitialState,
)
SM::Transition_strategy = st.builds(
    SM::Transition,
    effect=
        safe_text,
    trigger=
        safe_text
)
SM::StateMachine_strategy = st.builds(
    SM::StateMachine,
)
SM::State_strategy = st.builds(
    SM::State,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=SM::FinalState_strategy)
@settings(max_examples=50)
def test_sm::finalstate_instantiation(instance):
    assert isinstance(instance, SM::FinalState)

@given(instance=SM::InitialState_strategy)
@settings(max_examples=50)
def test_sm::initialstate_instantiation(instance):
    assert isinstance(instance, SM::InitialState)

@given(instance=SM::Transition_strategy)
@settings(max_examples=50)
def test_sm::transition_instantiation(instance):
    assert isinstance(instance, SM::Transition)

@given(instance=SM::Transition_strategy)
def test_sm::transition_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=SM::Transition_strategy)
def test_sm::transition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=SM::Transition_strategy)
def test_sm::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=SM::Transition_strategy)
def test_sm::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=SM::StateMachine_strategy)
@settings(max_examples=50)
def test_sm::statemachine_instantiation(instance):
    assert isinstance(instance, SM::StateMachine)

@given(instance=SM::State_strategy)
@settings(max_examples=50)
def test_sm::state_instantiation(instance):
    assert isinstance(instance, SM::State)

@given(instance=SM::State_strategy)
def test_sm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SM::State_strategy)
def test_sm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
