import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Graph::Edges,
    Graph::Vertices,
    Graph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::edges_is_not_abstract():
    assert not inspect.isabstract(Graph::Edges)


def test_graph::edges_constructor_exists():
    assert callable(Graph::Edges.__init__)


def test_graph::edges_constructor_args():
    sig = inspect.signature(Graph::Edges.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::edges_has_name():
    assert hasattr(Graph::Edges, "name")
    descriptor = None
    for klass in Graph::Edges.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::vertices_is_not_abstract():
    assert not inspect.isabstract(Graph::Vertices)


def test_graph::vertices_constructor_exists():
    assert callable(Graph::Vertices.__init__)


def test_graph::vertices_constructor_args():
    sig = inspect.signature(Graph::Vertices.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::vertices_has_name():
    assert hasattr(Graph::Vertices, "name")
    descriptor = None
    for klass in Graph::Vertices.__mro__:
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
Graph::Edges_strategy = st.builds(
    Graph::Edges,
    name=
        safe_text
)
Graph::Vertices_strategy = st.builds(
    Graph::Vertices,
    name=
        safe_text
)
Graph::Graph_strategy = st.builds(
    Graph::Graph,
)

@given(instance=Graph::Edges_strategy)
@settings(max_examples=50)
def test_graph::edges_instantiation(instance):
    assert isinstance(instance, Graph::Edges)

@given(instance=Graph::Edges_strategy)
def test_graph::edges_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Graph::Edges_strategy)
def test_graph::edges_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Graph::Vertices_strategy)
@settings(max_examples=50)
def test_graph::vertices_instantiation(instance):
    assert isinstance(instance, Graph::Vertices)

@given(instance=Graph::Vertices_strategy)
def test_graph::vertices_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Graph::Vertices_strategy)
def test_graph::vertices_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, Graph::Graph)
