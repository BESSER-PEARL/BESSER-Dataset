import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractStateElement,
    stateMachine::State,
    stateMachine::AbstractMachineElement,
    stateMachine::StateMachine,
    AbstractMachineElement,
    stateMachine::AbstractStateElement,
    stateMachine::StateTransition,
    VisibilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstateelement_is_not_abstract():
    assert not inspect.isabstract(AbstractStateElement)


def test_abstractstateelement_constructor_exists():
    assert callable(AbstractStateElement.__init__)


def test_abstractstateelement_constructor_args():
    sig = inspect.signature(AbstractStateElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(stateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(stateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(stateMachine::State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::abstractmachineelement_is_not_abstract():
    assert not inspect.isabstract(stateMachine::AbstractMachineElement)


def test_statemachine::abstractmachineelement_constructor_exists():
    assert callable(stateMachine::AbstractMachineElement.__init__)


def test_statemachine::abstractmachineelement_constructor_args():
    sig = inspect.signature(stateMachine::AbstractMachineElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(stateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(stateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_name():
    assert hasattr(stateMachine::StateMachine, "name")
    descriptor = None
    for klass in stateMachine::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractmachineelement_is_not_abstract():
    assert not inspect.isabstract(AbstractMachineElement)


def test_abstractmachineelement_constructor_exists():
    assert callable(AbstractMachineElement.__init__)


def test_abstractmachineelement_constructor_args():
    sig = inspect.signature(AbstractMachineElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::abstractstateelement_is_not_abstract():
    assert not inspect.isabstract(stateMachine::AbstractStateElement)


def test_statemachine::abstractstateelement_constructor_exists():
    assert callable(stateMachine::AbstractStateElement.__init__)


def test_statemachine::abstractstateelement_constructor_args():
    sig = inspect.signature(stateMachine::AbstractStateElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::abstractstateelement_has_name():
    assert hasattr(stateMachine::AbstractStateElement, "name")
    descriptor = None
    for klass in stateMachine::AbstractStateElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statetransition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StateTransition)


def test_statemachine::statetransition_constructor_exists():
    assert callable(stateMachine::StateTransition.__init__)


def test_statemachine::statetransition_constructor_args():
    sig = inspect.signature(stateMachine::StateTransition.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_statemachine::statetransition_has_visibility():
    assert hasattr(stateMachine::StateTransition, "visibility")
    descriptor = None
    for klass in stateMachine::StateTransition.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_visibilitytype_exists():
    # Check that the Enumeration exists
    assert VisibilityType is not None

def test_visibilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityType]
    expected_literals = [
        "PUBLIC",
        "PRIVATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityType"


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
AbstractStateElement_strategy = st.builds(
    AbstractStateElement,
)
stateMachine::State_strategy = st.builds(
    stateMachine::State,
)
stateMachine::AbstractMachineElement_strategy = st.builds(
    stateMachine::AbstractMachineElement,
)
stateMachine::StateMachine_strategy = st.builds(
    stateMachine::StateMachine,
    name=
        safe_text
)
AbstractMachineElement_strategy = st.builds(
    AbstractMachineElement,
)
stateMachine::AbstractStateElement_strategy = st.builds(
    stateMachine::AbstractStateElement,
    name=
        safe_text
)
stateMachine::StateTransition_strategy = st.builds(
    stateMachine::StateTransition,
    visibility=
        safe_text
)

@given(instance=AbstractStateElement_strategy)
@settings(max_examples=50)
def test_abstractstateelement_instantiation(instance):
    assert isinstance(instance, AbstractStateElement)

@given(instance=stateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, stateMachine::State)

@given(instance=stateMachine::AbstractMachineElement_strategy)
@settings(max_examples=50)
def test_statemachine::abstractmachineelement_instantiation(instance):
    assert isinstance(instance, stateMachine::AbstractMachineElement)

@given(instance=stateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine::StateMachine)

@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractMachineElement_strategy)
@settings(max_examples=50)
def test_abstractmachineelement_instantiation(instance):
    assert isinstance(instance, AbstractMachineElement)

@given(instance=stateMachine::AbstractStateElement_strategy)
@settings(max_examples=50)
def test_statemachine::abstractstateelement_instantiation(instance):
    assert isinstance(instance, stateMachine::AbstractStateElement)

@given(instance=stateMachine::AbstractStateElement_strategy)
def test_statemachine::abstractstateelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::AbstractStateElement_strategy)
def test_statemachine::abstractstateelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::StateTransition_strategy)
@settings(max_examples=50)
def test_statemachine::statetransition_instantiation(instance):
    assert isinstance(instance, stateMachine::StateTransition)

@given(instance=stateMachine::StateTransition_strategy)
def test_statemachine::statetransition_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=stateMachine::StateTransition_strategy)
def test_statemachine::statetransition_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original
