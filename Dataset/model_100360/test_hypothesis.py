import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fowlerdsl_Transition,
    fowlerdsl_State,
    fowlerdsl_Command,
    fowlerdsl_Event,
    fowlerdsl_Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fowlerdsl_transition_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_Transition)


def test_fowlerdsl_transition_constructor_exists():
    assert callable(fowlerdsl_Transition.__init__)


def test_fowlerdsl_transition_constructor_args():
    sig = inspect.signature(fowlerdsl_Transition.__init__)
    params = list(sig.parameters.keys())



def test_fowlerdsl_state_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_State)


def test_fowlerdsl_state_constructor_exists():
    assert callable(fowlerdsl_State.__init__)


def test_fowlerdsl_state_constructor_args():
    sig = inspect.signature(fowlerdsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fowlerdsl_state_has_name():
    assert hasattr(fowlerdsl_State, "name")
    descriptor = None
    for klass in fowlerdsl_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fowlerdsl_command_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_Command)


def test_fowlerdsl_command_constructor_exists():
    assert callable(fowlerdsl_Command.__init__)


def test_fowlerdsl_command_constructor_args():
    sig = inspect.signature(fowlerdsl_Command.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_fowlerdsl_command_has_code():
    assert hasattr(fowlerdsl_Command, "code")
    descriptor = None
    for klass in fowlerdsl_Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_fowlerdsl_command_has_name():
    assert hasattr(fowlerdsl_Command, "name")
    descriptor = None
    for klass in fowlerdsl_Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fowlerdsl_event_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_Event)


def test_fowlerdsl_event_constructor_exists():
    assert callable(fowlerdsl_Event.__init__)


def test_fowlerdsl_event_constructor_args():
    sig = inspect.signature(fowlerdsl_Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "resetting" in params, "Missing parameter 'resetting'"
    assert "name" in params, "Missing parameter 'name'"

def test_fowlerdsl_event_has_code():
    assert hasattr(fowlerdsl_Event, "code")
    descriptor = None
    for klass in fowlerdsl_Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_fowlerdsl_event_has_resetting():
    assert hasattr(fowlerdsl_Event, "resetting")
    descriptor = None
    for klass in fowlerdsl_Event.__mro__:
        if "resetting" in klass.__dict__:
            descriptor = klass.__dict__["resetting"]
            break
    assert isinstance(descriptor, property)

def test_fowlerdsl_event_has_name():
    assert hasattr(fowlerdsl_Event, "name")
    descriptor = None
    for klass in fowlerdsl_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fowlerdsl_statemachine_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl_Statemachine)


def test_fowlerdsl_statemachine_constructor_exists():
    assert callable(fowlerdsl_Statemachine.__init__)


def test_fowlerdsl_statemachine_constructor_args():
    sig = inspect.signature(fowlerdsl_Statemachine.__init__)
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
fowlerdsl_Transition_strategy = st.builds(
    fowlerdsl_Transition,
)
fowlerdsl_State_strategy = st.builds(
    fowlerdsl_State,
    name=
        safe_text
)
fowlerdsl_Command_strategy = st.builds(
    fowlerdsl_Command,
    code=
        safe_text,
    name=
        safe_text
)
fowlerdsl_Event_strategy = st.builds(
    fowlerdsl_Event,
    code=
        safe_text,
    resetting=
        st.booleans(),
    name=
        safe_text
)
fowlerdsl_Statemachine_strategy = st.builds(
    fowlerdsl_Statemachine,
)

@given(instance=fowlerdsl_Transition_strategy)
@settings(max_examples=50)
def test_fowlerdsl_transition_instantiation(instance):
    assert isinstance(instance, fowlerdsl_Transition)

@given(instance=fowlerdsl_State_strategy)
@settings(max_examples=50)
def test_fowlerdsl_state_instantiation(instance):
    assert isinstance(instance, fowlerdsl_State)



@given(instance=fowlerdsl_State_strategy)
def test_fowlerdsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fowlerdsl_Command_strategy)
@settings(max_examples=50)
def test_fowlerdsl_command_instantiation(instance):
    assert isinstance(instance, fowlerdsl_Command)



@given(instance=fowlerdsl_Command_strategy)
def test_fowlerdsl_command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=fowlerdsl_Command_strategy)
def test_fowlerdsl_command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fowlerdsl_Event_strategy)
@settings(max_examples=50)
def test_fowlerdsl_event_instantiation(instance):
    assert isinstance(instance, fowlerdsl_Event)



@given(instance=fowlerdsl_Event_strategy)
def test_fowlerdsl_event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=fowlerdsl_Event_strategy)
def test_fowlerdsl_event_resetting_setter(instance):
    original = instance.resetting
    instance.resetting = original
    assert instance.resetting == original



@given(instance=fowlerdsl_Event_strategy)
def test_fowlerdsl_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fowlerdsl_Statemachine_strategy)
@settings(max_examples=50)
def test_fowlerdsl_statemachine_instantiation(instance):
    assert isinstance(instance, fowlerdsl_Statemachine)
