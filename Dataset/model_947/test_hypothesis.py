import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Graph_Edge,
    Graph_Node,
    Graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(Graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(Graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(Graph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "relation" in params, "Missing parameter 'relation'"
    assert "degree" in params, "Missing parameter 'degree'"

def test_graph_edge_has_relation():
    assert hasattr(Graph_Edge, "relation")
    descriptor = None
    for klass in Graph_Edge.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)

def test_graph_edge_has_degree():
    assert hasattr(Graph_Edge, "degree")
    descriptor = None
    for klass in Graph_Edge.__mro__:
        if "degree" in klass.__dict__:
            descriptor = klass.__dict__["degree"]
            break
    assert isinstance(descriptor, property)



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(Graph_Node)


def test_graph_node_constructor_exists():
    assert callable(Graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(Graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_node_has_name():
    assert hasattr(Graph_Node, "name")
    descriptor = None
    for klass in Graph_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(Graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(Graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(Graph_Graph.__init__)
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
Graph_Edge_strategy = st.builds(
    Graph_Edge,
    relation=
        safe_text,
    degree=
        st.integers()
)
Graph_Node_strategy = st.builds(
    Graph_Node,
    name=
        safe_text
)
Graph_Graph_strategy = st.builds(
    Graph_Graph,
)

@given(instance=Graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, Graph_Edge)



@given(instance=Graph_Edge_strategy)
def test_graph_edge_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original



@given(instance=Graph_Edge_strategy)
def test_graph_edge_degree_setter(instance):
    original = instance.degree
    instance.degree = original
    assert instance.degree == original

@given(instance=Graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, Graph_Node)



@given(instance=Graph_Node_strategy)
def test_graph_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, Graph_Graph)
