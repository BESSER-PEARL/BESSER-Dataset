import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    etatma::State,
    etatma::Transition,
    etatma::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_etatma::state_is_not_abstract():
    assert not inspect.isabstract(etatma::State)


def test_etatma::state_constructor_exists():
    assert callable(etatma::State.__init__)


def test_etatma::state_constructor_args():
    sig = inspect.signature(etatma::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_etatma::state_has_name():
    assert hasattr(etatma::State, "name")
    descriptor = None
    for klass in etatma::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etatma::transition_is_not_abstract():
    assert not inspect.isabstract(etatma::Transition)


def test_etatma::transition_constructor_exists():
    assert callable(etatma::Transition.__init__)


def test_etatma::transition_constructor_args():
    sig = inspect.signature(etatma::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_etatma::transition_has_name():
    assert hasattr(etatma::Transition, "name")
    descriptor = None
    for klass in etatma::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etatma::statemachine_is_not_abstract():
    assert not inspect.isabstract(etatma::StateMachine)


def test_etatma::statemachine_constructor_exists():
    assert callable(etatma::StateMachine.__init__)


def test_etatma::statemachine_constructor_args():
    sig = inspect.signature(etatma::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_etatma::statemachine_has_name():
    assert hasattr(etatma::StateMachine, "name")
    descriptor = None
    for klass in etatma::StateMachine.__mro__:
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
etatma::State_strategy = st.builds(
    etatma::State,
    name=
        safe_text
)
etatma::Transition_strategy = st.builds(
    etatma::Transition,
    name=
        safe_text
)
etatma::StateMachine_strategy = st.builds(
    etatma::StateMachine,
    name=
        safe_text
)

@given(instance=etatma::State_strategy)
@settings(max_examples=50)
def test_etatma::state_instantiation(instance):
    assert isinstance(instance, etatma::State)

@given(instance=etatma::State_strategy)
def test_etatma::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=etatma::State_strategy)
def test_etatma::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=etatma::Transition_strategy)
@settings(max_examples=50)
def test_etatma::transition_instantiation(instance):
    assert isinstance(instance, etatma::Transition)

@given(instance=etatma::Transition_strategy)
def test_etatma::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=etatma::Transition_strategy)
def test_etatma::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=etatma::StateMachine_strategy)
@settings(max_examples=50)
def test_etatma::statemachine_instantiation(instance):
    assert isinstance(instance, etatma::StateMachine)

@given(instance=etatma::StateMachine_strategy)
def test_etatma::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=etatma::StateMachine_strategy)
def test_etatma::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
