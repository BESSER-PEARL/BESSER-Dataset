import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dot::Attribute,
    dot::Node,
    dot::DirectedEdge,
    dot::UnDirectedEdge,
    Graph,
    dot::DirectedGraph,
    dot::UndirectedGraph,
    dot::Graph,
    dot::GraphModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dot::attribute_is_not_abstract():
    assert not inspect.isabstract(dot::Attribute)


def test_dot::attribute_constructor_exists():
    assert callable(dot::Attribute.__init__)


def test_dot::attribute_constructor_args():
    sig = inspect.signature(dot::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_dot::attribute_has_weight():
    assert hasattr(dot::Attribute, "weight")
    descriptor = None
    for klass in dot::Attribute.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_dot::node_is_not_abstract():
    assert not inspect.isabstract(dot::Node)


def test_dot::node_constructor_exists():
    assert callable(dot::Node.__init__)


def test_dot::node_constructor_args():
    sig = inspect.signature(dot::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot::node_has_name():
    assert hasattr(dot::Node, "name")
    descriptor = None
    for klass in dot::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::directededge_is_not_abstract():
    assert not inspect.isabstract(dot::DirectedEdge)


def test_dot::directededge_constructor_exists():
    assert callable(dot::DirectedEdge.__init__)


def test_dot::directededge_constructor_args():
    sig = inspect.signature(dot::DirectedEdge.__init__)
    params = list(sig.parameters.keys())



def test_dot::undirectededge_is_not_abstract():
    assert not inspect.isabstract(dot::UnDirectedEdge)


def test_dot::undirectededge_constructor_exists():
    assert callable(dot::UnDirectedEdge.__init__)


def test_dot::undirectededge_constructor_args():
    sig = inspect.signature(dot::UnDirectedEdge.__init__)
    params = list(sig.parameters.keys())



def test_graph_is_not_abstract():
    assert not inspect.isabstract(Graph)


def test_graph_constructor_exists():
    assert callable(Graph.__init__)


def test_graph_constructor_args():
    sig = inspect.signature(Graph.__init__)
    params = list(sig.parameters.keys())



def test_dot::directedgraph_is_not_abstract():
    assert not inspect.isabstract(dot::DirectedGraph)


def test_dot::directedgraph_constructor_exists():
    assert callable(dot::DirectedGraph.__init__)


def test_dot::directedgraph_constructor_args():
    sig = inspect.signature(dot::DirectedGraph.__init__)
    params = list(sig.parameters.keys())



def test_dot::undirectedgraph_is_not_abstract():
    assert not inspect.isabstract(dot::UndirectedGraph)


def test_dot::undirectedgraph_constructor_exists():
    assert callable(dot::UndirectedGraph.__init__)


def test_dot::undirectedgraph_constructor_args():
    sig = inspect.signature(dot::UndirectedGraph.__init__)
    params = list(sig.parameters.keys())



def test_dot::graph_is_not_abstract():
    assert not inspect.isabstract(dot::Graph)


def test_dot::graph_constructor_exists():
    assert callable(dot::Graph.__init__)


def test_dot::graph_constructor_args():
    sig = inspect.signature(dot::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot::graph_has_name():
    assert hasattr(dot::Graph, "name")
    descriptor = None
    for klass in dot::Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::graphmodel_is_not_abstract():
    assert not inspect.isabstract(dot::GraphModel)


def test_dot::graphmodel_constructor_exists():
    assert callable(dot::GraphModel.__init__)


def test_dot::graphmodel_constructor_args():
    sig = inspect.signature(dot::GraphModel.__init__)
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
dot::Attribute_strategy = st.builds(
    dot::Attribute,
    weight=
        st.integers()
)
dot::Node_strategy = st.builds(
    dot::Node,
    name=
        safe_text
)
dot::DirectedEdge_strategy = st.builds(
    dot::DirectedEdge,
)
dot::UnDirectedEdge_strategy = st.builds(
    dot::UnDirectedEdge,
)
Graph_strategy = st.builds(
    Graph,
)
dot::DirectedGraph_strategy = st.builds(
    dot::DirectedGraph,
)
dot::UndirectedGraph_strategy = st.builds(
    dot::UndirectedGraph,
)
dot::Graph_strategy = st.builds(
    dot::Graph,
    name=
        safe_text
)
dot::GraphModel_strategy = st.builds(
    dot::GraphModel,
)

@given(instance=dot::Attribute_strategy)
@settings(max_examples=50)
def test_dot::attribute_instantiation(instance):
    assert isinstance(instance, dot::Attribute)

@given(instance=dot::Attribute_strategy)
def test_dot::attribute_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=dot::Attribute_strategy)
def test_dot::attribute_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=dot::Node_strategy)
@settings(max_examples=50)
def test_dot::node_instantiation(instance):
    assert isinstance(instance, dot::Node)

@given(instance=dot::Node_strategy)
def test_dot::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::Node_strategy)
def test_dot::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::DirectedEdge_strategy)
@settings(max_examples=50)
def test_dot::directededge_instantiation(instance):
    assert isinstance(instance, dot::DirectedEdge)

@given(instance=dot::UnDirectedEdge_strategy)
@settings(max_examples=50)
def test_dot::undirectededge_instantiation(instance):
    assert isinstance(instance, dot::UnDirectedEdge)

@given(instance=Graph_strategy)
@settings(max_examples=50)
def test_graph_instantiation(instance):
    assert isinstance(instance, Graph)

@given(instance=dot::DirectedGraph_strategy)
@settings(max_examples=50)
def test_dot::directedgraph_instantiation(instance):
    assert isinstance(instance, dot::DirectedGraph)

@given(instance=dot::UndirectedGraph_strategy)
@settings(max_examples=50)
def test_dot::undirectedgraph_instantiation(instance):
    assert isinstance(instance, dot::UndirectedGraph)

@given(instance=dot::Graph_strategy)
@settings(max_examples=50)
def test_dot::graph_instantiation(instance):
    assert isinstance(instance, dot::Graph)

@given(instance=dot::Graph_strategy)
def test_dot::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::Graph_strategy)
def test_dot::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::GraphModel_strategy)
@settings(max_examples=50)
def test_dot::graphmodel_instantiation(instance):
    assert isinstance(instance, dot::GraphModel)
