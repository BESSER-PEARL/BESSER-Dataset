import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::tp::Transition,
    fsm::tp::State,
    fsm::tp::FSM,
    State,
    fsm::tp::InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::tp::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::tp::Transition)


def test_fsm::tp::transition_constructor_exists():
    assert callable(fsm::tp::Transition.__init__)


def test_fsm::tp::transition_constructor_args():
    sig = inspect.signature(fsm::tp::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_fsm::tp::transition_has_name():
    assert hasattr(fsm::tp::Transition, "name")
    descriptor = None
    for klass in fsm::tp::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsm::tp::transition_has_trigger():
    assert hasattr(fsm::tp::Transition, "trigger")
    descriptor = None
    for klass in fsm::tp::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_fsm::tp::state_is_not_abstract():
    assert not inspect.isabstract(fsm::tp::State)


def test_fsm::tp::state_constructor_exists():
    assert callable(fsm::tp::State.__init__)


def test_fsm::tp::state_constructor_args():
    sig = inspect.signature(fsm::tp::State.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::tp::state_has_isFinal():
    assert hasattr(fsm::tp::State, "isFinal")
    descriptor = None
    for klass in fsm::tp::State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_fsm::tp::state_has_name():
    assert hasattr(fsm::tp::State, "name")
    descriptor = None
    for klass in fsm::tp::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::tp::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::tp::FSM)


def test_fsm::tp::fsm_constructor_exists():
    assert callable(fsm::tp::FSM.__init__)


def test_fsm::tp::fsm_constructor_args():
    sig = inspect.signature(fsm::tp::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::tp::fsm_has_name():
    assert hasattr(fsm::tp::FSM, "name")
    descriptor = None
    for klass in fsm::tp::FSM.__mro__:
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



def test_fsm::tp::initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm::tp::InitialState)


def test_fsm::tp::initialstate_constructor_exists():
    assert callable(fsm::tp::InitialState.__init__)


def test_fsm::tp::initialstate_constructor_args():
    sig = inspect.signature(fsm::tp::InitialState.__init__)
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
fsm::tp::Transition_strategy = st.builds(
    fsm::tp::Transition,
    name=
        safe_text,
    trigger=
        safe_text
)
fsm::tp::State_strategy = st.builds(
    fsm::tp::State,
    isFinal=
        st.booleans(),
    name=
        safe_text
)
fsm::tp::FSM_strategy = st.builds(
    fsm::tp::FSM,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm::tp::InitialState_strategy = st.builds(
    fsm::tp::InitialState,
)

@given(instance=fsm::tp::Transition_strategy)
@settings(max_examples=50)
def test_fsm::tp::transition_instantiation(instance):
    assert isinstance(instance, fsm::tp::Transition)

@given(instance=fsm::tp::Transition_strategy)
def test_fsm::tp::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::tp::Transition_strategy)
def test_fsm::tp::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::tp::Transition_strategy)
def test_fsm::tp::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=fsm::tp::Transition_strategy)
def test_fsm::tp::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=fsm::tp::State_strategy)
@settings(max_examples=50)
def test_fsm::tp::state_instantiation(instance):
    assert isinstance(instance, fsm::tp::State)

@given(instance=fsm::tp::State_strategy)
def test_fsm::tp::state_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=fsm::tp::State_strategy)
def test_fsm::tp::state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=fsm::tp::State_strategy)
def test_fsm::tp::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::tp::State_strategy)
def test_fsm::tp::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::tp::FSM_strategy)
@settings(max_examples=50)
def test_fsm::tp::fsm_instantiation(instance):
    assert isinstance(instance, fsm::tp::FSM)

@given(instance=fsm::tp::FSM_strategy)
def test_fsm::tp::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::tp::FSM_strategy)
def test_fsm::tp::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::tp::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::tp::initialstate_instantiation(instance):
    assert isinstance(instance, fsm::tp::InitialState)
