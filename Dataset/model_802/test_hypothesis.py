import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    k3fsm::Transition,
    k3fsm::State,
    k3fsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_k3fsm::transition_is_not_abstract():
    assert not inspect.isabstract(k3fsm::Transition)


def test_k3fsm::transition_constructor_exists():
    assert callable(k3fsm::Transition.__init__)


def test_k3fsm::transition_constructor_args():
    sig = inspect.signature(k3fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_k3fsm::transition_has_name():
    assert hasattr(k3fsm::Transition, "name")
    descriptor = None
    for klass in k3fsm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm::transition_has_output():
    assert hasattr(k3fsm::Transition, "output")
    descriptor = None
    for klass in k3fsm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm::transition_has_input():
    assert hasattr(k3fsm::Transition, "input")
    descriptor = None
    for klass in k3fsm::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_k3fsm::state_is_not_abstract():
    assert not inspect.isabstract(k3fsm::State)


def test_k3fsm::state_constructor_exists():
    assert callable(k3fsm::State.__init__)


def test_k3fsm::state_constructor_args():
    sig = inspect.signature(k3fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_k3fsm::state_has_name():
    assert hasattr(k3fsm::State, "name")
    descriptor = None
    for klass in k3fsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_k3fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(k3fsm::FSM)


def test_k3fsm::fsm_constructor_exists():
    assert callable(k3fsm::FSM.__init__)


def test_k3fsm::fsm_constructor_args():
    sig = inspect.signature(k3fsm::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "producedString" in params, "Missing parameter 'producedString'"
    assert "consummedString" in params, "Missing parameter 'consummedString'"
    assert "unprocessedString" in params, "Missing parameter 'unprocessedString'"
    assert "name" in params, "Missing parameter 'name'"

def test_k3fsm::fsm_has_producedString():
    assert hasattr(k3fsm::FSM, "producedString")
    descriptor = None
    for klass in k3fsm::FSM.__mro__:
        if "producedString" in klass.__dict__:
            descriptor = klass.__dict__["producedString"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm::fsm_has_consummedString():
    assert hasattr(k3fsm::FSM, "consummedString")
    descriptor = None
    for klass in k3fsm::FSM.__mro__:
        if "consummedString" in klass.__dict__:
            descriptor = klass.__dict__["consummedString"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm::fsm_has_unprocessedString():
    assert hasattr(k3fsm::FSM, "unprocessedString")
    descriptor = None
    for klass in k3fsm::FSM.__mro__:
        if "unprocessedString" in klass.__dict__:
            descriptor = klass.__dict__["unprocessedString"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm::fsm_has_name():
    assert hasattr(k3fsm::FSM, "name")
    descriptor = None
    for klass in k3fsm::FSM.__mro__:
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
k3fsm::Transition_strategy = st.builds(
    k3fsm::Transition,
    name=
        safe_text,
    output=
        safe_text,
    input=
        safe_text
)
k3fsm::State_strategy = st.builds(
    k3fsm::State,
    name=
        safe_text
)
k3fsm::FSM_strategy = st.builds(
    k3fsm::FSM,
    producedString=
        safe_text,
    consummedString=
        safe_text,
    unprocessedString=
        safe_text,
    name=
        safe_text
)

@given(instance=k3fsm::Transition_strategy)
@settings(max_examples=50)
def test_k3fsm::transition_instantiation(instance):
    assert isinstance(instance, k3fsm::Transition)

@given(instance=k3fsm::Transition_strategy)
def test_k3fsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=k3fsm::Transition_strategy)
def test_k3fsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=k3fsm::Transition_strategy)
def test_k3fsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=k3fsm::Transition_strategy)
def test_k3fsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=k3fsm::Transition_strategy)
def test_k3fsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=k3fsm::Transition_strategy)
def test_k3fsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=k3fsm::State_strategy)
@settings(max_examples=50)
def test_k3fsm::state_instantiation(instance):
    assert isinstance(instance, k3fsm::State)

@given(instance=k3fsm::State_strategy)
def test_k3fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=k3fsm::State_strategy)
def test_k3fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=k3fsm::FSM_strategy)
@settings(max_examples=50)
def test_k3fsm::fsm_instantiation(instance):
    assert isinstance(instance, k3fsm::FSM)

@given(instance=k3fsm::FSM_strategy)
def test_k3fsm::fsm_producedString_type(instance):
    assert isinstance(instance.producedString, str)


@given(instance=k3fsm::FSM_strategy)
def test_k3fsm::fsm_producedString_setter(instance):
    original = instance.producedString
    instance.producedString = original
    assert instance.producedString == original

@given(instance=k3fsm::FSM_strategy)
def test_k3fsm::fsm_consummedString_type(instance):
    assert isinstance(instance.consummedString, str)


@given(instance=k3fsm::FSM_strategy)
def test_k3fsm::fsm_consummedString_setter(instance):
    original = instance.consummedString
    instance.consummedString = original
    assert instance.consummedString == original

@given(instance=k3fsm::FSM_strategy)
def test_k3fsm::fsm_unprocessedString_type(instance):
    assert isinstance(instance.unprocessedString, str)


@given(instance=k3fsm::FSM_strategy)
def test_k3fsm::fsm_unprocessedString_setter(instance):
    original = instance.unprocessedString
    instance.unprocessedString = original
    assert instance.unprocessedString == original

@given(instance=k3fsm::FSM_strategy)
def test_k3fsm::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=k3fsm::FSM_strategy)
def test_k3fsm::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
