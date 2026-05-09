import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::State,
    fsm::FSM,
    fsm::Transition,
    State,
    fsm::Initial,
    fsm::Final,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::state_has_name():
    assert hasattr(fsm::State, "name")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fsm::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fsm::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::fsm_has_name():
    assert hasattr(fsm::FSM, "name")
    descriptor = None
    for klass in fsm::FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::transition_has_trigger():
    assert hasattr(fsm::Transition, "trigger")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_name():
    assert hasattr(fsm::Transition, "name")
    descriptor = None
    for klass in fsm::Transition.__mro__:
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



def test_fsm::initial_is_not_abstract():
    assert not inspect.isabstract(fsm::Initial)


def test_fsm::initial_constructor_exists():
    assert callable(fsm::Initial.__init__)


def test_fsm::initial_constructor_args():
    sig = inspect.signature(fsm::Initial.__init__)
    params = list(sig.parameters.keys())



def test_fsm::final_is_not_abstract():
    assert not inspect.isabstract(fsm::Final)


def test_fsm::final_constructor_exists():
    assert callable(fsm::Final.__init__)


def test_fsm::final_constructor_args():
    sig = inspect.signature(fsm::Final.__init__)
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
fsm::State_strategy = st.builds(
    fsm::State,
    name=
        safe_text
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
    name=
        safe_text
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    trigger=
        safe_text,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm::Initial_strategy = st.builds(
    fsm::Initial,
)
fsm::Final_strategy = st.builds(
    fsm::Final,
)

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fsm::FSM)

@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::Initial_strategy)
@settings(max_examples=50)
def test_fsm::initial_instantiation(instance):
    assert isinstance(instance, fsm::Initial)

@given(instance=fsm::Final_strategy)
@settings(max_examples=50)
def test_fsm::final_instantiation(instance):
    assert isinstance(instance, fsm::Final)
