import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleStateMachineMetaModel::Transition,
    simpleStateMachineMetaModel::State,
    simpleStateMachineMetaModel::SimpleStateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplestatemachinemetamodel::transition_is_not_abstract():
    assert not inspect.isabstract(simpleStateMachineMetaModel::Transition)


def test_simplestatemachinemetamodel::transition_constructor_exists():
    assert callable(simpleStateMachineMetaModel::Transition.__init__)


def test_simplestatemachinemetamodel::transition_constructor_args():
    sig = inspect.signature(simpleStateMachineMetaModel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_simplestatemachinemetamodel::transition_has_Name():
    assert hasattr(simpleStateMachineMetaModel::Transition, "Name")
    descriptor = None
    for klass in simpleStateMachineMetaModel::Transition.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_simplestatemachinemetamodel::state_is_not_abstract():
    assert not inspect.isabstract(simpleStateMachineMetaModel::State)


def test_simplestatemachinemetamodel::state_constructor_exists():
    assert callable(simpleStateMachineMetaModel::State.__init__)


def test_simplestatemachinemetamodel::state_constructor_args():
    sig = inspect.signature(simpleStateMachineMetaModel::State.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_simplestatemachinemetamodel::state_has_Name():
    assert hasattr(simpleStateMachineMetaModel::State, "Name")
    descriptor = None
    for klass in simpleStateMachineMetaModel::State.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_simplestatemachinemetamodel::simplestatemachine_is_not_abstract():
    assert not inspect.isabstract(simpleStateMachineMetaModel::SimpleStateMachine)


def test_simplestatemachinemetamodel::simplestatemachine_constructor_exists():
    assert callable(simpleStateMachineMetaModel::SimpleStateMachine.__init__)


def test_simplestatemachinemetamodel::simplestatemachine_constructor_args():
    sig = inspect.signature(simpleStateMachineMetaModel::SimpleStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_simplestatemachinemetamodel::simplestatemachine_has_Name():
    assert hasattr(simpleStateMachineMetaModel::SimpleStateMachine, "Name")
    descriptor = None
    for klass in simpleStateMachineMetaModel::SimpleStateMachine.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
simpleStateMachineMetaModel::Transition_strategy = st.builds(
    simpleStateMachineMetaModel::Transition,
    Name=
        safe_text
)
simpleStateMachineMetaModel::State_strategy = st.builds(
    simpleStateMachineMetaModel::State,
    Name=
        safe_text
)
simpleStateMachineMetaModel::SimpleStateMachine_strategy = st.builds(
    simpleStateMachineMetaModel::SimpleStateMachine,
    Name=
        safe_text
)

@given(instance=simpleStateMachineMetaModel::Transition_strategy)
@settings(max_examples=50)
def test_simplestatemachinemetamodel::transition_instantiation(instance):
    assert isinstance(instance, simpleStateMachineMetaModel::Transition)

@given(instance=simpleStateMachineMetaModel::Transition_strategy)
def test_simplestatemachinemetamodel::transition_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=simpleStateMachineMetaModel::Transition_strategy)
def test_simplestatemachinemetamodel::transition_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=simpleStateMachineMetaModel::State_strategy)
@settings(max_examples=50)
def test_simplestatemachinemetamodel::state_instantiation(instance):
    assert isinstance(instance, simpleStateMachineMetaModel::State)

@given(instance=simpleStateMachineMetaModel::State_strategy)
def test_simplestatemachinemetamodel::state_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=simpleStateMachineMetaModel::State_strategy)
def test_simplestatemachinemetamodel::state_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=simpleStateMachineMetaModel::SimpleStateMachine_strategy)
@settings(max_examples=50)
def test_simplestatemachinemetamodel::simplestatemachine_instantiation(instance):
    assert isinstance(instance, simpleStateMachineMetaModel::SimpleStateMachine)

@given(instance=simpleStateMachineMetaModel::SimpleStateMachine_strategy)
def test_simplestatemachinemetamodel::simplestatemachine_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=simpleStateMachineMetaModel::SimpleStateMachine_strategy)
def test_simplestatemachinemetamodel::simplestatemachine_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
