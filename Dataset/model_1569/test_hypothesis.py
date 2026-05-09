import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::Edge,
    graph::Vertice,
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



def test_graph::vertice_is_not_abstract():
    assert not inspect.isabstract(graph::Vertice)


def test_graph::vertice_constructor_exists():
    assert callable(graph::Vertice.__init__)


def test_graph::vertice_constructor_args():
    sig = inspect.signature(graph::Vertice.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_graph::vertice_has_label():
    assert hasattr(graph::Vertice, "label")
    descriptor = None
    for klass in graph::Vertice.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
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
graph::Vertice_strategy = st.builds(
    graph::Vertice,
    label=
        safe_text
)
graph::Graph_strategy = st.builds(
    graph::Graph,
)

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::Vertice_strategy)
@settings(max_examples=50)
def test_graph::vertice_instantiation(instance):
    assert isinstance(instance, graph::Vertice)

@given(instance=graph::Vertice_strategy)
def test_graph::vertice_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=graph::Vertice_strategy)
def test_graph::vertice_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)
