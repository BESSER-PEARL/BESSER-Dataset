import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    complexStateMachineMetaModel::CompositeState,
    complexStateMachineMetaModel::Transition,
    complexStateMachineMetaModel::State,
    complexStateMachineMetaModel::ComplexStateMachine,
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



def test_complexstatemachinemetamodel::compositestate_is_not_abstract():
    assert not inspect.isabstract(complexStateMachineMetaModel::CompositeState)


def test_complexstatemachinemetamodel::compositestate_constructor_exists():
    assert callable(complexStateMachineMetaModel::CompositeState.__init__)


def test_complexstatemachinemetamodel::compositestate_constructor_args():
    sig = inspect.signature(complexStateMachineMetaModel::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_complexstatemachinemetamodel::transition_is_not_abstract():
    assert not inspect.isabstract(complexStateMachineMetaModel::Transition)


def test_complexstatemachinemetamodel::transition_constructor_exists():
    assert callable(complexStateMachineMetaModel::Transition.__init__)


def test_complexstatemachinemetamodel::transition_constructor_args():
    sig = inspect.signature(complexStateMachineMetaModel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_complexstatemachinemetamodel::transition_has_Name():
    assert hasattr(complexStateMachineMetaModel::Transition, "Name")
    descriptor = None
    for klass in complexStateMachineMetaModel::Transition.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_complexstatemachinemetamodel::state_is_not_abstract():
    assert not inspect.isabstract(complexStateMachineMetaModel::State)


def test_complexstatemachinemetamodel::state_constructor_exists():
    assert callable(complexStateMachineMetaModel::State.__init__)


def test_complexstatemachinemetamodel::state_constructor_args():
    sig = inspect.signature(complexStateMachineMetaModel::State.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_complexstatemachinemetamodel::state_has_Name():
    assert hasattr(complexStateMachineMetaModel::State, "Name")
    descriptor = None
    for klass in complexStateMachineMetaModel::State.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_complexstatemachinemetamodel::complexstatemachine_is_not_abstract():
    assert not inspect.isabstract(complexStateMachineMetaModel::ComplexStateMachine)


def test_complexstatemachinemetamodel::complexstatemachine_constructor_exists():
    assert callable(complexStateMachineMetaModel::ComplexStateMachine.__init__)


def test_complexstatemachinemetamodel::complexstatemachine_constructor_args():
    sig = inspect.signature(complexStateMachineMetaModel::ComplexStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_complexstatemachinemetamodel::complexstatemachine_has_Name():
    assert hasattr(complexStateMachineMetaModel::ComplexStateMachine, "Name")
    descriptor = None
    for klass in complexStateMachineMetaModel::ComplexStateMachine.__mro__:
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
State_strategy = st.builds(
    State,
)
complexStateMachineMetaModel::CompositeState_strategy = st.builds(
    complexStateMachineMetaModel::CompositeState,
)
complexStateMachineMetaModel::Transition_strategy = st.builds(
    complexStateMachineMetaModel::Transition,
    Name=
        safe_text
)
complexStateMachineMetaModel::State_strategy = st.builds(
    complexStateMachineMetaModel::State,
    Name=
        safe_text
)
complexStateMachineMetaModel::ComplexStateMachine_strategy = st.builds(
    complexStateMachineMetaModel::ComplexStateMachine,
    Name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=complexStateMachineMetaModel::CompositeState_strategy)
@settings(max_examples=50)
def test_complexstatemachinemetamodel::compositestate_instantiation(instance):
    assert isinstance(instance, complexStateMachineMetaModel::CompositeState)

@given(instance=complexStateMachineMetaModel::Transition_strategy)
@settings(max_examples=50)
def test_complexstatemachinemetamodel::transition_instantiation(instance):
    assert isinstance(instance, complexStateMachineMetaModel::Transition)

@given(instance=complexStateMachineMetaModel::Transition_strategy)
def test_complexstatemachinemetamodel::transition_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=complexStateMachineMetaModel::Transition_strategy)
def test_complexstatemachinemetamodel::transition_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=complexStateMachineMetaModel::State_strategy)
@settings(max_examples=50)
def test_complexstatemachinemetamodel::state_instantiation(instance):
    assert isinstance(instance, complexStateMachineMetaModel::State)

@given(instance=complexStateMachineMetaModel::State_strategy)
def test_complexstatemachinemetamodel::state_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=complexStateMachineMetaModel::State_strategy)
def test_complexstatemachinemetamodel::state_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=complexStateMachineMetaModel::ComplexStateMachine_strategy)
@settings(max_examples=50)
def test_complexstatemachinemetamodel::complexstatemachine_instantiation(instance):
    assert isinstance(instance, complexStateMachineMetaModel::ComplexStateMachine)

@given(instance=complexStateMachineMetaModel::ComplexStateMachine_strategy)
def test_complexstatemachinemetamodel::complexstatemachine_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=complexStateMachineMetaModel::ComplexStateMachine_strategy)
def test_complexstatemachinemetamodel::complexstatemachine_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
