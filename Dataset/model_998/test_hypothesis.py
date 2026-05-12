import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Named,
    graph_Node,
    graph_Edge,
    graph_Graph,
    graph_Named,
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



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "derivedOrNotExists" in params, "Missing parameter 'derivedOrNotExists'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_graph_node_has_type():
    assert hasattr(graph_Node, "type")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graph_node_has_derivedOrNotExists():
    assert hasattr(graph_Node, "derivedOrNotExists")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "derivedOrNotExists" in klass.__dict__:
            descriptor = klass.__dict__["derivedOrNotExists"]
            break
    assert isinstance(descriptor, property)

def test_graph_node_has_uri():
    assert hasattr(graph_Node, "uri")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "pathDiscoveredByHeuristic" in params, "Missing parameter 'pathDiscoveredByHeuristic'"
    assert "exact" in params, "Missing parameter 'exact'"

def test_graph_edge_has_pathDiscoveredByHeuristic():
    assert hasattr(graph_Edge, "pathDiscoveredByHeuristic")
    descriptor = None
    for klass in graph_Edge.__mro__:
        if "pathDiscoveredByHeuristic" in klass.__dict__:
            descriptor = klass.__dict__["pathDiscoveredByHeuristic"]
            break
    assert isinstance(descriptor, property)

def test_graph_edge_has_exact():
    assert hasattr(graph_Edge, "exact")
    descriptor = None
    for klass in graph_Edge.__mro__:
        if "exact" in klass.__dict__:
            descriptor = klass.__dict__["exact"]
            break
    assert isinstance(descriptor, property)



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"

def test_graph_graph_has_owner():
    assert hasattr(graph_Graph, "owner")
    descriptor = None
    for klass in graph_Graph.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)



def test_graph_named_is_not_abstract():
    assert not inspect.isabstract(graph_Named)


def test_graph_named_constructor_exists():
    assert callable(graph_Named.__init__)


def test_graph_named_constructor_args():
    sig = inspect.signature(graph_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_named_has_name():
    assert hasattr(graph_Named, "name")
    descriptor = None
    for klass in graph_Named.__mro__:
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
graph_Node_strategy = st.builds(
    graph_Node,
    type=
        safe_text,
    derivedOrNotExists=
        st.booleans(),
    uri=
        safe_text
)
graph_Edge_strategy = st.builds(
    graph_Edge,
    pathDiscoveredByHeuristic=
        safe_text,
    exact=
        st.booleans()
)
graph_Graph_strategy = st.builds(
    graph_Graph,
    owner=
        safe_text
)
graph_Named_strategy = st.builds(
    graph_Named,
    name=
        safe_text
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, graph_Node)



@given(instance=graph_Node_strategy)
def test_graph_node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=graph_Node_strategy)
def test_graph_node_derivedOrNotExists_setter(instance):
    original = instance.derivedOrNotExists
    instance.derivedOrNotExists = original
    assert instance.derivedOrNotExists == original



@given(instance=graph_Node_strategy)
def test_graph_node_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)



@given(instance=graph_Edge_strategy)
def test_graph_edge_pathDiscoveredByHeuristic_setter(instance):
    original = instance.pathDiscoveredByHeuristic
    instance.pathDiscoveredByHeuristic = original
    assert instance.pathDiscoveredByHeuristic == original



@given(instance=graph_Edge_strategy)
def test_graph_edge_exact_setter(instance):
    original = instance.exact
    instance.exact = original
    assert instance.exact == original

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)



@given(instance=graph_Graph_strategy)
def test_graph_graph_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original

@given(instance=graph_Named_strategy)
@settings(max_examples=50)
def test_graph_named_instantiation(instance):
    assert isinstance(instance, graph_Named)



@given(instance=graph_Named_strategy)
def test_graph_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
