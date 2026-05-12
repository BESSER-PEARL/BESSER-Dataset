import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simplegraph_Node,
    simplegraph_Graph,
    simplegraph_Edge,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplegraph_node_is_not_abstract():
    assert not inspect.isabstract(simplegraph_Node)


def test_simplegraph_node_constructor_exists():
    assert callable(simplegraph_Node.__init__)


def test_simplegraph_node_constructor_args():
    sig = inspect.signature(simplegraph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplegraph_node_has_name():
    assert hasattr(simplegraph_Node, "name")
    descriptor = None
    for klass in simplegraph_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplegraph_graph_is_not_abstract():
    assert not inspect.isabstract(simplegraph_Graph)


def test_simplegraph_graph_constructor_exists():
    assert callable(simplegraph_Graph.__init__)


def test_simplegraph_graph_constructor_args():
    sig = inspect.signature(simplegraph_Graph.__init__)
    params = list(sig.parameters.keys())



def test_simplegraph_edge_is_not_abstract():
    assert not inspect.isabstract(simplegraph_Edge)


def test_simplegraph_edge_constructor_exists():
    assert callable(simplegraph_Edge.__init__)


def test_simplegraph_edge_constructor_args():
    sig = inspect.signature(simplegraph_Edge.__init__)
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
simplegraph_Node_strategy = st.builds(
    simplegraph_Node,
    name=
        safe_text
)
simplegraph_Graph_strategy = st.builds(
    simplegraph_Graph,
)
simplegraph_Edge_strategy = st.builds(
    simplegraph_Edge,
)

@given(instance=simplegraph_Node_strategy)
@settings(max_examples=50)
def test_simplegraph_node_instantiation(instance):
    assert isinstance(instance, simplegraph_Node)



@given(instance=simplegraph_Node_strategy)
def test_simplegraph_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplegraph_Graph_strategy)
@settings(max_examples=50)
def test_simplegraph_graph_instantiation(instance):
    assert isinstance(instance, simplegraph_Graph)

@given(instance=simplegraph_Edge_strategy)
@settings(max_examples=50)
def test_simplegraph_edge_instantiation(instance):
    assert isinstance(instance, simplegraph_Edge)
