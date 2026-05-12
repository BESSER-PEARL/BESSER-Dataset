import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsmSample::Transition,
    fsmSample::Action,
    fsmSample::State,
    fsmSample::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsmsample::transition_is_not_abstract():
    assert not inspect.isabstract(fsmSample::Transition)


def test_fsmsample::transition_constructor_exists():
    assert callable(fsmSample::Transition.__init__)


def test_fsmsample::transition_constructor_args():
    sig = inspect.signature(fsmSample::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsmsample::transition_has_output():
    assert hasattr(fsmSample::Transition, "output")
    descriptor = None
    for klass in fsmSample::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_fsmsample::transition_has_input():
    assert hasattr(fsmSample::Transition, "input")
    descriptor = None
    for klass in fsmSample::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_fsmsample::transition_has_name():
    assert hasattr(fsmSample::Transition, "name")
    descriptor = None
    for klass in fsmSample::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmsample::action_is_not_abstract():
    assert not inspect.isabstract(fsmSample::Action)


def test_fsmsample::action_constructor_exists():
    assert callable(fsmSample::Action.__init__)


def test_fsmsample::action_constructor_args():
    sig = inspect.signature(fsmSample::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmsample::action_has_name():
    assert hasattr(fsmSample::Action, "name")
    descriptor = None
    for klass in fsmSample::Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmsample::state_is_not_abstract():
    assert not inspect.isabstract(fsmSample::State)


def test_fsmsample::state_constructor_exists():
    assert callable(fsmSample::State.__init__)


def test_fsmsample::state_constructor_args():
    sig = inspect.signature(fsmSample::State.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsmsample::state_has_version():
    assert hasattr(fsmSample::State, "version")
    descriptor = None
    for klass in fsmSample::State.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_fsmsample::state_has_name():
    assert hasattr(fsmSample::State, "name")
    descriptor = None
    for klass in fsmSample::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmsample::fsm_is_not_abstract():
    assert not inspect.isabstract(fsmSample::FSM)


def test_fsmsample::fsm_constructor_exists():
    assert callable(fsmSample::FSM.__init__)


def test_fsmsample::fsm_constructor_args():
    sig = inspect.signature(fsmSample::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmsample::fsm_has_name():
    assert hasattr(fsmSample::FSM, "name")
    descriptor = None
    for klass in fsmSample::FSM.__mro__:
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
fsmSample::Transition_strategy = st.builds(
    fsmSample::Transition,
    output=
        safe_text,
    input=
        safe_text,
    name=
        safe_text
)
fsmSample::Action_strategy = st.builds(
    fsmSample::Action,
    name=
        safe_text
)
fsmSample::State_strategy = st.builds(
    fsmSample::State,
    version=
        safe_text,
    name=
        safe_text
)
fsmSample::FSM_strategy = st.builds(
    fsmSample::FSM,
    name=
        safe_text
)

@given(instance=fsmSample::Transition_strategy)
@settings(max_examples=50)
def test_fsmsample::transition_instantiation(instance):
    assert isinstance(instance, fsmSample::Transition)

@given(instance=fsmSample::Transition_strategy)
def test_fsmsample::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=fsmSample::Transition_strategy)
def test_fsmsample::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=fsmSample::Transition_strategy)
def test_fsmsample::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=fsmSample::Transition_strategy)
def test_fsmsample::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=fsmSample::Transition_strategy)
def test_fsmsample::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsmSample::Transition_strategy)
def test_fsmsample::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsmSample::Action_strategy)
@settings(max_examples=50)
def test_fsmsample::action_instantiation(instance):
    assert isinstance(instance, fsmSample::Action)

@given(instance=fsmSample::Action_strategy)
def test_fsmsample::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsmSample::Action_strategy)
def test_fsmsample::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsmSample::State_strategy)
@settings(max_examples=50)
def test_fsmsample::state_instantiation(instance):
    assert isinstance(instance, fsmSample::State)

@given(instance=fsmSample::State_strategy)
def test_fsmsample::state_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=fsmSample::State_strategy)
def test_fsmsample::state_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=fsmSample::State_strategy)
def test_fsmsample::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsmSample::State_strategy)
def test_fsmsample::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsmSample::FSM_strategy)
@settings(max_examples=50)
def test_fsmsample::fsm_instantiation(instance):
    assert isinstance(instance, fsmSample::FSM)

@given(instance=fsmSample::FSM_strategy)
def test_fsmsample::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsmSample::FSM_strategy)
def test_fsmsample::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
