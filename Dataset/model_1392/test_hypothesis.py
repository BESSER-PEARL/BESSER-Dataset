import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StatemachineMetamodel::State,
    StatemachineMetamodel::Statemachine,
    StatemachineMetamodel::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachinemetamodel::state_is_not_abstract():
    assert not inspect.isabstract(StatemachineMetamodel::State)


def test_statemachinemetamodel::state_constructor_exists():
    assert callable(StatemachineMetamodel::State.__init__)


def test_statemachinemetamodel::state_constructor_args():
    sig = inspect.signature(StatemachineMetamodel::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinemetamodel::state_has_name():
    assert hasattr(StatemachineMetamodel::State, "name")
    descriptor = None
    for klass in StatemachineMetamodel::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinemetamodel::statemachine_is_not_abstract():
    assert not inspect.isabstract(StatemachineMetamodel::Statemachine)


def test_statemachinemetamodel::statemachine_constructor_exists():
    assert callable(StatemachineMetamodel::Statemachine.__init__)


def test_statemachinemetamodel::statemachine_constructor_args():
    sig = inspect.signature(StatemachineMetamodel::Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachinemetamodel::transition_is_not_abstract():
    assert not inspect.isabstract(StatemachineMetamodel::Transition)


def test_statemachinemetamodel::transition_constructor_exists():
    assert callable(StatemachineMetamodel::Transition.__init__)


def test_statemachinemetamodel::transition_constructor_args():
    sig = inspect.signature(StatemachineMetamodel::Transition.__init__)
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
StatemachineMetamodel::State_strategy = st.builds(
    StatemachineMetamodel::State,
    name=
        safe_text
)
StatemachineMetamodel::Statemachine_strategy = st.builds(
    StatemachineMetamodel::Statemachine,
)
StatemachineMetamodel::Transition_strategy = st.builds(
    StatemachineMetamodel::Transition,
)

@given(instance=StatemachineMetamodel::State_strategy)
@settings(max_examples=50)
def test_statemachinemetamodel::state_instantiation(instance):
    assert isinstance(instance, StatemachineMetamodel::State)

@given(instance=StatemachineMetamodel::State_strategy)
def test_statemachinemetamodel::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StatemachineMetamodel::State_strategy)
def test_statemachinemetamodel::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StatemachineMetamodel::Statemachine_strategy)
@settings(max_examples=50)
def test_statemachinemetamodel::statemachine_instantiation(instance):
    assert isinstance(instance, StatemachineMetamodel::Statemachine)

@given(instance=StatemachineMetamodel::Transition_strategy)
@settings(max_examples=50)
def test_statemachinemetamodel::transition_instantiation(instance):
    assert isinstance(instance, StatemachineMetamodel::Transition)
