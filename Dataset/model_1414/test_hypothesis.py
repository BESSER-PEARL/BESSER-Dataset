import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NHSM::State,
    NHSM::StateMachine,
    NHSM::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nhsm::state_is_not_abstract():
    assert not inspect.isabstract(NHSM::State)


def test_nhsm::state_constructor_exists():
    assert callable(NHSM::State.__init__)


def test_nhsm::state_constructor_args():
    sig = inspect.signature(NHSM::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nhsm::state_has_name():
    assert hasattr(NHSM::State, "name")
    descriptor = None
    for klass in NHSM::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nhsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(NHSM::StateMachine)


def test_nhsm::statemachine_constructor_exists():
    assert callable(NHSM::StateMachine.__init__)


def test_nhsm::statemachine_constructor_args():
    sig = inspect.signature(NHSM::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_nhsm::transition_is_not_abstract():
    assert not inspect.isabstract(NHSM::Transition)


def test_nhsm::transition_constructor_exists():
    assert callable(NHSM::Transition.__init__)


def test_nhsm::transition_constructor_args():
    sig = inspect.signature(NHSM::Transition.__init__)
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
NHSM::State_strategy = st.builds(
    NHSM::State,
    name=
        safe_text
)
NHSM::StateMachine_strategy = st.builds(
    NHSM::StateMachine,
)
NHSM::Transition_strategy = st.builds(
    NHSM::Transition,
)

@given(instance=NHSM::State_strategy)
@settings(max_examples=50)
def test_nhsm::state_instantiation(instance):
    assert isinstance(instance, NHSM::State)

@given(instance=NHSM::State_strategy)
def test_nhsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=NHSM::State_strategy)
def test_nhsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NHSM::StateMachine_strategy)
@settings(max_examples=50)
def test_nhsm::statemachine_instantiation(instance):
    assert isinstance(instance, NHSM::StateMachine)

@given(instance=NHSM::Transition_strategy)
@settings(max_examples=50)
def test_nhsm::transition_instantiation(instance):
    assert isinstance(instance, NHSM::Transition)
