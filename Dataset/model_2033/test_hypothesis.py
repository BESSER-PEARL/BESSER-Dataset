import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    network_Transition,
    network_AbstractElement,
    AbstractElement,
    network_State,
    network_Statemachine,
    network_Channel,
    network_Network,
    TypeOfChannel,
    Event,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_network_transition_is_not_abstract():
    assert not inspect.isabstract(network_Transition)


def test_network_transition_constructor_exists():
    assert callable(network_Transition.__init__)


def test_network_transition_constructor_args():
    sig = inspect.signature(network_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Event" in params, "Missing parameter 'Event'"

def test_network_transition_has_Event():
    assert hasattr(network_Transition, "Event")
    descriptor = None
    for klass in network_Transition.__mro__:
        if "Event" in klass.__dict__:
            descriptor = klass.__dict__["Event"]
            break
    assert isinstance(descriptor, property)



def test_network_abstractelement_is_not_abstract():
    assert not inspect.isabstract(network_AbstractElement)


def test_network_abstractelement_constructor_exists():
    assert callable(network_AbstractElement.__init__)


def test_network_abstractelement_constructor_args():
    sig = inspect.signature(network_AbstractElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_network_abstractelement_has_name():
    assert hasattr(network_AbstractElement, "name")
    descriptor = None
    for klass in network_AbstractElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_network_state_is_not_abstract():
    assert not inspect.isabstract(network_State)


def test_network_state_constructor_exists():
    assert callable(network_State.__init__)


def test_network_state_constructor_args():
    sig = inspect.signature(network_State.__init__)
    params = list(sig.parameters.keys())



def test_network_statemachine_is_not_abstract():
    assert not inspect.isabstract(network_Statemachine)


def test_network_statemachine_constructor_exists():
    assert callable(network_Statemachine.__init__)


def test_network_statemachine_constructor_args():
    sig = inspect.signature(network_Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_network_channel_is_not_abstract():
    assert not inspect.isabstract(network_Channel)


def test_network_channel_constructor_exists():
    assert callable(network_Channel.__init__)


def test_network_channel_constructor_args():
    sig = inspect.signature(network_Channel.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_network_channel_has_Type():
    assert hasattr(network_Channel, "Type")
    descriptor = None
    for klass in network_Channel.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_network_network_is_not_abstract():
    assert not inspect.isabstract(network_Network)


def test_network_network_constructor_exists():
    assert callable(network_Network.__init__)


def test_network_network_constructor_args():
    sig = inspect.signature(network_Network.__init__)
    params = list(sig.parameters.keys())

def test_typeofchannel_exists():
    # Check that the Enumeration exists
    assert TypeOfChannel is not None

def test_typeofchannel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeOfChannel]
    expected_literals = [
        "Asynchronous",
        "Synchronous",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeOfChannel"

def test_event_exists():
    # Check that the Enumeration exists
    assert Event is not None

def test_event_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Event]
    expected_literals = [
        "SEND",
        "RECEIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Event"


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
network_Transition_strategy = st.builds(
    network_Transition,
    Event=
        safe_text
)
network_AbstractElement_strategy = st.builds(
    network_AbstractElement,
    name=
        safe_text
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
network_State_strategy = st.builds(
    network_State,
)
network_Statemachine_strategy = st.builds(
    network_Statemachine,
)
network_Channel_strategy = st.builds(
    network_Channel,
    Type=
        safe_text
)
network_Network_strategy = st.builds(
    network_Network,
)

@given(instance=network_Transition_strategy)
@settings(max_examples=50)
def test_network_transition_instantiation(instance):
    assert isinstance(instance, network_Transition)



@given(instance=network_Transition_strategy)
def test_network_transition_Event_setter(instance):
    original = instance.Event
    instance.Event = original
    assert instance.Event == original

@given(instance=network_AbstractElement_strategy)
@settings(max_examples=50)
def test_network_abstractelement_instantiation(instance):
    assert isinstance(instance, network_AbstractElement)



@given(instance=network_AbstractElement_strategy)
def test_network_abstractelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=network_State_strategy)
@settings(max_examples=50)
def test_network_state_instantiation(instance):
    assert isinstance(instance, network_State)

@given(instance=network_Statemachine_strategy)
@settings(max_examples=50)
def test_network_statemachine_instantiation(instance):
    assert isinstance(instance, network_Statemachine)

@given(instance=network_Channel_strategy)
@settings(max_examples=50)
def test_network_channel_instantiation(instance):
    assert isinstance(instance, network_Channel)



@given(instance=network_Channel_strategy)
def test_network_channel_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=network_Network_strategy)
@settings(max_examples=50)
def test_network_network_instantiation(instance):
    assert isinstance(instance, network_Network)
