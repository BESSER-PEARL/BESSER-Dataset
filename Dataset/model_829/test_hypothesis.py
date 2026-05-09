import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lts::av::PerJoinPointScope,
    lts::av::GlobalScope,
    lts::av::EObject,
    lts::av::Advice,
    lts::av::State,
    lts::av::LTS,
    lts::av::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lts::av::perjoinpointscope_is_not_abstract():
    assert not inspect.isabstract(lts::av::PerJoinPointScope)


def test_lts::av::perjoinpointscope_constructor_exists():
    assert callable(lts::av::PerJoinPointScope.__init__)


def test_lts::av::perjoinpointscope_constructor_args():
    sig = inspect.signature(lts::av::PerJoinPointScope.__init__)
    params = list(sig.parameters.keys())



def test_lts::av::globalscope_is_not_abstract():
    assert not inspect.isabstract(lts::av::GlobalScope)


def test_lts::av::globalscope_constructor_exists():
    assert callable(lts::av::GlobalScope.__init__)


def test_lts::av::globalscope_constructor_args():
    sig = inspect.signature(lts::av::GlobalScope.__init__)
    params = list(sig.parameters.keys())



def test_lts::av::eobject_is_not_abstract():
    assert not inspect.isabstract(lts::av::EObject)


def test_lts::av::eobject_constructor_exists():
    assert callable(lts::av::EObject.__init__)


def test_lts::av::eobject_constructor_args():
    sig = inspect.signature(lts::av::EObject.__init__)
    params = list(sig.parameters.keys())



def test_lts::av::advice_is_not_abstract():
    assert not inspect.isabstract(lts::av::Advice)


def test_lts::av::advice_constructor_exists():
    assert callable(lts::av::Advice.__init__)


def test_lts::av::advice_constructor_args():
    sig = inspect.signature(lts::av::Advice.__init__)
    params = list(sig.parameters.keys())



def test_lts::av::state_is_not_abstract():
    assert not inspect.isabstract(lts::av::State)


def test_lts::av::state_constructor_exists():
    assert callable(lts::av::State.__init__)


def test_lts::av::state_constructor_args():
    sig = inspect.signature(lts::av::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts::av::state_has_name():
    assert hasattr(lts::av::State, "name")
    descriptor = None
    for klass in lts::av::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts::av::lts_is_not_abstract():
    assert not inspect.isabstract(lts::av::LTS)


def test_lts::av::lts_constructor_exists():
    assert callable(lts::av::LTS.__init__)


def test_lts::av::lts_constructor_args():
    sig = inspect.signature(lts::av::LTS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts::av::lts_has_name():
    assert hasattr(lts::av::LTS, "name")
    descriptor = None
    for klass in lts::av::LTS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts::av::transition_is_not_abstract():
    assert not inspect.isabstract(lts::av::Transition)


def test_lts::av::transition_constructor_exists():
    assert callable(lts::av::Transition.__init__)


def test_lts::av::transition_constructor_args():
    sig = inspect.signature(lts::av::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_lts::av::transition_has_input():
    assert hasattr(lts::av::Transition, "input")
    descriptor = None
    for klass in lts::av::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_lts::av::transition_has_output():
    assert hasattr(lts::av::Transition, "output")
    descriptor = None
    for klass in lts::av::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
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
lts::av::PerJoinPointScope_strategy = st.builds(
    lts::av::PerJoinPointScope,
)
lts::av::GlobalScope_strategy = st.builds(
    lts::av::GlobalScope,
)
lts::av::EObject_strategy = st.builds(
    lts::av::EObject,
)
lts::av::Advice_strategy = st.builds(
    lts::av::Advice,
)
lts::av::State_strategy = st.builds(
    lts::av::State,
    name=
        safe_text
)
lts::av::LTS_strategy = st.builds(
    lts::av::LTS,
    name=
        safe_text
)
lts::av::Transition_strategy = st.builds(
    lts::av::Transition,
    input=
        safe_text,
    output=
        safe_text
)

@given(instance=lts::av::PerJoinPointScope_strategy)
@settings(max_examples=50)
def test_lts::av::perjoinpointscope_instantiation(instance):
    assert isinstance(instance, lts::av::PerJoinPointScope)

@given(instance=lts::av::GlobalScope_strategy)
@settings(max_examples=50)
def test_lts::av::globalscope_instantiation(instance):
    assert isinstance(instance, lts::av::GlobalScope)

@given(instance=lts::av::EObject_strategy)
@settings(max_examples=50)
def test_lts::av::eobject_instantiation(instance):
    assert isinstance(instance, lts::av::EObject)

@given(instance=lts::av::Advice_strategy)
@settings(max_examples=50)
def test_lts::av::advice_instantiation(instance):
    assert isinstance(instance, lts::av::Advice)

@given(instance=lts::av::State_strategy)
@settings(max_examples=50)
def test_lts::av::state_instantiation(instance):
    assert isinstance(instance, lts::av::State)

@given(instance=lts::av::State_strategy)
def test_lts::av::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lts::av::State_strategy)
def test_lts::av::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts::av::LTS_strategy)
@settings(max_examples=50)
def test_lts::av::lts_instantiation(instance):
    assert isinstance(instance, lts::av::LTS)

@given(instance=lts::av::LTS_strategy)
def test_lts::av::lts_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lts::av::LTS_strategy)
def test_lts::av::lts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts::av::Transition_strategy)
@settings(max_examples=50)
def test_lts::av::transition_instantiation(instance):
    assert isinstance(instance, lts::av::Transition)

@given(instance=lts::av::Transition_strategy)
def test_lts::av::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=lts::av::Transition_strategy)
def test_lts::av::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=lts::av::Transition_strategy)
def test_lts::av::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=lts::av::Transition_strategy)
def test_lts::av::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original
