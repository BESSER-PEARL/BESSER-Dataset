import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet2::Transition,
    petrinet2::Place,
    petrinet2::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet2::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet2::Transition)


def test_petrinet2::transition_constructor_exists():
    assert callable(petrinet2::Transition.__init__)


def test_petrinet2::transition_constructor_args():
    sig = inspect.signature(petrinet2::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet2::transition_has_name():
    assert hasattr(petrinet2::Transition, "name")
    descriptor = None
    for klass in petrinet2::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet2::place_is_not_abstract():
    assert not inspect.isabstract(petrinet2::Place)


def test_petrinet2::place_constructor_exists():
    assert callable(petrinet2::Place.__init__)


def test_petrinet2::place_constructor_args():
    sig = inspect.signature(petrinet2::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet2::place_has_name():
    assert hasattr(petrinet2::Place, "name")
    descriptor = None
    for klass in petrinet2::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet2::net_is_not_abstract():
    assert not inspect.isabstract(petrinet2::Net)


def test_petrinet2::net_constructor_exists():
    assert callable(petrinet2::Net.__init__)


def test_petrinet2::net_constructor_args():
    sig = inspect.signature(petrinet2::Net.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet2::net_has_name():
    assert hasattr(petrinet2::Net, "name")
    descriptor = None
    for klass in petrinet2::Net.__mro__:
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
petrinet2::Transition_strategy = st.builds(
    petrinet2::Transition,
    name=
        safe_text
)
petrinet2::Place_strategy = st.builds(
    petrinet2::Place,
    name=
        safe_text
)
petrinet2::Net_strategy = st.builds(
    petrinet2::Net,
    name=
        safe_text
)

@given(instance=petrinet2::Transition_strategy)
@settings(max_examples=50)
def test_petrinet2::transition_instantiation(instance):
    assert isinstance(instance, petrinet2::Transition)

@given(instance=petrinet2::Transition_strategy)
def test_petrinet2::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet2::Transition_strategy)
def test_petrinet2::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet2::Place_strategy)
@settings(max_examples=50)
def test_petrinet2::place_instantiation(instance):
    assert isinstance(instance, petrinet2::Place)

@given(instance=petrinet2::Place_strategy)
def test_petrinet2::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet2::Place_strategy)
def test_petrinet2::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet2::Net_strategy)
@settings(max_examples=50)
def test_petrinet2::net_instantiation(instance):
    assert isinstance(instance, petrinet2::Net)

@given(instance=petrinet2::Net_strategy)
def test_petrinet2::net_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet2::Net_strategy)
def test_petrinet2::net_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
