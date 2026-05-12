import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    FSM_State,
    FSM_StateMachine,
    FSM_FSMModel,
    FSM_Transition,
    FSM_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(FSM_State)


def test_fsm_state_constructor_exists():
    assert callable(FSM_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(FSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"

def test_fsm_state_has_isFinal():
    assert hasattr(FSM_State, "isFinal")
    descriptor = None
    for klass in FSM_State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(FSM_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(FSM_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_fsm_fsmmodel_is_not_abstract():
    assert not inspect.isabstract(FSM_FSMModel)


def test_fsm_fsmmodel_constructor_exists():
    assert callable(FSM_FSMModel.__init__)


def test_fsm_fsmmodel_constructor_args():
    sig = inspect.signature(FSM_FSMModel.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(FSM_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(FSM_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(FSM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_fsm_transition_has_output():
    assert hasattr(FSM_Transition, "output")
    descriptor = None
    for klass in FSM_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_input():
    assert hasattr(FSM_Transition, "input")
    descriptor = None
    for klass in FSM_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_fsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(FSM_NamedElement)


def test_fsm_namedelement_constructor_exists():
    assert callable(FSM_NamedElement.__init__)


def test_fsm_namedelement_constructor_args():
    sig = inspect.signature(FSM_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_namedelement_has_name():
    assert hasattr(FSM_NamedElement, "name")
    descriptor = None
    for klass in FSM_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
NamedElement_strategy = st.builds(
    NamedElement,
)
FSM_State_strategy = st.builds(
    FSM_State,
    isFinal=
        st.booleans()
)
FSM_StateMachine_strategy = st.builds(
    FSM_StateMachine,
)
FSM_FSMModel_strategy = st.builds(
    FSM_FSMModel,
)
FSM_Transition_strategy = st.builds(
    FSM_Transition,
    output=
        safe_text,
    input=
        safe_text
)
FSM_NamedElement_strategy = st.builds(
    FSM_NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=FSM_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, FSM_State)



@given(instance=FSM_State_strategy)
def test_fsm_state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=FSM_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, FSM_StateMachine)

@given(instance=FSM_FSMModel_strategy)
@settings(max_examples=50)
def test_fsm_fsmmodel_instantiation(instance):
    assert isinstance(instance, FSM_FSMModel)

@given(instance=FSM_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, FSM_Transition)



@given(instance=FSM_Transition_strategy)
def test_fsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=FSM_Transition_strategy)
def test_fsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=FSM_NamedElement_strategy)
@settings(max_examples=50)
def test_fsm_namedelement_instantiation(instance):
    assert isinstance(instance, FSM_NamedElement)



@given(instance=FSM_NamedElement_strategy)
def test_fsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
