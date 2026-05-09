import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HSM::Transition,
    HSM::StateMachine,
    HSM::State,
    State,
    HSM::CompositeState,
    HSM::InitialState,
    HSM::FinalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hsm::transition_is_not_abstract():
    assert not inspect.isabstract(HSM::Transition)


def test_hsm::transition_constructor_exists():
    assert callable(HSM::Transition.__init__)


def test_hsm::transition_constructor_args():
    sig = inspect.signature(HSM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_hsm::transition_has_effect():
    assert hasattr(HSM::Transition, "effect")
    descriptor = None
    for klass in HSM::Transition.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_hsm::transition_has_trigger():
    assert hasattr(HSM::Transition, "trigger")
    descriptor = None
    for klass in HSM::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_hsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(HSM::StateMachine)


def test_hsm::statemachine_constructor_exists():
    assert callable(HSM::StateMachine.__init__)


def test_hsm::statemachine_constructor_args():
    sig = inspect.signature(HSM::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_hsm::state_is_not_abstract():
    assert not inspect.isabstract(HSM::State)


def test_hsm::state_constructor_exists():
    assert callable(HSM::State.__init__)


def test_hsm::state_constructor_args():
    sig = inspect.signature(HSM::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::state_has_name():
    assert hasattr(HSM::State, "name")
    descriptor = None
    for klass in HSM::State.__mro__:
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



def test_hsm::compositestate_is_not_abstract():
    assert not inspect.isabstract(HSM::CompositeState)


def test_hsm::compositestate_constructor_exists():
    assert callable(HSM::CompositeState.__init__)


def test_hsm::compositestate_constructor_args():
    sig = inspect.signature(HSM::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(HSM::InitialState)


def test_hsm::initialstate_constructor_exists():
    assert callable(HSM::InitialState.__init__)


def test_hsm::initialstate_constructor_args():
    sig = inspect.signature(HSM::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(HSM::FinalState)


def test_hsm::finalstate_constructor_exists():
    assert callable(HSM::FinalState.__init__)


def test_hsm::finalstate_constructor_args():
    sig = inspect.signature(HSM::FinalState.__init__)
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
HSM::Transition_strategy = st.builds(
    HSM::Transition,
    effect=
        safe_text,
    trigger=
        safe_text
)
HSM::StateMachine_strategy = st.builds(
    HSM::StateMachine,
)
HSM::State_strategy = st.builds(
    HSM::State,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
HSM::CompositeState_strategy = st.builds(
    HSM::CompositeState,
)
HSM::InitialState_strategy = st.builds(
    HSM::InitialState,
)
HSM::FinalState_strategy = st.builds(
    HSM::FinalState,
)

@given(instance=HSM::Transition_strategy)
@settings(max_examples=50)
def test_hsm::transition_instantiation(instance):
    assert isinstance(instance, HSM::Transition)

@given(instance=HSM::Transition_strategy)
def test_hsm::transition_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=HSM::Transition_strategy)
def test_hsm::transition_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=HSM::Transition_strategy)
def test_hsm::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=HSM::Transition_strategy)
def test_hsm::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=HSM::StateMachine_strategy)
@settings(max_examples=50)
def test_hsm::statemachine_instantiation(instance):
    assert isinstance(instance, HSM::StateMachine)

@given(instance=HSM::State_strategy)
@settings(max_examples=50)
def test_hsm::state_instantiation(instance):
    assert isinstance(instance, HSM::State)

@given(instance=HSM::State_strategy)
def test_hsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HSM::State_strategy)
def test_hsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=HSM::CompositeState_strategy)
@settings(max_examples=50)
def test_hsm::compositestate_instantiation(instance):
    assert isinstance(instance, HSM::CompositeState)

@given(instance=HSM::InitialState_strategy)
@settings(max_examples=50)
def test_hsm::initialstate_instantiation(instance):
    assert isinstance(instance, HSM::InitialState)

@given(instance=HSM::FinalState_strategy)
@settings(max_examples=50)
def test_hsm::finalstate_instantiation(instance):
    assert isinstance(instance, HSM::FinalState)
