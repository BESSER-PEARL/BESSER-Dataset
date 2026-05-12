import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    eMFProject_State,
    eMFProject_Command,
    eMFProject_Event,
    eMFProject_Transition,
    eMFProject_Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_emfproject_state_is_not_abstract():
    assert not inspect.isabstract(eMFProject_State)


def test_emfproject_state_constructor_exists():
    assert callable(eMFProject_State.__init__)


def test_emfproject_state_constructor_args():
    sig = inspect.signature(eMFProject_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emfproject_state_has_name():
    assert hasattr(eMFProject_State, "name")
    descriptor = None
    for klass in eMFProject_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emfproject_command_is_not_abstract():
    assert not inspect.isabstract(eMFProject_Command)


def test_emfproject_command_constructor_exists():
    assert callable(eMFProject_Command.__init__)


def test_emfproject_command_constructor_args():
    sig = inspect.signature(eMFProject_Command.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_emfproject_command_has_name():
    assert hasattr(eMFProject_Command, "name")
    descriptor = None
    for klass in eMFProject_Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_emfproject_command_has_code():
    assert hasattr(eMFProject_Command, "code")
    descriptor = None
    for klass in eMFProject_Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_emfproject_event_is_not_abstract():
    assert not inspect.isabstract(eMFProject_Event)


def test_emfproject_event_constructor_exists():
    assert callable(eMFProject_Event.__init__)


def test_emfproject_event_constructor_args():
    sig = inspect.signature(eMFProject_Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_emfproject_event_has_code():
    assert hasattr(eMFProject_Event, "code")
    descriptor = None
    for klass in eMFProject_Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_emfproject_event_has_name():
    assert hasattr(eMFProject_Event, "name")
    descriptor = None
    for klass in eMFProject_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emfproject_transition_is_not_abstract():
    assert not inspect.isabstract(eMFProject_Transition)


def test_emfproject_transition_constructor_exists():
    assert callable(eMFProject_Transition.__init__)


def test_emfproject_transition_constructor_args():
    sig = inspect.signature(eMFProject_Transition.__init__)
    params = list(sig.parameters.keys())



def test_emfproject_statemachine_is_not_abstract():
    assert not inspect.isabstract(eMFProject_Statemachine)


def test_emfproject_statemachine_constructor_exists():
    assert callable(eMFProject_Statemachine.__init__)


def test_emfproject_statemachine_constructor_args():
    sig = inspect.signature(eMFProject_Statemachine.__init__)
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
eMFProject_State_strategy = st.builds(
    eMFProject_State,
    name=
        safe_text
)
eMFProject_Command_strategy = st.builds(
    eMFProject_Command,
    name=
        safe_text,
    code=
        safe_text
)
eMFProject_Event_strategy = st.builds(
    eMFProject_Event,
    code=
        safe_text,
    name=
        safe_text
)
eMFProject_Transition_strategy = st.builds(
    eMFProject_Transition,
)
eMFProject_Statemachine_strategy = st.builds(
    eMFProject_Statemachine,
)

@given(instance=eMFProject_State_strategy)
@settings(max_examples=50)
def test_emfproject_state_instantiation(instance):
    assert isinstance(instance, eMFProject_State)



@given(instance=eMFProject_State_strategy)
def test_emfproject_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eMFProject_Command_strategy)
@settings(max_examples=50)
def test_emfproject_command_instantiation(instance):
    assert isinstance(instance, eMFProject_Command)



@given(instance=eMFProject_Command_strategy)
def test_emfproject_command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eMFProject_Command_strategy)
def test_emfproject_command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=eMFProject_Event_strategy)
@settings(max_examples=50)
def test_emfproject_event_instantiation(instance):
    assert isinstance(instance, eMFProject_Event)



@given(instance=eMFProject_Event_strategy)
def test_emfproject_event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=eMFProject_Event_strategy)
def test_emfproject_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eMFProject_Transition_strategy)
@settings(max_examples=50)
def test_emfproject_transition_instantiation(instance):
    assert isinstance(instance, eMFProject_Transition)

@given(instance=eMFProject_Statemachine_strategy)
@settings(max_examples=50)
def test_emfproject_statemachine_instantiation(instance):
    assert isinstance(instance, eMFProject_Statemachine)
