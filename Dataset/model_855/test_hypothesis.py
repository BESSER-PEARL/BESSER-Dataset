import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_Buffer,
    fsm_Transition,
    fsm_System,
    fsm_State,
    fsm_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_buffer_is_not_abstract():
    assert not inspect.isabstract(fsm_Buffer)


def test_fsm_buffer_constructor_exists():
    assert callable(fsm_Buffer.__init__)


def test_fsm_buffer_constructor_args():
    sig = inspect.signature(fsm_Buffer.__init__)
    params = list(sig.parameters.keys())
    assert "initialValue" in params, "Missing parameter 'initialValue'"
    assert "currentValues" in params, "Missing parameter 'currentValues'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_buffer_has_initialValue():
    assert hasattr(fsm_Buffer, "initialValue")
    descriptor = None
    for klass in fsm_Buffer.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)

def test_fsm_buffer_has_currentValues():
    assert hasattr(fsm_Buffer, "currentValues")
    descriptor = None
    for klass in fsm_Buffer.__mro__:
        if "currentValues" in klass.__dict__:
            descriptor = klass.__dict__["currentValues"]
            break
    assert isinstance(descriptor, property)

def test_fsm_buffer_has_name():
    assert hasattr(fsm_Buffer, "name")
    descriptor = None
    for klass in fsm_Buffer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"
    assert "action" in params, "Missing parameter 'action'"

def test_fsm_transition_has_trigger():
    assert hasattr(fsm_Transition, "trigger")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_name():
    assert hasattr(fsm_Transition, "name")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_action():
    assert hasattr(fsm_Transition, "action")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_fsm_system_is_not_abstract():
    assert not inspect.isabstract(fsm_System)


def test_fsm_system_constructor_exists():
    assert callable(fsm_System.__init__)


def test_fsm_system_constructor_args():
    sig = inspect.signature(fsm_System.__init__)
    params = list(sig.parameters.keys())



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_state_has_name():
    assert hasattr(fsm_State, "name")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(fsm_FSM)


def test_fsm_fsm_constructor_exists():
    assert callable(fsm_FSM.__init__)


def test_fsm_fsm_constructor_args():
    sig = inspect.signature(fsm_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "consummedString" in params, "Missing parameter 'consummedString'"
    assert "underProcessTrigger" in params, "Missing parameter 'underProcessTrigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_fsm_has_consummedString():
    assert hasattr(fsm_FSM, "consummedString")
    descriptor = None
    for klass in fsm_FSM.__mro__:
        if "consummedString" in klass.__dict__:
            descriptor = klass.__dict__["consummedString"]
            break
    assert isinstance(descriptor, property)

def test_fsm_fsm_has_underProcessTrigger():
    assert hasattr(fsm_FSM, "underProcessTrigger")
    descriptor = None
    for klass in fsm_FSM.__mro__:
        if "underProcessTrigger" in klass.__dict__:
            descriptor = klass.__dict__["underProcessTrigger"]
            break
    assert isinstance(descriptor, property)

def test_fsm_fsm_has_name():
    assert hasattr(fsm_FSM, "name")
    descriptor = None
    for klass in fsm_FSM.__mro__:
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
fsm_Buffer_strategy = st.builds(
    fsm_Buffer,
    initialValue=
        safe_text,
    currentValues=
        safe_text,
    name=
        safe_text
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    trigger=
        safe_text,
    name=
        safe_text,
    action=
        safe_text
)
fsm_System_strategy = st.builds(
    fsm_System,
)
fsm_State_strategy = st.builds(
    fsm_State,
    name=
        safe_text
)
fsm_FSM_strategy = st.builds(
    fsm_FSM,
    consummedString=
        safe_text,
    underProcessTrigger=
        safe_text,
    name=
        safe_text
)

@given(instance=fsm_Buffer_strategy)
@settings(max_examples=50)
def test_fsm_buffer_instantiation(instance):
    assert isinstance(instance, fsm_Buffer)



@given(instance=fsm_Buffer_strategy)
def test_fsm_buffer_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original



@given(instance=fsm_Buffer_strategy)
def test_fsm_buffer_currentValues_setter(instance):
    original = instance.currentValues
    instance.currentValues = original
    assert instance.currentValues == original



@given(instance=fsm_Buffer_strategy)
def test_fsm_buffer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=fsm_System_strategy)
@settings(max_examples=50)
def test_fsm_system_instantiation(instance):
    assert isinstance(instance, fsm_System)

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)



@given(instance=fsm_State_strategy)
def test_fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_FSM_strategy)
@settings(max_examples=50)
def test_fsm_fsm_instantiation(instance):
    assert isinstance(instance, fsm_FSM)



@given(instance=fsm_FSM_strategy)
def test_fsm_fsm_consummedString_setter(instance):
    original = instance.consummedString
    instance.consummedString = original
    assert instance.consummedString == original



@given(instance=fsm_FSM_strategy)
def test_fsm_fsm_underProcessTrigger_setter(instance):
    original = instance.underProcessTrigger
    instance.underProcessTrigger = original
    assert instance.underProcessTrigger == original



@given(instance=fsm_FSM_strategy)
def test_fsm_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
