import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dsl_Command,
    dsl_Transition,
    dsl_State,
    dsl_Event,
    dsl_Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl_command_is_not_abstract():
    assert not inspect.isabstract(dsl_Command)


def test_dsl_command_constructor_exists():
    assert callable(dsl_Command.__init__)


def test_dsl_command_constructor_args():
    sig = inspect.signature(dsl_Command.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_command_has_code():
    assert hasattr(dsl_Command, "code")
    descriptor = None
    for klass in dsl_Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_dsl_command_has_name():
    assert hasattr(dsl_Command, "name")
    descriptor = None
    for klass in dsl_Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_transition_is_not_abstract():
    assert not inspect.isabstract(dsl_Transition)


def test_dsl_transition_constructor_exists():
    assert callable(dsl_Transition.__init__)


def test_dsl_transition_constructor_args():
    sig = inspect.signature(dsl_Transition.__init__)
    params = list(sig.parameters.keys())



def test_dsl_state_is_not_abstract():
    assert not inspect.isabstract(dsl_State)


def test_dsl_state_constructor_exists():
    assert callable(dsl_State.__init__)


def test_dsl_state_constructor_args():
    sig = inspect.signature(dsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_state_has_name():
    assert hasattr(dsl_State, "name")
    descriptor = None
    for klass in dsl_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_event_is_not_abstract():
    assert not inspect.isabstract(dsl_Event)


def test_dsl_event_constructor_exists():
    assert callable(dsl_Event.__init__)


def test_dsl_event_constructor_args():
    sig = inspect.signature(dsl_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_dsl_event_has_name():
    assert hasattr(dsl_Event, "name")
    descriptor = None
    for klass in dsl_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_event_has_code():
    assert hasattr(dsl_Event, "code")
    descriptor = None
    for klass in dsl_Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_dsl_statemachine_is_not_abstract():
    assert not inspect.isabstract(dsl_Statemachine)


def test_dsl_statemachine_constructor_exists():
    assert callable(dsl_Statemachine.__init__)


def test_dsl_statemachine_constructor_args():
    sig = inspect.signature(dsl_Statemachine.__init__)
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
dsl_Command_strategy = st.builds(
    dsl_Command,
    code=
        safe_text,
    name=
        safe_text
)
dsl_Transition_strategy = st.builds(
    dsl_Transition,
)
dsl_State_strategy = st.builds(
    dsl_State,
    name=
        safe_text
)
dsl_Event_strategy = st.builds(
    dsl_Event,
    name=
        safe_text,
    code=
        safe_text
)
dsl_Statemachine_strategy = st.builds(
    dsl_Statemachine,
)

@given(instance=dsl_Command_strategy)
@settings(max_examples=50)
def test_dsl_command_instantiation(instance):
    assert isinstance(instance, dsl_Command)



@given(instance=dsl_Command_strategy)
def test_dsl_command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=dsl_Command_strategy)
def test_dsl_command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl_Transition_strategy)
@settings(max_examples=50)
def test_dsl_transition_instantiation(instance):
    assert isinstance(instance, dsl_Transition)

@given(instance=dsl_State_strategy)
@settings(max_examples=50)
def test_dsl_state_instantiation(instance):
    assert isinstance(instance, dsl_State)



@given(instance=dsl_State_strategy)
def test_dsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl_Event_strategy)
@settings(max_examples=50)
def test_dsl_event_instantiation(instance):
    assert isinstance(instance, dsl_Event)



@given(instance=dsl_Event_strategy)
def test_dsl_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_Event_strategy)
def test_dsl_event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=dsl_Statemachine_strategy)
@settings(max_examples=50)
def test_dsl_statemachine_instantiation(instance):
    assert isinstance(instance, dsl_Statemachine)
