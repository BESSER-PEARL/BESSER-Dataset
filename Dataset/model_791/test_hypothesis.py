import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Transition,
    fsm::StringToStringMap,
    fsm::Message,
    fsm::Guard,
    fsm::Action,
    fsm::Event,
    fsm::State,
    fsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "InverseGuard" in params, "Missing parameter 'InverseGuard'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::transition_has_InverseGuard():
    assert hasattr(fsm::Transition, "InverseGuard")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "InverseGuard" in klass.__dict__:
            descriptor = klass.__dict__["InverseGuard"]
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



def test_fsm::stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(fsm::StringToStringMap)


def test_fsm::stringtostringmap_constructor_exists():
    assert callable(fsm::StringToStringMap.__init__)


def test_fsm::stringtostringmap_constructor_args():
    sig = inspect.signature(fsm::StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_fsm::stringtostringmap_has_value():
    assert hasattr(fsm::StringToStringMap, "value")
    descriptor = None
    for klass in fsm::StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fsm::stringtostringmap_has_key():
    assert hasattr(fsm::StringToStringMap, "key")
    descriptor = None
    for klass in fsm::StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_fsm::message_is_not_abstract():
    assert not inspect.isabstract(fsm::Message)


def test_fsm::message_constructor_exists():
    assert callable(fsm::Message.__init__)


def test_fsm::message_constructor_args():
    sig = inspect.signature(fsm::Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::message_has_name():
    assert hasattr(fsm::Message, "name")
    descriptor = None
    for klass in fsm::Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::guard_is_not_abstract():
    assert not inspect.isabstract(fsm::Guard)


def test_fsm::guard_constructor_exists():
    assert callable(fsm::Guard.__init__)


def test_fsm::guard_constructor_args():
    sig = inspect.signature(fsm::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::guard_has_name():
    assert hasattr(fsm::Guard, "name")
    descriptor = None
    for klass in fsm::Guard.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::action_is_not_abstract():
    assert not inspect.isabstract(fsm::Action)


def test_fsm::action_constructor_exists():
    assert callable(fsm::Action.__init__)


def test_fsm::action_constructor_args():
    sig = inspect.signature(fsm::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::action_has_name():
    assert hasattr(fsm::Action, "name")
    descriptor = None
    for klass in fsm::Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::event_is_not_abstract():
    assert not inspect.isabstract(fsm::Event)


def test_fsm::event_constructor_exists():
    assert callable(fsm::Event.__init__)


def test_fsm::event_constructor_args():
    sig = inspect.signature(fsm::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::event_has_name():
    assert hasattr(fsm::Event, "name")
    descriptor = None
    for klass in fsm::Event.__mro__:
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
    assert "name" in params, "Missing parameter 'name'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "isServer" in params, "Missing parameter 'isServer'"

def test_fsm::fsm_has_name():
    assert hasattr(fsm::FSM, "name")
    descriptor = None
    for klass in fsm::FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm::fsm_has_groupId():
    assert hasattr(fsm::FSM, "groupId")
    descriptor = None
    for klass in fsm::FSM.__mro__:
        if "groupId" in klass.__dict__:
            descriptor = klass.__dict__["groupId"]
            break
    assert isinstance(descriptor, property)

def test_fsm::fsm_has_isServer():
    assert hasattr(fsm::FSM, "isServer")
    descriptor = None
    for klass in fsm::FSM.__mro__:
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
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    InverseGuard=
        st.booleans(),
    name=
        safe_text
)
fsm::StringToStringMap_strategy = st.builds(
    fsm::StringToStringMap,
    value=
        safe_text,
    key=
        safe_text
)
fsm::Message_strategy = st.builds(
    fsm::Message,
    name=
        safe_text
)
fsm::Guard_strategy = st.builds(
    fsm::Guard,
    name=
        safe_text
)
fsm::Action_strategy = st.builds(
    fsm::Action,
    name=
        safe_text
)
fsm::Event_strategy = st.builds(
    fsm::Event,
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
    name=
        safe_text,
    groupId=
        safe_text,
    isServer=
        st.booleans()
)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_InverseGuard_type(instance):
    assert isinstance(instance.InverseGuard, bool)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_InverseGuard_setter(instance):
    original = instance.InverseGuard
    instance.InverseGuard = original
    assert instance.InverseGuard == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::StringToStringMap_strategy)
@settings(max_examples=50)
def test_fsm::stringtostringmap_instantiation(instance):
    assert isinstance(instance, fsm::StringToStringMap)

@given(instance=fsm::StringToStringMap_strategy)
def test_fsm::stringtostringmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fsm::StringToStringMap_strategy)
def test_fsm::stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fsm::StringToStringMap_strategy)
def test_fsm::stringtostringmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=fsm::StringToStringMap_strategy)
def test_fsm::stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=fsm::Message_strategy)
@settings(max_examples=50)
def test_fsm::message_instantiation(instance):
    assert isinstance(instance, fsm::Message)

@given(instance=fsm::Message_strategy)
def test_fsm::message_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Message_strategy)
def test_fsm::message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Guard_strategy)
@settings(max_examples=50)
def test_fsm::guard_instantiation(instance):
    assert isinstance(instance, fsm::Guard)

@given(instance=fsm::Guard_strategy)
def test_fsm::guard_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Guard_strategy)
def test_fsm::guard_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Action_strategy)
@settings(max_examples=50)
def test_fsm::action_instantiation(instance):
    assert isinstance(instance, fsm::Action)

@given(instance=fsm::Action_strategy)
def test_fsm::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Action_strategy)
def test_fsm::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Event_strategy)
@settings(max_examples=50)
def test_fsm::event_instantiation(instance):
    assert isinstance(instance, fsm::Event)

@given(instance=fsm::Event_strategy)
def test_fsm::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Event_strategy)
def test_fsm::event_name_setter(instance):
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
def test_fsm::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_groupId_type(instance):
    assert isinstance(instance.groupId, str)


@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original

@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_isServer_type(instance):
    assert isinstance(instance.isServer, bool)


@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_isServer_setter(instance):
    original = instance.isServer
    instance.isServer = original
    assert instance.isServer == original
