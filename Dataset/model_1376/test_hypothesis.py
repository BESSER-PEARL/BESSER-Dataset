import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachine::Transition,
    NamedElement,
    statemachine::NamedElement,
    statemachine::State,
    statemachine::Command,
    statemachine::Event,
    statemachine::Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::namedelement_is_not_abstract():
    assert not inspect.isabstract(statemachine::NamedElement)


def test_statemachine::namedelement_constructor_exists():
    assert callable(statemachine::NamedElement.__init__)


def test_statemachine::namedelement_constructor_args():
    sig = inspect.signature(statemachine::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "displayname" in params, "Missing parameter 'displayname'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::namedelement_has_displayname():
    assert hasattr(statemachine::NamedElement, "displayname")
    descriptor = None
    for klass in statemachine::NamedElement.__mro__:
        if "displayname" in klass.__dict__:
            descriptor = klass.__dict__["displayname"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::namedelement_has_name():
    assert hasattr(statemachine::NamedElement, "name")
    descriptor = None
    for klass in statemachine::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::command_is_not_abstract():
    assert not inspect.isabstract(statemachine::Command)


def test_statemachine::command_constructor_exists():
    assert callable(statemachine::Command.__init__)


def test_statemachine::command_constructor_args():
    sig = inspect.signature(statemachine::Command.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_statemachine::command_has_code():
    assert hasattr(statemachine::Command, "code")
    descriptor = None
    for klass in statemachine::Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(statemachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(statemachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(statemachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_statemachine::event_has_code():
    assert hasattr(statemachine::Event, "code")
    descriptor = None
    for klass in statemachine::Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::Statemachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::Statemachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::Statemachine.__init__)
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
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
statemachine::NamedElement_strategy = st.builds(
    statemachine::NamedElement,
    displayname=
        safe_text,
    name=
        safe_text
)
statemachine::State_strategy = st.builds(
    statemachine::State,
)
statemachine::Command_strategy = st.builds(
    statemachine::Command,
    code=
        safe_text
)
statemachine::Event_strategy = st.builds(
    statemachine::Event,
    code=
        safe_text
)
statemachine::Statemachine_strategy = st.builds(
    statemachine::Statemachine,
)

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=statemachine::NamedElement_strategy)
@settings(max_examples=50)
def test_statemachine::namedelement_instantiation(instance):
    assert isinstance(instance, statemachine::NamedElement)

@given(instance=statemachine::NamedElement_strategy)
def test_statemachine::namedelement_displayname_type(instance):
    assert isinstance(instance.displayname, str)


@given(instance=statemachine::NamedElement_strategy)
def test_statemachine::namedelement_displayname_setter(instance):
    original = instance.displayname
    instance.displayname = original
    assert instance.displayname == original

@given(instance=statemachine::NamedElement_strategy)
def test_statemachine::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::NamedElement_strategy)
def test_statemachine::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::Command_strategy)
@settings(max_examples=50)
def test_statemachine::command_instantiation(instance):
    assert isinstance(instance, statemachine::Command)

@given(instance=statemachine::Command_strategy)
def test_statemachine::command_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=statemachine::Command_strategy)
def test_statemachine::command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, statemachine::Event)

@given(instance=statemachine::Event_strategy)
def test_statemachine::event_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=statemachine::Event_strategy)
def test_statemachine::event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=statemachine::Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::Statemachine)
