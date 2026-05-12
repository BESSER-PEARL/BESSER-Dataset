import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsmcore_NamedElement,
    fsmcore_Trigger,
    fsmcore_Constraint,
    fsmcore_Program,
    NamedElement,
    fsmcore_State,
    fsmcore_Transition,
    fsmcore_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsmcore_namedelement_is_not_abstract():
    assert not inspect.isabstract(fsmcore_NamedElement)


def test_fsmcore_namedelement_constructor_exists():
    assert callable(fsmcore_NamedElement.__init__)


def test_fsmcore_namedelement_constructor_args():
    sig = inspect.signature(fsmcore_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmcore_namedelement_has_name():
    assert hasattr(fsmcore_NamedElement, "name")
    descriptor = None
    for klass in fsmcore_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmcore_trigger_is_not_abstract():
    assert not inspect.isabstract(fsmcore_Trigger)


def test_fsmcore_trigger_constructor_exists():
    assert callable(fsmcore_Trigger.__init__)


def test_fsmcore_trigger_constructor_args():
    sig = inspect.signature(fsmcore_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsmcore_trigger_has_expression():
    assert hasattr(fsmcore_Trigger, "expression")
    descriptor = None
    for klass in fsmcore_Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_fsmcore_constraint_is_not_abstract():
    assert not inspect.isabstract(fsmcore_Constraint)


def test_fsmcore_constraint_constructor_exists():
    assert callable(fsmcore_Constraint.__init__)


def test_fsmcore_constraint_constructor_args():
    sig = inspect.signature(fsmcore_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore_program_is_not_abstract():
    assert not inspect.isabstract(fsmcore_Program)


def test_fsmcore_program_constructor_exists():
    assert callable(fsmcore_Program.__init__)


def test_fsmcore_program_constructor_args():
    sig = inspect.signature(fsmcore_Program.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore_state_is_not_abstract():
    assert not inspect.isabstract(fsmcore_State)


def test_fsmcore_state_constructor_exists():
    assert callable(fsmcore_State.__init__)


def test_fsmcore_state_constructor_args():
    sig = inspect.signature(fsmcore_State.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore_transition_is_not_abstract():
    assert not inspect.isabstract(fsmcore_Transition)


def test_fsmcore_transition_constructor_exists():
    assert callable(fsmcore_Transition.__init__)


def test_fsmcore_transition_constructor_args():
    sig = inspect.signature(fsmcore_Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsmcore_StateMachine)


def test_fsmcore_statemachine_constructor_exists():
    assert callable(fsmcore_StateMachine.__init__)


def test_fsmcore_statemachine_constructor_args():
    sig = inspect.signature(fsmcore_StateMachine.__init__)
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
fsmcore_NamedElement_strategy = st.builds(
    fsmcore_NamedElement,
    name=
        safe_text
)
fsmcore_Trigger_strategy = st.builds(
    fsmcore_Trigger,
    expression=
        safe_text
)
fsmcore_Constraint_strategy = st.builds(
    fsmcore_Constraint,
)
fsmcore_Program_strategy = st.builds(
    fsmcore_Program,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsmcore_State_strategy = st.builds(
    fsmcore_State,
)
fsmcore_Transition_strategy = st.builds(
    fsmcore_Transition,
)
fsmcore_StateMachine_strategy = st.builds(
    fsmcore_StateMachine,
)

@given(instance=fsmcore_NamedElement_strategy)
@settings(max_examples=50)
def test_fsmcore_namedelement_instantiation(instance):
    assert isinstance(instance, fsmcore_NamedElement)



@given(instance=fsmcore_NamedElement_strategy)
def test_fsmcore_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsmcore_Trigger_strategy)
@settings(max_examples=50)
def test_fsmcore_trigger_instantiation(instance):
    assert isinstance(instance, fsmcore_Trigger)



@given(instance=fsmcore_Trigger_strategy)
def test_fsmcore_trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=fsmcore_Constraint_strategy)
@settings(max_examples=50)
def test_fsmcore_constraint_instantiation(instance):
    assert isinstance(instance, fsmcore_Constraint)

@given(instance=fsmcore_Program_strategy)
@settings(max_examples=50)
def test_fsmcore_program_instantiation(instance):
    assert isinstance(instance, fsmcore_Program)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsmcore_State_strategy)
@settings(max_examples=50)
def test_fsmcore_state_instantiation(instance):
    assert isinstance(instance, fsmcore_State)

@given(instance=fsmcore_Transition_strategy)
@settings(max_examples=50)
def test_fsmcore_transition_instantiation(instance):
    assert isinstance(instance, fsmcore_Transition)

@given(instance=fsmcore_StateMachine_strategy)
@settings(max_examples=50)
def test_fsmcore_statemachine_instantiation(instance):
    assert isinstance(instance, fsmcore_StateMachine)
