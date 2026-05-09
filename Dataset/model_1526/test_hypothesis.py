import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lab1::State,
    lab1::StateMachine,
    lab1::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lab1::state_is_not_abstract():
    assert not inspect.isabstract(lab1::State)


def test_lab1::state_constructor_exists():
    assert callable(lab1::State.__init__)


def test_lab1::state_constructor_args():
    sig = inspect.signature(lab1::State.__init__)
    params = list(sig.parameters.keys())
    assert "init" in params, "Missing parameter 'init'"
    assert "name" in params, "Missing parameter 'name'"

def test_lab1::state_has_init():
    assert hasattr(lab1::State, "init")
    descriptor = None
    for klass in lab1::State.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)

def test_lab1::state_has_name():
    assert hasattr(lab1::State, "name")
    descriptor = None
    for klass in lab1::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lab1::statemachine_is_not_abstract():
    assert not inspect.isabstract(lab1::StateMachine)


def test_lab1::statemachine_constructor_exists():
    assert callable(lab1::StateMachine.__init__)


def test_lab1::statemachine_constructor_args():
    sig = inspect.signature(lab1::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lab1::statemachine_has_name():
    assert hasattr(lab1::StateMachine, "name")
    descriptor = None
    for klass in lab1::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lab1::transition_is_not_abstract():
    assert not inspect.isabstract(lab1::Transition)


def test_lab1::transition_constructor_exists():
    assert callable(lab1::Transition.__init__)


def test_lab1::transition_constructor_args():
    sig = inspect.signature(lab1::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lab1::transition_has_name():
    assert hasattr(lab1::Transition, "name")
    descriptor = None
    for klass in lab1::Transition.__mro__:
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
lab1::State_strategy = st.builds(
    lab1::State,
    init=
        st.booleans(),
    name=
        safe_text
)
lab1::StateMachine_strategy = st.builds(
    lab1::StateMachine,
    name=
        safe_text
)
lab1::Transition_strategy = st.builds(
    lab1::Transition,
    name=
        safe_text
)

@given(instance=lab1::State_strategy)
@settings(max_examples=50)
def test_lab1::state_instantiation(instance):
    assert isinstance(instance, lab1::State)

@given(instance=lab1::State_strategy)
def test_lab1::state_init_type(instance):
    assert isinstance(instance.init, bool)


@given(instance=lab1::State_strategy)
def test_lab1::state_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original

@given(instance=lab1::State_strategy)
def test_lab1::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lab1::State_strategy)
def test_lab1::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lab1::StateMachine_strategy)
@settings(max_examples=50)
def test_lab1::statemachine_instantiation(instance):
    assert isinstance(instance, lab1::StateMachine)

@given(instance=lab1::StateMachine_strategy)
def test_lab1::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lab1::StateMachine_strategy)
def test_lab1::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lab1::Transition_strategy)
@settings(max_examples=50)
def test_lab1::transition_instantiation(instance):
    assert isinstance(instance, lab1::Transition)

@given(instance=lab1::Transition_strategy)
def test_lab1::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lab1::Transition_strategy)
def test_lab1::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
