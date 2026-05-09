import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    compositefsm::State,
    compositefsm::FSM,
    compositefsm::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_compositefsm::state_is_not_abstract():
    assert not inspect.isabstract(compositefsm::State)


def test_compositefsm::state_constructor_exists():
    assert callable(compositefsm::State.__init__)


def test_compositefsm::state_constructor_args():
    sig = inspect.signature(compositefsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_compositefsm::state_has_name():
    assert hasattr(compositefsm::State, "name")
    descriptor = None
    for klass in compositefsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_compositefsm::fsm_is_not_abstract():
    assert not inspect.isabstract(compositefsm::FSM)


def test_compositefsm::fsm_constructor_exists():
    assert callable(compositefsm::FSM.__init__)


def test_compositefsm::fsm_constructor_args():
    sig = inspect.signature(compositefsm::FSM.__init__)
    params = list(sig.parameters.keys())



def test_compositefsm::transition_is_not_abstract():
    assert not inspect.isabstract(compositefsm::Transition)


def test_compositefsm::transition_constructor_exists():
    assert callable(compositefsm::Transition.__init__)


def test_compositefsm::transition_constructor_args():
    sig = inspect.signature(compositefsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_compositefsm::transition_has_output():
    assert hasattr(compositefsm::Transition, "output")
    descriptor = None
    for klass in compositefsm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_compositefsm::transition_has_input():
    assert hasattr(compositefsm::Transition, "input")
    descriptor = None
    for klass in compositefsm::Transition.__mro__:
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
compositefsm::State_strategy = st.builds(
    compositefsm::State,
    name=
        safe_text
)
compositefsm::FSM_strategy = st.builds(
    compositefsm::FSM,
)
compositefsm::Transition_strategy = st.builds(
    compositefsm::Transition,
    output=
        safe_text,
    input=
        safe_text
)

@given(instance=compositefsm::State_strategy)
@settings(max_examples=50)
def test_compositefsm::state_instantiation(instance):
    assert isinstance(instance, compositefsm::State)

@given(instance=compositefsm::State_strategy)
def test_compositefsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=compositefsm::State_strategy)
def test_compositefsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=compositefsm::FSM_strategy)
@settings(max_examples=50)
def test_compositefsm::fsm_instantiation(instance):
    assert isinstance(instance, compositefsm::FSM)

@given(instance=compositefsm::Transition_strategy)
@settings(max_examples=50)
def test_compositefsm::transition_instantiation(instance):
    assert isinstance(instance, compositefsm::Transition)

@given(instance=compositefsm::Transition_strategy)
def test_compositefsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=compositefsm::Transition_strategy)
def test_compositefsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=compositefsm::Transition_strategy)
def test_compositefsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=compositefsm::Transition_strategy)
def test_compositefsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original
