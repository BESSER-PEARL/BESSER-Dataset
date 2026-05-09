import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Graph::Edge,
    Graph::Node,
    Graph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(Graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(Graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(Graph::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "degree" in params, "Missing parameter 'degree'"
    assert "relation" in params, "Missing parameter 'relation'"

def test_graph::edge_has_degree():
    assert hasattr(Graph::Edge, "degree")
    descriptor = None
    for klass in Graph::Edge.__mro__:
        if "degree" in klass.__dict__:
            descriptor = klass.__dict__["degree"]
            break
    assert isinstance(descriptor, property)

def test_graph::edge_has_relation():
    assert hasattr(Graph::Edge, "relation")
    descriptor = None
    for klass in Graph::Edge.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(Graph::Node)


def test_graph::node_constructor_exists():
    assert callable(Graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(Graph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::node_has_name():
    assert hasattr(Graph::Node, "name")
    descriptor = None
    for klass in Graph::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(Graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(Graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(Graph::Graph.__init__)
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
Graph::Edge_strategy = st.builds(
    Graph::Edge,
    degree=
        st.integers(),
    relation=
        safe_text
)
Graph::Node_strategy = st.builds(
    Graph::Node,
    name=
        safe_text
)
Graph::Graph_strategy = st.builds(
    Graph::Graph,
)

@given(instance=Graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, Graph::Edge)

@given(instance=Graph::Edge_strategy)
def test_graph::edge_degree_type(instance):
    assert isinstance(instance.degree, int)


@given(instance=Graph::Edge_strategy)
def test_graph::edge_degree_setter(instance):
    original = instance.degree
    instance.degree = original
    assert instance.degree == original

@given(instance=Graph::Edge_strategy)
def test_graph::edge_relation_type(instance):
    assert isinstance(instance.relation, str)


@given(instance=Graph::Edge_strategy)
def test_graph::edge_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=Graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, Graph::Node)

@given(instance=Graph::Node_strategy)
def test_graph::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Graph::Node_strategy)
def test_graph::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, Graph::Graph)
