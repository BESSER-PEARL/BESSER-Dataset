import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GraphElement,
    DirectedGraph_Edge,
    DirectedGraph_Node,
    DirectedGraph_GraphElement,
    DirectedGraph_Graph,
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



def test_directedgraph_edge_is_not_abstract():
    assert not inspect.isabstract(DirectedGraph_Edge)


def test_directedgraph_edge_constructor_exists():
    assert callable(DirectedGraph_Edge.__init__)


def test_directedgraph_edge_constructor_args():
    sig = inspect.signature(DirectedGraph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_directedgraph_edge_has_weight():
    assert hasattr(DirectedGraph_Edge, "weight")
    descriptor = None
    for klass in DirectedGraph_Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_directedgraph_node_is_not_abstract():
    assert not inspect.isabstract(DirectedGraph_Node)


def test_directedgraph_node_constructor_exists():
    assert callable(DirectedGraph_Node.__init__)


def test_directedgraph_node_constructor_args():
    sig = inspect.signature(DirectedGraph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_directedgraph_node_has_label():
    assert hasattr(DirectedGraph_Node, "label")
    descriptor = None
    for klass in DirectedGraph_Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_directedgraph_graphelement_is_not_abstract():
    assert not inspect.isabstract(DirectedGraph_GraphElement)


def test_directedgraph_graphelement_constructor_exists():
    assert callable(DirectedGraph_GraphElement.__init__)


def test_directedgraph_graphelement_constructor_args():
    sig = inspect.signature(DirectedGraph_GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_directedgraph_graph_is_not_abstract():
    assert not inspect.isabstract(DirectedGraph_Graph)


def test_directedgraph_graph_constructor_exists():
    assert callable(DirectedGraph_Graph.__init__)


def test_directedgraph_graph_constructor_args():
    sig = inspect.signature(DirectedGraph_Graph.__init__)
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
DirectedGraph_Edge_strategy = st.builds(
    DirectedGraph_Edge,
    weight=
        st.integers()
)
DirectedGraph_Node_strategy = st.builds(
    DirectedGraph_Node,
    label=
        safe_text
)
DirectedGraph_GraphElement_strategy = st.builds(
    DirectedGraph_GraphElement,
)
DirectedGraph_Graph_strategy = st.builds(
    DirectedGraph_Graph,
)

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=DirectedGraph_Edge_strategy)
@settings(max_examples=50)
def test_directedgraph_edge_instantiation(instance):
    assert isinstance(instance, DirectedGraph_Edge)



@given(instance=DirectedGraph_Edge_strategy)
def test_directedgraph_edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=DirectedGraph_Node_strategy)
@settings(max_examples=50)
def test_directedgraph_node_instantiation(instance):
    assert isinstance(instance, DirectedGraph_Node)



@given(instance=DirectedGraph_Node_strategy)
def test_directedgraph_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=DirectedGraph_GraphElement_strategy)
@settings(max_examples=50)
def test_directedgraph_graphelement_instantiation(instance):
    assert isinstance(instance, DirectedGraph_GraphElement)

@given(instance=DirectedGraph_Graph_strategy)
@settings(max_examples=50)
def test_directedgraph_graph_instantiation(instance):
    assert isinstance(instance, DirectedGraph_Graph)
