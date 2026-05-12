import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Adaptable,
    Attributable,
    graph_Vertex,
    graph_Edge,
    Vertex,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adaptable_is_not_abstract():
    assert not inspect.isabstract(Adaptable)


def test_adaptable_constructor_exists():
    assert callable(Adaptable.__init__)


def test_adaptable_constructor_args():
    sig = inspect.signature(Adaptable.__init__)
    params = list(sig.parameters.keys())



def test_attributable_is_not_abstract():
    assert not inspect.isabstract(Attributable)


def test_attributable_constructor_exists():
    assert callable(Attributable.__init__)


def test_attributable_constructor_args():
    sig = inspect.signature(Attributable.__init__)
    params = list(sig.parameters.keys())



def test_graph_vertex_is_not_abstract():
    assert not inspect.isabstract(graph_Vertex)


def test_graph_vertex_constructor_exists():
    assert callable(graph_Vertex.__init__)


def test_graph_vertex_constructor_args():
    sig = inspect.signature(graph_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "label" in params, "Missing parameter 'label'"

def test_graph_vertex_has_number():
    assert hasattr(graph_Vertex, "number")
    descriptor = None
    for klass in graph_Vertex.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_graph_vertex_has_label():
    assert hasattr(graph_Vertex, "label")
    descriptor = None
    for klass in graph_Vertex.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_graph_edge_has_label():
    assert hasattr(graph_Edge, "label")
    descriptor = None
    for klass in graph_Edge.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



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
Adaptable_strategy = st.builds(
    Adaptable,
)
Attributable_strategy = st.builds(
    Attributable,
)
graph_Vertex_strategy = st.builds(
    graph_Vertex,
    number=
        st.integers(),
    label=
        safe_text
)
graph_Edge_strategy = st.builds(
    graph_Edge,
    label=
        safe_text
)
Vertex_strategy = st.builds(
    Vertex,
)
graph_Graph_strategy = st.builds(
    graph_Graph,
)

@given(instance=Adaptable_strategy)
@settings(max_examples=50)
def test_adaptable_instantiation(instance):
    assert isinstance(instance, Adaptable)

@given(instance=Attributable_strategy)
@settings(max_examples=50)
def test_attributable_instantiation(instance):
    assert isinstance(instance, Attributable)

@given(instance=graph_Vertex_strategy)
@settings(max_examples=50)
def test_graph_vertex_instantiation(instance):
    assert isinstance(instance, graph_Vertex)



@given(instance=graph_Vertex_strategy)
def test_graph_vertex_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=graph_Vertex_strategy)
def test_graph_vertex_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)



@given(instance=graph_Edge_strategy)
def test_graph_edge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)
