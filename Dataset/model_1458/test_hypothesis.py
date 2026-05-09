import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph1::Graph,
    graph1::Edge,
    graph1::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph1::graph_is_not_abstract():
    assert not inspect.isabstract(graph1::Graph)


def test_graph1::graph_constructor_exists():
    assert callable(graph1::Graph.__init__)


def test_graph1::graph_constructor_args():
    sig = inspect.signature(graph1::Graph.__init__)
    params = list(sig.parameters.keys())



def test_graph1::edge_is_not_abstract():
    assert not inspect.isabstract(graph1::Edge)


def test_graph1::edge_constructor_exists():
    assert callable(graph1::Edge.__init__)


def test_graph1::edge_constructor_args():
    sig = inspect.signature(graph1::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph1::node_is_not_abstract():
    assert not inspect.isabstract(graph1::Node)


def test_graph1::node_constructor_exists():
    assert callable(graph1::Node.__init__)


def test_graph1::node_constructor_args():
    sig = inspect.signature(graph1::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph1::node_has_name():
    assert hasattr(graph1::Node, "name")
    descriptor = None
    for klass in graph1::Node.__mro__:
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
graph1::Graph_strategy = st.builds(
    graph1::Graph,
)
graph1::Edge_strategy = st.builds(
    graph1::Edge,
)
graph1::Node_strategy = st.builds(
    graph1::Node,
    name=
        safe_text
)

@given(instance=graph1::Graph_strategy)
@settings(max_examples=50)
def test_graph1::graph_instantiation(instance):
    assert isinstance(instance, graph1::Graph)

@given(instance=graph1::Edge_strategy)
@settings(max_examples=50)
def test_graph1::edge_instantiation(instance):
    assert isinstance(instance, graph1::Edge)

@given(instance=graph1::Node_strategy)
@settings(max_examples=50)
def test_graph1::node_instantiation(instance):
    assert isinstance(instance, graph1::Node)

@given(instance=graph1::Node_strategy)
def test_graph1::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph1::Node_strategy)
def test_graph1::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
