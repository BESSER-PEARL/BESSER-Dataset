import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    grapheditormodel::Edge,
    grapheditormodel::Node,
    grapheditormodel::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_grapheditormodel::edge_is_not_abstract():
    assert not inspect.isabstract(grapheditormodel::Edge)


def test_grapheditormodel::edge_constructor_exists():
    assert callable(grapheditormodel::Edge.__init__)


def test_grapheditormodel::edge_constructor_args():
    sig = inspect.signature(grapheditormodel::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"

def test_grapheditormodel::edge_has_Value():
    assert hasattr(grapheditormodel::Edge, "Value")
    descriptor = None
    for klass in grapheditormodel::Edge.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_grapheditormodel::node_is_not_abstract():
    assert not inspect.isabstract(grapheditormodel::Node)


def test_grapheditormodel::node_constructor_exists():
    assert callable(grapheditormodel::Node.__init__)


def test_grapheditormodel::node_constructor_args():
    sig = inspect.signature(grapheditormodel::Node.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_grapheditormodel::node_has_Name():
    assert hasattr(grapheditormodel::Node, "Name")
    descriptor = None
    for klass in grapheditormodel::Node.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_grapheditormodel::graph_is_not_abstract():
    assert not inspect.isabstract(grapheditormodel::Graph)


def test_grapheditormodel::graph_constructor_exists():
    assert callable(grapheditormodel::Graph.__init__)


def test_grapheditormodel::graph_constructor_args():
    sig = inspect.signature(grapheditormodel::Graph.__init__)
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
grapheditormodel::Edge_strategy = st.builds(
    grapheditormodel::Edge,
    Value=
        safe_text
)
grapheditormodel::Node_strategy = st.builds(
    grapheditormodel::Node,
    Name=
        safe_text
)
grapheditormodel::Graph_strategy = st.builds(
    grapheditormodel::Graph,
)

@given(instance=grapheditormodel::Edge_strategy)
@settings(max_examples=50)
def test_grapheditormodel::edge_instantiation(instance):
    assert isinstance(instance, grapheditormodel::Edge)

@given(instance=grapheditormodel::Edge_strategy)
def test_grapheditormodel::edge_Value_type(instance):
    assert isinstance(instance.Value, str)


@given(instance=grapheditormodel::Edge_strategy)
def test_grapheditormodel::edge_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=grapheditormodel::Node_strategy)
@settings(max_examples=50)
def test_grapheditormodel::node_instantiation(instance):
    assert isinstance(instance, grapheditormodel::Node)

@given(instance=grapheditormodel::Node_strategy)
def test_grapheditormodel::node_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=grapheditormodel::Node_strategy)
def test_grapheditormodel::node_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=grapheditormodel::Graph_strategy)
@settings(max_examples=50)
def test_grapheditormodel::graph_instantiation(instance):
    assert isinstance(instance, grapheditormodel::Graph)
