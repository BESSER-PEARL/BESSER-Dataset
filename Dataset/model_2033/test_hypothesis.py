import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    network::Transition,
    network::AbstractElement,
    AbstractElement,
    network::Channel,
    network::State,
    network::Statemachine,
    network::Network,
    Event,
    TypeOfChannel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_network::transition_is_not_abstract():
    assert not inspect.isabstract(network::Transition)


def test_network::transition_constructor_exists():
    assert callable(network::Transition.__init__)


def test_network::transition_constructor_args():
    sig = inspect.signature(network::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Event" in params, "Missing parameter 'Event'"

def test_network::transition_has_Event():
    assert hasattr(network::Transition, "Event")
    descriptor = None
    for klass in network::Transition.__mro__:
        if "Event" in klass.__dict__:
            descriptor = klass.__dict__["Event"]
            break
    assert isinstance(descriptor, property)



def test_network::abstractelement_is_not_abstract():
    assert not inspect.isabstract(network::AbstractElement)


def test_network::abstractelement_constructor_exists():
    assert callable(network::AbstractElement.__init__)


def test_network::abstractelement_constructor_args():
    sig = inspect.signature(network::AbstractElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_network::abstractelement_has_name():
    assert hasattr(network::AbstractElement, "name")
    descriptor = None
    for klass in network::AbstractElement.__mro__:
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



def test_network::channel_is_not_abstract():
    assert not inspect.isabstract(network::Channel)


def test_network::channel_constructor_exists():
    assert callable(network::Channel.__init__)


def test_network::channel_constructor_args():
    sig = inspect.signature(network::Channel.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_network::channel_has_Type():
    assert hasattr(network::Channel, "Type")
    descriptor = None
    for klass in network::Channel.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_network::state_is_not_abstract():
    assert not inspect.isabstract(network::State)


def test_network::state_constructor_exists():
    assert callable(network::State.__init__)


def test_network::state_constructor_args():
    sig = inspect.signature(network::State.__init__)
    params = list(sig.parameters.keys())



def test_network::statemachine_is_not_abstract():
    assert not inspect.isabstract(network::Statemachine)


def test_network::statemachine_constructor_exists():
    assert callable(network::Statemachine.__init__)


def test_network::statemachine_constructor_args():
    sig = inspect.signature(network::Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_network::network_is_not_abstract():
    assert not inspect.isabstract(network::Network)


def test_network::network_constructor_exists():
    assert callable(network::Network.__init__)


def test_network::network_constructor_args():
    sig = inspect.signature(network::Network.__init__)
    params = list(sig.parameters.keys())

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
network::Transition_strategy = st.builds(
    network::Transition,
    Event=
        safe_text
)
network::AbstractElement_strategy = st.builds(
    network::AbstractElement,
    name=
        safe_text
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
network::Channel_strategy = st.builds(
    network::Channel,
    Type=
        safe_text
)
network::State_strategy = st.builds(
    network::State,
)
network::Statemachine_strategy = st.builds(
    network::Statemachine,
)
network::Network_strategy = st.builds(
    network::Network,
)

@given(instance=network::Transition_strategy)
@settings(max_examples=50)
def test_network::transition_instantiation(instance):
    assert isinstance(instance, network::Transition)

@given(instance=network::Transition_strategy)
def test_network::transition_Event_type(instance):
    assert isinstance(instance.Event, str)


@given(instance=network::Transition_strategy)
def test_network::transition_Event_setter(instance):
    original = instance.Event
    instance.Event = original
    assert instance.Event == original

@given(instance=network::AbstractElement_strategy)
@settings(max_examples=50)
def test_network::abstractelement_instantiation(instance):
    assert isinstance(instance, network::AbstractElement)

@given(instance=network::AbstractElement_strategy)
def test_network::abstractelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=network::AbstractElement_strategy)
def test_network::abstractelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=network::Channel_strategy)
@settings(max_examples=50)
def test_network::channel_instantiation(instance):
    assert isinstance(instance, network::Channel)

@given(instance=network::Channel_strategy)
def test_network::channel_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=network::Channel_strategy)
def test_network::channel_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=network::State_strategy)
@settings(max_examples=50)
def test_network::state_instantiation(instance):
    assert isinstance(instance, network::State)

@given(instance=network::Statemachine_strategy)
@settings(max_examples=50)
def test_network::statemachine_instantiation(instance):
    assert isinstance(instance, network::Statemachine)

@given(instance=network::Network_strategy)
@settings(max_examples=50)
def test_network::network_instantiation(instance):
    assert isinstance(instance, network::Network)
