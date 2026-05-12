import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ecore_Transition,
    ecore_State,
    ecore_FSM,
    ecore_ENamedElement,
    FSM,
    ecore_EClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecore_transition_is_not_abstract():
    assert not inspect.isabstract(ecore_Transition)


def test_ecore_transition_constructor_exists():
    assert callable(ecore_Transition.__init__)


def test_ecore_transition_constructor_args():
    sig = inspect.signature(ecore_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_ecore_transition_has_input():
    assert hasattr(ecore_Transition, "input")
    descriptor = None
    for klass in ecore_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_ecore_transition_has_output():
    assert hasattr(ecore_Transition, "output")
    descriptor = None
    for klass in ecore_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_ecore_state_is_not_abstract():
    assert not inspect.isabstract(ecore_State)


def test_ecore_state_constructor_exists():
    assert callable(ecore_State.__init__)


def test_ecore_state_constructor_args():
    sig = inspect.signature(ecore_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecore_state_has_name():
    assert hasattr(ecore_State, "name")
    descriptor = None
    for klass in ecore_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecore_fsm_is_not_abstract():
    assert not inspect.isabstract(ecore_FSM)


def test_ecore_fsm_constructor_exists():
    assert callable(ecore_FSM.__init__)


def test_ecore_fsm_constructor_args():
    sig = inspect.signature(ecore_FSM.__init__)
    params = list(sig.parameters.keys())



def test_ecore_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ecore_ENamedElement)


def test_ecore_enamedelement_constructor_exists():
    assert callable(ecore_ENamedElement.__init__)


def test_ecore_enamedelement_constructor_args():
    sig = inspect.signature(ecore_ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_ecore_eclass_is_not_abstract():
    assert not inspect.isabstract(ecore_EClass)


def test_ecore_eclass_constructor_exists():
    assert callable(ecore_EClass.__init__)


def test_ecore_eclass_constructor_args():
    sig = inspect.signature(ecore_EClass.__init__)
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
ecore_Transition_strategy = st.builds(
    ecore_Transition,
    input=
        safe_text,
    output=
        safe_text
)
ecore_State_strategy = st.builds(
    ecore_State,
    name=
        safe_text
)
ecore_FSM_strategy = st.builds(
    ecore_FSM,
)
ecore_ENamedElement_strategy = st.builds(
    ecore_ENamedElement,
)
FSM_strategy = st.builds(
    FSM,
)
ecore_EClass_strategy = st.builds(
    ecore_EClass,
)

@given(instance=ecore_Transition_strategy)
@settings(max_examples=50)
def test_ecore_transition_instantiation(instance):
    assert isinstance(instance, ecore_Transition)



@given(instance=ecore_Transition_strategy)
def test_ecore_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=ecore_Transition_strategy)
def test_ecore_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=ecore_State_strategy)
@settings(max_examples=50)
def test_ecore_state_instantiation(instance):
    assert isinstance(instance, ecore_State)



@given(instance=ecore_State_strategy)
def test_ecore_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecore_FSM_strategy)
@settings(max_examples=50)
def test_ecore_fsm_instantiation(instance):
    assert isinstance(instance, ecore_FSM)

@given(instance=ecore_ENamedElement_strategy)
@settings(max_examples=50)
def test_ecore_enamedelement_instantiation(instance):
    assert isinstance(instance, ecore_ENamedElement)

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=ecore_EClass_strategy)
@settings(max_examples=50)
def test_ecore_eclass_instantiation(instance):
    assert isinstance(instance, ecore_EClass)
