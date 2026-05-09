import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GraphElement,
    digraph::Edge,
    digraph::Node,
    digraph::GraphElement,
    digraph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_digraph::edge_is_not_abstract():
    assert not inspect.isabstract(digraph::Edge)


def test_digraph::edge_constructor_exists():
    assert callable(digraph::Edge.__init__)


def test_digraph::edge_constructor_args():
    sig = inspect.signature(digraph::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_digraph::edge_has_weight():
    assert hasattr(digraph::Edge, "weight")
    descriptor = None
    for klass in digraph::Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_digraph::node_is_not_abstract():
    assert not inspect.isabstract(digraph::Node)


def test_digraph::node_constructor_exists():
    assert callable(digraph::Node.__init__)


def test_digraph::node_constructor_args():
    sig = inspect.signature(digraph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_digraph::node_has_label():
    assert hasattr(digraph::Node, "label")
    descriptor = None
    for klass in digraph::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_digraph::graphelement_is_not_abstract():
    assert not inspect.isabstract(digraph::GraphElement)


def test_digraph::graphelement_constructor_exists():
    assert callable(digraph::GraphElement.__init__)


def test_digraph::graphelement_constructor_args():
    sig = inspect.signature(digraph::GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_digraph::graph_is_not_abstract():
    assert not inspect.isabstract(digraph::Graph)


def test_digraph::graph_constructor_exists():
    assert callable(digraph::Graph.__init__)


def test_digraph::graph_constructor_args():
    sig = inspect.signature(digraph::Graph.__init__)
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
GraphElement_strategy = st.builds(
    GraphElement,
)
digraph::Edge_strategy = st.builds(
    digraph::Edge,
    weight=
        safe_text
)
digraph::Node_strategy = st.builds(
    digraph::Node,
    label=
        safe_text
)
digraph::GraphElement_strategy = st.builds(
    digraph::GraphElement,
)
digraph::Graph_strategy = st.builds(
    digraph::Graph,
)

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=digraph::Edge_strategy)
@settings(max_examples=50)
def test_digraph::edge_instantiation(instance):
    assert isinstance(instance, digraph::Edge)

@given(instance=digraph::Edge_strategy)
def test_digraph::edge_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=digraph::Edge_strategy)
def test_digraph::edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=digraph::Node_strategy)
@settings(max_examples=50)
def test_digraph::node_instantiation(instance):
    assert isinstance(instance, digraph::Node)

@given(instance=digraph::Node_strategy)
def test_digraph::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=digraph::Node_strategy)
def test_digraph::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=digraph::GraphElement_strategy)
@settings(max_examples=50)
def test_digraph::graphelement_instantiation(instance):
    assert isinstance(instance, digraph::GraphElement)

@given(instance=digraph::Graph_strategy)
@settings(max_examples=50)
def test_digraph::graph_instantiation(instance):
    assert isinstance(instance, digraph::Graph)
