import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StatemachineMetamodel_State,
    StatemachineMetamodel_Statemachine,
    StatemachineMetamodel_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachinemetamodel_state_is_not_abstract():
    assert not inspect.isabstract(StatemachineMetamodel_State)


def test_statemachinemetamodel_state_constructor_exists():
    assert callable(StatemachineMetamodel_State.__init__)


def test_statemachinemetamodel_state_constructor_args():
    sig = inspect.signature(StatemachineMetamodel_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinemetamodel_state_has_name():
    assert hasattr(StatemachineMetamodel_State, "name")
    descriptor = None
    for klass in StatemachineMetamodel_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinemetamodel_statemachine_is_not_abstract():
    assert not inspect.isabstract(StatemachineMetamodel_Statemachine)


def test_statemachinemetamodel_statemachine_constructor_exists():
    assert callable(StatemachineMetamodel_Statemachine.__init__)


def test_statemachinemetamodel_statemachine_constructor_args():
    sig = inspect.signature(StatemachineMetamodel_Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachinemetamodel_transition_is_not_abstract():
    assert not inspect.isabstract(StatemachineMetamodel_Transition)


def test_statemachinemetamodel_transition_constructor_exists():
    assert callable(StatemachineMetamodel_Transition.__init__)


def test_statemachinemetamodel_transition_constructor_args():
    sig = inspect.signature(StatemachineMetamodel_Transition.__init__)
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
StatemachineMetamodel_State_strategy = st.builds(
    StatemachineMetamodel_State,
    name=
        safe_text
)
StatemachineMetamodel_Statemachine_strategy = st.builds(
    StatemachineMetamodel_Statemachine,
)
StatemachineMetamodel_Transition_strategy = st.builds(
    StatemachineMetamodel_Transition,
)

@given(instance=StatemachineMetamodel_State_strategy)
@settings(max_examples=50)
def test_statemachinemetamodel_state_instantiation(instance):
    assert isinstance(instance, StatemachineMetamodel_State)



@given(instance=StatemachineMetamodel_State_strategy)
def test_statemachinemetamodel_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StatemachineMetamodel_Statemachine_strategy)
@settings(max_examples=50)
def test_statemachinemetamodel_statemachine_instantiation(instance):
    assert isinstance(instance, StatemachineMetamodel_Statemachine)

@given(instance=StatemachineMetamodel_Transition_strategy)
@settings(max_examples=50)
def test_statemachinemetamodel_transition_instantiation(instance):
    assert isinstance(instance, StatemachineMetamodel_Transition)
