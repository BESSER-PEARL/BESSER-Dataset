import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    oclstates::CompoundState,
    oclstates::SimpleState,
    oclstates::Transition,
    oclstates::State,
    oclstates::Event,
    oclstates::Statemachine,
    oclstates::Module,
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



def test_oclstates::compoundstate_is_not_abstract():
    assert not inspect.isabstract(oclstates::CompoundState)


def test_oclstates::compoundstate_constructor_exists():
    assert callable(oclstates::CompoundState.__init__)


def test_oclstates::compoundstate_constructor_args():
    sig = inspect.signature(oclstates::CompoundState.__init__)
    params = list(sig.parameters.keys())



def test_oclstates::simplestate_is_not_abstract():
    assert not inspect.isabstract(oclstates::SimpleState)


def test_oclstates::simplestate_constructor_exists():
    assert callable(oclstates::SimpleState.__init__)


def test_oclstates::simplestate_constructor_args():
    sig = inspect.signature(oclstates::SimpleState.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oclstates::simplestate_has_value():
    assert hasattr(oclstates::SimpleState, "value")
    descriptor = None
    for klass in oclstates::SimpleState.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oclstates::transition_is_not_abstract():
    assert not inspect.isabstract(oclstates::Transition)


def test_oclstates::transition_constructor_exists():
    assert callable(oclstates::Transition.__init__)


def test_oclstates::transition_constructor_args():
    sig = inspect.signature(oclstates::Transition.__init__)
    params = list(sig.parameters.keys())



def test_oclstates::state_is_not_abstract():
    assert not inspect.isabstract(oclstates::State)


def test_oclstates::state_constructor_exists():
    assert callable(oclstates::State.__init__)


def test_oclstates::state_constructor_args():
    sig = inspect.signature(oclstates::State.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_oclstates::state_has_initial():
    assert hasattr(oclstates::State, "initial")
    descriptor = None
    for klass in oclstates::State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_oclstates::state_has_name():
    assert hasattr(oclstates::State, "name")
    descriptor = None
    for klass in oclstates::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclstates::event_is_not_abstract():
    assert not inspect.isabstract(oclstates::Event)


def test_oclstates::event_constructor_exists():
    assert callable(oclstates::Event.__init__)


def test_oclstates::event_constructor_args():
    sig = inspect.signature(oclstates::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclstates::event_has_name():
    assert hasattr(oclstates::Event, "name")
    descriptor = None
    for klass in oclstates::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclstates::statemachine_is_not_abstract():
    assert not inspect.isabstract(oclstates::Statemachine)


def test_oclstates::statemachine_constructor_exists():
    assert callable(oclstates::Statemachine.__init__)


def test_oclstates::statemachine_constructor_args():
    sig = inspect.signature(oclstates::Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_oclstates::statemachine_has_initial():
    assert hasattr(oclstates::Statemachine, "initial")
    descriptor = None
    for klass in oclstates::Statemachine.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_oclstates::statemachine_has_name():
    assert hasattr(oclstates::Statemachine, "name")
    descriptor = None
    for klass in oclstates::Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oclstates::statemachine_has_value():
    assert hasattr(oclstates::Statemachine, "value")
    descriptor = None
    for klass in oclstates::Statemachine.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oclstates::module_is_not_abstract():
    assert not inspect.isabstract(oclstates::Module)


def test_oclstates::module_constructor_exists():
    assert callable(oclstates::Module.__init__)


def test_oclstates::module_constructor_args():
    sig = inspect.signature(oclstates::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclstates::module_has_name():
    assert hasattr(oclstates::Module, "name")
    descriptor = None
    for klass in oclstates::Module.__mro__:
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
oclstates::CompoundState_strategy = st.builds(
    oclstates::CompoundState,
)
oclstates::SimpleState_strategy = st.builds(
    oclstates::SimpleState,
    value=
        st.integers()
)
oclstates::Transition_strategy = st.builds(
    oclstates::Transition,
)
oclstates::State_strategy = st.builds(
    oclstates::State,
    initial=
        st.booleans(),
    name=
        safe_text
)
oclstates::Event_strategy = st.builds(
    oclstates::Event,
    name=
        safe_text
)
oclstates::Statemachine_strategy = st.builds(
    oclstates::Statemachine,
    initial=
        st.booleans(),
    name=
        safe_text,
    value=
        st.integers()
)
oclstates::Module_strategy = st.builds(
    oclstates::Module,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=oclstates::CompoundState_strategy)
@settings(max_examples=50)
def test_oclstates::compoundstate_instantiation(instance):
    assert isinstance(instance, oclstates::CompoundState)

@given(instance=oclstates::SimpleState_strategy)
@settings(max_examples=50)
def test_oclstates::simplestate_instantiation(instance):
    assert isinstance(instance, oclstates::SimpleState)

@given(instance=oclstates::SimpleState_strategy)
def test_oclstates::simplestate_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=oclstates::SimpleState_strategy)
def test_oclstates::simplestate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oclstates::Transition_strategy)
@settings(max_examples=50)
def test_oclstates::transition_instantiation(instance):
    assert isinstance(instance, oclstates::Transition)

@given(instance=oclstates::State_strategy)
@settings(max_examples=50)
def test_oclstates::state_instantiation(instance):
    assert isinstance(instance, oclstates::State)

@given(instance=oclstates::State_strategy)
def test_oclstates::state_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=oclstates::State_strategy)
def test_oclstates::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=oclstates::State_strategy)
def test_oclstates::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oclstates::State_strategy)
def test_oclstates::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oclstates::Event_strategy)
@settings(max_examples=50)
def test_oclstates::event_instantiation(instance):
    assert isinstance(instance, oclstates::Event)

@given(instance=oclstates::Event_strategy)
def test_oclstates::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oclstates::Event_strategy)
def test_oclstates::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oclstates::Statemachine_strategy)
@settings(max_examples=50)
def test_oclstates::statemachine_instantiation(instance):
    assert isinstance(instance, oclstates::Statemachine)

@given(instance=oclstates::Statemachine_strategy)
def test_oclstates::statemachine_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=oclstates::Statemachine_strategy)
def test_oclstates::statemachine_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=oclstates::Statemachine_strategy)
def test_oclstates::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oclstates::Statemachine_strategy)
def test_oclstates::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oclstates::Statemachine_strategy)
def test_oclstates::statemachine_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=oclstates::Statemachine_strategy)
def test_oclstates::statemachine_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oclstates::Module_strategy)
@settings(max_examples=50)
def test_oclstates::module_instantiation(instance):
    assert isinstance(instance, oclstates::Module)

@given(instance=oclstates::Module_strategy)
def test_oclstates::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oclstates::Module_strategy)
def test_oclstates::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
