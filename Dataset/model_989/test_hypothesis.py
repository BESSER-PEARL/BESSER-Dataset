import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::Mark,
    graph::Edge,
    graph::Node,
    graph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::mark_is_not_abstract():
    assert not inspect.isabstract(graph::Mark)


def test_graph::mark_constructor_exists():
    assert callable(graph::Mark.__init__)


def test_graph::mark_constructor_args():
    sig = inspect.signature(graph::Mark.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_graph::mark_has_time():
    assert hasattr(graph::Mark, "time")
    descriptor = None
    for klass in graph::Mark.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::edge_has_name():
    assert hasattr(graph::Edge, "name")
    descriptor = None
    for klass in graph::Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::node_has_name():
    assert hasattr(graph::Node, "name")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(graph::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::graph_has_name():
    assert hasattr(graph::Graph, "name")
    descriptor = None
    for klass in graph::Graph.__mro__:
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
graph::Mark_strategy = st.builds(
    graph::Mark,
    time=
        safe_text
)
graph::Edge_strategy = st.builds(
    graph::Edge,
    name=
        safe_text
)
graph::Node_strategy = st.builds(
    graph::Node,
    name=
        safe_text
)
graph::Graph_strategy = st.builds(
    graph::Graph,
    name=
        safe_text
)

@given(instance=graph::Mark_strategy)
@settings(max_examples=50)
def test_graph::mark_instantiation(instance):
    assert isinstance(instance, graph::Mark)

@given(instance=graph::Mark_strategy)
def test_graph::mark_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=graph::Mark_strategy)
def test_graph::mark_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::Edge_strategy)
def test_graph::edge_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Edge_strategy)
def test_graph::edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)

@given(instance=graph::Node_strategy)
def test_graph::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Node_strategy)
def test_graph::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)

@given(instance=graph::Graph_strategy)
def test_graph::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Graph_strategy)
def test_graph::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
