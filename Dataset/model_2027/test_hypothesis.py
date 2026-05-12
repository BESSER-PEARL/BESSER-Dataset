import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    amf_Transition,
    amf_State,
    amf_Statemachine,
    amf_Channel,
    amf_Network,
    Event,
    TypeOfChannel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_amf_transition_is_not_abstract():
    assert not inspect.isabstract(amf_Transition)


def test_amf_transition_constructor_exists():
    assert callable(amf_Transition.__init__)


def test_amf_transition_constructor_args():
    sig = inspect.signature(amf_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_amf_transition_has_event():
    assert hasattr(amf_Transition, "event")
    descriptor = None
    for klass in amf_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_amf_state_is_not_abstract():
    assert not inspect.isabstract(amf_State)


def test_amf_state_constructor_exists():
    assert callable(amf_State.__init__)


def test_amf_state_constructor_args():
    sig = inspect.signature(amf_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_amf_state_has_name():
    assert hasattr(amf_State, "name")
    descriptor = None
    for klass in amf_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_amf_statemachine_is_not_abstract():
    assert not inspect.isabstract(amf_Statemachine)


def test_amf_statemachine_constructor_exists():
    assert callable(amf_Statemachine.__init__)


def test_amf_statemachine_constructor_args():
    sig = inspect.signature(amf_Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_amf_statemachine_has_name():
    assert hasattr(amf_Statemachine, "name")
    descriptor = None
    for klass in amf_Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_amf_channel_is_not_abstract():
    assert not inspect.isabstract(amf_Channel)


def test_amf_channel_constructor_exists():
    assert callable(amf_Channel.__init__)


def test_amf_channel_constructor_args():
    sig = inspect.signature(amf_Channel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_amf_channel_has_name():
    assert hasattr(amf_Channel, "name")
    descriptor = None
    for klass in amf_Channel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_amf_channel_has_Type():
    assert hasattr(amf_Channel, "Type")
    descriptor = None
    for klass in amf_Channel.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_amf_network_is_not_abstract():
    assert not inspect.isabstract(amf_Network)


def test_amf_network_constructor_exists():
    assert callable(amf_Network.__init__)


def test_amf_network_constructor_args():
    sig = inspect.signature(amf_Network.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_amf_network_has_name():
    assert hasattr(amf_Network, "name")
    descriptor = None
    for klass in amf_Network.__mro__:
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
amf_Transition_strategy = st.builds(
    amf_Transition,
    event=
        safe_text
)
amf_State_strategy = st.builds(
    amf_State,
    name=
        safe_text
)
amf_Statemachine_strategy = st.builds(
    amf_Statemachine,
    name=
        safe_text
)
amf_Channel_strategy = st.builds(
    amf_Channel,
    name=
        safe_text,
    Type=
        safe_text
)
amf_Network_strategy = st.builds(
    amf_Network,
    name=
        safe_text
)

@given(instance=amf_Transition_strategy)
@settings(max_examples=50)
def test_amf_transition_instantiation(instance):
    assert isinstance(instance, amf_Transition)



@given(instance=amf_Transition_strategy)
def test_amf_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=amf_State_strategy)
@settings(max_examples=50)
def test_amf_state_instantiation(instance):
    assert isinstance(instance, amf_State)



@given(instance=amf_State_strategy)
def test_amf_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=amf_Statemachine_strategy)
@settings(max_examples=50)
def test_amf_statemachine_instantiation(instance):
    assert isinstance(instance, amf_Statemachine)



@given(instance=amf_Statemachine_strategy)
def test_amf_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=amf_Channel_strategy)
@settings(max_examples=50)
def test_amf_channel_instantiation(instance):
    assert isinstance(instance, amf_Channel)



@given(instance=amf_Channel_strategy)
def test_amf_channel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=amf_Channel_strategy)
def test_amf_channel_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=amf_Network_strategy)
@settings(max_examples=50)
def test_amf_network_instantiation(instance):
    assert isinstance(instance, amf_Network)



@given(instance=amf_Network_strategy)
def test_amf_network_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
