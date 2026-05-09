import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::NamedElement,
    Edge,
    petrinet::OutputEdge,
    petrinet::ReadEdge,
    petrinet::InhibitorEdge,
    petrinet::InputEdge,
    NamedElement,
    petrinet::PetriNet,
    petrinet::Edge,
    petrinet::Transition,
    petrinet::Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::outputedge_is_not_abstract():
    assert not inspect.isabstract(petrinet::OutputEdge)


def test_petrinet::outputedge_constructor_exists():
    assert callable(petrinet::OutputEdge.__init__)


def test_petrinet::outputedge_constructor_args():
    sig = inspect.signature(petrinet::OutputEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::readedge_is_not_abstract():
    assert not inspect.isabstract(petrinet::ReadEdge)


def test_petrinet::readedge_constructor_exists():
    assert callable(petrinet::ReadEdge.__init__)


def test_petrinet::readedge_constructor_args():
    sig = inspect.signature(petrinet::ReadEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::inhibitoredge_is_not_abstract():
    assert not inspect.isabstract(petrinet::InhibitorEdge)


def test_petrinet::inhibitoredge_constructor_exists():
    assert callable(petrinet::InhibitorEdge.__init__)


def test_petrinet::inhibitoredge_constructor_args():
    sig = inspect.signature(petrinet::InhibitorEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::inputedge_is_not_abstract():
    assert not inspect.isabstract(petrinet::InputEdge)


def test_petrinet::inputedge_constructor_exists():
    assert callable(petrinet::InputEdge.__init__)


def test_petrinet::inputedge_constructor_args():
    sig = inspect.signature(petrinet::InputEdge.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::edge_is_not_abstract():
    assert not inspect.isabstract(petrinet::Edge)


def test_petrinet::edge_constructor_exists():
    assert callable(petrinet::Edge.__init__)


def test_petrinet::edge_constructor_args():
    sig = inspect.signature(petrinet::Edge.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petrinet::place_has_tokens():
    assert hasattr(petrinet::Place, "tokens")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
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
petrinet::NamedElement_strategy = st.builds(
    petrinet::NamedElement,
    name=
        safe_text
)
Edge_strategy = st.builds(
    Edge,
)
petrinet::OutputEdge_strategy = st.builds(
    petrinet::OutputEdge,
)
petrinet::ReadEdge_strategy = st.builds(
    petrinet::ReadEdge,
)
petrinet::InhibitorEdge_strategy = st.builds(
    petrinet::InhibitorEdge,
)
petrinet::InputEdge_strategy = st.builds(
    petrinet::InputEdge,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
petrinet::PetriNet_strategy = st.builds(
    petrinet::PetriNet,
)
petrinet::Edge_strategy = st.builds(
    petrinet::Edge,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
    tokens=
        st.integers()
)

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

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=petrinet::OutputEdge_strategy)
@settings(max_examples=50)
def test_petrinet::outputedge_instantiation(instance):
    assert isinstance(instance, petrinet::OutputEdge)

@given(instance=petrinet::ReadEdge_strategy)
@settings(max_examples=50)
def test_petrinet::readedge_instantiation(instance):
    assert isinstance(instance, petrinet::ReadEdge)

@given(instance=petrinet::InhibitorEdge_strategy)
@settings(max_examples=50)
def test_petrinet::inhibitoredge_instantiation(instance):
    assert isinstance(instance, petrinet::InhibitorEdge)

@given(instance=petrinet::InputEdge_strategy)
@settings(max_examples=50)
def test_petrinet::inputedge_instantiation(instance):
    assert isinstance(instance, petrinet::InputEdge)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=petrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::PetriNet)

@given(instance=petrinet::Edge_strategy)
@settings(max_examples=50)
def test_petrinet::edge_instantiation(instance):
    assert isinstance(instance, petrinet::Edge)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original
