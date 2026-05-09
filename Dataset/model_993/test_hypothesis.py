import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GraphElement,
    DirectedGraph::Edge,
    DirectedGraph::Node,
    DirectedGraph::GraphElement,
    DirectedGraph::Graph,
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



def test_directedgraph::edge_is_not_abstract():
    assert not inspect.isabstract(DirectedGraph::Edge)


def test_directedgraph::edge_constructor_exists():
    assert callable(DirectedGraph::Edge.__init__)


def test_directedgraph::edge_constructor_args():
    sig = inspect.signature(DirectedGraph::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_directedgraph::edge_has_weight():
    assert hasattr(DirectedGraph::Edge, "weight")
    descriptor = None
    for klass in DirectedGraph::Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_directedgraph::node_is_not_abstract():
    assert not inspect.isabstract(DirectedGraph::Node)


def test_directedgraph::node_constructor_exists():
    assert callable(DirectedGraph::Node.__init__)


def test_directedgraph::node_constructor_args():
    sig = inspect.signature(DirectedGraph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_directedgraph::node_has_label():
    assert hasattr(DirectedGraph::Node, "label")
    descriptor = None
    for klass in DirectedGraph::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_directedgraph::graphelement_is_not_abstract():
    assert not inspect.isabstract(DirectedGraph::GraphElement)


def test_directedgraph::graphelement_constructor_exists():
    assert callable(DirectedGraph::GraphElement.__init__)


def test_directedgraph::graphelement_constructor_args():
    sig = inspect.signature(DirectedGraph::GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_directedgraph::graph_is_not_abstract():
    assert not inspect.isabstract(DirectedGraph::Graph)


def test_directedgraph::graph_constructor_exists():
    assert callable(DirectedGraph::Graph.__init__)


def test_directedgraph::graph_constructor_args():
    sig = inspect.signature(DirectedGraph::Graph.__init__)
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
DirectedGraph::Edge_strategy = st.builds(
    DirectedGraph::Edge,
    weight=
        st.integers()
)
DirectedGraph::Node_strategy = st.builds(
    DirectedGraph::Node,
    label=
        safe_text
)
DirectedGraph::GraphElement_strategy = st.builds(
    DirectedGraph::GraphElement,
)
DirectedGraph::Graph_strategy = st.builds(
    DirectedGraph::Graph,
)

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=DirectedGraph::Edge_strategy)
@settings(max_examples=50)
def test_directedgraph::edge_instantiation(instance):
    assert isinstance(instance, DirectedGraph::Edge)

@given(instance=DirectedGraph::Edge_strategy)
def test_directedgraph::edge_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=DirectedGraph::Edge_strategy)
def test_directedgraph::edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=DirectedGraph::Node_strategy)
@settings(max_examples=50)
def test_directedgraph::node_instantiation(instance):
    assert isinstance(instance, DirectedGraph::Node)

@given(instance=DirectedGraph::Node_strategy)
def test_directedgraph::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=DirectedGraph::Node_strategy)
def test_directedgraph::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=DirectedGraph::GraphElement_strategy)
@settings(max_examples=50)
def test_directedgraph::graphelement_instantiation(instance):
    assert isinstance(instance, DirectedGraph::GraphElement)

@given(instance=DirectedGraph::Graph_strategy)
@settings(max_examples=50)
def test_directedgraph::graph_instantiation(instance):
    assert isinstance(instance, DirectedGraph::Graph)
