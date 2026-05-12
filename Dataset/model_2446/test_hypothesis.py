import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ioautomaton_Object,
    ioautomaton_OutMessage,
    ioautomaton_Return,
    ioautomaton_Operation,
    ioautomaton_Transition,
    ioautomaton_State,
    ioautomaton_Automaton,
    ioautomaton_AutomatonContainer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ioautomaton_object_is_not_abstract():
    assert not inspect.isabstract(ioautomaton_Object)


def test_ioautomaton_object_constructor_exists():
    assert callable(ioautomaton_Object.__init__)


def test_ioautomaton_object_constructor_args():
    sig = inspect.signature(ioautomaton_Object.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton_object_has_name():
    assert hasattr(ioautomaton_Object, "name")
    descriptor = None
    for klass in ioautomaton_Object.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton_outmessage_is_not_abstract():
    assert not inspect.isabstract(ioautomaton_OutMessage)


def test_ioautomaton_outmessage_constructor_exists():
    assert callable(ioautomaton_OutMessage.__init__)


def test_ioautomaton_outmessage_constructor_args():
    sig = inspect.signature(ioautomaton_OutMessage.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton_return_is_not_abstract():
    assert not inspect.isabstract(ioautomaton_Return)


def test_ioautomaton_return_constructor_exists():
    assert callable(ioautomaton_Return.__init__)


def test_ioautomaton_return_constructor_args():
    sig = inspect.signature(ioautomaton_Return.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ioautomaton_return_has_value():
    assert hasattr(ioautomaton_Return, "value")
    descriptor = None
    for klass in ioautomaton_Return.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton_operation_is_not_abstract():
    assert not inspect.isabstract(ioautomaton_Operation)


def test_ioautomaton_operation_constructor_exists():
    assert callable(ioautomaton_Operation.__init__)


def test_ioautomaton_operation_constructor_args():
    sig = inspect.signature(ioautomaton_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton_operation_has_name():
    assert hasattr(ioautomaton_Operation, "name")
    descriptor = None
    for klass in ioautomaton_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton_transition_is_not_abstract():
    assert not inspect.isabstract(ioautomaton_Transition)


def test_ioautomaton_transition_constructor_exists():
    assert callable(ioautomaton_Transition.__init__)


def test_ioautomaton_transition_constructor_args():
    sig = inspect.signature(ioautomaton_Transition.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton_state_is_not_abstract():
    assert not inspect.isabstract(ioautomaton_State)


def test_ioautomaton_state_constructor_exists():
    assert callable(ioautomaton_State.__init__)


def test_ioautomaton_state_constructor_args():
    sig = inspect.signature(ioautomaton_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton_state_has_name():
    assert hasattr(ioautomaton_State, "name")
    descriptor = None
    for klass in ioautomaton_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton_automaton_is_not_abstract():
    assert not inspect.isabstract(ioautomaton_Automaton)


def test_ioautomaton_automaton_constructor_exists():
    assert callable(ioautomaton_Automaton.__init__)


def test_ioautomaton_automaton_constructor_args():
    sig = inspect.signature(ioautomaton_Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "sender" in params, "Missing parameter 'sender'"

def test_ioautomaton_automaton_has_sender():
    assert hasattr(ioautomaton_Automaton, "sender")
    descriptor = None
    for klass in ioautomaton_Automaton.__mro__:
        if "sender" in klass.__dict__:
            descriptor = klass.__dict__["sender"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton_automatoncontainer_is_not_abstract():
    assert not inspect.isabstract(ioautomaton_AutomatonContainer)


def test_ioautomaton_automatoncontainer_constructor_exists():
    assert callable(ioautomaton_AutomatonContainer.__init__)


def test_ioautomaton_automatoncontainer_constructor_args():
    sig = inspect.signature(ioautomaton_AutomatonContainer.__init__)
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
ioautomaton_Object_strategy = st.builds(
    ioautomaton_Object,
    name=
        safe_text
)
ioautomaton_OutMessage_strategy = st.builds(
    ioautomaton_OutMessage,
)
ioautomaton_Return_strategy = st.builds(
    ioautomaton_Return,
    value=
        safe_text
)
ioautomaton_Operation_strategy = st.builds(
    ioautomaton_Operation,
    name=
        safe_text
)
ioautomaton_Transition_strategy = st.builds(
    ioautomaton_Transition,
)
ioautomaton_State_strategy = st.builds(
    ioautomaton_State,
    name=
        safe_text
)
ioautomaton_Automaton_strategy = st.builds(
    ioautomaton_Automaton,
    sender=
        safe_text
)
ioautomaton_AutomatonContainer_strategy = st.builds(
    ioautomaton_AutomatonContainer,
)

@given(instance=ioautomaton_Object_strategy)
@settings(max_examples=50)
def test_ioautomaton_object_instantiation(instance):
    assert isinstance(instance, ioautomaton_Object)



@given(instance=ioautomaton_Object_strategy)
def test_ioautomaton_object_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioautomaton_OutMessage_strategy)
@settings(max_examples=50)
def test_ioautomaton_outmessage_instantiation(instance):
    assert isinstance(instance, ioautomaton_OutMessage)

@given(instance=ioautomaton_Return_strategy)
@settings(max_examples=50)
def test_ioautomaton_return_instantiation(instance):
    assert isinstance(instance, ioautomaton_Return)



@given(instance=ioautomaton_Return_strategy)
def test_ioautomaton_return_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ioautomaton_Operation_strategy)
@settings(max_examples=50)
def test_ioautomaton_operation_instantiation(instance):
    assert isinstance(instance, ioautomaton_Operation)



@given(instance=ioautomaton_Operation_strategy)
def test_ioautomaton_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioautomaton_Transition_strategy)
@settings(max_examples=50)
def test_ioautomaton_transition_instantiation(instance):
    assert isinstance(instance, ioautomaton_Transition)

@given(instance=ioautomaton_State_strategy)
@settings(max_examples=50)
def test_ioautomaton_state_instantiation(instance):
    assert isinstance(instance, ioautomaton_State)



@given(instance=ioautomaton_State_strategy)
def test_ioautomaton_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ioautomaton_Automaton_strategy)
@settings(max_examples=50)
def test_ioautomaton_automaton_instantiation(instance):
    assert isinstance(instance, ioautomaton_Automaton)



@given(instance=ioautomaton_Automaton_strategy)
def test_ioautomaton_automaton_sender_setter(instance):
    original = instance.sender
    instance.sender = original
    assert instance.sender == original

@given(instance=ioautomaton_AutomatonContainer_strategy)
@settings(max_examples=50)
def test_ioautomaton_automatoncontainer_instantiation(instance):
    assert isinstance(instance, ioautomaton_AutomatonContainer)
