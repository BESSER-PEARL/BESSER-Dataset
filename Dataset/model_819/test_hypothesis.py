import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lts_Transition,
    lts_State,
    lts_LTS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lts_transition_is_not_abstract():
    assert not inspect.isabstract(lts_Transition)


def test_lts_transition_constructor_exists():
    assert callable(lts_Transition.__init__)


def test_lts_transition_constructor_args():
    sig = inspect.signature(lts_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_lts_transition_has_input():
    assert hasattr(lts_Transition, "input")
    descriptor = None
    for klass in lts_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_lts_transition_has_output():
    assert hasattr(lts_Transition, "output")
    descriptor = None
    for klass in lts_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_lts_state_is_not_abstract():
    assert not inspect.isabstract(lts_State)


def test_lts_state_constructor_exists():
    assert callable(lts_State.__init__)


def test_lts_state_constructor_args():
    sig = inspect.signature(lts_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts_state_has_name():
    assert hasattr(lts_State, "name")
    descriptor = None
    for klass in lts_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts_lts_is_not_abstract():
    assert not inspect.isabstract(lts_LTS)


def test_lts_lts_constructor_exists():
    assert callable(lts_LTS.__init__)


def test_lts_lts_constructor_args():
    sig = inspect.signature(lts_LTS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts_lts_has_name():
    assert hasattr(lts_LTS, "name")
    descriptor = None
    for klass in lts_LTS.__mro__:
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
lts_Transition_strategy = st.builds(
    lts_Transition,
    input=
        safe_text,
    output=
        safe_text
)
lts_State_strategy = st.builds(
    lts_State,
    name=
        safe_text
)
lts_LTS_strategy = st.builds(
    lts_LTS,
    name=
        safe_text
)

@given(instance=lts_Transition_strategy)
@settings(max_examples=50)
def test_lts_transition_instantiation(instance):
    assert isinstance(instance, lts_Transition)



@given(instance=lts_Transition_strategy)
def test_lts_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=lts_Transition_strategy)
def test_lts_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=lts_State_strategy)
@settings(max_examples=50)
def test_lts_state_instantiation(instance):
    assert isinstance(instance, lts_State)



@given(instance=lts_State_strategy)
def test_lts_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts_LTS_strategy)
@settings(max_examples=50)
def test_lts_lts_instantiation(instance):
    assert isinstance(instance, lts_LTS)



@given(instance=lts_LTS_strategy)
def test_lts_lts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
