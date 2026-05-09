import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    gfsm::State,
    gfsm::Transition,
    gfsm::Machine,
    State,
    gfsm::FinalState,
    gfsm::InitialState,
    gfsm::Guard,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gfsm::state_is_not_abstract():
    assert not inspect.isabstract(gfsm::State)


def test_gfsm::state_constructor_exists():
    assert callable(gfsm::State.__init__)


def test_gfsm::state_constructor_args():
    sig = inspect.signature(gfsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm::state_has_name():
    assert hasattr(gfsm::State, "name")
    descriptor = None
    for klass in gfsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gfsm::transition_is_not_abstract():
    assert not inspect.isabstract(gfsm::Transition)


def test_gfsm::transition_constructor_exists():
    assert callable(gfsm::Transition.__init__)


def test_gfsm::transition_constructor_args():
    sig = inspect.signature(gfsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_gfsm::transition_has_event():
    assert hasattr(gfsm::Transition, "event")
    descriptor = None
    for klass in gfsm::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_gfsm::machine_is_not_abstract():
    assert not inspect.isabstract(gfsm::Machine)


def test_gfsm::machine_constructor_exists():
    assert callable(gfsm::Machine.__init__)


def test_gfsm::machine_constructor_args():
    sig = inspect.signature(gfsm::Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gfsm::machine_has_name():
    assert hasattr(gfsm::Machine, "name")
    descriptor = None
    for klass in gfsm::Machine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(gfsm::FinalState)


def test_gfsm::finalstate_constructor_exists():
    assert callable(gfsm::FinalState.__init__)


def test_gfsm::finalstate_constructor_args():
    sig = inspect.signature(gfsm::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(gfsm::InitialState)


def test_gfsm::initialstate_constructor_exists():
    assert callable(gfsm::InitialState.__init__)


def test_gfsm::initialstate_constructor_args():
    sig = inspect.signature(gfsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::guard_is_not_abstract():
    assert not inspect.isabstract(gfsm::Guard)


def test_gfsm::guard_constructor_exists():
    assert callable(gfsm::Guard.__init__)


def test_gfsm::guard_constructor_args():
    sig = inspect.signature(gfsm::Guard.__init__)
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
gfsm::State_strategy = st.builds(
    gfsm::State,
    name=
        safe_text
)
gfsm::Transition_strategy = st.builds(
    gfsm::Transition,
    event=
        safe_text
)
gfsm::Machine_strategy = st.builds(
    gfsm::Machine,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
gfsm::FinalState_strategy = st.builds(
    gfsm::FinalState,
)
gfsm::InitialState_strategy = st.builds(
    gfsm::InitialState,
)
gfsm::Guard_strategy = st.builds(
    gfsm::Guard,
)

@given(instance=gfsm::State_strategy)
@settings(max_examples=50)
def test_gfsm::state_instantiation(instance):
    assert isinstance(instance, gfsm::State)

@given(instance=gfsm::State_strategy)
def test_gfsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gfsm::State_strategy)
def test_gfsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gfsm::Transition_strategy)
@settings(max_examples=50)
def test_gfsm::transition_instantiation(instance):
    assert isinstance(instance, gfsm::Transition)

@given(instance=gfsm::Transition_strategy)
def test_gfsm::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=gfsm::Transition_strategy)
def test_gfsm::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=gfsm::Machine_strategy)
@settings(max_examples=50)
def test_gfsm::machine_instantiation(instance):
    assert isinstance(instance, gfsm::Machine)

@given(instance=gfsm::Machine_strategy)
def test_gfsm::machine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gfsm::Machine_strategy)
def test_gfsm::machine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=gfsm::FinalState_strategy)
@settings(max_examples=50)
def test_gfsm::finalstate_instantiation(instance):
    assert isinstance(instance, gfsm::FinalState)

@given(instance=gfsm::InitialState_strategy)
@settings(max_examples=50)
def test_gfsm::initialstate_instantiation(instance):
    assert isinstance(instance, gfsm::InitialState)

@given(instance=gfsm::Guard_strategy)
@settings(max_examples=50)
def test_gfsm::guard_instantiation(instance):
    assert isinstance(instance, gfsm::Guard)
