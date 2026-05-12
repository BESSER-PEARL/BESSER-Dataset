import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IOAutomaton::ReturnValue,
    IOAutomaton::Object,
    IOAutomaton::Operation,
    IOAutomaton::Output,
    IOAutomaton::Transition,
    IOAutomaton::Activation,
    IOAutomaton::Input,
    IOAutomaton::State,
    IOAutomaton::Automaton,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ioautomaton::returnvalue_is_not_abstract():
    assert not inspect.isabstract(IOAutomaton::ReturnValue)


def test_ioautomaton::returnvalue_constructor_exists():
    assert callable(IOAutomaton::ReturnValue.__init__)


def test_ioautomaton::returnvalue_constructor_args():
    sig = inspect.signature(IOAutomaton::ReturnValue.__init__)
    params = list(sig.parameters.keys())
    assert "isVoid" in params, "Missing parameter 'isVoid'"
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::returnvalue_has_isVoid():
    assert hasattr(IOAutomaton::ReturnValue, "isVoid")
    descriptor = None
    for klass in IOAutomaton::ReturnValue.__mro__:
        if "isVoid" in klass.__dict__:
            descriptor = klass.__dict__["isVoid"]
            break
    assert isinstance(descriptor, property)

def test_ioautomaton::returnvalue_has_name():
    assert hasattr(IOAutomaton::ReturnValue, "name")
    descriptor = None
    for klass in IOAutomaton::ReturnValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::object_is_not_abstract():
    assert not inspect.isabstract(IOAutomaton::Object)


def test_ioautomaton::object_constructor_exists():
    assert callable(IOAutomaton::Object.__init__)


def test_ioautomaton::object_constructor_args():
    sig = inspect.signature(IOAutomaton::Object.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::object_has_name():
    assert hasattr(IOAutomaton::Object, "name")
    descriptor = None
    for klass in IOAutomaton::Object.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::operation_is_not_abstract():
    assert not inspect.isabstract(IOAutomaton::Operation)


def test_ioautomaton::operation_constructor_exists():
    assert callable(IOAutomaton::Operation.__init__)


def test_ioautomaton::operation_constructor_args():
    sig = inspect.signature(IOAutomaton::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::operation_has_name():
    assert hasattr(IOAutomaton::Operation, "name")
    descriptor = None
    for klass in IOAutomaton::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::output_is_not_abstract():
    assert not inspect.isabstract(IOAutomaton::Output)


def test_ioautomaton::output_constructor_exists():
    assert callable(IOAutomaton::Output.__init__)


def test_ioautomaton::output_constructor_args():
    sig = inspect.signature(IOAutomaton::Output.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::output_has_name():
    assert hasattr(IOAutomaton::Output, "name")
    descriptor = None
    for klass in IOAutomaton::Output.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::transition_is_not_abstract():
    assert not inspect.isabstract(IOAutomaton::Transition)


def test_ioautomaton::transition_constructor_exists():
    assert callable(IOAutomaton::Transition.__init__)


def test_ioautomaton::transition_constructor_args():
    sig = inspect.signature(IOAutomaton::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::transition_has_name():
    assert hasattr(IOAutomaton::Transition, "name")
    descriptor = None
    for klass in IOAutomaton::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::activation_is_not_abstract():
    assert not inspect.isabstract(IOAutomaton::Activation)


def test_ioautomaton::activation_constructor_exists():
    assert callable(IOAutomaton::Activation.__init__)


def test_ioautomaton::activation_constructor_args():
    sig = inspect.signature(IOAutomaton::Activation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::activation_has_name():
    assert hasattr(IOAutomaton::Activation, "name")
    descriptor = None
    for klass in IOAutomaton::Activation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::input_is_not_abstract():
    assert not inspect.isabstract(IOAutomaton::Input)


def test_ioautomaton::input_constructor_exists():
    assert callable(IOAutomaton::Input.__init__)


def test_ioautomaton::input_constructor_args():
    sig = inspect.signature(IOAutomaton::Input.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::input_has_name():
    assert hasattr(IOAutomaton::Input, "name")
    descriptor = None
    for klass in IOAutomaton::Input.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::state_is_not_abstract():
    assert not inspect.isabstract(IOAutomaton::State)


def test_ioautomaton::state_constructor_exists():
    assert callable(IOAutomaton::State.__init__)


def test_ioautomaton::state_constructor_args():
    sig = inspect.signature(IOAutomaton::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::state_has_name():
    assert hasattr(IOAutomaton::State, "name")
    descriptor = None
    for klass in IOAutomaton::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ioautomaton::automaton_is_not_abstract():
    assert not inspect.isabstract(IOAutomaton::Automaton)


def test_ioautomaton::automaton_constructor_exists():
    assert callable(IOAutomaton::Automaton.__init__)


def test_ioautomaton::automaton_constructor_args():
    sig = inspect.signature(IOAutomaton::Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ioautomaton::automaton_has_name():
    assert hasattr(IOAutomaton::Automaton, "name")
    descriptor = None
    for klass in IOAutomaton::Automaton.__mro__:
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
IOAutomaton::ReturnValue_strategy = st.builds(
    IOAutomaton::ReturnValue,
    isVoid=
        st.booleans(),
    name=
        safe_text
)
IOAutomaton::Object_strategy = st.builds(
    IOAutomaton::Object,
    name=
        safe_text
)
IOAutomaton::Operation_strategy = st.builds(
    IOAutomaton::Operation,
    name=
        safe_text
)
IOAutomaton::Output_strategy = st.builds(
    IOAutomaton::Output,
    name=
        safe_text
)
IOAutomaton::Transition_strategy = st.builds(
    IOAutomaton::Transition,
    name=
        safe_text
)
IOAutomaton::Activation_strategy = st.builds(
    IOAutomaton::Activation,
    name=
        safe_text
)
IOAutomaton::Input_strategy = st.builds(
    IOAutomaton::Input,
    name=
        safe_text
)
IOAutomaton::State_strategy = st.builds(
    IOAutomaton::State,
    name=
        safe_text
)
IOAutomaton::Automaton_strategy = st.builds(
    IOAutomaton::Automaton,
    name=
        safe_text
)

@given(instance=IOAutomaton::ReturnValue_strategy)
@settings(max_examples=50)
def test_ioautomaton::returnvalue_instantiation(instance):
    assert isinstance(instance, IOAutomaton::ReturnValue)

@given(instance=IOAutomaton::ReturnValue_strategy)
def test_ioautomaton::returnvalue_isVoid_type(instance):
    assert isinstance(instance.isVoid, bool)


@given(instance=IOAutomaton::ReturnValue_strategy)
def test_ioautomaton::returnvalue_isVoid_setter(instance):
    original = instance.isVoid
    instance.isVoid = original
    assert instance.isVoid == original

@given(instance=IOAutomaton::ReturnValue_strategy)
def test_ioautomaton::returnvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=IOAutomaton::ReturnValue_strategy)
def test_ioautomaton::returnvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IOAutomaton::Object_strategy)
@settings(max_examples=50)
def test_ioautomaton::object_instantiation(instance):
    assert isinstance(instance, IOAutomaton::Object)

@given(instance=IOAutomaton::Object_strategy)
def test_ioautomaton::object_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=IOAutomaton::Object_strategy)
def test_ioautomaton::object_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IOAutomaton::Operation_strategy)
@settings(max_examples=50)
def test_ioautomaton::operation_instantiation(instance):
    assert isinstance(instance, IOAutomaton::Operation)

@given(instance=IOAutomaton::Operation_strategy)
def test_ioautomaton::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=IOAutomaton::Operation_strategy)
def test_ioautomaton::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IOAutomaton::Output_strategy)
@settings(max_examples=50)
def test_ioautomaton::output_instantiation(instance):
    assert isinstance(instance, IOAutomaton::Output)

@given(instance=IOAutomaton::Output_strategy)
def test_ioautomaton::output_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=IOAutomaton::Output_strategy)
def test_ioautomaton::output_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IOAutomaton::Transition_strategy)
@settings(max_examples=50)
def test_ioautomaton::transition_instantiation(instance):
    assert isinstance(instance, IOAutomaton::Transition)

@given(instance=IOAutomaton::Transition_strategy)
def test_ioautomaton::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=IOAutomaton::Transition_strategy)
def test_ioautomaton::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IOAutomaton::Activation_strategy)
@settings(max_examples=50)
def test_ioautomaton::activation_instantiation(instance):
    assert isinstance(instance, IOAutomaton::Activation)

@given(instance=IOAutomaton::Activation_strategy)
def test_ioautomaton::activation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=IOAutomaton::Activation_strategy)
def test_ioautomaton::activation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IOAutomaton::Input_strategy)
@settings(max_examples=50)
def test_ioautomaton::input_instantiation(instance):
    assert isinstance(instance, IOAutomaton::Input)

@given(instance=IOAutomaton::Input_strategy)
def test_ioautomaton::input_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=IOAutomaton::Input_strategy)
def test_ioautomaton::input_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IOAutomaton::State_strategy)
@settings(max_examples=50)
def test_ioautomaton::state_instantiation(instance):
    assert isinstance(instance, IOAutomaton::State)

@given(instance=IOAutomaton::State_strategy)
def test_ioautomaton::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=IOAutomaton::State_strategy)
def test_ioautomaton::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IOAutomaton::Automaton_strategy)
@settings(max_examples=50)
def test_ioautomaton::automaton_instantiation(instance):
    assert isinstance(instance, IOAutomaton::Automaton)

@given(instance=IOAutomaton::Automaton_strategy)
def test_ioautomaton::automaton_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=IOAutomaton::Automaton_strategy)
def test_ioautomaton::automaton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
