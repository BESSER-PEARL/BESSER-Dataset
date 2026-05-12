import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    egraphs_EHyperEdge,
    egraphs_ENode,
    egraphs_EGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_egraphs_ehyperedge_is_not_abstract():
    assert not inspect.isabstract(egraphs_EHyperEdge)


def test_egraphs_ehyperedge_constructor_exists():
    assert callable(egraphs_EHyperEdge.__init__)


def test_egraphs_ehyperedge_constructor_args():
    sig = inspect.signature(egraphs_EHyperEdge.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_egraphs_ehyperedge_has_label():
    assert hasattr(egraphs_EHyperEdge, "label")
    descriptor = None
    for klass in egraphs_EHyperEdge.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_egraphs_enode_is_not_abstract():
    assert not inspect.isabstract(egraphs_ENode)


def test_egraphs_enode_constructor_exists():
    assert callable(egraphs_ENode.__init__)


def test_egraphs_enode_constructor_args():
    sig = inspect.signature(egraphs_ENode.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"

def test_egraphs_enode_has_element():
    assert hasattr(egraphs_ENode, "element")
    descriptor = None
    for klass in egraphs_ENode.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_egraphs_egraph_is_not_abstract():
    assert not inspect.isabstract(egraphs_EGraph)


def test_egraphs_egraph_constructor_exists():
    assert callable(egraphs_EGraph.__init__)


def test_egraphs_egraph_constructor_args():
    sig = inspect.signature(egraphs_EGraph.__init__)
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
egraphs_EHyperEdge_strategy = st.builds(
    egraphs_EHyperEdge,
    label=
        safe_text
)
egraphs_ENode_strategy = st.builds(
    egraphs_ENode,
    element=
        safe_text
)
egraphs_EGraph_strategy = st.builds(
    egraphs_EGraph,
)

@given(instance=egraphs_EHyperEdge_strategy)
@settings(max_examples=50)
def test_egraphs_ehyperedge_instantiation(instance):
    assert isinstance(instance, egraphs_EHyperEdge)



@given(instance=egraphs_EHyperEdge_strategy)
def test_egraphs_ehyperedge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=egraphs_ENode_strategy)
@settings(max_examples=50)
def test_egraphs_enode_instantiation(instance):
    assert isinstance(instance, egraphs_ENode)



@given(instance=egraphs_ENode_strategy)
def test_egraphs_enode_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=egraphs_EGraph_strategy)
@settings(max_examples=50)
def test_egraphs_egraph_instantiation(instance):
    assert isinstance(instance, egraphs_EGraph)
