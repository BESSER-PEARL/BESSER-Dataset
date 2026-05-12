import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    automata::Transition,
    automata::Final,
    automata::State,
    automata::Initial,
    automata::Current,
    automata::Automata,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_automata::transition_is_not_abstract():
    assert not inspect.isabstract(automata::Transition)


def test_automata::transition_constructor_exists():
    assert callable(automata::Transition.__init__)


def test_automata::transition_constructor_args():
    sig = inspect.signature(automata::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"
    assert "name" in params, "Missing parameter 'name'"

def test_automata::transition_has_token():
    assert hasattr(automata::Transition, "token")
    descriptor = None
    for klass in automata::Transition.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)

def test_automata::transition_has_name():
    assert hasattr(automata::Transition, "name")
    descriptor = None
    for klass in automata::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata::final_is_not_abstract():
    assert not inspect.isabstract(automata::Final)


def test_automata::final_constructor_exists():
    assert callable(automata::Final.__init__)


def test_automata::final_constructor_args():
    sig = inspect.signature(automata::Final.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automata::final_has_name():
    assert hasattr(automata::Final, "name")
    descriptor = None
    for klass in automata::Final.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata::state_is_not_abstract():
    assert not inspect.isabstract(automata::State)


def test_automata::state_constructor_exists():
    assert callable(automata::State.__init__)


def test_automata::state_constructor_args():
    sig = inspect.signature(automata::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automata::state_has_name():
    assert hasattr(automata::State, "name")
    descriptor = None
    for klass in automata::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata::initial_is_not_abstract():
    assert not inspect.isabstract(automata::Initial)


def test_automata::initial_constructor_exists():
    assert callable(automata::Initial.__init__)


def test_automata::initial_constructor_args():
    sig = inspect.signature(automata::Initial.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automata::initial_has_name():
    assert hasattr(automata::Initial, "name")
    descriptor = None
    for klass in automata::Initial.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata::current_is_not_abstract():
    assert not inspect.isabstract(automata::Current)


def test_automata::current_constructor_exists():
    assert callable(automata::Current.__init__)


def test_automata::current_constructor_args():
    sig = inspect.signature(automata::Current.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automata::current_has_name():
    assert hasattr(automata::Current, "name")
    descriptor = None
    for klass in automata::Current.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata::automata_is_not_abstract():
    assert not inspect.isabstract(automata::Automata)


def test_automata::automata_constructor_exists():
    assert callable(automata::Automata.__init__)


def test_automata::automata_constructor_args():
    sig = inspect.signature(automata::Automata.__init__)
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
automata::Transition_strategy = st.builds(
    automata::Transition,
    token=
        safe_text,
    name=
        safe_text
)
automata::Final_strategy = st.builds(
    automata::Final,
    name=
        safe_text
)
automata::State_strategy = st.builds(
    automata::State,
    name=
        safe_text
)
automata::Initial_strategy = st.builds(
    automata::Initial,
    name=
        safe_text
)
automata::Current_strategy = st.builds(
    automata::Current,
    name=
        safe_text
)
automata::Automata_strategy = st.builds(
    automata::Automata,
)

@given(instance=automata::Transition_strategy)
@settings(max_examples=50)
def test_automata::transition_instantiation(instance):
    assert isinstance(instance, automata::Transition)

@given(instance=automata::Transition_strategy)
def test_automata::transition_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=automata::Transition_strategy)
def test_automata::transition_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=automata::Transition_strategy)
def test_automata::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automata::Transition_strategy)
def test_automata::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata::Final_strategy)
@settings(max_examples=50)
def test_automata::final_instantiation(instance):
    assert isinstance(instance, automata::Final)

@given(instance=automata::Final_strategy)
def test_automata::final_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automata::Final_strategy)
def test_automata::final_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata::State_strategy)
@settings(max_examples=50)
def test_automata::state_instantiation(instance):
    assert isinstance(instance, automata::State)

@given(instance=automata::State_strategy)
def test_automata::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automata::State_strategy)
def test_automata::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata::Initial_strategy)
@settings(max_examples=50)
def test_automata::initial_instantiation(instance):
    assert isinstance(instance, automata::Initial)

@given(instance=automata::Initial_strategy)
def test_automata::initial_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automata::Initial_strategy)
def test_automata::initial_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata::Current_strategy)
@settings(max_examples=50)
def test_automata::current_instantiation(instance):
    assert isinstance(instance, automata::Current)

@given(instance=automata::Current_strategy)
def test_automata::current_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automata::Current_strategy)
def test_automata::current_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata::Automata_strategy)
@settings(max_examples=50)
def test_automata::automata_instantiation(instance):
    assert isinstance(instance, automata::Automata)
