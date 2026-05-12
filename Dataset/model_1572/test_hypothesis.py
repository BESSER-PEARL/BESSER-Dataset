import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Graph_Edges,
    Graph_Vertices,
    Graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_edges_is_not_abstract():
    assert not inspect.isabstract(Graph_Edges)


def test_graph_edges_constructor_exists():
    assert callable(Graph_Edges.__init__)


def test_graph_edges_constructor_args():
    sig = inspect.signature(Graph_Edges.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_edges_has_name():
    assert hasattr(Graph_Edges, "name")
    descriptor = None
    for klass in Graph_Edges.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_vertices_is_not_abstract():
    assert not inspect.isabstract(Graph_Vertices)


def test_graph_vertices_constructor_exists():
    assert callable(Graph_Vertices.__init__)


def test_graph_vertices_constructor_args():
    sig = inspect.signature(Graph_Vertices.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_vertices_has_name():
    assert hasattr(Graph_Vertices, "name")
    descriptor = None
    for klass in Graph_Vertices.__mro__:
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
Graph_Edges_strategy = st.builds(
    Graph_Edges,
    name=
        safe_text
)
Graph_Vertices_strategy = st.builds(
    Graph_Vertices,
    name=
        safe_text
)
Graph_Graph_strategy = st.builds(
    Graph_Graph,
)

@given(instance=Graph_Edges_strategy)
@settings(max_examples=50)
def test_graph_edges_instantiation(instance):
    assert isinstance(instance, Graph_Edges)



@given(instance=Graph_Edges_strategy)
def test_graph_edges_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Graph_Vertices_strategy)
@settings(max_examples=50)
def test_graph_vertices_instantiation(instance):
    assert isinstance(instance, Graph_Vertices)



@given(instance=Graph_Vertices_strategy)
def test_graph_vertices_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, Graph_Graph)
