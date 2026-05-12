import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_GraphElement,
    GraphElement,
    graph_Edge,
    graph_Node,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_graphelement_is_not_abstract():
    assert not inspect.isabstract(graph_GraphElement)


def test_graph_graphelement_constructor_exists():
    assert callable(graph_GraphElement.__init__)


def test_graph_graphelement_constructor_args():
    sig = inspect.signature(graph_GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_graphelement_has_name():
    assert hasattr(graph_GraphElement, "name")
    descriptor = None
    for klass in graph_GraphElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_graph_has_name():
    assert hasattr(graph_Graph, "name")
    descriptor = None
    for klass in graph_Graph.__mro__:
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
graph_GraphElement_strategy = st.builds(
    graph_GraphElement,
    name=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
graph_Edge_strategy = st.builds(
    graph_Edge,
)
graph_Node_strategy = st.builds(
    graph_Node,
)
graph_Graph_strategy = st.builds(
    graph_Graph,
    name=
        safe_text
)

@given(instance=graph_GraphElement_strategy)
@settings(max_examples=50)
def test_graph_graphelement_instantiation(instance):
    assert isinstance(instance, graph_GraphElement)



@given(instance=graph_GraphElement_strategy)
def test_graph_graphelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)

@given(instance=graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, graph_Node)

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)



@given(instance=graph_Graph_strategy)
def test_graph_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
