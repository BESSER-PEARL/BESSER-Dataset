import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NetElement,
    Edge,
    pnw_TPEdge,
    pnw_PTEdge,
    pnw_Edge,
    pnw_NetElement,
    NamedElement,
    pnw_Place,
    pnw_Transition,
    pnw_Net,
    pnw_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_pnw_tpedge_is_not_abstract():
    assert not inspect.isabstract(pnw_TPEdge)


def test_pnw_tpedge_constructor_exists():
    assert callable(pnw_TPEdge.__init__)


def test_pnw_tpedge_constructor_args():
    sig = inspect.signature(pnw_TPEdge.__init__)
    params = list(sig.parameters.keys())



def test_pnw_ptedge_is_not_abstract():
    assert not inspect.isabstract(pnw_PTEdge)


def test_pnw_ptedge_constructor_exists():
    assert callable(pnw_PTEdge.__init__)


def test_pnw_ptedge_constructor_args():
    sig = inspect.signature(pnw_PTEdge.__init__)
    params = list(sig.parameters.keys())



def test_pnw_edge_is_not_abstract():
    assert not inspect.isabstract(pnw_Edge)


def test_pnw_edge_constructor_exists():
    assert callable(pnw_Edge.__init__)


def test_pnw_edge_constructor_args():
    sig = inspect.signature(pnw_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_pnw_edge_has_weight():
    assert hasattr(pnw_Edge, "weight")
    descriptor = None
    for klass in pnw_Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_pnw_netelement_is_not_abstract():
    assert not inspect.isabstract(pnw_NetElement)


def test_pnw_netelement_constructor_exists():
    assert callable(pnw_NetElement.__init__)


def test_pnw_netelement_constructor_args():
    sig = inspect.signature(pnw_NetElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_pnw_place_is_not_abstract():
    assert not inspect.isabstract(pnw_Place)


def test_pnw_place_constructor_exists():
    assert callable(pnw_Place.__init__)


def test_pnw_place_constructor_args():
    sig = inspect.signature(pnw_Place.__init__)
    params = list(sig.parameters.keys())
    assert "noOfTokens" in params, "Missing parameter 'noOfTokens'"

def test_pnw_place_has_noOfTokens():
    assert hasattr(pnw_Place, "noOfTokens")
    descriptor = None
    for klass in pnw_Place.__mro__:
        if "noOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["noOfTokens"]
            break
    assert isinstance(descriptor, property)



def test_pnw_transition_is_not_abstract():
    assert not inspect.isabstract(pnw_Transition)


def test_pnw_transition_constructor_exists():
    assert callable(pnw_Transition.__init__)


def test_pnw_transition_constructor_args():
    sig = inspect.signature(pnw_Transition.__init__)
    params = list(sig.parameters.keys())



def test_pnw_net_is_not_abstract():
    assert not inspect.isabstract(pnw_Net)


def test_pnw_net_constructor_exists():
    assert callable(pnw_Net.__init__)


def test_pnw_net_constructor_args():
    sig = inspect.signature(pnw_Net.__init__)
    params = list(sig.parameters.keys())
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"

def test_pnw_net_has_incrementalID():
    assert hasattr(pnw_Net, "incrementalID")
    descriptor = None
    for klass in pnw_Net.__mro__:
        if "incrementalID" in klass.__dict__:
            descriptor = klass.__dict__["incrementalID"]
            break
    assert isinstance(descriptor, property)



def test_pnw_namedelement_is_not_abstract():
    assert not inspect.isabstract(pnw_NamedElement)


def test_pnw_namedelement_constructor_exists():
    assert callable(pnw_NamedElement.__init__)


def test_pnw_namedelement_constructor_args():
    sig = inspect.signature(pnw_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pnw_namedelement_has_name():
    assert hasattr(pnw_NamedElement, "name")
    descriptor = None
    for klass in pnw_NamedElement.__mro__:
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
NetElement_strategy = st.builds(
    NetElement,
)
Edge_strategy = st.builds(
    Edge,
)
pnw_TPEdge_strategy = st.builds(
    pnw_TPEdge,
)
pnw_PTEdge_strategy = st.builds(
    pnw_PTEdge,
)
pnw_Edge_strategy = st.builds(
    pnw_Edge,
    weight=
        st.integers()
)
pnw_NetElement_strategy = st.builds(
    pnw_NetElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
pnw_Place_strategy = st.builds(
    pnw_Place,
    noOfTokens=
        st.integers()
)
pnw_Transition_strategy = st.builds(
    pnw_Transition,
)
pnw_Net_strategy = st.builds(
    pnw_Net,
    incrementalID=
        safe_text
)
pnw_NamedElement_strategy = st.builds(
    pnw_NamedElement,
    name=
        safe_text
)

@given(instance=NetElement_strategy)
@settings(max_examples=50)
def test_netelement_instantiation(instance):
    assert isinstance(instance, NetElement)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=pnw_TPEdge_strategy)
@settings(max_examples=50)
def test_pnw_tpedge_instantiation(instance):
    assert isinstance(instance, pnw_TPEdge)

@given(instance=pnw_PTEdge_strategy)
@settings(max_examples=50)
def test_pnw_ptedge_instantiation(instance):
    assert isinstance(instance, pnw_PTEdge)

@given(instance=pnw_Edge_strategy)
@settings(max_examples=50)
def test_pnw_edge_instantiation(instance):
    assert isinstance(instance, pnw_Edge)



@given(instance=pnw_Edge_strategy)
def test_pnw_edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=pnw_NetElement_strategy)
@settings(max_examples=50)
def test_pnw_netelement_instantiation(instance):
    assert isinstance(instance, pnw_NetElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=pnw_Place_strategy)
@settings(max_examples=50)
def test_pnw_place_instantiation(instance):
    assert isinstance(instance, pnw_Place)



@given(instance=pnw_Place_strategy)
def test_pnw_place_noOfTokens_setter(instance):
    original = instance.noOfTokens
    instance.noOfTokens = original
    assert instance.noOfTokens == original

@given(instance=pnw_Transition_strategy)
@settings(max_examples=50)
def test_pnw_transition_instantiation(instance):
    assert isinstance(instance, pnw_Transition)

@given(instance=pnw_Net_strategy)
@settings(max_examples=50)
def test_pnw_net_instantiation(instance):
    assert isinstance(instance, pnw_Net)



@given(instance=pnw_Net_strategy)
def test_pnw_net_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original

@given(instance=pnw_NamedElement_strategy)
@settings(max_examples=50)
def test_pnw_namedelement_instantiation(instance):
    assert isinstance(instance, pnw_NamedElement)



@given(instance=pnw_NamedElement_strategy)
def test_pnw_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
