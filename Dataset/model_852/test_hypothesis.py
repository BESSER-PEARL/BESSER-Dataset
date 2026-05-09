import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FSM::State,
    FSM::StateMachine,
    FSM::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(FSM::State)


def test_fsm::state_constructor_exists():
    assert callable(FSM::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(FSM::State.__init__)
    params = list(sig.parameters.keys())
    assert "isAccepting" in params, "Missing parameter 'isAccepting'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::state_has_isAccepting():
    assert hasattr(FSM::State, "isAccepting")
    descriptor = None
    for klass in FSM::State.__mro__:
        if "isAccepting" in klass.__dict__:
            descriptor = klass.__dict__["isAccepting"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_name():
    assert hasattr(FSM::State, "name")
    descriptor = None
    for klass in FSM::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(FSM::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(FSM::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::statemachine_has_name():
    assert hasattr(FSM::StateMachine, "name")
    descriptor = None
    for klass in FSM::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(FSM::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(FSM::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(FSM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_fsm::transition_has_input():
    assert hasattr(FSM::Transition, "input")
    descriptor = None
    for klass in FSM::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
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
FSM::State_strategy = st.builds(
    FSM::State,
    isAccepting=
        st.booleans(),
    name=
        safe_text
)
FSM::StateMachine_strategy = st.builds(
    FSM::StateMachine,
    name=
        safe_text
)
FSM::Transition_strategy = st.builds(
    FSM::Transition,
    input=
        safe_text
)

@given(instance=FSM::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, FSM::State)

@given(instance=FSM::State_strategy)
def test_fsm::state_isAccepting_type(instance):
    assert isinstance(instance.isAccepting, bool)


@given(instance=FSM::State_strategy)
def test_fsm::state_isAccepting_setter(instance):
    original = instance.isAccepting
    instance.isAccepting = original
    assert instance.isAccepting == original

@given(instance=FSM::State_strategy)
def test_fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::State_strategy)
def test_fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, FSM::StateMachine)

@given(instance=FSM::StateMachine_strategy)
def test_fsm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::StateMachine_strategy)
def test_fsm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, FSM::Transition)

@given(instance=FSM::Transition_strategy)
def test_fsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=FSM::Transition_strategy)
def test_fsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original
