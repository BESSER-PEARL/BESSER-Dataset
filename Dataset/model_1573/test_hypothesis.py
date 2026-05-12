import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ScaffoldGraph_Edge,
    ScaffoldGraph_Vertex,
    ScaffoldGraph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scaffoldgraph_edge_is_not_abstract():
    assert not inspect.isabstract(ScaffoldGraph_Edge)


def test_scaffoldgraph_edge_constructor_exists():
    assert callable(ScaffoldGraph_Edge.__init__)


def test_scaffoldgraph_edge_constructor_args():
    sig = inspect.signature(ScaffoldGraph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_scaffoldgraph_edge_has_weight():
    assert hasattr(ScaffoldGraph_Edge, "weight")
    descriptor = None
    for klass in ScaffoldGraph_Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_scaffoldgraph_vertex_is_not_abstract():
    assert not inspect.isabstract(ScaffoldGraph_Vertex)


def test_scaffoldgraph_vertex_constructor_exists():
    assert callable(ScaffoldGraph_Vertex.__init__)


def test_scaffoldgraph_vertex_constructor_args():
    sig = inspect.signature(ScaffoldGraph_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_scaffoldgraph_graph_is_not_abstract():
    assert not inspect.isabstract(ScaffoldGraph_Graph)


def test_scaffoldgraph_graph_constructor_exists():
    assert callable(ScaffoldGraph_Graph.__init__)


def test_scaffoldgraph_graph_constructor_args():
    sig = inspect.signature(ScaffoldGraph_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scaffoldgraph_graph_has_name():
    assert hasattr(ScaffoldGraph_Graph, "name")
    descriptor = None
    for klass in ScaffoldGraph_Graph.__mro__:
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
ScaffoldGraph_Edge_strategy = st.builds(
    ScaffoldGraph_Edge,
    weight=
        st.integers()
)
ScaffoldGraph_Vertex_strategy = st.builds(
    ScaffoldGraph_Vertex,
)
ScaffoldGraph_Graph_strategy = st.builds(
    ScaffoldGraph_Graph,
    name=
        safe_text
)

@given(instance=ScaffoldGraph_Edge_strategy)
@settings(max_examples=50)
def test_scaffoldgraph_edge_instantiation(instance):
    assert isinstance(instance, ScaffoldGraph_Edge)



@given(instance=ScaffoldGraph_Edge_strategy)
def test_scaffoldgraph_edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=ScaffoldGraph_Vertex_strategy)
@settings(max_examples=50)
def test_scaffoldgraph_vertex_instantiation(instance):
    assert isinstance(instance, ScaffoldGraph_Vertex)

@given(instance=ScaffoldGraph_Graph_strategy)
@settings(max_examples=50)
def test_scaffoldgraph_graph_instantiation(instance):
    assert isinstance(instance, ScaffoldGraph_Graph)



@given(instance=ScaffoldGraph_Graph_strategy)
def test_scaffoldgraph_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
