import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    sample::Finalstate,
    sample::Initstate,
    sample::Transition,
    sample::FSM,
    sample::State,
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



def test_sample::finalstate_is_not_abstract():
    assert not inspect.isabstract(sample::Finalstate)


def test_sample::finalstate_constructor_exists():
    assert callable(sample::Finalstate.__init__)


def test_sample::finalstate_constructor_args():
    sig = inspect.signature(sample::Finalstate.__init__)
    params = list(sig.parameters.keys())



def test_sample::initstate_is_not_abstract():
    assert not inspect.isabstract(sample::Initstate)


def test_sample::initstate_constructor_exists():
    assert callable(sample::Initstate.__init__)


def test_sample::initstate_constructor_args():
    sig = inspect.signature(sample::Initstate.__init__)
    params = list(sig.parameters.keys())



def test_sample::transition_is_not_abstract():
    assert not inspect.isabstract(sample::Transition)


def test_sample::transition_constructor_exists():
    assert callable(sample::Transition.__init__)


def test_sample::transition_constructor_args():
    sig = inspect.signature(sample::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_sample::transition_has_name():
    assert hasattr(sample::Transition, "name")
    descriptor = None
    for klass in sample::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sample::transition_has_trigger():
    assert hasattr(sample::Transition, "trigger")
    descriptor = None
    for klass in sample::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_sample::fsm_is_not_abstract():
    assert not inspect.isabstract(sample::FSM)


def test_sample::fsm_constructor_exists():
    assert callable(sample::FSM.__init__)


def test_sample::fsm_constructor_args():
    sig = inspect.signature(sample::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample::fsm_has_name():
    assert hasattr(sample::FSM, "name")
    descriptor = None
    for klass in sample::FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample::state_is_not_abstract():
    assert not inspect.isabstract(sample::State)


def test_sample::state_constructor_exists():
    assert callable(sample::State.__init__)


def test_sample::state_constructor_args():
    sig = inspect.signature(sample::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample::state_has_name():
    assert hasattr(sample::State, "name")
    descriptor = None
    for klass in sample::State.__mro__:
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
sample::Finalstate_strategy = st.builds(
    sample::Finalstate,
)
sample::Initstate_strategy = st.builds(
    sample::Initstate,
)
sample::Transition_strategy = st.builds(
    sample::Transition,
    name=
        safe_text,
    trigger=
        safe_text
)
sample::FSM_strategy = st.builds(
    sample::FSM,
    name=
        safe_text
)
sample::State_strategy = st.builds(
    sample::State,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=sample::Finalstate_strategy)
@settings(max_examples=50)
def test_sample::finalstate_instantiation(instance):
    assert isinstance(instance, sample::Finalstate)

@given(instance=sample::Initstate_strategy)
@settings(max_examples=50)
def test_sample::initstate_instantiation(instance):
    assert isinstance(instance, sample::Initstate)

@given(instance=sample::Transition_strategy)
@settings(max_examples=50)
def test_sample::transition_instantiation(instance):
    assert isinstance(instance, sample::Transition)

@given(instance=sample::Transition_strategy)
def test_sample::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::Transition_strategy)
def test_sample::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample::Transition_strategy)
def test_sample::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=sample::Transition_strategy)
def test_sample::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=sample::FSM_strategy)
@settings(max_examples=50)
def test_sample::fsm_instantiation(instance):
    assert isinstance(instance, sample::FSM)

@given(instance=sample::FSM_strategy)
def test_sample::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::FSM_strategy)
def test_sample::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample::State_strategy)
@settings(max_examples=50)
def test_sample::state_instantiation(instance):
    assert isinstance(instance, sample::State)

@given(instance=sample::State_strategy)
def test_sample::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sample::State_strategy)
def test_sample::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
