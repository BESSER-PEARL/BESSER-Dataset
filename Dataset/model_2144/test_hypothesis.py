import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_Vertex,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_vertex_is_not_abstract():
    assert not inspect.isabstract(graph_Vertex)


def test_graph_vertex_constructor_exists():
    assert callable(graph_Vertex.__init__)


def test_graph_vertex_constructor_args():
    sig = inspect.signature(graph_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "internalId" in params, "Missing parameter 'internalId'"

def test_graph_vertex_has_internalId():
    assert hasattr(graph_Vertex, "internalId")
    descriptor = None
    for klass in graph_Vertex.__mro__:
        if "internalId" in klass.__dict__:
            descriptor = klass.__dict__["internalId"]
            break
    assert isinstance(descriptor, property)



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "graphName" in params, "Missing parameter 'graphName'"

def test_graph_graph_has_graphName():
    assert hasattr(graph_Graph, "graphName")
    descriptor = None
    for klass in graph_Graph.__mro__:
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
graph_Vertex_strategy = st.builds(
    graph_Vertex,
    internalId=
        safe_text
)
graph_Graph_strategy = st.builds(
    graph_Graph,
    graphName=
        safe_text
)

@given(instance=graph_Vertex_strategy)
@settings(max_examples=50)
def test_graph_vertex_instantiation(instance):
    assert isinstance(instance, graph_Vertex)



@given(instance=graph_Vertex_strategy)
def test_graph_vertex_internalId_setter(instance):
    original = instance.internalId
    instance.internalId = original
    assert instance.internalId == original

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)



@given(instance=graph_Graph_strategy)
def test_graph_graph_graphName_setter(instance):
    original = instance.graphName
    instance.graphName = original
    assert instance.graphName == original
