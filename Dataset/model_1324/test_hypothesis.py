import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractStateElement,
    stateMachine_State,
    stateMachine_AbstractMachineElement,
    stateMachine_StateMachine,
    AbstractMachineElement,
    stateMachine_AbstractStateElement,
    stateMachine_StateTransition,
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



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(stateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(stateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(stateMachine_State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_abstractmachineelement_is_not_abstract():
    assert not inspect.isabstract(stateMachine_AbstractMachineElement)


def test_statemachine_abstractmachineelement_constructor_exists():
    assert callable(stateMachine_AbstractMachineElement.__init__)


def test_statemachine_abstractmachineelement_constructor_args():
    sig = inspect.signature(stateMachine_AbstractMachineElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(stateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(stateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statemachine_has_name():
    assert hasattr(stateMachine_StateMachine, "name")
    descriptor = None
    for klass in stateMachine_StateMachine.__mro__:
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



def test_statemachine_abstractstateelement_is_not_abstract():
    assert not inspect.isabstract(stateMachine_AbstractStateElement)


def test_statemachine_abstractstateelement_constructor_exists():
    assert callable(stateMachine_AbstractStateElement.__init__)


def test_statemachine_abstractstateelement_constructor_args():
    sig = inspect.signature(stateMachine_AbstractStateElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_abstractstateelement_has_name():
    assert hasattr(stateMachine_AbstractStateElement, "name")
    descriptor = None
    for klass in stateMachine_AbstractStateElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statetransition_is_not_abstract():
    assert not inspect.isabstract(stateMachine_StateTransition)


def test_statemachine_statetransition_constructor_exists():
    assert callable(stateMachine_StateTransition.__init__)


def test_statemachine_statetransition_constructor_args():
    sig = inspect.signature(stateMachine_StateTransition.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_statemachine_statetransition_has_visibility():
    assert hasattr(stateMachine_StateTransition, "visibility")
    descriptor = None
    for klass in stateMachine_StateTransition.__mro__:
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
stateMachine_State_strategy = st.builds(
    stateMachine_State,
)
stateMachine_AbstractMachineElement_strategy = st.builds(
    stateMachine_AbstractMachineElement,
)
stateMachine_StateMachine_strategy = st.builds(
    stateMachine_StateMachine,
    name=
        safe_text
)
AbstractMachineElement_strategy = st.builds(
    AbstractMachineElement,
)
stateMachine_AbstractStateElement_strategy = st.builds(
    stateMachine_AbstractStateElement,
    name=
        safe_text
)
stateMachine_StateTransition_strategy = st.builds(
    stateMachine_StateTransition,
    visibility=
        safe_text
)

@given(instance=AbstractStateElement_strategy)
@settings(max_examples=50)
def test_abstractstateelement_instantiation(instance):
    assert isinstance(instance, AbstractStateElement)

@given(instance=stateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, stateMachine_State)

@given(instance=stateMachine_AbstractMachineElement_strategy)
@settings(max_examples=50)
def test_statemachine_abstractmachineelement_instantiation(instance):
    assert isinstance(instance, stateMachine_AbstractMachineElement)

@given(instance=stateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine_StateMachine)



@given(instance=stateMachine_StateMachine_strategy)
def test_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractMachineElement_strategy)
@settings(max_examples=50)
def test_abstractmachineelement_instantiation(instance):
    assert isinstance(instance, AbstractMachineElement)

@given(instance=stateMachine_AbstractStateElement_strategy)
@settings(max_examples=50)
def test_statemachine_abstractstateelement_instantiation(instance):
    assert isinstance(instance, stateMachine_AbstractStateElement)



@given(instance=stateMachine_AbstractStateElement_strategy)
def test_statemachine_abstractstateelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_StateTransition_strategy)
@settings(max_examples=50)
def test_statemachine_statetransition_instantiation(instance):
    assert isinstance(instance, stateMachine_StateTransition)



@given(instance=stateMachine_StateTransition_strategy)
def test_statemachine_statetransition_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original
