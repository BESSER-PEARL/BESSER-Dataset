import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    automata_Transition,
    automata_Final,
    automata_State,
    automata_Initial,
    automata_Current,
    automata_Automata,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_automata_transition_is_not_abstract():
    assert not inspect.isabstract(automata_Transition)


def test_automata_transition_constructor_exists():
    assert callable(automata_Transition.__init__)


def test_automata_transition_constructor_args():
    sig = inspect.signature(automata_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"
    assert "name" in params, "Missing parameter 'name'"

def test_automata_transition_has_token():
    assert hasattr(automata_Transition, "token")
    descriptor = None
    for klass in automata_Transition.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)

def test_automata_transition_has_name():
    assert hasattr(automata_Transition, "name")
    descriptor = None
    for klass in automata_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata_final_is_not_abstract():
    assert not inspect.isabstract(automata_Final)


def test_automata_final_constructor_exists():
    assert callable(automata_Final.__init__)


def test_automata_final_constructor_args():
    sig = inspect.signature(automata_Final.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automata_final_has_name():
    assert hasattr(automata_Final, "name")
    descriptor = None
    for klass in automata_Final.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata_state_is_not_abstract():
    assert not inspect.isabstract(automata_State)


def test_automata_state_constructor_exists():
    assert callable(automata_State.__init__)


def test_automata_state_constructor_args():
    sig = inspect.signature(automata_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automata_state_has_name():
    assert hasattr(automata_State, "name")
    descriptor = None
    for klass in automata_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata_initial_is_not_abstract():
    assert not inspect.isabstract(automata_Initial)


def test_automata_initial_constructor_exists():
    assert callable(automata_Initial.__init__)


def test_automata_initial_constructor_args():
    sig = inspect.signature(automata_Initial.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automata_initial_has_name():
    assert hasattr(automata_Initial, "name")
    descriptor = None
    for klass in automata_Initial.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata_current_is_not_abstract():
    assert not inspect.isabstract(automata_Current)


def test_automata_current_constructor_exists():
    assert callable(automata_Current.__init__)


def test_automata_current_constructor_args():
    sig = inspect.signature(automata_Current.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automata_current_has_name():
    assert hasattr(automata_Current, "name")
    descriptor = None
    for klass in automata_Current.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata_automata_is_not_abstract():
    assert not inspect.isabstract(automata_Automata)


def test_automata_automata_constructor_exists():
    assert callable(automata_Automata.__init__)


def test_automata_automata_constructor_args():
    sig = inspect.signature(automata_Automata.__init__)
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
automata_Transition_strategy = st.builds(
    automata_Transition,
    token=
        safe_text,
    name=
        safe_text
)
automata_Final_strategy = st.builds(
    automata_Final,
    name=
        safe_text
)
automata_State_strategy = st.builds(
    automata_State,
    name=
        safe_text
)
automata_Initial_strategy = st.builds(
    automata_Initial,
    name=
        safe_text
)
automata_Current_strategy = st.builds(
    automata_Current,
    name=
        safe_text
)
automata_Automata_strategy = st.builds(
    automata_Automata,
)

@given(instance=automata_Transition_strategy)
@settings(max_examples=50)
def test_automata_transition_instantiation(instance):
    assert isinstance(instance, automata_Transition)



@given(instance=automata_Transition_strategy)
def test_automata_transition_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original



@given(instance=automata_Transition_strategy)
def test_automata_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata_Final_strategy)
@settings(max_examples=50)
def test_automata_final_instantiation(instance):
    assert isinstance(instance, automata_Final)



@given(instance=automata_Final_strategy)
def test_automata_final_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata_State_strategy)
@settings(max_examples=50)
def test_automata_state_instantiation(instance):
    assert isinstance(instance, automata_State)



@given(instance=automata_State_strategy)
def test_automata_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata_Initial_strategy)
@settings(max_examples=50)
def test_automata_initial_instantiation(instance):
    assert isinstance(instance, automata_Initial)



@given(instance=automata_Initial_strategy)
def test_automata_initial_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata_Current_strategy)
@settings(max_examples=50)
def test_automata_current_instantiation(instance):
    assert isinstance(instance, automata_Current)



@given(instance=automata_Current_strategy)
def test_automata_current_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata_Automata_strategy)
@settings(max_examples=50)
def test_automata_automata_instantiation(instance):
    assert isinstance(instance, automata_Automata)
