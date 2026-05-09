import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tP1::EM::State,
    tP1::EM::Transition,
    tP1::EM::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tp1::em::state_is_not_abstract():
    assert not inspect.isabstract(tP1::EM::State)


def test_tp1::em::state_constructor_exists():
    assert callable(tP1::EM::State.__init__)


def test_tp1::em::state_constructor_args():
    sig = inspect.signature(tP1::EM::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1::em::state_has_name():
    assert hasattr(tP1::EM::State, "name")
    descriptor = None
    for klass in tP1::EM::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1::em::transition_is_not_abstract():
    assert not inspect.isabstract(tP1::EM::Transition)


def test_tp1::em::transition_constructor_exists():
    assert callable(tP1::EM::Transition.__init__)


def test_tp1::em::transition_constructor_args():
    sig = inspect.signature(tP1::EM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1::em::transition_has_name():
    assert hasattr(tP1::EM::Transition, "name")
    descriptor = None
    for klass in tP1::EM::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1::em::statemachine_is_not_abstract():
    assert not inspect.isabstract(tP1::EM::StateMachine)


def test_tp1::em::statemachine_constructor_exists():
    assert callable(tP1::EM::StateMachine.__init__)


def test_tp1::em::statemachine_constructor_args():
    sig = inspect.signature(tP1::EM::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1::em::statemachine_has_name():
    assert hasattr(tP1::EM::StateMachine, "name")
    descriptor = None
    for klass in tP1::EM::StateMachine.__mro__:
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
tP1::EM::State_strategy = st.builds(
    tP1::EM::State,
    name=
        safe_text
)
tP1::EM::Transition_strategy = st.builds(
    tP1::EM::Transition,
    name=
        safe_text
)
tP1::EM::StateMachine_strategy = st.builds(
    tP1::EM::StateMachine,
    name=
        safe_text
)

@given(instance=tP1::EM::State_strategy)
@settings(max_examples=50)
def test_tp1::em::state_instantiation(instance):
    assert isinstance(instance, tP1::EM::State)

@given(instance=tP1::EM::State_strategy)
def test_tp1::em::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tP1::EM::State_strategy)
def test_tp1::em::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tP1::EM::Transition_strategy)
@settings(max_examples=50)
def test_tp1::em::transition_instantiation(instance):
    assert isinstance(instance, tP1::EM::Transition)

@given(instance=tP1::EM::Transition_strategy)
def test_tp1::em::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tP1::EM::Transition_strategy)
def test_tp1::em::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tP1::EM::StateMachine_strategy)
@settings(max_examples=50)
def test_tp1::em::statemachine_instantiation(instance):
    assert isinstance(instance, tP1::EM::StateMachine)

@given(instance=tP1::EM::StateMachine_strategy)
def test_tp1::em::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tP1::EM::StateMachine_strategy)
def test_tp1::em::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
