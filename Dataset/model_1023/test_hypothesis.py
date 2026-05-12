import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractState,
    FSM_RegularState,
    FSM_InitialState,
    FSM_CompositeState,
    FSM_AbstractState,
    FSM_Transition,
    FSM_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_regularstate_is_not_abstract():
    assert not inspect.isabstract(FSM_RegularState)


def test_fsm_regularstate_constructor_exists():
    assert callable(FSM_RegularState.__init__)


def test_fsm_regularstate_constructor_args():
    sig = inspect.signature(FSM_RegularState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(FSM_InitialState)


def test_fsm_initialstate_constructor_exists():
    assert callable(FSM_InitialState.__init__)


def test_fsm_initialstate_constructor_args():
    sig = inspect.signature(FSM_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_compositestate_is_not_abstract():
    assert not inspect.isabstract(FSM_CompositeState)


def test_fsm_compositestate_constructor_exists():
    assert callable(FSM_CompositeState.__init__)


def test_fsm_compositestate_constructor_args():
    sig = inspect.signature(FSM_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(FSM_AbstractState)


def test_fsm_abstractstate_constructor_exists():
    assert callable(FSM_AbstractState.__init__)


def test_fsm_abstractstate_constructor_args():
    sig = inspect.signature(FSM_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_abstractstate_has_name():
    assert hasattr(FSM_AbstractState, "name")
    descriptor = None
    for klass in FSM_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(FSM_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(FSM_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(FSM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_fsm_transition_has_label():
    assert hasattr(FSM_Transition, "label")
    descriptor = None
    for klass in FSM_Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(FSM_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(FSM_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_statemachine_has_name():
    assert hasattr(FSM_StateMachine, "name")
    descriptor = None
    for klass in FSM_StateMachine.__mro__:
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
AbstractState_strategy = st.builds(
    AbstractState,
)
FSM_RegularState_strategy = st.builds(
    FSM_RegularState,
)
FSM_InitialState_strategy = st.builds(
    FSM_InitialState,
)
FSM_CompositeState_strategy = st.builds(
    FSM_CompositeState,
)
FSM_AbstractState_strategy = st.builds(
    FSM_AbstractState,
    name=
        safe_text
)
FSM_Transition_strategy = st.builds(
    FSM_Transition,
    label=
        safe_text
)
FSM_StateMachine_strategy = st.builds(
    FSM_StateMachine,
    name=
        safe_text
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=FSM_RegularState_strategy)
@settings(max_examples=50)
def test_fsm_regularstate_instantiation(instance):
    assert isinstance(instance, FSM_RegularState)

@given(instance=FSM_InitialState_strategy)
@settings(max_examples=50)
def test_fsm_initialstate_instantiation(instance):
    assert isinstance(instance, FSM_InitialState)

@given(instance=FSM_CompositeState_strategy)
@settings(max_examples=50)
def test_fsm_compositestate_instantiation(instance):
    assert isinstance(instance, FSM_CompositeState)

@given(instance=FSM_AbstractState_strategy)
@settings(max_examples=50)
def test_fsm_abstractstate_instantiation(instance):
    assert isinstance(instance, FSM_AbstractState)



@given(instance=FSM_AbstractState_strategy)
def test_fsm_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, FSM_Transition)



@given(instance=FSM_Transition_strategy)
def test_fsm_transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=FSM_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, FSM_StateMachine)



@given(instance=FSM_StateMachine_strategy)
def test_fsm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
