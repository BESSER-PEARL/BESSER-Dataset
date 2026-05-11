import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    egraphs::EHyperEdge,
    egraphs::ENode,
    egraphs::EGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_egraphs::ehyperedge_is_not_abstract():
    assert not inspect.isabstract(egraphs::EHyperEdge)


def test_egraphs::ehyperedge_constructor_exists():
    assert callable(egraphs::EHyperEdge.__init__)


def test_egraphs::ehyperedge_constructor_args():
    sig = inspect.signature(egraphs::EHyperEdge.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_egraphs::ehyperedge_has_label():
    assert hasattr(egraphs::EHyperEdge, "label")
    descriptor = None
    for klass in egraphs::EHyperEdge.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_egraphs::enode_is_not_abstract():
    assert not inspect.isabstract(egraphs::ENode)


def test_egraphs::enode_constructor_exists():
    assert callable(egraphs::ENode.__init__)


def test_egraphs::enode_constructor_args():
    sig = inspect.signature(egraphs::ENode.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"

def test_egraphs::enode_has_element():
    assert hasattr(egraphs::ENode, "element")
    descriptor = None
    for klass in egraphs::ENode.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_egraphs::egraph_is_not_abstract():
    assert not inspect.isabstract(egraphs::EGraph)


def test_egraphs::egraph_constructor_exists():
    assert callable(egraphs::EGraph.__init__)


def test_egraphs::egraph_constructor_args():
    sig = inspect.signature(egraphs::EGraph.__init__)
    params = list(sig.parameters.keys())


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
egraphs::EHyperEdge_strategy = st.builds(
    egraphs::EHyperEdge,
    label=
        safe_text
)
egraphs::ENode_strategy = st.builds(
    egraphs::ENode,
    element=
        safe_text
)
egraphs::EGraph_strategy = st.builds(
    egraphs::EGraph,
)

@given(instance=egraphs::EHyperEdge_strategy)
@settings(max_examples=50)
def test_egraphs::ehyperedge_instantiation(instance):
    assert isinstance(instance, egraphs::EHyperEdge)

@given(instance=egraphs::EHyperEdge_strategy)
def test_egraphs::ehyperedge_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=egraphs::EHyperEdge_strategy)
def test_egraphs::ehyperedge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=egraphs::ENode_strategy)
@settings(max_examples=50)
def test_egraphs::enode_instantiation(instance):
    assert isinstance(instance, egraphs::ENode)

@given(instance=egraphs::ENode_strategy)
def test_egraphs::enode_element_type(instance):
    assert isinstance(instance.element, str)


@given(instance=egraphs::ENode_strategy)
def test_egraphs::enode_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=egraphs::EGraph_strategy)
@settings(max_examples=50)
def test_egraphs::egraph_instantiation(instance):
    assert isinstance(instance, egraphs::EGraph)
