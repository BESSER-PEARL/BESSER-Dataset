import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::Arc,
    Arc,
    petrinet::PTArc,
    petrinet::TPArc,
    NamedElement,
    petrinet::Place,
    petrinet::Transition,
    petrinet::Petrinet,
    petrinet::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::arc_has_weight():
    assert hasattr(petrinet::Arc, "weight")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::ptarc_is_not_abstract():
    assert not inspect.isabstract(petrinet::PTArc)


def test_petrinet::ptarc_constructor_exists():
    assert callable(petrinet::PTArc.__init__)


def test_petrinet::ptarc_constructor_args():
    sig = inspect.signature(petrinet::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::tparc_is_not_abstract():
    assert not inspect.isabstract(petrinet::TPArc)


def test_petrinet::tparc_constructor_exists():
    assert callable(petrinet::TPArc.__init__)


def test_petrinet::tparc_constructor_args():
    sig = inspect.signature(petrinet::TPArc.__init__)
    params = list(sig.parameters.keys())



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



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::Petrinet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::Petrinet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::Petrinet.__init__)
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
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
    weight=
        st.integers()
)
Arc_strategy = st.builds(
    Arc,
)
petrinet::PTArc_strategy = st.builds(
    petrinet::PTArc,
)
petrinet::TPArc_strategy = st.builds(
    petrinet::TPArc,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
petrinet::Petrinet_strategy = st.builds(
    petrinet::Petrinet,
)
petrinet::NamedElement_strategy = st.builds(
    petrinet::NamedElement,
    name=
        safe_text
)

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet::PTArc_strategy)
@settings(max_examples=50)
def test_petrinet::ptarc_instantiation(instance):
    assert isinstance(instance, petrinet::PTArc)

@given(instance=petrinet::TPArc_strategy)
@settings(max_examples=50)
def test_petrinet::tparc_instantiation(instance):
    assert isinstance(instance, petrinet::TPArc)

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

@given(instance=petrinet::Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::Petrinet)

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
