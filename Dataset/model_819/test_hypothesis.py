import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lts::Transition,
    lts::State,
    lts::LTS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lts::transition_is_not_abstract():
    assert not inspect.isabstract(lts::Transition)


def test_lts::transition_constructor_exists():
    assert callable(lts::Transition.__init__)


def test_lts::transition_constructor_args():
    sig = inspect.signature(lts::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_lts::transition_has_output():
    assert hasattr(lts::Transition, "output")
    descriptor = None
    for klass in lts::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_lts::transition_has_input():
    assert hasattr(lts::Transition, "input")
    descriptor = None
    for klass in lts::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_lts::state_is_not_abstract():
    assert not inspect.isabstract(lts::State)


def test_lts::state_constructor_exists():
    assert callable(lts::State.__init__)


def test_lts::state_constructor_args():
    sig = inspect.signature(lts::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts::state_has_name():
    assert hasattr(lts::State, "name")
    descriptor = None
    for klass in lts::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts::lts_is_not_abstract():
    assert not inspect.isabstract(lts::LTS)


def test_lts::lts_constructor_exists():
    assert callable(lts::LTS.__init__)


def test_lts::lts_constructor_args():
    sig = inspect.signature(lts::LTS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts::lts_has_name():
    assert hasattr(lts::LTS, "name")
    descriptor = None
    for klass in lts::LTS.__mro__:
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
lts::Transition_strategy = st.builds(
    lts::Transition,
    output=
        safe_text,
    input=
        safe_text
)
lts::State_strategy = st.builds(
    lts::State,
    name=
        safe_text
)
lts::LTS_strategy = st.builds(
    lts::LTS,
    name=
        safe_text
)

@given(instance=lts::Transition_strategy)
@settings(max_examples=50)
def test_lts::transition_instantiation(instance):
    assert isinstance(instance, lts::Transition)

@given(instance=lts::Transition_strategy)
def test_lts::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=lts::Transition_strategy)
def test_lts::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=lts::Transition_strategy)
def test_lts::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=lts::Transition_strategy)
def test_lts::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=lts::State_strategy)
@settings(max_examples=50)
def test_lts::state_instantiation(instance):
    assert isinstance(instance, lts::State)

@given(instance=lts::State_strategy)
def test_lts::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lts::State_strategy)
def test_lts::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts::LTS_strategy)
@settings(max_examples=50)
def test_lts::lts_instantiation(instance):
    assert isinstance(instance, lts::LTS)

@given(instance=lts::LTS_strategy)
def test_lts::lts_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lts::LTS_strategy)
def test_lts::lts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
