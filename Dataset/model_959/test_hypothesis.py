import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simplegraph::Node,
    simplegraph::Graph,
    simplegraph::Edge,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplegraph::node_is_not_abstract():
    assert not inspect.isabstract(simplegraph::Node)


def test_simplegraph::node_constructor_exists():
    assert callable(simplegraph::Node.__init__)


def test_simplegraph::node_constructor_args():
    sig = inspect.signature(simplegraph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplegraph::node_has_name():
    assert hasattr(simplegraph::Node, "name")
    descriptor = None
    for klass in simplegraph::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplegraph::graph_is_not_abstract():
    assert not inspect.isabstract(simplegraph::Graph)


def test_simplegraph::graph_constructor_exists():
    assert callable(simplegraph::Graph.__init__)


def test_simplegraph::graph_constructor_args():
    sig = inspect.signature(simplegraph::Graph.__init__)
    params = list(sig.parameters.keys())



def test_simplegraph::edge_is_not_abstract():
    assert not inspect.isabstract(simplegraph::Edge)


def test_simplegraph::edge_constructor_exists():
    assert callable(simplegraph::Edge.__init__)


def test_simplegraph::edge_constructor_args():
    sig = inspect.signature(simplegraph::Edge.__init__)
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
simplegraph::Node_strategy = st.builds(
    simplegraph::Node,
    name=
        safe_text
)
simplegraph::Graph_strategy = st.builds(
    simplegraph::Graph,
)
simplegraph::Edge_strategy = st.builds(
    simplegraph::Edge,
)

@given(instance=simplegraph::Node_strategy)
@settings(max_examples=50)
def test_simplegraph::node_instantiation(instance):
    assert isinstance(instance, simplegraph::Node)

@given(instance=simplegraph::Node_strategy)
def test_simplegraph::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplegraph::Node_strategy)
def test_simplegraph::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplegraph::Graph_strategy)
@settings(max_examples=50)
def test_simplegraph::graph_instantiation(instance):
    assert isinstance(instance, simplegraph::Graph)

@given(instance=simplegraph::Edge_strategy)
@settings(max_examples=50)
def test_simplegraph::edge_instantiation(instance):
    assert isinstance(instance, simplegraph::Edge)
