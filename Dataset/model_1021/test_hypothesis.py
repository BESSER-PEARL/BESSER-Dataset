import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    dsl::State,
    dsl::FSM,
    dsl::InitialState,
    dsl::Transition,
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



def test_dsl::state_is_not_abstract():
    assert not inspect.isabstract(dsl::State)


def test_dsl::state_constructor_exists():
    assert callable(dsl::State.__init__)


def test_dsl::state_constructor_args():
    sig = inspect.signature(dsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"

def test_dsl::state_has_name():
    assert hasattr(dsl::State, "name")
    descriptor = None
    for klass in dsl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl::state_has_isFinal():
    assert hasattr(dsl::State, "isFinal")
    descriptor = None
    for klass in dsl::State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)



def test_dsl::fsm_is_not_abstract():
    assert not inspect.isabstract(dsl::FSM)


def test_dsl::fsm_constructor_exists():
    assert callable(dsl::FSM.__init__)


def test_dsl::fsm_constructor_args():
    sig = inspect.signature(dsl::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::fsm_has_name():
    assert hasattr(dsl::FSM, "name")
    descriptor = None
    for klass in dsl::FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::initialstate_is_not_abstract():
    assert not inspect.isabstract(dsl::InitialState)


def test_dsl::initialstate_constructor_exists():
    assert callable(dsl::InitialState.__init__)


def test_dsl::initialstate_constructor_args():
    sig = inspect.signature(dsl::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_dsl::transition_is_not_abstract():
    assert not inspect.isabstract(dsl::Transition)


def test_dsl::transition_constructor_exists():
    assert callable(dsl::Transition.__init__)


def test_dsl::transition_constructor_args():
    sig = inspect.signature(dsl::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::transition_has_trigger():
    assert hasattr(dsl::Transition, "trigger")
    descriptor = None
    for klass in dsl::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_dsl::transition_has_name():
    assert hasattr(dsl::Transition, "name")
    descriptor = None
    for klass in dsl::Transition.__mro__:
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
dsl::State_strategy = st.builds(
    dsl::State,
    name=
        safe_text,
    isFinal=
        st.booleans()
)
dsl::FSM_strategy = st.builds(
    dsl::FSM,
    name=
        safe_text
)
dsl::InitialState_strategy = st.builds(
    dsl::InitialState,
)
dsl::Transition_strategy = st.builds(
    dsl::Transition,
    trigger=
        safe_text,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=dsl::State_strategy)
@settings(max_examples=50)
def test_dsl::state_instantiation(instance):
    assert isinstance(instance, dsl::State)

@given(instance=dsl::State_strategy)
def test_dsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::State_strategy)
def test_dsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::State_strategy)
def test_dsl::state_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=dsl::State_strategy)
def test_dsl::state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=dsl::FSM_strategy)
@settings(max_examples=50)
def test_dsl::fsm_instantiation(instance):
    assert isinstance(instance, dsl::FSM)

@given(instance=dsl::FSM_strategy)
def test_dsl::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::FSM_strategy)
def test_dsl::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::InitialState_strategy)
@settings(max_examples=50)
def test_dsl::initialstate_instantiation(instance):
    assert isinstance(instance, dsl::InitialState)

@given(instance=dsl::Transition_strategy)
@settings(max_examples=50)
def test_dsl::transition_instantiation(instance):
    assert isinstance(instance, dsl::Transition)

@given(instance=dsl::Transition_strategy)
def test_dsl::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=dsl::Transition_strategy)
def test_dsl::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=dsl::Transition_strategy)
def test_dsl::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Transition_strategy)
def test_dsl::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
