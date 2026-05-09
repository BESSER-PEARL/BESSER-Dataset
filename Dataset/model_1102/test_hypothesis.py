import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    petrinet::Place,
    petrinet::Transition,
    petrinet::Net,
    petrinet::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::net_is_not_abstract():
    assert not inspect.isabstract(petrinet::Net)


def test_petrinet::net_constructor_exists():
    assert callable(petrinet::Net.__init__)


def test_petrinet::net_constructor_args():
    sig = inspect.signature(petrinet::Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::namedelement_is_not_abstract():
    assert not inspect.isabstract(petrinet::NamedElement)


def test_petrinet::namedelement_constructor_exists():
    assert callable(petrinet::NamedElement.__init__)


def test_petrinet::namedelement_constructor_args():
    sig = inspect.signature(petrinet::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::namedelement_has_name():
    assert hasattr(petrinet::NamedElement, "name")
    descriptor = None
    for klass in petrinet::NamedElement.__mro__:
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
NamedElement_strategy = st.builds(
    NamedElement,
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
petrinet::Net_strategy = st.builds(
    petrinet::Net,
)
petrinet::NamedElement_strategy = st.builds(
    petrinet::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Net_strategy)
@settings(max_examples=50)
def test_petrinet::net_instantiation(instance):
    assert isinstance(instance, petrinet::Net)

@given(instance=petrinet::NamedElement_strategy)
@settings(max_examples=50)
def test_petrinet::namedelement_instantiation(instance):
    assert isinstance(instance, petrinet::NamedElement)

@given(instance=petrinet::NamedElement_strategy)
def test_petrinet::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::NamedElement_strategy)
def test_petrinet::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
