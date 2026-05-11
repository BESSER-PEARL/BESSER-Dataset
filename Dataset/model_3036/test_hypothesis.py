import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    basicfsm::Action,
    basicfsm::Guard,
    basicfsm::Trans,
    basicfsm::State,
    basicfsm::Machine,
    State,
    basicfsm::InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basicfsm::action_is_not_abstract():
    assert not inspect.isabstract(basicfsm::Action)


def test_basicfsm::action_constructor_exists():
    assert callable(basicfsm::Action.__init__)


def test_basicfsm::action_constructor_args():
    sig = inspect.signature(basicfsm::Action.__init__)
    params = list(sig.parameters.keys())



def test_basicfsm::guard_is_not_abstract():
    assert not inspect.isabstract(basicfsm::Guard)


def test_basicfsm::guard_constructor_exists():
    assert callable(basicfsm::Guard.__init__)


def test_basicfsm::guard_constructor_args():
    sig = inspect.signature(basicfsm::Guard.__init__)
    params = list(sig.parameters.keys())



def test_basicfsm::trans_is_not_abstract():
    assert not inspect.isabstract(basicfsm::Trans)


def test_basicfsm::trans_constructor_exists():
    assert callable(basicfsm::Trans.__init__)


def test_basicfsm::trans_constructor_args():
    sig = inspect.signature(basicfsm::Trans.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_basicfsm::trans_has_event():
    assert hasattr(basicfsm::Trans, "event")
    descriptor = None
    for klass in basicfsm::Trans.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_basicfsm::state_is_not_abstract():
    assert not inspect.isabstract(basicfsm::State)


def test_basicfsm::state_constructor_exists():
    assert callable(basicfsm::State.__init__)


def test_basicfsm::state_constructor_args():
    sig = inspect.signature(basicfsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfsm::state_has_name():
    assert hasattr(basicfsm::State, "name")
    descriptor = None
    for klass in basicfsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basicfsm::machine_is_not_abstract():
    assert not inspect.isabstract(basicfsm::Machine)


def test_basicfsm::machine_constructor_exists():
    assert callable(basicfsm::Machine.__init__)


def test_basicfsm::machine_constructor_args():
    sig = inspect.signature(basicfsm::Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfsm::machine_has_name():
    assert hasattr(basicfsm::Machine, "name")
    descriptor = None
    for klass in basicfsm::Machine.__mro__:
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



def test_basicfsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(basicfsm::InitialState)


def test_basicfsm::initialstate_constructor_exists():
    assert callable(basicfsm::InitialState.__init__)


def test_basicfsm::initialstate_constructor_args():
    sig = inspect.signature(basicfsm::InitialState.__init__)
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
basicfsm::Action_strategy = st.builds(
    basicfsm::Action,
)
basicfsm::Guard_strategy = st.builds(
    basicfsm::Guard,
)
basicfsm::Trans_strategy = st.builds(
    basicfsm::Trans,
    event=
        safe_text
)
basicfsm::State_strategy = st.builds(
    basicfsm::State,
    name=
        safe_text
)
basicfsm::Machine_strategy = st.builds(
    basicfsm::Machine,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
basicfsm::InitialState_strategy = st.builds(
    basicfsm::InitialState,
)

@given(instance=basicfsm::Action_strategy)
@settings(max_examples=50)
def test_basicfsm::action_instantiation(instance):
    assert isinstance(instance, basicfsm::Action)

@given(instance=basicfsm::Guard_strategy)
@settings(max_examples=50)
def test_basicfsm::guard_instantiation(instance):
    assert isinstance(instance, basicfsm::Guard)

@given(instance=basicfsm::Trans_strategy)
@settings(max_examples=50)
def test_basicfsm::trans_instantiation(instance):
    assert isinstance(instance, basicfsm::Trans)

@given(instance=basicfsm::Trans_strategy)
def test_basicfsm::trans_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=basicfsm::Trans_strategy)
def test_basicfsm::trans_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=basicfsm::State_strategy)
@settings(max_examples=50)
def test_basicfsm::state_instantiation(instance):
    assert isinstance(instance, basicfsm::State)

@given(instance=basicfsm::State_strategy)
def test_basicfsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basicfsm::State_strategy)
def test_basicfsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basicfsm::Machine_strategy)
@settings(max_examples=50)
def test_basicfsm::machine_instantiation(instance):
    assert isinstance(instance, basicfsm::Machine)

@given(instance=basicfsm::Machine_strategy)
def test_basicfsm::machine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basicfsm::Machine_strategy)
def test_basicfsm::machine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=basicfsm::InitialState_strategy)
@settings(max_examples=50)
def test_basicfsm::initialstate_instantiation(instance):
    assert isinstance(instance, basicfsm::InitialState)
