import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachine::State,
    statemachine::Event,
    statemachine::Condition,
    statemachine::Transition,
    statemachine::Signal,
    statemachine::Statemachine,
    statemachine::Command,
    Signal,
    statemachine::OutputSignal,
    statemachine::InputSignal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::state_has_name():
    assert hasattr(statemachine::State, "name")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(statemachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(statemachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(statemachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachine::event_has_value():
    assert hasattr(statemachine::Event, "value")
    descriptor = None
    for klass in statemachine::Event.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::condition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Condition)


def test_statemachine::condition_constructor_exists():
    assert callable(statemachine::Condition.__init__)


def test_statemachine::condition_constructor_args():
    sig = inspect.signature(statemachine::Condition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::signal_is_not_abstract():
    assert not inspect.isabstract(statemachine::Signal)


def test_statemachine::signal_constructor_exists():
    assert callable(statemachine::Signal.__init__)


def test_statemachine::signal_constructor_args():
    sig = inspect.signature(statemachine::Signal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::signal_has_name():
    assert hasattr(statemachine::Signal, "name")
    descriptor = None
    for klass in statemachine::Signal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::Statemachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::Statemachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::command_is_not_abstract():
    assert not inspect.isabstract(statemachine::Command)


def test_statemachine::command_constructor_exists():
    assert callable(statemachine::Command.__init__)


def test_statemachine::command_constructor_args():
    sig = inspect.signature(statemachine::Command.__init__)
    params = list(sig.parameters.keys())
    assert "newValue" in params, "Missing parameter 'newValue'"

def test_statemachine::command_has_newValue():
    assert hasattr(statemachine::Command, "newValue")
    descriptor = None
    for klass in statemachine::Command.__mro__:
        if "newValue" in klass.__dict__:
            descriptor = klass.__dict__["newValue"]
            break
    assert isinstance(descriptor, property)



def test_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::outputsignal_is_not_abstract():
    assert not inspect.isabstract(statemachine::OutputSignal)


def test_statemachine::outputsignal_constructor_exists():
    assert callable(statemachine::OutputSignal.__init__)


def test_statemachine::outputsignal_constructor_args():
    sig = inspect.signature(statemachine::OutputSignal.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::inputsignal_is_not_abstract():
    assert not inspect.isabstract(statemachine::InputSignal)


def test_statemachine::inputsignal_constructor_exists():
    assert callable(statemachine::InputSignal.__init__)


def test_statemachine::inputsignal_constructor_args():
    sig = inspect.signature(statemachine::InputSignal.__init__)
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
statemachine::State_strategy = st.builds(
    statemachine::State,
    name=
        safe_text
)
statemachine::Event_strategy = st.builds(
    statemachine::Event,
    value=
        st.booleans()
)
statemachine::Condition_strategy = st.builds(
    statemachine::Condition,
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
)
statemachine::Signal_strategy = st.builds(
    statemachine::Signal,
    name=
        safe_text
)
statemachine::Statemachine_strategy = st.builds(
    statemachine::Statemachine,
)
statemachine::Command_strategy = st.builds(
    statemachine::Command,
    newValue=
        st.booleans()
)
Signal_strategy = st.builds(
    Signal,
)
statemachine::OutputSignal_strategy = st.builds(
    statemachine::OutputSignal,
)
statemachine::InputSignal_strategy = st.builds(
    statemachine::InputSignal,
)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, statemachine::Event)

@given(instance=statemachine::Event_strategy)
def test_statemachine::event_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=statemachine::Event_strategy)
def test_statemachine::event_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachine::Condition_strategy)
@settings(max_examples=50)
def test_statemachine::condition_instantiation(instance):
    assert isinstance(instance, statemachine::Condition)

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Signal_strategy)
@settings(max_examples=50)
def test_statemachine::signal_instantiation(instance):
    assert isinstance(instance, statemachine::Signal)

@given(instance=statemachine::Signal_strategy)
def test_statemachine::signal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Signal_strategy)
def test_statemachine::signal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::Statemachine)

@given(instance=statemachine::Command_strategy)
@settings(max_examples=50)
def test_statemachine::command_instantiation(instance):
    assert isinstance(instance, statemachine::Command)

@given(instance=statemachine::Command_strategy)
def test_statemachine::command_newValue_type(instance):
    assert isinstance(instance.newValue, bool)


@given(instance=statemachine::Command_strategy)
def test_statemachine::command_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=statemachine::OutputSignal_strategy)
@settings(max_examples=50)
def test_statemachine::outputsignal_instantiation(instance):
    assert isinstance(instance, statemachine::OutputSignal)

@given(instance=statemachine::InputSignal_strategy)
@settings(max_examples=50)
def test_statemachine::inputsignal_instantiation(instance):
    assert isinstance(instance, statemachine::InputSignal)
