import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_Transition,
    fsm_StringToStringMap,
    fsm_Message,
    fsm_Guard,
    fsm_Action,
    fsm_Event,
    fsm_State,
    fsm_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "InverseGuard" in params, "Missing parameter 'InverseGuard'"

def test_fsm_transition_has_name():
    assert hasattr(fsm_Transition, "name")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_InverseGuard():
    assert hasattr(fsm_Transition, "InverseGuard")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "InverseGuard" in klass.__dict__:
            descriptor = klass.__dict__["InverseGuard"]
            break
    assert isinstance(descriptor, property)



def test_fsm_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(fsm_StringToStringMap)


def test_fsm_stringtostringmap_constructor_exists():
    assert callable(fsm_StringToStringMap.__init__)


def test_fsm_stringtostringmap_constructor_args():
    sig = inspect.signature(fsm_StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_fsm_stringtostringmap_has_value():
    assert hasattr(fsm_StringToStringMap, "value")
    descriptor = None
    for klass in fsm_StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fsm_stringtostringmap_has_key():
    assert hasattr(fsm_StringToStringMap, "key")
    descriptor = None
    for klass in fsm_StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_fsm_message_is_not_abstract():
    assert not inspect.isabstract(fsm_Message)


def test_fsm_message_constructor_exists():
    assert callable(fsm_Message.__init__)


def test_fsm_message_constructor_args():
    sig = inspect.signature(fsm_Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_message_has_name():
    assert hasattr(fsm_Message, "name")
    descriptor = None
    for klass in fsm_Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_guard_is_not_abstract():
    assert not inspect.isabstract(fsm_Guard)


def test_fsm_guard_constructor_exists():
    assert callable(fsm_Guard.__init__)


def test_fsm_guard_constructor_args():
    sig = inspect.signature(fsm_Guard.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_guard_has_name():
    assert hasattr(fsm_Guard, "name")
    descriptor = None
    for klass in fsm_Guard.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_action_is_not_abstract():
    assert not inspect.isabstract(fsm_Action)


def test_fsm_action_constructor_exists():
    assert callable(fsm_Action.__init__)


def test_fsm_action_constructor_args():
    sig = inspect.signature(fsm_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_action_has_name():
    assert hasattr(fsm_Action, "name")
    descriptor = None
    for klass in fsm_Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_event_is_not_abstract():
    assert not inspect.isabstract(fsm_Event)


def test_fsm_event_constructor_exists():
    assert callable(fsm_Event.__init__)


def test_fsm_event_constructor_args():
    sig = inspect.signature(fsm_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_event_has_name():
    assert hasattr(fsm_Event, "name")
    descriptor = None
    for klass in fsm_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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
    assert "name" in params, "Missing parameter 'name'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "isServer" in params, "Missing parameter 'isServer'"

def test_fsm_fsm_has_name():
    assert hasattr(fsm_FSM, "name")
    descriptor = None
    for klass in fsm_FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm_fsm_has_groupId():
    assert hasattr(fsm_FSM, "groupId")
    descriptor = None
    for klass in fsm_FSM.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_fsm_fsm_has_isServer():
    assert hasattr(fsm_FSM, "isServer")
    descriptor = None
    for klass in fsm_FSM.__mro__:
        if "isServer" in klass.__dict__:
            descriptor = klass.__dict__["isServer"]
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
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    name=
        safe_text,
    InverseGuard=
        st.booleans()
)
fsm_StringToStringMap_strategy = st.builds(
    fsm_StringToStringMap,
    value=
        safe_text,
    key=
        safe_text
)
fsm_Message_strategy = st.builds(
    fsm_Message,
    name=
        safe_text
)
fsm_Guard_strategy = st.builds(
    fsm_Guard,
    name=
        safe_text
)
fsm_Action_strategy = st.builds(
    fsm_Action,
    name=
        safe_text
)
fsm_Event_strategy = st.builds(
    fsm_Event,
    name=
        safe_text
)
fsm_State_strategy = st.builds(
    fsm_State,
    name=
        safe_text
)
fsm_FSM_strategy = st.builds(
    fsm_FSM,
    name=
        safe_text,
    groupId=
        safe_text,
    isServer=
        st.booleans()
)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_InverseGuard_setter(instance):
    original = instance.InverseGuard
    instance.InverseGuard = original
    assert instance.InverseGuard == original

@given(instance=fsm_StringToStringMap_strategy)
@settings(max_examples=50)
def test_fsm_stringtostringmap_instantiation(instance):
    assert isinstance(instance, fsm_StringToStringMap)



@given(instance=fsm_StringToStringMap_strategy)
def test_fsm_stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fsm_StringToStringMap_strategy)
def test_fsm_stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=fsm_Message_strategy)
@settings(max_examples=50)
def test_fsm_message_instantiation(instance):
    assert isinstance(instance, fsm_Message)



@given(instance=fsm_Message_strategy)
def test_fsm_message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_Guard_strategy)
@settings(max_examples=50)
def test_fsm_guard_instantiation(instance):
    assert isinstance(instance, fsm_Guard)



@given(instance=fsm_Guard_strategy)
def test_fsm_guard_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_Action_strategy)
@settings(max_examples=50)
def test_fsm_action_instantiation(instance):
    assert isinstance(instance, fsm_Action)



@given(instance=fsm_Action_strategy)
def test_fsm_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_Event_strategy)
@settings(max_examples=50)
def test_fsm_event_instantiation(instance):
    assert isinstance(instance, fsm_Event)



@given(instance=fsm_Event_strategy)
def test_fsm_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_fsm_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsm_FSM_strategy)
def test_fsm_fsm_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=fsm_FSM_strategy)
def test_fsm_fsm_isServer_setter(instance):
    original = instance.isServer
    instance.isServer = original
    assert instance.isServer == original
