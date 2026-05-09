import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::PetriNet,
    petrinet::Arc,
    petrinet::Transition,
    petrinet::Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinet_has_name():
    assert hasattr(petrinet::PetriNet, "name")
    descriptor = None
    for klass in petrinet::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "toPlace" in params, "Missing parameter 'toPlace'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::arc_has_toPlace():
    assert hasattr(petrinet::Arc, "toPlace")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "toPlace" in klass.__dict__:
            descriptor = klass.__dict__["toPlace"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_weight():
    assert hasattr(petrinet::Arc, "weight")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



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



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "token" in params, "Missing parameter 'token'"

def test_petrinet::place_has_name():
    assert hasattr(petrinet::Place, "name")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::place_has_token():
    assert hasattr(petrinet::Place, "token")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
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
petrinet::PetriNet_strategy = st.builds(
    petrinet::PetriNet,
    name=
        safe_text
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
    toPlace=
        st.booleans(),
    weight=
        st.integers()
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
    name=
        safe_text
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
    name=
        safe_text,
    token=
        st.integers()
)

@given(instance=petrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::PetriNet)

@given(instance=petrinet::PetriNet_strategy)
def test_petrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::PetriNet_strategy)
def test_petrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_toPlace_type(instance):
    assert isinstance(instance.toPlace, bool)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_toPlace_setter(instance):
    original = instance.toPlace
    instance.toPlace = original
    assert instance.toPlace == original

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

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
def test_petrinet::place_token_type(instance):
    assert isinstance(instance.token, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original
