import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Transition,
    fsm::State,
    fsm::FiniteStateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "name" in params, "Missing parameter 'name'"
    assert "input" in params, "Missing parameter 'input'"

def test_fsm::transition_has_output():
    assert hasattr(fsm::Transition, "output")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_name():
    assert hasattr(fsm::Transition, "name")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_input():
    assert hasattr(fsm::Transition, "input")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isInitialState" in params, "Missing parameter 'isInitialState'"

def test_fsm::state_has_name():
    assert hasattr(fsm::State, "name")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm::state_has_isInitialState():
    assert hasattr(fsm::State, "isInitialState")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "isInitialState" in klass.__dict__:
            descriptor = klass.__dict__["isInitialState"]
            break
    assert isinstance(descriptor, property)



def test_fsm::finitestatemachine_is_not_abstract():
    assert not inspect.isabstract(fsm::FiniteStateMachine)


def test_fsm::finitestatemachine_constructor_exists():
    assert callable(fsm::FiniteStateMachine.__init__)


def test_fsm::finitestatemachine_constructor_args():
    sig = inspect.signature(fsm::FiniteStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::finitestatemachine_has_name():
    assert hasattr(fsm::FiniteStateMachine, "name")
    descriptor = None
    for klass in fsm::FiniteStateMachine.__mro__:
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
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    output=
        safe_text,
    name=
        safe_text,
    input=
        safe_text
)
fsm::State_strategy = st.builds(
    fsm::State,
    name=
        safe_text,
    isInitialState=
        st.booleans()
)
fsm::FiniteStateMachine_strategy = st.builds(
    fsm::FiniteStateMachine,
    name=
        safe_text
)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::State_strategy)
def test_fsm::state_isInitialState_type(instance):
    assert isinstance(instance.isInitialState, bool)


@given(instance=fsm::State_strategy)
def test_fsm::state_isInitialState_setter(instance):
    original = instance.isInitialState
    instance.isInitialState = original
    assert instance.isInitialState == original

@given(instance=fsm::FiniteStateMachine_strategy)
@settings(max_examples=50)
def test_fsm::finitestatemachine_instantiation(instance):
    assert isinstance(instance, fsm::FiniteStateMachine)

@given(instance=fsm::FiniteStateMachine_strategy)
def test_fsm::finitestatemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::FiniteStateMachine_strategy)
def test_fsm::finitestatemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
