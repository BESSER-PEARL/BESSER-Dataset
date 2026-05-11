import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    amf::Transition,
    amf::State,
    amf::Statemachine,
    amf::Channel,
    amf::Network,
    Event,
    TypeOfChannel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_amf::transition_is_not_abstract():
    assert not inspect.isabstract(amf::Transition)


def test_amf::transition_constructor_exists():
    assert callable(amf::Transition.__init__)


def test_amf::transition_constructor_args():
    sig = inspect.signature(amf::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_amf::transition_has_event():
    assert hasattr(amf::Transition, "event")
    descriptor = None
    for klass in amf::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_amf::state_is_not_abstract():
    assert not inspect.isabstract(amf::State)


def test_amf::state_constructor_exists():
    assert callable(amf::State.__init__)


def test_amf::state_constructor_args():
    sig = inspect.signature(amf::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_amf::state_has_name():
    assert hasattr(amf::State, "name")
    descriptor = None
    for klass in amf::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_amf::statemachine_is_not_abstract():
    assert not inspect.isabstract(amf::Statemachine)


def test_amf::statemachine_constructor_exists():
    assert callable(amf::Statemachine.__init__)


def test_amf::statemachine_constructor_args():
    sig = inspect.signature(amf::Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_amf::statemachine_has_name():
    assert hasattr(amf::Statemachine, "name")
    descriptor = None
    for klass in amf::Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_amf::channel_is_not_abstract():
    assert not inspect.isabstract(amf::Channel)


def test_amf::channel_constructor_exists():
    assert callable(amf::Channel.__init__)


def test_amf::channel_constructor_args():
    sig = inspect.signature(amf::Channel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_amf::channel_has_name():
    assert hasattr(amf::Channel, "name")
    descriptor = None
    for klass in amf::Channel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_amf::channel_has_Type():
    assert hasattr(amf::Channel, "Type")
    descriptor = None
    for klass in amf::Channel.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_amf::network_is_not_abstract():
    assert not inspect.isabstract(amf::Network)


def test_amf::network_constructor_exists():
    assert callable(amf::Network.__init__)


def test_amf::network_constructor_args():
    sig = inspect.signature(amf::Network.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_amf::network_has_name():
    assert hasattr(amf::Network, "name")
    descriptor = None
    for klass in amf::Network.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_event_exists():
    # Check that the Enumeration exists
    assert Event is not None

def test_event_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Event]
    expected_literals = [
        "RECEIVE",
        "SEND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Event"

def test_typeofchannel_exists():
    # Check that the Enumeration exists
    assert TypeOfChannel is not None

def test_typeofchannel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeOfChannel]
    expected_literals = [
        "Synchronous",
        "Asynchronous",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeOfChannel"


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
amf::Transition_strategy = st.builds(
    amf::Transition,
    event=
        safe_text
)
amf::State_strategy = st.builds(
    amf::State,
    name=
        safe_text
)
amf::Statemachine_strategy = st.builds(
    amf::Statemachine,
    name=
        safe_text
)
amf::Channel_strategy = st.builds(
    amf::Channel,
    name=
        safe_text,
    Type=
        safe_text
)
amf::Network_strategy = st.builds(
    amf::Network,
    name=
        safe_text
)

@given(instance=amf::Transition_strategy)
@settings(max_examples=50)
def test_amf::transition_instantiation(instance):
    assert isinstance(instance, amf::Transition)

@given(instance=amf::Transition_strategy)
def test_amf::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=amf::Transition_strategy)
def test_amf::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=amf::State_strategy)
@settings(max_examples=50)
def test_amf::state_instantiation(instance):
    assert isinstance(instance, amf::State)

@given(instance=amf::State_strategy)
def test_amf::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=amf::State_strategy)
def test_amf::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=amf::Statemachine_strategy)
@settings(max_examples=50)
def test_amf::statemachine_instantiation(instance):
    assert isinstance(instance, amf::Statemachine)

@given(instance=amf::Statemachine_strategy)
def test_amf::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=amf::Statemachine_strategy)
def test_amf::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=amf::Channel_strategy)
@settings(max_examples=50)
def test_amf::channel_instantiation(instance):
    assert isinstance(instance, amf::Channel)

@given(instance=amf::Channel_strategy)
def test_amf::channel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=amf::Channel_strategy)
def test_amf::channel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=amf::Channel_strategy)
def test_amf::channel_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=amf::Channel_strategy)
def test_amf::channel_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=amf::Network_strategy)
@settings(max_examples=50)
def test_amf::network_instantiation(instance):
    assert isinstance(instance, amf::Network)

@given(instance=amf::Network_strategy)
def test_amf::network_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=amf::Network_strategy)
def test_amf::network_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
