import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GraphElement,
    digraph_Edge,
    digraph_Node,
    digraph_GraphElement,
    digraph_Graph,
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



def test_digraph_edge_is_not_abstract():
    assert not inspect.isabstract(digraph_Edge)


def test_digraph_edge_constructor_exists():
    assert callable(digraph_Edge.__init__)


def test_digraph_edge_constructor_args():
    sig = inspect.signature(digraph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_digraph_edge_has_weight():
    assert hasattr(digraph_Edge, "weight")
    descriptor = None
    for klass in digraph_Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_digraph_node_is_not_abstract():
    assert not inspect.isabstract(digraph_Node)


def test_digraph_node_constructor_exists():
    assert callable(digraph_Node.__init__)


def test_digraph_node_constructor_args():
    sig = inspect.signature(digraph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_digraph_node_has_label():
    assert hasattr(digraph_Node, "label")
    descriptor = None
    for klass in digraph_Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_digraph_graphelement_is_not_abstract():
    assert not inspect.isabstract(digraph_GraphElement)


def test_digraph_graphelement_constructor_exists():
    assert callable(digraph_GraphElement.__init__)


def test_digraph_graphelement_constructor_args():
    sig = inspect.signature(digraph_GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_digraph_graph_is_not_abstract():
    assert not inspect.isabstract(digraph_Graph)


def test_digraph_graph_constructor_exists():
    assert callable(digraph_Graph.__init__)


def test_digraph_graph_constructor_args():
    sig = inspect.signature(digraph_Graph.__init__)
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
digraph_Edge_strategy = st.builds(
    digraph_Edge,
    weight=
        safe_text
)
digraph_Node_strategy = st.builds(
    digraph_Node,
    label=
        safe_text
)
digraph_GraphElement_strategy = st.builds(
    digraph_GraphElement,
)
digraph_Graph_strategy = st.builds(
    digraph_Graph,
)

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=digraph_Edge_strategy)
@settings(max_examples=50)
def test_digraph_edge_instantiation(instance):
    assert isinstance(instance, digraph_Edge)



@given(instance=digraph_Edge_strategy)
def test_digraph_edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=digraph_Node_strategy)
@settings(max_examples=50)
def test_digraph_node_instantiation(instance):
    assert isinstance(instance, digraph_Node)



@given(instance=digraph_Node_strategy)
def test_digraph_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=digraph_GraphElement_strategy)
@settings(max_examples=50)
def test_digraph_graphelement_instantiation(instance):
    assert isinstance(instance, digraph_GraphElement)

@given(instance=digraph_Graph_strategy)
@settings(max_examples=50)
def test_digraph_graph_instantiation(instance):
    assert isinstance(instance, digraph_Graph)
