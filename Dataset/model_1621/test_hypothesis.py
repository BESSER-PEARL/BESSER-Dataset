import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pnw::NamedElement,
    NetElement,
    Edge,
    pnw::TPEdge,
    pnw::PTEdge,
    pnw::Edge,
    pnw::NetElement,
    NamedElement,
    pnw::Transition,
    pnw::Place,
    pnw::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pnw::namedelement_is_not_abstract():
    assert not inspect.isabstract(pnw::NamedElement)


def test_pnw::namedelement_constructor_exists():
    assert callable(pnw::NamedElement.__init__)


def test_pnw::namedelement_constructor_args():
    sig = inspect.signature(pnw::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pnw::namedelement_has_name():
    assert hasattr(pnw::NamedElement, "name")
    descriptor = None
    for klass in pnw::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_netelement_is_not_abstract():
    assert not inspect.isabstract(NetElement)


def test_netelement_constructor_exists():
    assert callable(NetElement.__init__)


def test_netelement_constructor_args():
    sig = inspect.signature(NetElement.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_pnw::tpedge_is_not_abstract():
    assert not inspect.isabstract(pnw::TPEdge)


def test_pnw::tpedge_constructor_exists():
    assert callable(pnw::TPEdge.__init__)


def test_pnw::tpedge_constructor_args():
    sig = inspect.signature(pnw::TPEdge.__init__)
    params = list(sig.parameters.keys())



def test_pnw::ptedge_is_not_abstract():
    assert not inspect.isabstract(pnw::PTEdge)


def test_pnw::ptedge_constructor_exists():
    assert callable(pnw::PTEdge.__init__)


def test_pnw::ptedge_constructor_args():
    sig = inspect.signature(pnw::PTEdge.__init__)
    params = list(sig.parameters.keys())



def test_pnw::edge_is_not_abstract():
    assert not inspect.isabstract(pnw::Edge)


def test_pnw::edge_constructor_exists():
    assert callable(pnw::Edge.__init__)


def test_pnw::edge_constructor_args():
    sig = inspect.signature(pnw::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_pnw::edge_has_weight():
    assert hasattr(pnw::Edge, "weight")
    descriptor = None
    for klass in pnw::Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_pnw::netelement_is_not_abstract():
    assert not inspect.isabstract(pnw::NetElement)


def test_pnw::netelement_constructor_exists():
    assert callable(pnw::NetElement.__init__)


def test_pnw::netelement_constructor_args():
    sig = inspect.signature(pnw::NetElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_pnw::transition_is_not_abstract():
    assert not inspect.isabstract(pnw::Transition)


def test_pnw::transition_constructor_exists():
    assert callable(pnw::Transition.__init__)


def test_pnw::transition_constructor_args():
    sig = inspect.signature(pnw::Transition.__init__)
    params = list(sig.parameters.keys())



def test_pnw::place_is_not_abstract():
    assert not inspect.isabstract(pnw::Place)


def test_pnw::place_constructor_exists():
    assert callable(pnw::Place.__init__)


def test_pnw::place_constructor_args():
    sig = inspect.signature(pnw::Place.__init__)
    params = list(sig.parameters.keys())
    assert "noOfTokens" in params, "Missing parameter 'noOfTokens'"

def test_pnw::place_has_noOfTokens():
    assert hasattr(pnw::Place, "noOfTokens")
    descriptor = None
    for klass in pnw::Place.__mro__:
        if "noOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["noOfTokens"]
            break
    assert isinstance(descriptor, property)



def test_pnw::net_is_not_abstract():
    assert not inspect.isabstract(pnw::Net)


def test_pnw::net_constructor_exists():
    assert callable(pnw::Net.__init__)


def test_pnw::net_constructor_args():
    sig = inspect.signature(pnw::Net.__init__)
    params = list(sig.parameters.keys())
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"

def test_pnw::net_has_incrementalID():
    assert hasattr(pnw::Net, "incrementalID")
    descriptor = None
    for klass in pnw::Net.__mro__:
        if "incrementalID" in klass.__dict__:
            descriptor = klass.__dict__["incrementalID"]
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
pnw::NamedElement_strategy = st.builds(
    pnw::NamedElement,
    name=
        safe_text
)
NetElement_strategy = st.builds(
    NetElement,
)
Edge_strategy = st.builds(
    Edge,
)
pnw::TPEdge_strategy = st.builds(
    pnw::TPEdge,
)
pnw::PTEdge_strategy = st.builds(
    pnw::PTEdge,
)
pnw::Edge_strategy = st.builds(
    pnw::Edge,
    weight=
        st.integers()
)
pnw::NetElement_strategy = st.builds(
    pnw::NetElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
pnw::Transition_strategy = st.builds(
    pnw::Transition,
)
pnw::Place_strategy = st.builds(
    pnw::Place,
    noOfTokens=
        st.integers()
)
pnw::Net_strategy = st.builds(
    pnw::Net,
    incrementalID=
        safe_text
)

@given(instance=pnw::NamedElement_strategy)
@settings(max_examples=50)
def test_pnw::namedelement_instantiation(instance):
    assert isinstance(instance, pnw::NamedElement)

@given(instance=pnw::NamedElement_strategy)
def test_pnw::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pnw::NamedElement_strategy)
def test_pnw::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NetElement_strategy)
@settings(max_examples=50)
def test_netelement_instantiation(instance):
    assert isinstance(instance, NetElement)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=pnw::TPEdge_strategy)
@settings(max_examples=50)
def test_pnw::tpedge_instantiation(instance):
    assert isinstance(instance, pnw::TPEdge)

@given(instance=pnw::PTEdge_strategy)
@settings(max_examples=50)
def test_pnw::ptedge_instantiation(instance):
    assert isinstance(instance, pnw::PTEdge)

@given(instance=pnw::Edge_strategy)
@settings(max_examples=50)
def test_pnw::edge_instantiation(instance):
    assert isinstance(instance, pnw::Edge)

@given(instance=pnw::Edge_strategy)
def test_pnw::edge_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=pnw::Edge_strategy)
def test_pnw::edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=pnw::NetElement_strategy)
@settings(max_examples=50)
def test_pnw::netelement_instantiation(instance):
    assert isinstance(instance, pnw::NetElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=pnw::Transition_strategy)
@settings(max_examples=50)
def test_pnw::transition_instantiation(instance):
    assert isinstance(instance, pnw::Transition)

@given(instance=pnw::Place_strategy)
@settings(max_examples=50)
def test_pnw::place_instantiation(instance):
    assert isinstance(instance, pnw::Place)

@given(instance=pnw::Place_strategy)
def test_pnw::place_noOfTokens_type(instance):
    assert isinstance(instance.noOfTokens, int)


@given(instance=pnw::Place_strategy)
def test_pnw::place_noOfTokens_setter(instance):
    original = instance.noOfTokens
    instance.noOfTokens = original
    assert instance.noOfTokens == original

@given(instance=pnw::Net_strategy)
@settings(max_examples=50)
def test_pnw::net_instantiation(instance):
    assert isinstance(instance, pnw::Net)

@given(instance=pnw::Net_strategy)
def test_pnw::net_incrementalID_type(instance):
    assert isinstance(instance.incrementalID, str)


@given(instance=pnw::Net_strategy)
def test_pnw::net_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original
