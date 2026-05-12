import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Graph_Edge,
    Graph_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(Graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(Graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(Graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(Graph_Node)


def test_graph_node_constructor_exists():
    assert callable(Graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(Graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"

def test_graph_node_has_type():
    assert hasattr(Graph_Node, "type")
    descriptor = None
    for klass in Graph_Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graph_node_has_size():
    assert hasattr(Graph_Node, "size")
    descriptor = None
    for klass in Graph_Node.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_graph_node_has_name():
    assert hasattr(Graph_Node, "name")
    descriptor = None
    for klass in Graph_Node.__mro__:
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
Graph_Edge_strategy = st.builds(
    Graph_Edge,
)
Graph_Node_strategy = st.builds(
    Graph_Node,
    type=
        safe_text,
    size=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)

@given(instance=Graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, Graph_Edge)

@given(instance=Graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, Graph_Node)



@given(instance=Graph_Node_strategy)
def test_graph_node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Graph_Node_strategy)
def test_graph_node_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=Graph_Node_strategy)
def test_graph_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
