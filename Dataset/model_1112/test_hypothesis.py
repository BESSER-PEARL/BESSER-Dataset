import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    states::CompoundState,
    states::SimpleState,
    states::Transition,
    states::State,
    states::Event,
    states::Statemachine,
    states::Module,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_states::compoundstate_is_not_abstract():
    assert not inspect.isabstract(states::CompoundState)


def test_states::compoundstate_constructor_exists():
    assert callable(states::CompoundState.__init__)


def test_states::compoundstate_constructor_args():
    sig = inspect.signature(states::CompoundState.__init__)
    params = list(sig.parameters.keys())



def test_states::simplestate_is_not_abstract():
    assert not inspect.isabstract(states::SimpleState)


def test_states::simplestate_constructor_exists():
    assert callable(states::SimpleState.__init__)


def test_states::simplestate_constructor_args():
    sig = inspect.signature(states::SimpleState.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_states::simplestate_has_value():
    assert hasattr(states::SimpleState, "value")
    descriptor = None
    for klass in states::SimpleState.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_states::transition_is_not_abstract():
    assert not inspect.isabstract(states::Transition)


def test_states::transition_constructor_exists():
    assert callable(states::Transition.__init__)


def test_states::transition_constructor_args():
    sig = inspect.signature(states::Transition.__init__)
    params = list(sig.parameters.keys())



def test_states::state_is_not_abstract():
    assert not inspect.isabstract(states::State)


def test_states::state_constructor_exists():
    assert callable(states::State.__init__)


def test_states::state_constructor_args():
    sig = inspect.signature(states::State.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_states::state_has_initial():
    assert hasattr(states::State, "initial")
    descriptor = None
    for klass in states::State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_states::state_has_name():
    assert hasattr(states::State, "name")
    descriptor = None
    for klass in states::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_states::event_is_not_abstract():
    assert not inspect.isabstract(states::Event)


def test_states::event_constructor_exists():
    assert callable(states::Event.__init__)


def test_states::event_constructor_args():
    sig = inspect.signature(states::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_states::event_has_name():
    assert hasattr(states::Event, "name")
    descriptor = None
    for klass in states::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_states::statemachine_is_not_abstract():
    assert not inspect.isabstract(states::Statemachine)


def test_states::statemachine_constructor_exists():
    assert callable(states::Statemachine.__init__)


def test_states::statemachine_constructor_args():
    sig = inspect.signature(states::Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_states::statemachine_has_name():
    assert hasattr(states::Statemachine, "name")
    descriptor = None
    for klass in states::Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_states::statemachine_has_value():
    assert hasattr(states::Statemachine, "value")
    descriptor = None
    for klass in states::Statemachine.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_states::statemachine_has_initial():
    assert hasattr(states::Statemachine, "initial")
    descriptor = None
    for klass in states::Statemachine.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_states::module_is_not_abstract():
    assert not inspect.isabstract(states::Module)


def test_states::module_constructor_exists():
    assert callable(states::Module.__init__)


def test_states::module_constructor_args():
    sig = inspect.signature(states::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_states::module_has_name():
    assert hasattr(states::Module, "name")
    descriptor = None
    for klass in states::Module.__mro__:
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
State_strategy = st.builds(
    State,
)
states::CompoundState_strategy = st.builds(
    states::CompoundState,
)
states::SimpleState_strategy = st.builds(
    states::SimpleState,
    value=
        st.integers()
)
states::Transition_strategy = st.builds(
    states::Transition,
)
states::State_strategy = st.builds(
    states::State,
    initial=
        st.booleans(),
    name=
        safe_text
)
states::Event_strategy = st.builds(
    states::Event,
    name=
        safe_text
)
states::Statemachine_strategy = st.builds(
    states::Statemachine,
    name=
        safe_text,
    value=
        st.integers(),
    initial=
        st.booleans()
)
states::Module_strategy = st.builds(
    states::Module,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=states::CompoundState_strategy)
@settings(max_examples=50)
def test_states::compoundstate_instantiation(instance):
    assert isinstance(instance, states::CompoundState)

@given(instance=states::SimpleState_strategy)
@settings(max_examples=50)
def test_states::simplestate_instantiation(instance):
    assert isinstance(instance, states::SimpleState)

@given(instance=states::SimpleState_strategy)
def test_states::simplestate_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=states::SimpleState_strategy)
def test_states::simplestate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=states::Transition_strategy)
@settings(max_examples=50)
def test_states::transition_instantiation(instance):
    assert isinstance(instance, states::Transition)

@given(instance=states::State_strategy)
@settings(max_examples=50)
def test_states::state_instantiation(instance):
    assert isinstance(instance, states::State)

@given(instance=states::State_strategy)
def test_states::state_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=states::State_strategy)
def test_states::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=states::State_strategy)
def test_states::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=states::State_strategy)
def test_states::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=states::Event_strategy)
@settings(max_examples=50)
def test_states::event_instantiation(instance):
    assert isinstance(instance, states::Event)

@given(instance=states::Event_strategy)
def test_states::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=states::Event_strategy)
def test_states::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=states::Statemachine_strategy)
@settings(max_examples=50)
def test_states::statemachine_instantiation(instance):
    assert isinstance(instance, states::Statemachine)

@given(instance=states::Statemachine_strategy)
def test_states::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=states::Statemachine_strategy)
def test_states::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=states::Statemachine_strategy)
def test_states::statemachine_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=states::Statemachine_strategy)
def test_states::statemachine_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=states::Statemachine_strategy)
def test_states::statemachine_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=states::Statemachine_strategy)
def test_states::statemachine_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=states::Module_strategy)
@settings(max_examples=50)
def test_states::module_instantiation(instance):
    assert isinstance(instance, states::Module)

@given(instance=states::Module_strategy)
def test_states::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=states::Module_strategy)
def test_states::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
