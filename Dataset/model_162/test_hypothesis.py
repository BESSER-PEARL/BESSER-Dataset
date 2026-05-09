import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::Place,
    petrinet::Net,
    petrinet::Box,
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
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::place_has_id():
    assert hasattr(petrinet::Place, "id")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::place_has_name():
    assert hasattr(petrinet::Place, "name")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::net_is_not_abstract():
    assert not inspect.isabstract(petrinet::Net)


def test_petrinet::net_constructor_exists():
    assert callable(petrinet::Net.__init__)


def test_petrinet::net_constructor_args():
    sig = inspect.signature(petrinet::Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::box_is_not_abstract():
    assert not inspect.isabstract(petrinet::Box)


def test_petrinet::box_constructor_exists():
    assert callable(petrinet::Box.__init__)


def test_petrinet::box_constructor_args():
    sig = inspect.signature(petrinet::Box.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::box_has_id():
    assert hasattr(petrinet::Box, "id")
    descriptor = None
    for klass in petrinet::Box.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::box_has_name():
    assert hasattr(petrinet::Box, "name")
    descriptor = None
    for klass in petrinet::Box.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::transition_has_id():
    assert hasattr(petrinet::Transition, "id")
    descriptor = None
    for klass in petrinet::Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

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
    id=
        st.integers(),
    name=
        safe_text
)
petrinet::Net_strategy = st.builds(
    petrinet::Net,
)
petrinet::Box_strategy = st.builds(
    petrinet::Box,
    id=
        st.integers(),
    name=
        safe_text
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
    id=
        st.integers(),
    name=
        safe_text
)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::Net_strategy)
@settings(max_examples=50)
def test_petrinet::net_instantiation(instance):
    assert isinstance(instance, petrinet::Net)

@given(instance=petrinet::Box_strategy)
@settings(max_examples=50)
def test_petrinet::box_instantiation(instance):
    assert isinstance(instance, petrinet::Box)

@given(instance=petrinet::Box_strategy)
def test_petrinet::box_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=petrinet::Box_strategy)
def test_petrinet::box_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=petrinet::Box_strategy)
def test_petrinet::box_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Box_strategy)
def test_petrinet::box_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
