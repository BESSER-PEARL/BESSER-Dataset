import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph1_Graph,
    graph1_Edge,
    graph1_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph1_graph_is_not_abstract():
    assert not inspect.isabstract(graph1_Graph)


def test_graph1_graph_constructor_exists():
    assert callable(graph1_Graph.__init__)


def test_graph1_graph_constructor_args():
    sig = inspect.signature(graph1_Graph.__init__)
    params = list(sig.parameters.keys())



def test_graph1_edge_is_not_abstract():
    assert not inspect.isabstract(graph1_Edge)


def test_graph1_edge_constructor_exists():
    assert callable(graph1_Edge.__init__)


def test_graph1_edge_constructor_args():
    sig = inspect.signature(graph1_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph1_node_is_not_abstract():
    assert not inspect.isabstract(graph1_Node)


def test_graph1_node_constructor_exists():
    assert callable(graph1_Node.__init__)


def test_graph1_node_constructor_args():
    sig = inspect.signature(graph1_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph1_node_has_name():
    assert hasattr(graph1_Node, "name")
    descriptor = None
    for klass in graph1_Node.__mro__:
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
graph1_Graph_strategy = st.builds(
    graph1_Graph,
)
graph1_Edge_strategy = st.builds(
    graph1_Edge,
)
graph1_Node_strategy = st.builds(
    graph1_Node,
    name=
        safe_text
)

@given(instance=graph1_Graph_strategy)
@settings(max_examples=50)
def test_graph1_graph_instantiation(instance):
    assert isinstance(instance, graph1_Graph)

@given(instance=graph1_Edge_strategy)
@settings(max_examples=50)
def test_graph1_edge_instantiation(instance):
    assert isinstance(instance, graph1_Edge)

@given(instance=graph1_Node_strategy)
@settings(max_examples=50)
def test_graph1_node_instantiation(instance):
    assert isinstance(instance, graph1_Node)



@given(instance=graph1_Node_strategy)
def test_graph1_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
