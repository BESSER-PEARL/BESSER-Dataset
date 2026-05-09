import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::GraphElement,
    GraphElement,
    graph::Edge,
    graph::Node,
    graph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::graphelement_is_not_abstract():
    assert not inspect.isabstract(graph::GraphElement)


def test_graph::graphelement_constructor_exists():
    assert callable(graph::GraphElement.__init__)


def test_graph::graphelement_constructor_args():
    sig = inspect.signature(graph::GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::graphelement_has_name():
    assert hasattr(graph::GraphElement, "name")
    descriptor = None
    for klass in graph::GraphElement.__mro__:
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



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
    params = list(sig.parameters.keys())



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(graph::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::graph_has_name():
    assert hasattr(graph::Graph, "name")
    descriptor = None
    for klass in graph::Graph.__mro__:
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
graph::GraphElement_strategy = st.builds(
    graph::GraphElement,
    name=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
graph::Edge_strategy = st.builds(
    graph::Edge,
)
graph::Node_strategy = st.builds(
    graph::Node,
)
graph::Graph_strategy = st.builds(
    graph::Graph,
    name=
        safe_text
)

@given(instance=graph::GraphElement_strategy)
@settings(max_examples=50)
def test_graph::graphelement_instantiation(instance):
    assert isinstance(instance, graph::GraphElement)

@given(instance=graph::GraphElement_strategy)
def test_graph::graphelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::GraphElement_strategy)
def test_graph::graphelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)

@given(instance=graph::Graph_strategy)
def test_graph::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Graph_strategy)
def test_graph::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
