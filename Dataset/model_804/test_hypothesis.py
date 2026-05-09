import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    kfsm::Action,
    kfsm::Transition,
    kfsm::State,
    kfsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kfsm::action_is_not_abstract():
    assert not inspect.isabstract(kfsm::Action)


def test_kfsm::action_constructor_exists():
    assert callable(kfsm::Action.__init__)


def test_kfsm::action_constructor_args():
    sig = inspect.signature(kfsm::Action.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_kfsm::action_has_id():
    assert hasattr(kfsm::Action, "id")
    descriptor = None
    for klass in kfsm::Action.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_kfsm::transition_is_not_abstract():
    assert not inspect.isabstract(kfsm::Transition)


def test_kfsm::transition_constructor_exists():
    assert callable(kfsm::Transition.__init__)


def test_kfsm::transition_constructor_args():
    sig = inspect.signature(kfsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_kfsm::transition_has_input():
    assert hasattr(kfsm::Transition, "input")
    descriptor = None
    for klass in kfsm::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_kfsm::transition_has_output():
    assert hasattr(kfsm::Transition, "output")
    descriptor = None
    for klass in kfsm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_kfsm::state_is_not_abstract():
    assert not inspect.isabstract(kfsm::State)


def test_kfsm::state_constructor_exists():
    assert callable(kfsm::State.__init__)


def test_kfsm::state_constructor_args():
    sig = inspect.signature(kfsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kfsm::state_has_name():
    assert hasattr(kfsm::State, "name")
    descriptor = None
    for klass in kfsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kfsm::fsm_is_not_abstract():
    assert not inspect.isabstract(kfsm::FSM)


def test_kfsm::fsm_constructor_exists():
    assert callable(kfsm::FSM.__init__)


def test_kfsm::fsm_constructor_args():
    sig = inspect.signature(kfsm::FSM.__init__)
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
kfsm::Action_strategy = st.builds(
    kfsm::Action,
    id=
        safe_text
)
kfsm::Transition_strategy = st.builds(
    kfsm::Transition,
    input=
        safe_text,
    output=
        safe_text
)
kfsm::State_strategy = st.builds(
    kfsm::State,
    name=
        safe_text
)
kfsm::FSM_strategy = st.builds(
    kfsm::FSM,
)

@given(instance=kfsm::Action_strategy)
@settings(max_examples=50)
def test_kfsm::action_instantiation(instance):
    assert isinstance(instance, kfsm::Action)

@given(instance=kfsm::Action_strategy)
def test_kfsm::action_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=kfsm::Action_strategy)
def test_kfsm::action_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=kfsm::Transition_strategy)
@settings(max_examples=50)
def test_kfsm::transition_instantiation(instance):
    assert isinstance(instance, kfsm::Transition)

@given(instance=kfsm::Transition_strategy)
def test_kfsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=kfsm::Transition_strategy)
def test_kfsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=kfsm::Transition_strategy)
def test_kfsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=kfsm::Transition_strategy)
def test_kfsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=kfsm::State_strategy)
@settings(max_examples=50)
def test_kfsm::state_instantiation(instance):
    assert isinstance(instance, kfsm::State)

@given(instance=kfsm::State_strategy)
def test_kfsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kfsm::State_strategy)
def test_kfsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kfsm::FSM_strategy)
@settings(max_examples=50)
def test_kfsm::fsm_instantiation(instance):
    assert isinstance(instance, kfsm::FSM)
