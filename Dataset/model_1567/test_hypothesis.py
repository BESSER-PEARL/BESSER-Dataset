import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GraphComponent,
    graph2::Edge,
    graph2::Node,
    graph2::GraphComponent,
    graph2::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graphcomponent_is_not_abstract():
    assert not inspect.isabstract(GraphComponent)


def test_graphcomponent_constructor_exists():
    assert callable(GraphComponent.__init__)


def test_graphcomponent_constructor_args():
    sig = inspect.signature(GraphComponent.__init__)
    params = list(sig.parameters.keys())



def test_graph2::edge_is_not_abstract():
    assert not inspect.isabstract(graph2::Edge)


def test_graph2::edge_constructor_exists():
    assert callable(graph2::Edge.__init__)


def test_graph2::edge_constructor_args():
    sig = inspect.signature(graph2::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph2::node_is_not_abstract():
    assert not inspect.isabstract(graph2::Node)


def test_graph2::node_constructor_exists():
    assert callable(graph2::Node.__init__)


def test_graph2::node_constructor_args():
    sig = inspect.signature(graph2::Node.__init__)
    params = list(sig.parameters.keys())



def test_graph2::graphcomponent_is_not_abstract():
    assert not inspect.isabstract(graph2::GraphComponent)


def test_graph2::graphcomponent_constructor_exists():
    assert callable(graph2::GraphComponent.__init__)


def test_graph2::graphcomponent_constructor_args():
    sig = inspect.signature(graph2::GraphComponent.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_graph2::graphcomponent_has_text():
    assert hasattr(graph2::GraphComponent, "text")
    descriptor = None
    for klass in graph2::GraphComponent.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_graph2::graph_is_not_abstract():
    assert not inspect.isabstract(graph2::Graph)


def test_graph2::graph_constructor_exists():
    assert callable(graph2::Graph.__init__)


def test_graph2::graph_constructor_args():
    sig = inspect.signature(graph2::Graph.__init__)
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
GraphComponent_strategy = st.builds(
    GraphComponent,
)
graph2::Edge_strategy = st.builds(
    graph2::Edge,
)
graph2::Node_strategy = st.builds(
    graph2::Node,
)
graph2::GraphComponent_strategy = st.builds(
    graph2::GraphComponent,
    text=
        safe_text
)
graph2::Graph_strategy = st.builds(
    graph2::Graph,
)

@given(instance=GraphComponent_strategy)
@settings(max_examples=50)
def test_graphcomponent_instantiation(instance):
    assert isinstance(instance, GraphComponent)

@given(instance=graph2::Edge_strategy)
@settings(max_examples=50)
def test_graph2::edge_instantiation(instance):
    assert isinstance(instance, graph2::Edge)

@given(instance=graph2::Node_strategy)
@settings(max_examples=50)
def test_graph2::node_instantiation(instance):
    assert isinstance(instance, graph2::Node)

@given(instance=graph2::GraphComponent_strategy)
@settings(max_examples=50)
def test_graph2::graphcomponent_instantiation(instance):
    assert isinstance(instance, graph2::GraphComponent)

@given(instance=graph2::GraphComponent_strategy)
def test_graph2::graphcomponent_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=graph2::GraphComponent_strategy)
def test_graph2::graphcomponent_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=graph2::Graph_strategy)
@settings(max_examples=50)
def test_graph2::graph_instantiation(instance):
    assert isinstance(instance, graph2::Graph)
