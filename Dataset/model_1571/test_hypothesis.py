import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::Edge,
    graph::Vertex,
    graph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph::vertex_is_not_abstract():
    assert not inspect.isabstract(graph::Vertex)


def test_graph::vertex_constructor_exists():
    assert callable(graph::Vertex.__init__)


def test_graph::vertex_constructor_args():
    sig = inspect.signature(graph::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "weigth" in params, "Missing parameter 'weigth'"

def test_graph::vertex_has_label():
    assert hasattr(graph::Vertex, "label")
    descriptor = None
    for klass in graph::Vertex.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_graph::vertex_has_weigth():
    assert hasattr(graph::Vertex, "weigth")
    descriptor = None
    for klass in graph::Vertex.__mro__:
        if "weigth" in klass.__dict__:
            descriptor = klass.__dict__["weigth"]
            break
    assert isinstance(descriptor, property)



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(graph::Graph.__init__)
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
graph::Edge_strategy = st.builds(
    graph::Edge,
)
graph::Vertex_strategy = st.builds(
    graph::Vertex,
    label=
        safe_text,
    weigth=
        st.integers()
)
graph::Graph_strategy = st.builds(
    graph::Graph,
)

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::Vertex_strategy)
@settings(max_examples=50)
def test_graph::vertex_instantiation(instance):
    assert isinstance(instance, graph::Vertex)

@given(instance=graph::Vertex_strategy)
def test_graph::vertex_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=graph::Vertex_strategy)
def test_graph::vertex_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=graph::Vertex_strategy)
def test_graph::vertex_weigth_type(instance):
    assert isinstance(instance.weigth, int)


@given(instance=graph::Vertex_strategy)
def test_graph::vertex_weigth_setter(instance):
    original = instance.weigth
    instance.weigth = original
    assert instance.weigth == original

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)
