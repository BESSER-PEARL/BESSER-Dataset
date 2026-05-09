import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lts::pc::EObject,
    lts::pc::Pointcut,
    lts::pc::Transition,
    lts::pc::State,
    lts::pc::LTS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lts::pc::eobject_is_not_abstract():
    assert not inspect.isabstract(lts::pc::EObject)


def test_lts::pc::eobject_constructor_exists():
    assert callable(lts::pc::EObject.__init__)


def test_lts::pc::eobject_constructor_args():
    sig = inspect.signature(lts::pc::EObject.__init__)
    params = list(sig.parameters.keys())



def test_lts::pc::pointcut_is_not_abstract():
    assert not inspect.isabstract(lts::pc::Pointcut)


def test_lts::pc::pointcut_constructor_exists():
    assert callable(lts::pc::Pointcut.__init__)


def test_lts::pc::pointcut_constructor_args():
    sig = inspect.signature(lts::pc::Pointcut.__init__)
    params = list(sig.parameters.keys())



def test_lts::pc::transition_is_not_abstract():
    assert not inspect.isabstract(lts::pc::Transition)


def test_lts::pc::transition_constructor_exists():
    assert callable(lts::pc::Transition.__init__)


def test_lts::pc::transition_constructor_args():
    sig = inspect.signature(lts::pc::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_lts::pc::transition_has_input():
    assert hasattr(lts::pc::Transition, "input")
    descriptor = None
    for klass in lts::pc::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_lts::pc::transition_has_output():
    assert hasattr(lts::pc::Transition, "output")
    descriptor = None
    for klass in lts::pc::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_lts::pc::state_is_not_abstract():
    assert not inspect.isabstract(lts::pc::State)


def test_lts::pc::state_constructor_exists():
    assert callable(lts::pc::State.__init__)


def test_lts::pc::state_constructor_args():
    sig = inspect.signature(lts::pc::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts::pc::state_has_name():
    assert hasattr(lts::pc::State, "name")
    descriptor = None
    for klass in lts::pc::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts::pc::lts_is_not_abstract():
    assert not inspect.isabstract(lts::pc::LTS)


def test_lts::pc::lts_constructor_exists():
    assert callable(lts::pc::LTS.__init__)


def test_lts::pc::lts_constructor_args():
    sig = inspect.signature(lts::pc::LTS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts::pc::lts_has_name():
    assert hasattr(lts::pc::LTS, "name")
    descriptor = None
    for klass in lts::pc::LTS.__mro__:
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
lts::pc::EObject_strategy = st.builds(
    lts::pc::EObject,
)
lts::pc::Pointcut_strategy = st.builds(
    lts::pc::Pointcut,
)
lts::pc::Transition_strategy = st.builds(
    lts::pc::Transition,
    input=
        safe_text,
    output=
        safe_text
)
lts::pc::State_strategy = st.builds(
    lts::pc::State,
    name=
        safe_text
)
lts::pc::LTS_strategy = st.builds(
    lts::pc::LTS,
    name=
        safe_text
)

@given(instance=lts::pc::EObject_strategy)
@settings(max_examples=50)
def test_lts::pc::eobject_instantiation(instance):
    assert isinstance(instance, lts::pc::EObject)

@given(instance=lts::pc::Pointcut_strategy)
@settings(max_examples=50)
def test_lts::pc::pointcut_instantiation(instance):
    assert isinstance(instance, lts::pc::Pointcut)

@given(instance=lts::pc::Transition_strategy)
@settings(max_examples=50)
def test_lts::pc::transition_instantiation(instance):
    assert isinstance(instance, lts::pc::Transition)

@given(instance=lts::pc::Transition_strategy)
def test_lts::pc::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=lts::pc::Transition_strategy)
def test_lts::pc::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=lts::pc::Transition_strategy)
def test_lts::pc::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=lts::pc::Transition_strategy)
def test_lts::pc::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=lts::pc::State_strategy)
@settings(max_examples=50)
def test_lts::pc::state_instantiation(instance):
    assert isinstance(instance, lts::pc::State)

@given(instance=lts::pc::State_strategy)
def test_lts::pc::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lts::pc::State_strategy)
def test_lts::pc::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts::pc::LTS_strategy)
@settings(max_examples=50)
def test_lts::pc::lts_instantiation(instance):
    assert isinstance(instance, lts::pc::LTS)

@given(instance=lts::pc::LTS_strategy)
def test_lts::pc::lts_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lts::pc::LTS_strategy)
def test_lts::pc::lts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
