import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::Transition,
    model::State,
    model::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::transition_is_not_abstract():
    assert not inspect.isabstract(model::Transition)


def test_model::transition_constructor_exists():
    assert callable(model::Transition.__init__)


def test_model::transition_constructor_args():
    sig = inspect.signature(model::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::transition_has_name():
    assert hasattr(model::Transition, "name")
    descriptor = None
    for klass in model::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::state_is_not_abstract():
    assert not inspect.isabstract(model::State)


def test_model::state_constructor_exists():
    assert callable(model::State.__init__)


def test_model::state_constructor_args():
    sig = inspect.signature(model::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::state_has_name():
    assert hasattr(model::State, "name")
    descriptor = None
    for klass in model::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::fsm_is_not_abstract():
    assert not inspect.isabstract(model::FSM)


def test_model::fsm_constructor_exists():
    assert callable(model::FSM.__init__)


def test_model::fsm_constructor_args():
    sig = inspect.signature(model::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::fsm_has_name():
    assert hasattr(model::FSM, "name")
    descriptor = None
    for klass in model::FSM.__mro__:
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
model::Transition_strategy = st.builds(
    model::Transition,
    name=
        safe_text
)
model::State_strategy = st.builds(
    model::State,
    name=
        safe_text
)
model::FSM_strategy = st.builds(
    model::FSM,
    name=
        safe_text
)

@given(instance=model::Transition_strategy)
@settings(max_examples=50)
def test_model::transition_instantiation(instance):
    assert isinstance(instance, model::Transition)

@given(instance=model::Transition_strategy)
def test_model::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Transition_strategy)
def test_model::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::State_strategy)
@settings(max_examples=50)
def test_model::state_instantiation(instance):
    assert isinstance(instance, model::State)

@given(instance=model::State_strategy)
def test_model::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::State_strategy)
def test_model::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::FSM_strategy)
@settings(max_examples=50)
def test_model::fsm_instantiation(instance):
    assert isinstance(instance, model::FSM)

@given(instance=model::FSM_strategy)
def test_model::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::FSM_strategy)
def test_model::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
