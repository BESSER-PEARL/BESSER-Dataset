import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    eMFProject::State,
    eMFProject::Command,
    eMFProject::Event,
    eMFProject::Transition,
    eMFProject::Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emfproject::state_is_not_abstract():
    assert not inspect.isabstract(eMFProject::State)


def test_emfproject::state_constructor_exists():
    assert callable(eMFProject::State.__init__)


def test_emfproject::state_constructor_args():
    sig = inspect.signature(eMFProject::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emfproject::state_has_name():
    assert hasattr(eMFProject::State, "name")
    descriptor = None
    for klass in eMFProject::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emfproject::command_is_not_abstract():
    assert not inspect.isabstract(eMFProject::Command)


def test_emfproject::command_constructor_exists():
    assert callable(eMFProject::Command.__init__)


def test_emfproject::command_constructor_args():
    sig = inspect.signature(eMFProject::Command.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_emfproject::command_has_code():
    assert hasattr(eMFProject::Command, "code")
    descriptor = None
    for klass in eMFProject::Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_emfproject::command_has_name():
    assert hasattr(eMFProject::Command, "name")
    descriptor = None
    for klass in eMFProject::Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emfproject::event_is_not_abstract():
    assert not inspect.isabstract(eMFProject::Event)


def test_emfproject::event_constructor_exists():
    assert callable(eMFProject::Event.__init__)


def test_emfproject::event_constructor_args():
    sig = inspect.signature(eMFProject::Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_emfproject::event_has_code():
    assert hasattr(eMFProject::Event, "code")
    descriptor = None
    for klass in eMFProject::Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_emfproject::event_has_name():
    assert hasattr(eMFProject::Event, "name")
    descriptor = None
    for klass in eMFProject::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emfproject::transition_is_not_abstract():
    assert not inspect.isabstract(eMFProject::Transition)


def test_emfproject::transition_constructor_exists():
    assert callable(eMFProject::Transition.__init__)


def test_emfproject::transition_constructor_args():
    sig = inspect.signature(eMFProject::Transition.__init__)
    params = list(sig.parameters.keys())



def test_emfproject::statemachine_is_not_abstract():
    assert not inspect.isabstract(eMFProject::Statemachine)


def test_emfproject::statemachine_constructor_exists():
    assert callable(eMFProject::Statemachine.__init__)


def test_emfproject::statemachine_constructor_args():
    sig = inspect.signature(eMFProject::Statemachine.__init__)
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
eMFProject::State_strategy = st.builds(
    eMFProject::State,
    name=
        safe_text
)
eMFProject::Command_strategy = st.builds(
    eMFProject::Command,
    code=
        safe_text,
    name=
        safe_text
)
eMFProject::Event_strategy = st.builds(
    eMFProject::Event,
    code=
        safe_text,
    name=
        safe_text
)
eMFProject::Transition_strategy = st.builds(
    eMFProject::Transition,
)
eMFProject::Statemachine_strategy = st.builds(
    eMFProject::Statemachine,
)

@given(instance=eMFProject::State_strategy)
@settings(max_examples=50)
def test_emfproject::state_instantiation(instance):
    assert isinstance(instance, eMFProject::State)

@given(instance=eMFProject::State_strategy)
def test_emfproject::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eMFProject::State_strategy)
def test_emfproject::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eMFProject::Command_strategy)
@settings(max_examples=50)
def test_emfproject::command_instantiation(instance):
    assert isinstance(instance, eMFProject::Command)

@given(instance=eMFProject::Command_strategy)
def test_emfproject::command_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=eMFProject::Command_strategy)
def test_emfproject::command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=eMFProject::Command_strategy)
def test_emfproject::command_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eMFProject::Command_strategy)
def test_emfproject::command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eMFProject::Event_strategy)
@settings(max_examples=50)
def test_emfproject::event_instantiation(instance):
    assert isinstance(instance, eMFProject::Event)

@given(instance=eMFProject::Event_strategy)
def test_emfproject::event_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=eMFProject::Event_strategy)
def test_emfproject::event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=eMFProject::Event_strategy)
def test_emfproject::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eMFProject::Event_strategy)
def test_emfproject::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eMFProject::Transition_strategy)
@settings(max_examples=50)
def test_emfproject::transition_instantiation(instance):
    assert isinstance(instance, eMFProject::Transition)

@given(instance=eMFProject::Statemachine_strategy)
@settings(max_examples=50)
def test_emfproject::statemachine_instantiation(instance):
    assert isinstance(instance, eMFProject::Statemachine)
