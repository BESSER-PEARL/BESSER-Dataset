import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ScaffoldGraph::Edge,
    ScaffoldGraph::Vertex,
    ScaffoldGraph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scaffoldgraph::edge_is_not_abstract():
    assert not inspect.isabstract(ScaffoldGraph::Edge)


def test_scaffoldgraph::edge_constructor_exists():
    assert callable(ScaffoldGraph::Edge.__init__)


def test_scaffoldgraph::edge_constructor_args():
    sig = inspect.signature(ScaffoldGraph::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_scaffoldgraph::edge_has_weight():
    assert hasattr(ScaffoldGraph::Edge, "weight")
    descriptor = None
    for klass in ScaffoldGraph::Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_scaffoldgraph::vertex_is_not_abstract():
    assert not inspect.isabstract(ScaffoldGraph::Vertex)


def test_scaffoldgraph::vertex_constructor_exists():
    assert callable(ScaffoldGraph::Vertex.__init__)


def test_scaffoldgraph::vertex_constructor_args():
    sig = inspect.signature(ScaffoldGraph::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_scaffoldgraph::graph_is_not_abstract():
    assert not inspect.isabstract(ScaffoldGraph::Graph)


def test_scaffoldgraph::graph_constructor_exists():
    assert callable(ScaffoldGraph::Graph.__init__)


def test_scaffoldgraph::graph_constructor_args():
    sig = inspect.signature(ScaffoldGraph::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scaffoldgraph::graph_has_name():
    assert hasattr(ScaffoldGraph::Graph, "name")
    descriptor = None
    for klass in ScaffoldGraph::Graph.__mro__:
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
ScaffoldGraph::Edge_strategy = st.builds(
    ScaffoldGraph::Edge,
    weight=
        st.integers()
)
ScaffoldGraph::Vertex_strategy = st.builds(
    ScaffoldGraph::Vertex,
)
ScaffoldGraph::Graph_strategy = st.builds(
    ScaffoldGraph::Graph,
    name=
        safe_text
)

@given(instance=ScaffoldGraph::Edge_strategy)
@settings(max_examples=50)
def test_scaffoldgraph::edge_instantiation(instance):
    assert isinstance(instance, ScaffoldGraph::Edge)

@given(instance=ScaffoldGraph::Edge_strategy)
def test_scaffoldgraph::edge_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=ScaffoldGraph::Edge_strategy)
def test_scaffoldgraph::edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=ScaffoldGraph::Vertex_strategy)
@settings(max_examples=50)
def test_scaffoldgraph::vertex_instantiation(instance):
    assert isinstance(instance, ScaffoldGraph::Vertex)

@given(instance=ScaffoldGraph::Graph_strategy)
@settings(max_examples=50)
def test_scaffoldgraph::graph_instantiation(instance):
    assert isinstance(instance, ScaffoldGraph::Graph)

@given(instance=ScaffoldGraph::Graph_strategy)
def test_scaffoldgraph::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ScaffoldGraph::Graph_strategy)
def test_scaffoldgraph::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
