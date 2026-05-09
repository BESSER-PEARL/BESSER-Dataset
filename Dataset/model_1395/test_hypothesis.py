import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractState,
    model::State,
    model::Transition,
    model::FiniteStateMachine,
    model::AbstractState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_model::state_is_not_abstract():
    assert not inspect.isabstract(model::State)


def test_model::state_constructor_exists():
    assert callable(model::State.__init__)


def test_model::state_constructor_args():
    sig = inspect.signature(model::State.__init__)
    params = list(sig.parameters.keys())



def test_model::transition_is_not_abstract():
    assert not inspect.isabstract(model::Transition)


def test_model::transition_constructor_exists():
    assert callable(model::Transition.__init__)


def test_model::transition_constructor_args():
    sig = inspect.signature(model::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_model::transition_has_trigger():
    assert hasattr(model::Transition, "trigger")
    descriptor = None
    for klass in model::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_model::transition_has_name():
    assert hasattr(model::Transition, "name")
    descriptor = None
    for klass in model::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::finitestatemachine_is_not_abstract():
    assert not inspect.isabstract(model::FiniteStateMachine)


def test_model::finitestatemachine_constructor_exists():
    assert callable(model::FiniteStateMachine.__init__)


def test_model::finitestatemachine_constructor_args():
    sig = inspect.signature(model::FiniteStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_model::abstractstate_is_not_abstract():
    assert not inspect.isabstract(model::AbstractState)


def test_model::abstractstate_constructor_exists():
    assert callable(model::AbstractState.__init__)


def test_model::abstractstate_constructor_args():
    sig = inspect.signature(model::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::abstractstate_has_name():
    assert hasattr(model::AbstractState, "name")
    descriptor = None
    for klass in model::AbstractState.__mro__:
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
AbstractState_strategy = st.builds(
    AbstractState,
)
model::State_strategy = st.builds(
    model::State,
)
model::Transition_strategy = st.builds(
    model::Transition,
    trigger=
        safe_text,
    name=
        safe_text
)
model::FiniteStateMachine_strategy = st.builds(
    model::FiniteStateMachine,
)
model::AbstractState_strategy = st.builds(
    model::AbstractState,
    name=
        safe_text
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=model::State_strategy)
@settings(max_examples=50)
def test_model::state_instantiation(instance):
    assert isinstance(instance, model::State)

@given(instance=model::Transition_strategy)
@settings(max_examples=50)
def test_model::transition_instantiation(instance):
    assert isinstance(instance, model::Transition)

@given(instance=model::Transition_strategy)
def test_model::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=model::Transition_strategy)
def test_model::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=model::Transition_strategy)
def test_model::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Transition_strategy)
def test_model::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::FiniteStateMachine_strategy)
@settings(max_examples=50)
def test_model::finitestatemachine_instantiation(instance):
    assert isinstance(instance, model::FiniteStateMachine)

@given(instance=model::AbstractState_strategy)
@settings(max_examples=50)
def test_model::abstractstate_instantiation(instance):
    assert isinstance(instance, model::AbstractState)

@given(instance=model::AbstractState_strategy)
def test_model::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::AbstractState_strategy)
def test_model::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
