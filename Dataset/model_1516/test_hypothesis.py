import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mydsl::Transition,
    mydsl::State,
    mydsl::FSM,
    State,
    mydsl::Final,
    mydsl::Initial,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::transition_is_not_abstract():
    assert not inspect.isabstract(mydsl::Transition)


def test_mydsl::transition_constructor_exists():
    assert callable(mydsl::Transition.__init__)


def test_mydsl::transition_constructor_args():
    sig = inspect.signature(mydsl::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_mydsl::transition_has_name():
    assert hasattr(mydsl::Transition, "name")
    descriptor = None
    for klass in mydsl::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::transition_has_trigger():
    assert hasattr(mydsl::Transition, "trigger")
    descriptor = None
    for klass in mydsl::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::state_is_not_abstract():
    assert not inspect.isabstract(mydsl::State)


def test_mydsl::state_constructor_exists():
    assert callable(mydsl::State.__init__)


def test_mydsl::state_constructor_args():
    sig = inspect.signature(mydsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::state_has_name():
    assert hasattr(mydsl::State, "name")
    descriptor = None
    for klass in mydsl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::fsm_is_not_abstract():
    assert not inspect.isabstract(mydsl::FSM)


def test_mydsl::fsm_constructor_exists():
    assert callable(mydsl::FSM.__init__)


def test_mydsl::fsm_constructor_args():
    sig = inspect.signature(mydsl::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::fsm_has_name():
    assert hasattr(mydsl::FSM, "name")
    descriptor = None
    for klass in mydsl::FSM.__mro__:
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



def test_mydsl::final_is_not_abstract():
    assert not inspect.isabstract(mydsl::Final)


def test_mydsl::final_constructor_exists():
    assert callable(mydsl::Final.__init__)


def test_mydsl::final_constructor_args():
    sig = inspect.signature(mydsl::Final.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initial_is_not_abstract():
    assert not inspect.isabstract(mydsl::Initial)


def test_mydsl::initial_constructor_exists():
    assert callable(mydsl::Initial.__init__)


def test_mydsl::initial_constructor_args():
    sig = inspect.signature(mydsl::Initial.__init__)
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
mydsl::Transition_strategy = st.builds(
    mydsl::Transition,
    name=
        safe_text,
    trigger=
        safe_text
)
mydsl::State_strategy = st.builds(
    mydsl::State,
    name=
        safe_text
)
mydsl::FSM_strategy = st.builds(
    mydsl::FSM,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
mydsl::Final_strategy = st.builds(
    mydsl::Final,
)
mydsl::Initial_strategy = st.builds(
    mydsl::Initial,
)

@given(instance=mydsl::Transition_strategy)
@settings(max_examples=50)
def test_mydsl::transition_instantiation(instance):
    assert isinstance(instance, mydsl::Transition)

@given(instance=mydsl::Transition_strategy)
def test_mydsl::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mydsl::Transition_strategy)
def test_mydsl::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mydsl::Transition_strategy)
def test_mydsl::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=mydsl::Transition_strategy)
def test_mydsl::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=mydsl::State_strategy)
@settings(max_examples=50)
def test_mydsl::state_instantiation(instance):
    assert isinstance(instance, mydsl::State)

@given(instance=mydsl::State_strategy)
def test_mydsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mydsl::State_strategy)
def test_mydsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mydsl::FSM_strategy)
@settings(max_examples=50)
def test_mydsl::fsm_instantiation(instance):
    assert isinstance(instance, mydsl::FSM)

@given(instance=mydsl::FSM_strategy)
def test_mydsl::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mydsl::FSM_strategy)
def test_mydsl::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=mydsl::Final_strategy)
@settings(max_examples=50)
def test_mydsl::final_instantiation(instance):
    assert isinstance(instance, mydsl::Final)

@given(instance=mydsl::Initial_strategy)
@settings(max_examples=50)
def test_mydsl::initial_instantiation(instance):
    assert isinstance(instance, mydsl::Initial)
