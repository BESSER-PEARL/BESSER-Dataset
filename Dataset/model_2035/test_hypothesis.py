import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dsl::Command,
    dsl::Transition,
    dsl::State,
    dsl::Event,
    dsl::Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl::command_is_not_abstract():
    assert not inspect.isabstract(dsl::Command)


def test_dsl::command_constructor_exists():
    assert callable(dsl::Command.__init__)


def test_dsl::command_constructor_args():
    sig = inspect.signature(dsl::Command.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_dsl::command_has_name():
    assert hasattr(dsl::Command, "name")
    descriptor = None
    for klass in dsl::Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl::command_has_code():
    assert hasattr(dsl::Command, "code")
    descriptor = None
    for klass in dsl::Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_dsl::transition_is_not_abstract():
    assert not inspect.isabstract(dsl::Transition)


def test_dsl::transition_constructor_exists():
    assert callable(dsl::Transition.__init__)


def test_dsl::transition_constructor_args():
    sig = inspect.signature(dsl::Transition.__init__)
    params = list(sig.parameters.keys())



def test_dsl::state_is_not_abstract():
    assert not inspect.isabstract(dsl::State)


def test_dsl::state_constructor_exists():
    assert callable(dsl::State.__init__)


def test_dsl::state_constructor_args():
    sig = inspect.signature(dsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::state_has_name():
    assert hasattr(dsl::State, "name")
    descriptor = None
    for klass in dsl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::event_is_not_abstract():
    assert not inspect.isabstract(dsl::Event)


def test_dsl::event_constructor_exists():
    assert callable(dsl::Event.__init__)


def test_dsl::event_constructor_args():
    sig = inspect.signature(dsl::Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::event_has_code():
    assert hasattr(dsl::Event, "code")
    descriptor = None
    for klass in dsl::Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_dsl::event_has_name():
    assert hasattr(dsl::Event, "name")
    descriptor = None
    for klass in dsl::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::statemachine_is_not_abstract():
    assert not inspect.isabstract(dsl::Statemachine)


def test_dsl::statemachine_constructor_exists():
    assert callable(dsl::Statemachine.__init__)


def test_dsl::statemachine_constructor_args():
    sig = inspect.signature(dsl::Statemachine.__init__)
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
dsl::Command_strategy = st.builds(
    dsl::Command,
    name=
        safe_text,
    code=
        safe_text
)
dsl::Transition_strategy = st.builds(
    dsl::Transition,
)
dsl::State_strategy = st.builds(
    dsl::State,
    name=
        safe_text
)
dsl::Event_strategy = st.builds(
    dsl::Event,
    code=
        safe_text,
    name=
        safe_text
)
dsl::Statemachine_strategy = st.builds(
    dsl::Statemachine,
)

@given(instance=dsl::Command_strategy)
@settings(max_examples=50)
def test_dsl::command_instantiation(instance):
    assert isinstance(instance, dsl::Command)

@given(instance=dsl::Command_strategy)
def test_dsl::command_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Command_strategy)
def test_dsl::command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Command_strategy)
def test_dsl::command_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=dsl::Command_strategy)
def test_dsl::command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=dsl::Transition_strategy)
@settings(max_examples=50)
def test_dsl::transition_instantiation(instance):
    assert isinstance(instance, dsl::Transition)

@given(instance=dsl::State_strategy)
@settings(max_examples=50)
def test_dsl::state_instantiation(instance):
    assert isinstance(instance, dsl::State)

@given(instance=dsl::State_strategy)
def test_dsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::State_strategy)
def test_dsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Event_strategy)
@settings(max_examples=50)
def test_dsl::event_instantiation(instance):
    assert isinstance(instance, dsl::Event)

@given(instance=dsl::Event_strategy)
def test_dsl::event_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=dsl::Event_strategy)
def test_dsl::event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=dsl::Event_strategy)
def test_dsl::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Event_strategy)
def test_dsl::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Statemachine_strategy)
@settings(max_examples=50)
def test_dsl::statemachine_instantiation(instance):
    assert isinstance(instance, dsl::Statemachine)
