import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Buffer,
    fsm::System,
    fsm::Transition,
    fsm::State,
    fsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::buffer_is_not_abstract():
    assert not inspect.isabstract(fsm::Buffer)


def test_fsm::buffer_constructor_exists():
    assert callable(fsm::Buffer.__init__)


def test_fsm::buffer_constructor_args():
    sig = inspect.signature(fsm::Buffer.__init__)
    params = list(sig.parameters.keys())
    assert "currentValues" in params, "Missing parameter 'currentValues'"
    assert "initialValue" in params, "Missing parameter 'initialValue'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::buffer_has_currentValues():
    assert hasattr(fsm::Buffer, "currentValues")
    descriptor = None
    for klass in fsm::Buffer.__mro__:
        if "currentValues" in klass.__dict__:
            descriptor = klass.__dict__["currentValues"]
            break
    assert isinstance(descriptor, property)

def test_fsm::buffer_has_initialValue():
    assert hasattr(fsm::Buffer, "initialValue")
    descriptor = None
    for klass in fsm::Buffer.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)

def test_fsm::buffer_has_name():
    assert hasattr(fsm::Buffer, "name")
    descriptor = None
    for klass in fsm::Buffer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::system_is_not_abstract():
    assert not inspect.isabstract(fsm::System)


def test_fsm::system_constructor_exists():
    assert callable(fsm::System.__init__)


def test_fsm::system_constructor_args():
    sig = inspect.signature(fsm::System.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::transition_has_action():
    assert hasattr(fsm::Transition, "action")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_trigger():
    assert hasattr(fsm::Transition, "trigger")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_name():
    assert hasattr(fsm::Transition, "name")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::state_has_name():
    assert hasattr(fsm::State, "name")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fsm::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fsm::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "consummedString" in params, "Missing parameter 'consummedString'"
    assert "underProcessTrigger" in params, "Missing parameter 'underProcessTrigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::fsm_has_consummedString():
    assert hasattr(fsm::FSM, "consummedString")
    descriptor = None
    for klass in fsm::FSM.__mro__:
        if "consummedString" in klass.__dict__:
            descriptor = klass.__dict__["consummedString"]
            break
    assert isinstance(descriptor, property)

def test_fsm::fsm_has_underProcessTrigger():
    assert hasattr(fsm::FSM, "underProcessTrigger")
    descriptor = None
    for klass in fsm::FSM.__mro__:
        if "underProcessTrigger" in klass.__dict__:
            descriptor = klass.__dict__["underProcessTrigger"]
            break
    assert isinstance(descriptor, property)

def test_fsm::fsm_has_name():
    assert hasattr(fsm::FSM, "name")
    descriptor = None
    for klass in fsm::FSM.__mro__:
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
fsm::Buffer_strategy = st.builds(
    fsm::Buffer,
    currentValues=
        safe_text,
    initialValue=
        safe_text,
    name=
        safe_text
)
fsm::System_strategy = st.builds(
    fsm::System,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    action=
        safe_text,
    trigger=
        safe_text,
    name=
        safe_text
)
fsm::State_strategy = st.builds(
    fsm::State,
    name=
        safe_text
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
    consummedString=
        safe_text,
    underProcessTrigger=
        safe_text,
    name=
        safe_text
)

@given(instance=fsm::Buffer_strategy)
@settings(max_examples=50)
def test_fsm::buffer_instantiation(instance):
    assert isinstance(instance, fsm::Buffer)

@given(instance=fsm::Buffer_strategy)
def test_fsm::buffer_currentValues_type(instance):
    assert isinstance(instance.currentValues, str)


@given(instance=fsm::Buffer_strategy)
def test_fsm::buffer_currentValues_setter(instance):
    original = instance.currentValues
    instance.currentValues = original
    assert instance.currentValues == original

@given(instance=fsm::Buffer_strategy)
def test_fsm::buffer_initialValue_type(instance):
    assert isinstance(instance.initialValue, str)


@given(instance=fsm::Buffer_strategy)
def test_fsm::buffer_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=fsm::Buffer_strategy)
def test_fsm::buffer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Buffer_strategy)
def test_fsm::buffer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::System_strategy)
@settings(max_examples=50)
def test_fsm::system_instantiation(instance):
    assert isinstance(instance, fsm::System)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fsm::FSM)

@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_consummedString_type(instance):
    assert isinstance(instance.consummedString, str)


@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_consummedString_setter(instance):
    original = instance.consummedString
    instance.consummedString = original
    assert instance.consummedString == original

@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_underProcessTrigger_type(instance):
    assert isinstance(instance.underProcessTrigger, str)


@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_underProcessTrigger_setter(instance):
    original = instance.underProcessTrigger
    instance.underProcessTrigger = original
    assert instance.underProcessTrigger == original

@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
