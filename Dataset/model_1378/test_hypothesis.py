import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsmcore::NamedElement,
    fsmcore::Trigger,
    fsmcore::Constraint,
    fsmcore::Program,
    NamedElement,
    fsmcore::Transition,
    fsmcore::State,
    fsmcore::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsmcore::namedelement_is_not_abstract():
    assert not inspect.isabstract(fsmcore::NamedElement)


def test_fsmcore::namedelement_constructor_exists():
    assert callable(fsmcore::NamedElement.__init__)


def test_fsmcore::namedelement_constructor_args():
    sig = inspect.signature(fsmcore::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmcore::namedelement_has_name():
    assert hasattr(fsmcore::NamedElement, "name")
    descriptor = None
    for klass in fsmcore::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmcore::trigger_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Trigger)


def test_fsmcore::trigger_constructor_exists():
    assert callable(fsmcore::Trigger.__init__)


def test_fsmcore::trigger_constructor_args():
    sig = inspect.signature(fsmcore::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsmcore::trigger_has_expression():
    assert hasattr(fsmcore::Trigger, "expression")
    descriptor = None
    for klass in fsmcore::Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_fsmcore::constraint_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Constraint)


def test_fsmcore::constraint_constructor_exists():
    assert callable(fsmcore::Constraint.__init__)


def test_fsmcore::constraint_constructor_args():
    sig = inspect.signature(fsmcore::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::program_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Program)


def test_fsmcore::program_constructor_exists():
    assert callable(fsmcore::Program.__init__)


def test_fsmcore::program_constructor_args():
    sig = inspect.signature(fsmcore::Program.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::transition_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Transition)


def test_fsmcore::transition_constructor_exists():
    assert callable(fsmcore::Transition.__init__)


def test_fsmcore::transition_constructor_args():
    sig = inspect.signature(fsmcore::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::state_is_not_abstract():
    assert not inspect.isabstract(fsmcore::State)


def test_fsmcore::state_constructor_exists():
    assert callable(fsmcore::State.__init__)


def test_fsmcore::state_constructor_args():
    sig = inspect.signature(fsmcore::State.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsmcore::StateMachine)


def test_fsmcore::statemachine_constructor_exists():
    assert callable(fsmcore::StateMachine.__init__)


def test_fsmcore::statemachine_constructor_args():
    sig = inspect.signature(fsmcore::StateMachine.__init__)
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
fsmcore::NamedElement_strategy = st.builds(
    fsmcore::NamedElement,
    name=
        safe_text
)
fsmcore::Trigger_strategy = st.builds(
    fsmcore::Trigger,
    expression=
        safe_text
)
fsmcore::Constraint_strategy = st.builds(
    fsmcore::Constraint,
)
fsmcore::Program_strategy = st.builds(
    fsmcore::Program,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsmcore::Transition_strategy = st.builds(
    fsmcore::Transition,
)
fsmcore::State_strategy = st.builds(
    fsmcore::State,
)
fsmcore::StateMachine_strategy = st.builds(
    fsmcore::StateMachine,
)

@given(instance=fsmcore::NamedElement_strategy)
@settings(max_examples=50)
def test_fsmcore::namedelement_instantiation(instance):
    assert isinstance(instance, fsmcore::NamedElement)

@given(instance=fsmcore::NamedElement_strategy)
def test_fsmcore::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsmcore::NamedElement_strategy)
def test_fsmcore::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsmcore::Trigger_strategy)
@settings(max_examples=50)
def test_fsmcore::trigger_instantiation(instance):
    assert isinstance(instance, fsmcore::Trigger)

@given(instance=fsmcore::Trigger_strategy)
def test_fsmcore::trigger_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=fsmcore::Trigger_strategy)
def test_fsmcore::trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=fsmcore::Constraint_strategy)
@settings(max_examples=50)
def test_fsmcore::constraint_instantiation(instance):
    assert isinstance(instance, fsmcore::Constraint)

@given(instance=fsmcore::Program_strategy)
@settings(max_examples=50)
def test_fsmcore::program_instantiation(instance):
    assert isinstance(instance, fsmcore::Program)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsmcore::Transition_strategy)
@settings(max_examples=50)
def test_fsmcore::transition_instantiation(instance):
    assert isinstance(instance, fsmcore::Transition)

@given(instance=fsmcore::State_strategy)
@settings(max_examples=50)
def test_fsmcore::state_instantiation(instance):
    assert isinstance(instance, fsmcore::State)

@given(instance=fsmcore::StateMachine_strategy)
@settings(max_examples=50)
def test_fsmcore::statemachine_instantiation(instance):
    assert isinstance(instance, fsmcore::StateMachine)
