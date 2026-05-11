import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::Vertex,
    graph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::vertex_is_not_abstract():
    assert not inspect.isabstract(graph::Vertex)


def test_graph::vertex_constructor_exists():
    assert callable(graph::Vertex.__init__)


def test_graph::vertex_constructor_args():
    sig = inspect.signature(graph::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "internalId" in params, "Missing parameter 'internalId'"

def test_graph::vertex_has_internalId():
    assert hasattr(graph::Vertex, "internalId")
    descriptor = None
    for klass in graph::Vertex.__mro__:
        if "internalId" in klass.__dict__:
            descriptor = klass.__dict__["internalId"]
            break
    assert isinstance(descriptor, property)



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(graph::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "graphName" in params, "Missing parameter 'graphName'"

def test_graph::graph_has_graphName():
    assert hasattr(graph::Graph, "graphName")
    descriptor = None
    for klass in graph::Graph.__mro__:
        if "graphName" in klass.__dict__:
            descriptor = klass.__dict__["graphName"]
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
graph::Vertex_strategy = st.builds(
    graph::Vertex,
    internalId=
        safe_text
)
graph::Graph_strategy = st.builds(
    graph::Graph,
    graphName=
        safe_text
)

@given(instance=graph::Vertex_strategy)
@settings(max_examples=50)
def test_graph::vertex_instantiation(instance):
    assert isinstance(instance, graph::Vertex)

@given(instance=graph::Vertex_strategy)
def test_graph::vertex_internalId_type(instance):
    assert isinstance(instance.internalId, str)


@given(instance=graph::Vertex_strategy)
def test_graph::vertex_internalId_setter(instance):
    original = instance.internalId
    instance.internalId = original
    assert instance.internalId == original

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)

@given(instance=graph::Graph_strategy)
def test_graph::graph_graphName_type(instance):
    assert isinstance(instance.graphName, str)


@given(instance=graph::Graph_strategy)
def test_graph::graph_graphName_setter(instance):
    original = instance.graphName
    instance.graphName = original
    assert instance.graphName == original
