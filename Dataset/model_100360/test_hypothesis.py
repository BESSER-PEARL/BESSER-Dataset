import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fowlerdsl::Transition,
    fowlerdsl::State,
    fowlerdsl::Command,
    fowlerdsl::Event,
    fowlerdsl::Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fowlerdsl::transition_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl::Transition)


def test_fowlerdsl::transition_constructor_exists():
    assert callable(fowlerdsl::Transition.__init__)


def test_fowlerdsl::transition_constructor_args():
    sig = inspect.signature(fowlerdsl::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fowlerdsl::state_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl::State)


def test_fowlerdsl::state_constructor_exists():
    assert callable(fowlerdsl::State.__init__)


def test_fowlerdsl::state_constructor_args():
    sig = inspect.signature(fowlerdsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fowlerdsl::state_has_name():
    assert hasattr(fowlerdsl::State, "name")
    descriptor = None
    for klass in fowlerdsl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fowlerdsl::command_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl::Command)


def test_fowlerdsl::command_constructor_exists():
    assert callable(fowlerdsl::Command.__init__)


def test_fowlerdsl::command_constructor_args():
    sig = inspect.signature(fowlerdsl::Command.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_fowlerdsl::command_has_name():
    assert hasattr(fowlerdsl::Command, "name")
    descriptor = None
    for klass in fowlerdsl::Command.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fowlerdsl::command_has_code():
    assert hasattr(fowlerdsl::Command, "code")
    descriptor = None
    for klass in fowlerdsl::Command.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_fowlerdsl::event_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl::Event)


def test_fowlerdsl::event_constructor_exists():
    assert callable(fowlerdsl::Event.__init__)


def test_fowlerdsl::event_constructor_args():
    sig = inspect.signature(fowlerdsl::Event.__init__)
    params = list(sig.parameters.keys())
    assert "resetting" in params, "Missing parameter 'resetting'"
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_fowlerdsl::event_has_resetting():
    assert hasattr(fowlerdsl::Event, "resetting")
    descriptor = None
    for klass in fowlerdsl::Event.__mro__:
        if "resetting" in klass.__dict__:
            descriptor = klass.__dict__["resetting"]
            break
    assert isinstance(descriptor, property)

def test_fowlerdsl::event_has_name():
    assert hasattr(fowlerdsl::Event, "name")
    descriptor = None
    for klass in fowlerdsl::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fowlerdsl::event_has_code():
    assert hasattr(fowlerdsl::Event, "code")
    descriptor = None
    for klass in fowlerdsl::Event.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_fowlerdsl::statemachine_is_not_abstract():
    assert not inspect.isabstract(fowlerdsl::Statemachine)


def test_fowlerdsl::statemachine_constructor_exists():
    assert callable(fowlerdsl::Statemachine.__init__)


def test_fowlerdsl::statemachine_constructor_args():
    sig = inspect.signature(fowlerdsl::Statemachine.__init__)
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
fowlerdsl::Transition_strategy = st.builds(
    fowlerdsl::Transition,
)
fowlerdsl::State_strategy = st.builds(
    fowlerdsl::State,
    name=
        safe_text
)
fowlerdsl::Command_strategy = st.builds(
    fowlerdsl::Command,
    name=
        safe_text,
    code=
        safe_text
)
fowlerdsl::Event_strategy = st.builds(
    fowlerdsl::Event,
    resetting=
        st.booleans(),
    name=
        safe_text,
    code=
        safe_text
)
fowlerdsl::Statemachine_strategy = st.builds(
    fowlerdsl::Statemachine,
)

@given(instance=fowlerdsl::Transition_strategy)
@settings(max_examples=50)
def test_fowlerdsl::transition_instantiation(instance):
    assert isinstance(instance, fowlerdsl::Transition)

@given(instance=fowlerdsl::State_strategy)
@settings(max_examples=50)
def test_fowlerdsl::state_instantiation(instance):
    assert isinstance(instance, fowlerdsl::State)

@given(instance=fowlerdsl::State_strategy)
def test_fowlerdsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fowlerdsl::State_strategy)
def test_fowlerdsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fowlerdsl::Command_strategy)
@settings(max_examples=50)
def test_fowlerdsl::command_instantiation(instance):
    assert isinstance(instance, fowlerdsl::Command)

@given(instance=fowlerdsl::Command_strategy)
def test_fowlerdsl::command_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fowlerdsl::Command_strategy)
def test_fowlerdsl::command_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fowlerdsl::Command_strategy)
def test_fowlerdsl::command_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=fowlerdsl::Command_strategy)
def test_fowlerdsl::command_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=fowlerdsl::Event_strategy)
@settings(max_examples=50)
def test_fowlerdsl::event_instantiation(instance):
    assert isinstance(instance, fowlerdsl::Event)

@given(instance=fowlerdsl::Event_strategy)
def test_fowlerdsl::event_resetting_type(instance):
    assert isinstance(instance.resetting, bool)


@given(instance=fowlerdsl::Event_strategy)
def test_fowlerdsl::event_resetting_setter(instance):
    original = instance.resetting
    instance.resetting = original
    assert instance.resetting == original

@given(instance=fowlerdsl::Event_strategy)
def test_fowlerdsl::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fowlerdsl::Event_strategy)
def test_fowlerdsl::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fowlerdsl::Event_strategy)
def test_fowlerdsl::event_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=fowlerdsl::Event_strategy)
def test_fowlerdsl::event_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=fowlerdsl::Statemachine_strategy)
@settings(max_examples=50)
def test_fowlerdsl::statemachine_instantiation(instance):
    assert isinstance(instance, fowlerdsl::Statemachine)
