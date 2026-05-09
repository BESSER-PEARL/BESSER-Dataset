import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Named,
    graph::Node,
    graph::Edge,
    graph::Graph,
    graph::Named,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "derivedOrNotExists" in params, "Missing parameter 'derivedOrNotExists'"
    assert "type" in params, "Missing parameter 'type'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_graph::node_has_derivedOrNotExists():
    assert hasattr(graph::Node, "derivedOrNotExists")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "derivedOrNotExists" in klass.__dict__:
            descriptor = klass.__dict__["derivedOrNotExists"]
            break
    assert isinstance(descriptor, property)

def test_graph::node_has_type():
    assert hasattr(graph::Node, "type")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graph::node_has_uri():
    assert hasattr(graph::Node, "uri")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "exact" in params, "Missing parameter 'exact'"
    assert "pathDiscoveredByHeuristic" in params, "Missing parameter 'pathDiscoveredByHeuristic'"

def test_graph::edge_has_exact():
    assert hasattr(graph::Edge, "exact")
    descriptor = None
    for klass in graph::Edge.__mro__:
        if "exact" in klass.__dict__:
            descriptor = klass.__dict__["exact"]
            break
    assert isinstance(descriptor, property)

def test_graph::edge_has_pathDiscoveredByHeuristic():
    assert hasattr(graph::Edge, "pathDiscoveredByHeuristic")
    descriptor = None
    for klass in graph::Edge.__mro__:
        if "pathDiscoveredByHeuristic" in klass.__dict__:
            descriptor = klass.__dict__["pathDiscoveredByHeuristic"]
            break
    assert isinstance(descriptor, property)



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(graph::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"

def test_graph::graph_has_owner():
    assert hasattr(graph::Graph, "owner")
    descriptor = None
    for klass in graph::Graph.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)



def test_graph::named_is_not_abstract():
    assert not inspect.isabstract(graph::Named)


def test_graph::named_constructor_exists():
    assert callable(graph::Named.__init__)


def test_graph::named_constructor_args():
    sig = inspect.signature(graph::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::named_has_name():
    assert hasattr(graph::Named, "name")
    descriptor = None
    for klass in graph::Named.__mro__:
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
Named_strategy = st.builds(
    Named,
)
graph::Node_strategy = st.builds(
    graph::Node,
    derivedOrNotExists=
        st.booleans(),
    type=
        safe_text,
    uri=
        safe_text
)
graph::Edge_strategy = st.builds(
    graph::Edge,
    exact=
        st.booleans(),
    pathDiscoveredByHeuristic=
        safe_text
)
graph::Graph_strategy = st.builds(
    graph::Graph,
    owner=
        safe_text
)
graph::Named_strategy = st.builds(
    graph::Named,
    name=
        safe_text
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)

@given(instance=graph::Node_strategy)
def test_graph::node_derivedOrNotExists_type(instance):
    assert isinstance(instance.derivedOrNotExists, bool)


@given(instance=graph::Node_strategy)
def test_graph::node_derivedOrNotExists_setter(instance):
    original = instance.derivedOrNotExists
    instance.derivedOrNotExists = original
    assert instance.derivedOrNotExists == original

@given(instance=graph::Node_strategy)
def test_graph::node_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graph::Node_strategy)
def test_graph::node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graph::Node_strategy)
def test_graph::node_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=graph::Node_strategy)
def test_graph::node_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::Edge_strategy)
def test_graph::edge_exact_type(instance):
    assert isinstance(instance.exact, bool)


@given(instance=graph::Edge_strategy)
def test_graph::edge_exact_setter(instance):
    original = instance.exact
    instance.exact = original
    assert instance.exact == original

@given(instance=graph::Edge_strategy)
def test_graph::edge_pathDiscoveredByHeuristic_type(instance):
    assert isinstance(instance.pathDiscoveredByHeuristic, str)


@given(instance=graph::Edge_strategy)
def test_graph::edge_pathDiscoveredByHeuristic_setter(instance):
    original = instance.pathDiscoveredByHeuristic
    instance.pathDiscoveredByHeuristic = original
    assert instance.pathDiscoveredByHeuristic == original

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)

@given(instance=graph::Graph_strategy)
def test_graph::graph_owner_type(instance):
    assert isinstance(instance.owner, str)


@given(instance=graph::Graph_strategy)
def test_graph::graph_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=graph::Named_strategy)
@settings(max_examples=50)
def test_graph::named_instantiation(instance):
    assert isinstance(instance, graph::Named)

@given(instance=graph::Named_strategy)
def test_graph::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Named_strategy)
def test_graph::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
