import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_NamedElement,
    NamedElement,
    fsm_State,
    fsm_Transition,
    fsm_FSMSystem,
    fsm_Buffer,
    fsm_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm_NamedElement)


def test_fsm_namedelement_constructor_exists():
    assert callable(fsm_NamedElement.__init__)


def test_fsm_namedelement_constructor_args():
    sig = inspect.signature(fsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_namedelement_has_name():
    assert hasattr(fsm_NamedElement, "name")
    descriptor = None
    for klass in fsm_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_fsm_transition_has_output():
    assert hasattr(fsm_Transition, "output")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_input():
    assert hasattr(fsm_Transition, "input")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_fsm_fsmsystem_is_not_abstract():
    assert not inspect.isabstract(fsm_FSMSystem)


def test_fsm_fsmsystem_constructor_exists():
    assert callable(fsm_FSMSystem.__init__)


def test_fsm_fsmsystem_constructor_args():
    sig = inspect.signature(fsm_FSMSystem.__init__)
    params = list(sig.parameters.keys())



def test_fsm_buffer_is_not_abstract():
    assert not inspect.isabstract(fsm_Buffer)


def test_fsm_buffer_constructor_exists():
    assert callable(fsm_Buffer.__init__)


def test_fsm_buffer_constructor_args():
    sig = inspect.signature(fsm_Buffer.__init__)
    params = list(sig.parameters.keys())
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_fsm_buffer_has_initialValue():
    assert hasattr(fsm_Buffer, "initialValue")
    descriptor = None
    for klass in fsm_Buffer.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(fsm_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(fsm_StateMachine.__init__)
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
fsm_NamedElement_strategy = st.builds(
    fsm_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm_State_strategy = st.builds(
    fsm_State,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    output=
        safe_text,
    input=
        safe_text
)
fsm_FSMSystem_strategy = st.builds(
    fsm_FSMSystem,
)
fsm_Buffer_strategy = st.builds(
    fsm_Buffer,
    initialValue=
        safe_text
)
fsm_StateMachine_strategy = st.builds(
    fsm_StateMachine,
)

@given(instance=fsm_NamedElement_strategy)
@settings(max_examples=50)
def test_fsm_namedelement_instantiation(instance):
    assert isinstance(instance, fsm_NamedElement)



@given(instance=fsm_NamedElement_strategy)
def test_fsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=fsm_FSMSystem_strategy)
@settings(max_examples=50)
def test_fsm_fsmsystem_instantiation(instance):
    assert isinstance(instance, fsm_FSMSystem)

@given(instance=fsm_Buffer_strategy)
@settings(max_examples=50)
def test_fsm_buffer_instantiation(instance):
    assert isinstance(instance, fsm_Buffer)



@given(instance=fsm_Buffer_strategy)
def test_fsm_buffer_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, fsm_StateMachine)
