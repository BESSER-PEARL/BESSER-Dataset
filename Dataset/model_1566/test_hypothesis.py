import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph2_GraphComponent,
    graph2_Graph,
    GraphComponent,
    graph2_Edge,
    graph2_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph2_graphcomponent_is_not_abstract():
    assert not inspect.isabstract(graph2_GraphComponent)


def test_graph2_graphcomponent_constructor_exists():
    assert callable(graph2_GraphComponent.__init__)


def test_graph2_graphcomponent_constructor_args():
    sig = inspect.signature(graph2_GraphComponent.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_graph2_graphcomponent_has_text():
    assert hasattr(graph2_GraphComponent, "text")
    descriptor = None
    for klass in graph2_GraphComponent.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_graph2_graph_is_not_abstract():
    assert not inspect.isabstract(graph2_Graph)


def test_graph2_graph_constructor_exists():
    assert callable(graph2_Graph.__init__)


def test_graph2_graph_constructor_args():
    sig = inspect.signature(graph2_Graph.__init__)
    params = list(sig.parameters.keys())



def test_graphcomponent_is_not_abstract():
    assert not inspect.isabstract(GraphComponent)


def test_graphcomponent_constructor_exists():
    assert callable(GraphComponent.__init__)


def test_graphcomponent_constructor_args():
    sig = inspect.signature(GraphComponent.__init__)
    params = list(sig.parameters.keys())



def test_graph2_edge_is_not_abstract():
    assert not inspect.isabstract(graph2_Edge)


def test_graph2_edge_constructor_exists():
    assert callable(graph2_Edge.__init__)


def test_graph2_edge_constructor_args():
    sig = inspect.signature(graph2_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph2_node_is_not_abstract():
    assert not inspect.isabstract(graph2_Node)


def test_graph2_node_constructor_exists():
    assert callable(graph2_Node.__init__)


def test_graph2_node_constructor_args():
    sig = inspect.signature(graph2_Node.__init__)
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
graph2_GraphComponent_strategy = st.builds(
    graph2_GraphComponent,
    text=
        safe_text
)
graph2_Graph_strategy = st.builds(
    graph2_Graph,
)
GraphComponent_strategy = st.builds(
    GraphComponent,
)
graph2_Edge_strategy = st.builds(
    graph2_Edge,
)
graph2_Node_strategy = st.builds(
    graph2_Node,
)

@given(instance=graph2_GraphComponent_strategy)
@settings(max_examples=50)
def test_graph2_graphcomponent_instantiation(instance):
    assert isinstance(instance, graph2_GraphComponent)



@given(instance=graph2_GraphComponent_strategy)
def test_graph2_graphcomponent_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=graph2_Graph_strategy)
@settings(max_examples=50)
def test_graph2_graph_instantiation(instance):
    assert isinstance(instance, graph2_Graph)

@given(instance=GraphComponent_strategy)
@settings(max_examples=50)
def test_graphcomponent_instantiation(instance):
    assert isinstance(instance, GraphComponent)

@given(instance=graph2_Edge_strategy)
@settings(max_examples=50)
def test_graph2_edge_instantiation(instance):
    assert isinstance(instance, graph2_Edge)

@given(instance=graph2_Node_strategy)
@settings(max_examples=50)
def test_graph2_node_instantiation(instance):
    assert isinstance(instance, graph2_Node)
