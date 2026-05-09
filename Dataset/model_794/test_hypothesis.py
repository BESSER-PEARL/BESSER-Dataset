import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ecore::Transition,
    ecore::State,
    ecore::FSM,
    ecore::ENamedElement,
    FSM,
    ecore::EClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecore::transition_is_not_abstract():
    assert not inspect.isabstract(ecore::Transition)


def test_ecore::transition_constructor_exists():
    assert callable(ecore::Transition.__init__)


def test_ecore::transition_constructor_args():
    sig = inspect.signature(ecore::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_ecore::transition_has_output():
    assert hasattr(ecore::Transition, "output")
    descriptor = None
    for klass in ecore::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_ecore::transition_has_input():
    assert hasattr(ecore::Transition, "input")
    descriptor = None
    for klass in ecore::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_ecore::state_is_not_abstract():
    assert not inspect.isabstract(ecore::State)


def test_ecore::state_constructor_exists():
    assert callable(ecore::State.__init__)


def test_ecore::state_constructor_args():
    sig = inspect.signature(ecore::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecore::state_has_name():
    assert hasattr(ecore::State, "name")
    descriptor = None
    for klass in ecore::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecore::fsm_is_not_abstract():
    assert not inspect.isabstract(ecore::FSM)


def test_ecore::fsm_constructor_exists():
    assert callable(ecore::FSM.__init__)


def test_ecore::fsm_constructor_args():
    sig = inspect.signature(ecore::FSM.__init__)
    params = list(sig.parameters.keys())



def test_ecore::enamedelement_is_not_abstract():
    assert not inspect.isabstract(ecore::ENamedElement)


def test_ecore::enamedelement_constructor_exists():
    assert callable(ecore::ENamedElement.__init__)


def test_ecore::enamedelement_constructor_args():
    sig = inspect.signature(ecore::ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_ecore::eclass_is_not_abstract():
    assert not inspect.isabstract(ecore::EClass)


def test_ecore::eclass_constructor_exists():
    assert callable(ecore::EClass.__init__)


def test_ecore::eclass_constructor_args():
    sig = inspect.signature(ecore::EClass.__init__)
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
ecore::Transition_strategy = st.builds(
    ecore::Transition,
    output=
        safe_text,
    input=
        safe_text
)
ecore::State_strategy = st.builds(
    ecore::State,
    name=
        safe_text
)
ecore::FSM_strategy = st.builds(
    ecore::FSM,
)
ecore::ENamedElement_strategy = st.builds(
    ecore::ENamedElement,
)
FSM_strategy = st.builds(
    FSM,
)
ecore::EClass_strategy = st.builds(
    ecore::EClass,
)

@given(instance=ecore::Transition_strategy)
@settings(max_examples=50)
def test_ecore::transition_instantiation(instance):
    assert isinstance(instance, ecore::Transition)

@given(instance=ecore::Transition_strategy)
def test_ecore::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=ecore::Transition_strategy)
def test_ecore::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=ecore::Transition_strategy)
def test_ecore::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=ecore::Transition_strategy)
def test_ecore::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=ecore::State_strategy)
@settings(max_examples=50)
def test_ecore::state_instantiation(instance):
    assert isinstance(instance, ecore::State)

@given(instance=ecore::State_strategy)
def test_ecore::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecore::State_strategy)
def test_ecore::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecore::FSM_strategy)
@settings(max_examples=50)
def test_ecore::fsm_instantiation(instance):
    assert isinstance(instance, ecore::FSM)

@given(instance=ecore::ENamedElement_strategy)
@settings(max_examples=50)
def test_ecore::enamedelement_instantiation(instance):
    assert isinstance(instance, ecore::ENamedElement)

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=ecore::EClass_strategy)
@settings(max_examples=50)
def test_ecore::eclass_instantiation(instance):
    assert isinstance(instance, ecore::EClass)
