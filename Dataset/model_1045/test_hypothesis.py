import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FAbstractState,
    FSM_FRegularState,
    FSM_FInitialState,
    FSM_FTransition,
    FSM_FStateMachine,
    FSM_FAbstractState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fabstractstate_is_not_abstract():
    assert not inspect.isabstract(FAbstractState)


def test_fabstractstate_constructor_exists():
    assert callable(FAbstractState.__init__)


def test_fabstractstate_constructor_args():
    sig = inspect.signature(FAbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_fregularstate_is_not_abstract():
    assert not inspect.isabstract(FSM_FRegularState)


def test_fsm_fregularstate_constructor_exists():
    assert callable(FSM_FRegularState.__init__)


def test_fsm_fregularstate_constructor_args():
    sig = inspect.signature(FSM_FRegularState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_finitialstate_is_not_abstract():
    assert not inspect.isabstract(FSM_FInitialState)


def test_fsm_finitialstate_constructor_exists():
    assert callable(FSM_FInitialState.__init__)


def test_fsm_finitialstate_constructor_args():
    sig = inspect.signature(FSM_FInitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_ftransition_is_not_abstract():
    assert not inspect.isabstract(FSM_FTransition)


def test_fsm_ftransition_constructor_exists():
    assert callable(FSM_FTransition.__init__)


def test_fsm_ftransition_constructor_args():
    sig = inspect.signature(FSM_FTransition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_fsm_ftransition_has_label():
    assert hasattr(FSM_FTransition, "label")
    descriptor = None
    for klass in FSM_FTransition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_fsm_fstatemachine_is_not_abstract():
    assert not inspect.isabstract(FSM_FStateMachine)


def test_fsm_fstatemachine_constructor_exists():
    assert callable(FSM_FStateMachine.__init__)


def test_fsm_fstatemachine_constructor_args():
    sig = inspect.signature(FSM_FStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_fstatemachine_has_name():
    assert hasattr(FSM_FStateMachine, "name")
    descriptor = None
    for klass in FSM_FStateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_fabstractstate_is_not_abstract():
    assert not inspect.isabstract(FSM_FAbstractState)


def test_fsm_fabstractstate_constructor_exists():
    assert callable(FSM_FAbstractState.__init__)


def test_fsm_fabstractstate_constructor_args():
    sig = inspect.signature(FSM_FAbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_fabstractstate_has_name():
    assert hasattr(FSM_FAbstractState, "name")
    descriptor = None
    for klass in FSM_FAbstractState.__mro__:
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
FAbstractState_strategy = st.builds(
    FAbstractState,
)
FSM_FRegularState_strategy = st.builds(
    FSM_FRegularState,
)
FSM_FInitialState_strategy = st.builds(
    FSM_FInitialState,
)
FSM_FTransition_strategy = st.builds(
    FSM_FTransition,
    label=
        safe_text
)
FSM_FStateMachine_strategy = st.builds(
    FSM_FStateMachine,
    name=
        safe_text
)
FSM_FAbstractState_strategy = st.builds(
    FSM_FAbstractState,
    name=
        safe_text
)

@given(instance=FAbstractState_strategy)
@settings(max_examples=50)
def test_fabstractstate_instantiation(instance):
    assert isinstance(instance, FAbstractState)

@given(instance=FSM_FRegularState_strategy)
@settings(max_examples=50)
def test_fsm_fregularstate_instantiation(instance):
    assert isinstance(instance, FSM_FRegularState)

@given(instance=FSM_FInitialState_strategy)
@settings(max_examples=50)
def test_fsm_finitialstate_instantiation(instance):
    assert isinstance(instance, FSM_FInitialState)

@given(instance=FSM_FTransition_strategy)
@settings(max_examples=50)
def test_fsm_ftransition_instantiation(instance):
    assert isinstance(instance, FSM_FTransition)



@given(instance=FSM_FTransition_strategy)
def test_fsm_ftransition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=FSM_FStateMachine_strategy)
@settings(max_examples=50)
def test_fsm_fstatemachine_instantiation(instance):
    assert isinstance(instance, FSM_FStateMachine)



@given(instance=FSM_FStateMachine_strategy)
def test_fsm_fstatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM_FAbstractState_strategy)
@settings(max_examples=50)
def test_fsm_fabstractstate_instantiation(instance):
    assert isinstance(instance, FSM_FAbstractState)



@given(instance=FSM_FAbstractState_strategy)
def test_fsm_fabstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
