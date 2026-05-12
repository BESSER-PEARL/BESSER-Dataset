import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleStateMachineMetaModel_Transition,
    simpleStateMachineMetaModel_State,
    simpleStateMachineMetaModel_SimpleStateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplestatemachinemetamodel_transition_is_not_abstract():
    assert not inspect.isabstract(simpleStateMachineMetaModel_Transition)


def test_simplestatemachinemetamodel_transition_constructor_exists():
    assert callable(simpleStateMachineMetaModel_Transition.__init__)


def test_simplestatemachinemetamodel_transition_constructor_args():
    sig = inspect.signature(simpleStateMachineMetaModel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_simplestatemachinemetamodel_transition_has_Name():
    assert hasattr(simpleStateMachineMetaModel_Transition, "Name")
    descriptor = None
    for klass in simpleStateMachineMetaModel_Transition.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_simplestatemachinemetamodel_state_is_not_abstract():
    assert not inspect.isabstract(simpleStateMachineMetaModel_State)


def test_simplestatemachinemetamodel_state_constructor_exists():
    assert callable(simpleStateMachineMetaModel_State.__init__)


def test_simplestatemachinemetamodel_state_constructor_args():
    sig = inspect.signature(simpleStateMachineMetaModel_State.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_simplestatemachinemetamodel_state_has_Name():
    assert hasattr(simpleStateMachineMetaModel_State, "Name")
    descriptor = None
    for klass in simpleStateMachineMetaModel_State.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_simplestatemachinemetamodel_simplestatemachine_is_not_abstract():
    assert not inspect.isabstract(simpleStateMachineMetaModel_SimpleStateMachine)


def test_simplestatemachinemetamodel_simplestatemachine_constructor_exists():
    assert callable(simpleStateMachineMetaModel_SimpleStateMachine.__init__)


def test_simplestatemachinemetamodel_simplestatemachine_constructor_args():
    sig = inspect.signature(simpleStateMachineMetaModel_SimpleStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_simplestatemachinemetamodel_simplestatemachine_has_Name():
    assert hasattr(simpleStateMachineMetaModel_SimpleStateMachine, "Name")
    descriptor = None
    for klass in simpleStateMachineMetaModel_SimpleStateMachine.__mro__:
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
simpleStateMachineMetaModel_Transition_strategy = st.builds(
    simpleStateMachineMetaModel_Transition,
    Name=
        safe_text
)
simpleStateMachineMetaModel_State_strategy = st.builds(
    simpleStateMachineMetaModel_State,
    Name=
        safe_text
)
simpleStateMachineMetaModel_SimpleStateMachine_strategy = st.builds(
    simpleStateMachineMetaModel_SimpleStateMachine,
    Name=
        safe_text
)

@given(instance=simpleStateMachineMetaModel_Transition_strategy)
@settings(max_examples=50)
def test_simplestatemachinemetamodel_transition_instantiation(instance):
    assert isinstance(instance, simpleStateMachineMetaModel_Transition)



@given(instance=simpleStateMachineMetaModel_Transition_strategy)
def test_simplestatemachinemetamodel_transition_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=simpleStateMachineMetaModel_State_strategy)
@settings(max_examples=50)
def test_simplestatemachinemetamodel_state_instantiation(instance):
    assert isinstance(instance, simpleStateMachineMetaModel_State)



@given(instance=simpleStateMachineMetaModel_State_strategy)
def test_simplestatemachinemetamodel_state_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=simpleStateMachineMetaModel_SimpleStateMachine_strategy)
@settings(max_examples=50)
def test_simplestatemachinemetamodel_simplestatemachine_instantiation(instance):
    assert isinstance(instance, simpleStateMachineMetaModel_SimpleStateMachine)



@given(instance=simpleStateMachineMetaModel_SimpleStateMachine_strategy)
def test_simplestatemachinemetamodel_simplestatemachine_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
