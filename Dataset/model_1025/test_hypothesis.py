import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    nicoLang::State,
    nicoLang::Transition,
    State,
    nicoLang::FinalState,
    nicoLang::InitState,
    nicoLang::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nicolang::state_is_not_abstract():
    assert not inspect.isabstract(nicoLang::State)


def test_nicolang::state_constructor_exists():
    assert callable(nicoLang::State.__init__)


def test_nicolang::state_constructor_args():
    sig = inspect.signature(nicoLang::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nicolang::state_has_name():
    assert hasattr(nicoLang::State, "name")
    descriptor = None
    for klass in nicoLang::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nicolang::transition_is_not_abstract():
    assert not inspect.isabstract(nicoLang::Transition)


def test_nicolang::transition_constructor_exists():
    assert callable(nicoLang::Transition.__init__)


def test_nicolang::transition_constructor_args():
    sig = inspect.signature(nicoLang::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_nicolang::transition_has_name():
    assert hasattr(nicoLang::Transition, "name")
    descriptor = None
    for klass in nicoLang::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nicolang::transition_has_trigger():
    assert hasattr(nicoLang::Transition, "trigger")
    descriptor = None
    for klass in nicoLang::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_nicolang::finalstate_is_not_abstract():
    assert not inspect.isabstract(nicoLang::FinalState)


def test_nicolang::finalstate_constructor_exists():
    assert callable(nicoLang::FinalState.__init__)


def test_nicolang::finalstate_constructor_args():
    sig = inspect.signature(nicoLang::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_nicolang::initstate_is_not_abstract():
    assert not inspect.isabstract(nicoLang::InitState)


def test_nicolang::initstate_constructor_exists():
    assert callable(nicoLang::InitState.__init__)


def test_nicolang::initstate_constructor_args():
    sig = inspect.signature(nicoLang::InitState.__init__)
    params = list(sig.parameters.keys())



def test_nicolang::fsm_is_not_abstract():
    assert not inspect.isabstract(nicoLang::FSM)


def test_nicolang::fsm_constructor_exists():
    assert callable(nicoLang::FSM.__init__)


def test_nicolang::fsm_constructor_args():
    sig = inspect.signature(nicoLang::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nicolang::fsm_has_name():
    assert hasattr(nicoLang::FSM, "name")
    descriptor = None
    for klass in nicoLang::FSM.__mro__:
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
nicoLang::State_strategy = st.builds(
    nicoLang::State,
    name=
        safe_text
)
nicoLang::Transition_strategy = st.builds(
    nicoLang::Transition,
    name=
        safe_text,
    trigger=
        safe_text
)
State_strategy = st.builds(
    State,
)
nicoLang::FinalState_strategy = st.builds(
    nicoLang::FinalState,
)
nicoLang::InitState_strategy = st.builds(
    nicoLang::InitState,
)
nicoLang::FSM_strategy = st.builds(
    nicoLang::FSM,
    name=
        safe_text
)

@given(instance=nicoLang::State_strategy)
@settings(max_examples=50)
def test_nicolang::state_instantiation(instance):
    assert isinstance(instance, nicoLang::State)

@given(instance=nicoLang::State_strategy)
def test_nicolang::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nicoLang::State_strategy)
def test_nicolang::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nicoLang::Transition_strategy)
@settings(max_examples=50)
def test_nicolang::transition_instantiation(instance):
    assert isinstance(instance, nicoLang::Transition)

@given(instance=nicoLang::Transition_strategy)
def test_nicolang::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nicoLang::Transition_strategy)
def test_nicolang::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nicoLang::Transition_strategy)
def test_nicolang::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=nicoLang::Transition_strategy)
def test_nicolang::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=nicoLang::FinalState_strategy)
@settings(max_examples=50)
def test_nicolang::finalstate_instantiation(instance):
    assert isinstance(instance, nicoLang::FinalState)

@given(instance=nicoLang::InitState_strategy)
@settings(max_examples=50)
def test_nicolang::initstate_instantiation(instance):
    assert isinstance(instance, nicoLang::InitState)

@given(instance=nicoLang::FSM_strategy)
@settings(max_examples=50)
def test_nicolang::fsm_instantiation(instance):
    assert isinstance(instance, nicoLang::FSM)

@given(instance=nicoLang::FSM_strategy)
def test_nicolang::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nicoLang::FSM_strategy)
def test_nicolang::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
