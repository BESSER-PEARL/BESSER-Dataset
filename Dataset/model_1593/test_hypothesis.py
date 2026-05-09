import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::Place,
    petrinet::Net,
    petrinet::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"

def test_petrinet::place_has_name():
    assert hasattr(petrinet::Place, "name")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::place_has_initialTokens():
    assert hasattr(petrinet::Place, "initialTokens")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::net_is_not_abstract():
    assert not inspect.isabstract(petrinet::Net)


def test_petrinet::net_constructor_exists():
    assert callable(petrinet::Net.__init__)


def test_petrinet::net_constructor_args():
    sig = inspect.signature(petrinet::Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::transition_has_name():
    assert hasattr(petrinet::Transition, "name")
    descriptor = None
    for klass in petrinet::Transition.__mro__:
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
petrinet::Place_strategy = st.builds(
    petrinet::Place,
    name=
        safe_text,
    initialTokens=
        st.integers()
)
petrinet::Net_strategy = st.builds(
    petrinet::Net,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
    name=
        safe_text
)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_initialTokens_type(instance):
    assert isinstance(instance.initialTokens, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=petrinet::Net_strategy)
@settings(max_examples=50)
def test_petrinet::net_instantiation(instance):
    assert isinstance(instance, petrinet::Net)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
