import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_Mark,
    graph_Edge,
    graph_Node,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_mark_is_not_abstract():
    assert not inspect.isabstract(graph_Mark)


def test_graph_mark_constructor_exists():
    assert callable(graph_Mark.__init__)


def test_graph_mark_constructor_args():
    sig = inspect.signature(graph_Mark.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_graph_mark_has_time():
    assert hasattr(graph_Mark, "time")
    descriptor = None
    for klass in graph_Mark.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_edge_has_name():
    assert hasattr(graph_Edge, "name")
    descriptor = None
    for klass in graph_Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_node_has_name():
    assert hasattr(graph_Node, "name")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_graph_has_name():
    assert hasattr(graph_Graph, "name")
    descriptor = None
    for klass in graph_Graph.__mro__:
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
graph_Mark_strategy = st.builds(
    graph_Mark,
    time=
        safe_text
)
graph_Edge_strategy = st.builds(
    graph_Edge,
    name=
        safe_text
)
graph_Node_strategy = st.builds(
    graph_Node,
    name=
        safe_text
)
graph_Graph_strategy = st.builds(
    graph_Graph,
    name=
        safe_text
)

@given(instance=graph_Mark_strategy)
@settings(max_examples=50)
def test_graph_mark_instantiation(instance):
    assert isinstance(instance, graph_Mark)



@given(instance=graph_Mark_strategy)
def test_graph_mark_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)



@given(instance=graph_Edge_strategy)
def test_graph_edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, graph_Node)



@given(instance=graph_Node_strategy)
def test_graph_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)



@given(instance=graph_Graph_strategy)
def test_graph_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
