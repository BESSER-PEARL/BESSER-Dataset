import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    idm::Transition,
    idm::State,
    idm::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_idm::transition_is_not_abstract():
    assert not inspect.isabstract(idm::Transition)


def test_idm::transition_constructor_exists():
    assert callable(idm::Transition.__init__)


def test_idm::transition_constructor_args():
    sig = inspect.signature(idm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm::transition_has_name():
    assert hasattr(idm::Transition, "name")
    descriptor = None
    for klass in idm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idm::state_is_not_abstract():
    assert not inspect.isabstract(idm::State)


def test_idm::state_constructor_exists():
    assert callable(idm::State.__init__)


def test_idm::state_constructor_args():
    sig = inspect.signature(idm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm::state_has_name():
    assert hasattr(idm::State, "name")
    descriptor = None
    for klass in idm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idm::statemachine_is_not_abstract():
    assert not inspect.isabstract(idm::StateMachine)


def test_idm::statemachine_constructor_exists():
    assert callable(idm::StateMachine.__init__)


def test_idm::statemachine_constructor_args():
    sig = inspect.signature(idm::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idm::statemachine_has_name():
    assert hasattr(idm::StateMachine, "name")
    descriptor = None
    for klass in idm::StateMachine.__mro__:
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
idm::Transition_strategy = st.builds(
    idm::Transition,
    name=
        safe_text
)
idm::State_strategy = st.builds(
    idm::State,
    name=
        safe_text
)
idm::StateMachine_strategy = st.builds(
    idm::StateMachine,
    name=
        safe_text
)

@given(instance=idm::Transition_strategy)
@settings(max_examples=50)
def test_idm::transition_instantiation(instance):
    assert isinstance(instance, idm::Transition)

@given(instance=idm::Transition_strategy)
def test_idm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idm::Transition_strategy)
def test_idm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idm::State_strategy)
@settings(max_examples=50)
def test_idm::state_instantiation(instance):
    assert isinstance(instance, idm::State)

@given(instance=idm::State_strategy)
def test_idm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idm::State_strategy)
def test_idm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idm::StateMachine_strategy)
@settings(max_examples=50)
def test_idm::statemachine_instantiation(instance):
    assert isinstance(instance, idm::StateMachine)

@given(instance=idm::StateMachine_strategy)
def test_idm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idm::StateMachine_strategy)
def test_idm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
