import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_Transition,
    NamedElement,
    statemachine_NamedElement,
    statemachine_State,
    statemachine_Command,
    statemachine_Event,
    statemachine_Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_namedelement_is_not_abstract():
    assert not inspect.isabstract(statemachine_NamedElement)


def test_statemachine_namedelement_constructor_exists():
    assert callable(statemachine_NamedElement.__init__)


def test_statemachine_namedelement_constructor_args():
    sig = inspect.signature(statemachine_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "displayname" in params, "Missing parameter 'displayname'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_namedelement_has_displayname():
    assert hasattr(statemachine_NamedElement, "displayname")
    descriptor = None
    for klass in statemachine_NamedElement.__mro__:
        if "displayname" in klass.__dict__:
            descriptor = klass.__dict__["displayname"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_namedelement_has_name():
    assert hasattr(statemachine_NamedElement, "name")
    descriptor = None
    for klass in statemachine_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_command_is_not_abstract():
    assert not inspect.isabstract(statemachine_Command)


def test_statemachine_command_constructor_exists():
    assert callable(statemachine_Command.__init__)


def test_statemachine_command_constructor_args():
    sig = inspect.signature(statemachine_Command.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_statemachine_command_has_code():
    assert hasattr(statemachine_Command, "code")
    descriptor = None
    for klass in statemachine_Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(statemachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(statemachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(statemachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_statemachine_event_has_code():
    assert hasattr(statemachine_Event, "code")
    descriptor = None
    for klass in statemachine_Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statemachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_Statemachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_Statemachine.__init__)
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
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
statemachine_NamedElement_strategy = st.builds(
    statemachine_NamedElement,
    displayname=
        safe_text,
    name=
        safe_text
)
statemachine_State_strategy = st.builds(
    statemachine_State,
)
statemachine_Command_strategy = st.builds(
    statemachine_Command,
    code=
        safe_text
)
statemachine_Event_strategy = st.builds(
    statemachine_Event,
    code=
        safe_text
)
statemachine_Statemachine_strategy = st.builds(
    statemachine_Statemachine,
)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=statemachine_NamedElement_strategy)
@settings(max_examples=50)
def test_statemachine_namedelement_instantiation(instance):
    assert isinstance(instance, statemachine_NamedElement)



@given(instance=statemachine_NamedElement_strategy)
def test_statemachine_namedelement_displayname_setter(instance):
    original = instance.displayname
    instance.displayname = original
    assert instance.displayname == original



@given(instance=statemachine_NamedElement_strategy)
def test_statemachine_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)

@given(instance=statemachine_Command_strategy)
@settings(max_examples=50)
def test_statemachine_command_instantiation(instance):
    assert isinstance(instance, statemachine_Command)



@given(instance=statemachine_Command_strategy)
def test_statemachine_command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, statemachine_Event)



@given(instance=statemachine_Event_strategy)
def test_statemachine_event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)
