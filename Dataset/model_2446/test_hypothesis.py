import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ioautomaton::Object,
    ioautomaton::OutMessage,
    ioautomaton::Return,
    ioautomaton::Operation,
    ioautomaton::Transition,
    ioautomaton::State,
    ioautomaton::Automaton,
    ioautomaton::AutomatonContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ioautomaton::object_is_not_abstract():
    assert not inspect.isabstract(ioautomaton::Object)


def test_ioautomaton::object_constructor_exists():
    assert callable(ioautomaton::Object.__init__)


def test_ioautomaton::object_constructor_args():
    sig = inspect.signature(ioautomaton::Object.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::object_has_name():
    assert hasattr(ioautomaton::Object, "name")
    descriptor = None
    for klass in ioautomaton::Object.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::outmessage_is_not_abstract():
    assert not inspect.isabstract(ioautomaton::OutMessage)


def test_ioautomaton::outmessage_constructor_exists():
    assert callable(ioautomaton::OutMessage.__init__)


def test_ioautomaton::outmessage_constructor_args():
    sig = inspect.signature(ioautomaton::OutMessage.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::return_is_not_abstract():
    assert not inspect.isabstract(ioautomaton::Return)


def test_ioautomaton::return_constructor_exists():
    assert callable(ioautomaton::Return.__init__)


def test_ioautomaton::return_constructor_args():
    sig = inspect.signature(ioautomaton::Return.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ioautomaton::return_has_value():
    assert hasattr(ioautomaton::Return, "value")
    descriptor = None
    for klass in ioautomaton::Return.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::operation_is_not_abstract():
    assert not inspect.isabstract(ioautomaton::Operation)


def test_ioautomaton::operation_constructor_exists():
    assert callable(ioautomaton::Operation.__init__)


def test_ioautomaton::operation_constructor_args():
    sig = inspect.signature(ioautomaton::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::operation_has_name():
    assert hasattr(ioautomaton::Operation, "name")
    descriptor = None
    for klass in ioautomaton::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::transition_is_not_abstract():
    assert not inspect.isabstract(ioautomaton::Transition)


def test_ioautomaton::transition_constructor_exists():
    assert callable(ioautomaton::Transition.__init__)


def test_ioautomaton::transition_constructor_args():
    sig = inspect.signature(ioautomaton::Transition.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::state_is_not_abstract():
    assert not inspect.isabstract(ioautomaton::State)


def test_ioautomaton::state_constructor_exists():
    assert callable(ioautomaton::State.__init__)


def test_ioautomaton::state_constructor_args():
    sig = inspect.signature(ioautomaton::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::state_has_name():
    assert hasattr(ioautomaton::State, "name")
    descriptor = None
    for klass in ioautomaton::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::automaton_is_not_abstract():
    assert not inspect.isabstract(ioautomaton::Automaton)


def test_ioautomaton::automaton_constructor_exists():
    assert callable(ioautomaton::Automaton.__init__)


def test_ioautomaton::automaton_constructor_args():
    sig = inspect.signature(ioautomaton::Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "sender" in params, "Missing parameter 'sender'"

def test_ioautomaton::automaton_has_sender():
    assert hasattr(ioautomaton::Automaton, "sender")
    descriptor = None
    for klass in ioautomaton::Automaton.__mro__:
        if "sender" in klass.__dict__:
            descriptor = klass.__dict__["sender"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::automatoncontainer_is_not_abstract():
    assert not inspect.isabstract(ioautomaton::AutomatonContainer)


def test_ioautomaton::automatoncontainer_constructor_exists():
    assert callable(ioautomaton::AutomatonContainer.__init__)


def test_ioautomaton::automatoncontainer_constructor_args():
    sig = inspect.signature(ioautomaton::AutomatonContainer.__init__)
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
ioautomaton::Object_strategy = st.builds(
    ioautomaton::Object,
    name=
        safe_text
)
ioautomaton::OutMessage_strategy = st.builds(
    ioautomaton::OutMessage,
)
ioautomaton::Return_strategy = st.builds(
    ioautomaton::Return,
    value=
        safe_text
)
ioautomaton::Operation_strategy = st.builds(
    ioautomaton::Operation,
    name=
        safe_text
)
ioautomaton::Transition_strategy = st.builds(
    ioautomaton::Transition,
)
ioautomaton::State_strategy = st.builds(
    ioautomaton::State,
    name=
        safe_text
)
ioautomaton::Automaton_strategy = st.builds(
    ioautomaton::Automaton,
    sender=
        safe_text
)
ioautomaton::AutomatonContainer_strategy = st.builds(
    ioautomaton::AutomatonContainer,
)

@given(instance=ioautomaton::Object_strategy)
@settings(max_examples=50)
def test_ioautomaton::object_instantiation(instance):
    assert isinstance(instance, ioautomaton::Object)

@given(instance=ioautomaton::Object_strategy)
def test_ioautomaton::object_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ioautomaton::Object_strategy)
def test_ioautomaton::object_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioautomaton::OutMessage_strategy)
@settings(max_examples=50)
def test_ioautomaton::outmessage_instantiation(instance):
    assert isinstance(instance, ioautomaton::OutMessage)

@given(instance=ioautomaton::Return_strategy)
@settings(max_examples=50)
def test_ioautomaton::return_instantiation(instance):
    assert isinstance(instance, ioautomaton::Return)

@given(instance=ioautomaton::Return_strategy)
def test_ioautomaton::return_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ioautomaton::Return_strategy)
def test_ioautomaton::return_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ioautomaton::Operation_strategy)
@settings(max_examples=50)
def test_ioautomaton::operation_instantiation(instance):
    assert isinstance(instance, ioautomaton::Operation)

@given(instance=ioautomaton::Operation_strategy)
def test_ioautomaton::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ioautomaton::Operation_strategy)
def test_ioautomaton::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioautomaton::Transition_strategy)
@settings(max_examples=50)
def test_ioautomaton::transition_instantiation(instance):
    assert isinstance(instance, ioautomaton::Transition)

@given(instance=ioautomaton::State_strategy)
@settings(max_examples=50)
def test_ioautomaton::state_instantiation(instance):
    assert isinstance(instance, ioautomaton::State)

@given(instance=ioautomaton::State_strategy)
def test_ioautomaton::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ioautomaton::State_strategy)
def test_ioautomaton::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioautomaton::Automaton_strategy)
@settings(max_examples=50)
def test_ioautomaton::automaton_instantiation(instance):
    assert isinstance(instance, ioautomaton::Automaton)

@given(instance=ioautomaton::Automaton_strategy)
def test_ioautomaton::automaton_sender_type(instance):
    assert isinstance(instance.sender, str)


@given(instance=ioautomaton::Automaton_strategy)
def test_ioautomaton::automaton_sender_setter(instance):
    original = instance.sender
    instance.sender = original
    assert instance.sender == original

@given(instance=ioautomaton::AutomatonContainer_strategy)
@settings(max_examples=50)
def test_ioautomaton::automatoncontainer_instantiation(instance):
    assert isinstance(instance, ioautomaton::AutomatonContainer)
