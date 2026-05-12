import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_Edge,
    graph_Vertex,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph_vertex_is_not_abstract():
    assert not inspect.isabstract(graph_Vertex)


def test_graph_vertex_constructor_exists():
    assert callable(graph_Vertex.__init__)


def test_graph_vertex_constructor_args():
    sig = inspect.signature(graph_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "weigth" in params, "Missing parameter 'weigth'"

def test_graph_vertex_has_label():
    assert hasattr(graph_Vertex, "label")
    descriptor = None
    for klass in graph_Vertex.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_graph_vertex_has_weigth():
    assert hasattr(graph_Vertex, "weigth")
    descriptor = None
    for klass in graph_Vertex.__mro__:
        if "weigth" in klass.__dict__:
            descriptor = klass.__dict__["weigth"]
            break
    assert isinstance(descriptor, property)



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
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
graph_Edge_strategy = st.builds(
    graph_Edge,
)
graph_Vertex_strategy = st.builds(
    graph_Vertex,
    label=
        safe_text,
    weigth=
        st.integers()
)
graph_Graph_strategy = st.builds(
    graph_Graph,
)

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)

@given(instance=graph_Vertex_strategy)
@settings(max_examples=50)
def test_graph_vertex_instantiation(instance):
    assert isinstance(instance, graph_Vertex)



@given(instance=graph_Vertex_strategy)
def test_graph_vertex_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=graph_Vertex_strategy)
def test_graph_vertex_weigth_setter(instance):
    original = instance.weigth
    instance.weigth = original
    assert instance.weigth == original

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)
