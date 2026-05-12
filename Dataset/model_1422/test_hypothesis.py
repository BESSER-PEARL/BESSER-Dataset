import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_Command,
    Signal,
    statemachine_OutputSignal,
    statemachine_InputSignal,
    statemachine_State,
    statemachine_Signal,
    statemachine_Statemachine,
    statemachine_Event,
    statemachine_Condition,
    statemachine_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_command_is_not_abstract():
    assert not inspect.isabstract(statemachine_Command)


def test_statemachine_command_constructor_exists():
    assert callable(statemachine_Command.__init__)


def test_statemachine_command_constructor_args():
    sig = inspect.signature(statemachine_Command.__init__)
    params = list(sig.parameters.keys())
    assert "newValue" in params, "Missing parameter 'newValue'"

def test_statemachine_command_has_newValue():
    assert hasattr(statemachine_Command, "newValue")
    descriptor = None
    for klass in statemachine_Command.__mro__:
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



def test_statemachine_outputsignal_is_not_abstract():
    assert not inspect.isabstract(statemachine_OutputSignal)


def test_statemachine_outputsignal_constructor_exists():
    assert callable(statemachine_OutputSignal.__init__)


def test_statemachine_outputsignal_constructor_args():
    sig = inspect.signature(statemachine_OutputSignal.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_inputsignal_is_not_abstract():
    assert not inspect.isabstract(statemachine_InputSignal)


def test_statemachine_inputsignal_constructor_exists():
    assert callable(statemachine_InputSignal.__init__)


def test_statemachine_inputsignal_constructor_args():
    sig = inspect.signature(statemachine_InputSignal.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_state_has_name():
    assert hasattr(statemachine_State, "name")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_signal_is_not_abstract():
    assert not inspect.isabstract(statemachine_Signal)


def test_statemachine_signal_constructor_exists():
    assert callable(statemachine_Signal.__init__)


def test_statemachine_signal_constructor_args():
    sig = inspect.signature(statemachine_Signal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_signal_has_name():
    assert hasattr(statemachine_Signal, "name")
    descriptor = None
    for klass in statemachine_Signal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statemachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_Statemachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_Statemachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(statemachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(statemachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(statemachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statemachine_event_has_value():
    assert hasattr(statemachine_Event, "value")
    descriptor = None
    for klass in statemachine_Event.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_condition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Condition)


def test_statemachine_condition_constructor_exists():
    assert callable(statemachine_Condition.__init__)


def test_statemachine_condition_constructor_args():
    sig = inspect.signature(statemachine_Condition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
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
statemachine_Command_strategy = st.builds(
    statemachine_Command,
    newValue=
        st.booleans()
)
Signal_strategy = st.builds(
    Signal,
)
statemachine_OutputSignal_strategy = st.builds(
    statemachine_OutputSignal,
)
statemachine_InputSignal_strategy = st.builds(
    statemachine_InputSignal,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    name=
        safe_text
)
statemachine_Signal_strategy = st.builds(
    statemachine_Signal,
    name=
        safe_text
)
statemachine_Statemachine_strategy = st.builds(
    statemachine_Statemachine,
)
statemachine_Event_strategy = st.builds(
    statemachine_Event,
    value=
        st.booleans()
)
statemachine_Condition_strategy = st.builds(
    statemachine_Condition,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)

@given(instance=statemachine_Command_strategy)
@settings(max_examples=50)
def test_statemachine_command_instantiation(instance):
    assert isinstance(instance, statemachine_Command)



@given(instance=statemachine_Command_strategy)
def test_statemachine_command_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=statemachine_OutputSignal_strategy)
@settings(max_examples=50)
def test_statemachine_outputsignal_instantiation(instance):
    assert isinstance(instance, statemachine_OutputSignal)

@given(instance=statemachine_InputSignal_strategy)
@settings(max_examples=50)
def test_statemachine_inputsignal_instantiation(instance):
    assert isinstance(instance, statemachine_InputSignal)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_Signal_strategy)
@settings(max_examples=50)
def test_statemachine_signal_instantiation(instance):
    assert isinstance(instance, statemachine_Signal)



@given(instance=statemachine_Signal_strategy)
def test_statemachine_signal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)

@given(instance=statemachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, statemachine_Event)



@given(instance=statemachine_Event_strategy)
def test_statemachine_event_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statemachine_Condition_strategy)
@settings(max_examples=50)
def test_statemachine_condition_instantiation(instance):
    assert isinstance(instance, statemachine_Condition)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)
