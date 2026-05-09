import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FAbstractState,
    FSM::FRegularState,
    FSM::FInitialState,
    FSM::FTransition,
    FSM::FStateMachine,
    FSM::FAbstractState,
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



def test_fsm::fregularstate_is_not_abstract():
    assert not inspect.isabstract(FSM::FRegularState)


def test_fsm::fregularstate_constructor_exists():
    assert callable(FSM::FRegularState.__init__)


def test_fsm::fregularstate_constructor_args():
    sig = inspect.signature(FSM::FRegularState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::finitialstate_is_not_abstract():
    assert not inspect.isabstract(FSM::FInitialState)


def test_fsm::finitialstate_constructor_exists():
    assert callable(FSM::FInitialState.__init__)


def test_fsm::finitialstate_constructor_args():
    sig = inspect.signature(FSM::FInitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::ftransition_is_not_abstract():
    assert not inspect.isabstract(FSM::FTransition)


def test_fsm::ftransition_constructor_exists():
    assert callable(FSM::FTransition.__init__)


def test_fsm::ftransition_constructor_args():
    sig = inspect.signature(FSM::FTransition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_fsm::ftransition_has_label():
    assert hasattr(FSM::FTransition, "label")
    descriptor = None
    for klass in FSM::FTransition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_fsm::fstatemachine_is_not_abstract():
    assert not inspect.isabstract(FSM::FStateMachine)


def test_fsm::fstatemachine_constructor_exists():
    assert callable(FSM::FStateMachine.__init__)


def test_fsm::fstatemachine_constructor_args():
    sig = inspect.signature(FSM::FStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::fstatemachine_has_name():
    assert hasattr(FSM::FStateMachine, "name")
    descriptor = None
    for klass in FSM::FStateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::fabstractstate_is_not_abstract():
    assert not inspect.isabstract(FSM::FAbstractState)


def test_fsm::fabstractstate_constructor_exists():
    assert callable(FSM::FAbstractState.__init__)


def test_fsm::fabstractstate_constructor_args():
    sig = inspect.signature(FSM::FAbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::fabstractstate_has_name():
    assert hasattr(FSM::FAbstractState, "name")
    descriptor = None
    for klass in FSM::FAbstractState.__mro__:
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
FSM::FRegularState_strategy = st.builds(
    FSM::FRegularState,
)
FSM::FInitialState_strategy = st.builds(
    FSM::FInitialState,
)
FSM::FTransition_strategy = st.builds(
    FSM::FTransition,
    label=
        safe_text
)
FSM::FStateMachine_strategy = st.builds(
    FSM::FStateMachine,
    name=
        safe_text
)
FSM::FAbstractState_strategy = st.builds(
    FSM::FAbstractState,
    name=
        safe_text
)

@given(instance=FAbstractState_strategy)
@settings(max_examples=50)
def test_fabstractstate_instantiation(instance):
    assert isinstance(instance, FAbstractState)

@given(instance=FSM::FRegularState_strategy)
@settings(max_examples=50)
def test_fsm::fregularstate_instantiation(instance):
    assert isinstance(instance, FSM::FRegularState)

@given(instance=FSM::FInitialState_strategy)
@settings(max_examples=50)
def test_fsm::finitialstate_instantiation(instance):
    assert isinstance(instance, FSM::FInitialState)

@given(instance=FSM::FTransition_strategy)
@settings(max_examples=50)
def test_fsm::ftransition_instantiation(instance):
    assert isinstance(instance, FSM::FTransition)

@given(instance=FSM::FTransition_strategy)
def test_fsm::ftransition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=FSM::FTransition_strategy)
def test_fsm::ftransition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=FSM::FStateMachine_strategy)
@settings(max_examples=50)
def test_fsm::fstatemachine_instantiation(instance):
    assert isinstance(instance, FSM::FStateMachine)

@given(instance=FSM::FStateMachine_strategy)
def test_fsm::fstatemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::FStateMachine_strategy)
def test_fsm::fstatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM::FAbstractState_strategy)
@settings(max_examples=50)
def test_fsm::fabstractstate_instantiation(instance):
    assert isinstance(instance, FSM::FAbstractState)

@given(instance=FSM::FAbstractState_strategy)
def test_fsm::fabstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::FAbstractState_strategy)
def test_fsm::fabstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
