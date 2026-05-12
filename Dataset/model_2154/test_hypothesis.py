import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    jgrapht_Vertex,
    jgrapht_Edge,
    jgrapht_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jgrapht_vertex_is_not_abstract():
    assert not inspect.isabstract(jgrapht_Vertex)


def test_jgrapht_vertex_constructor_exists():
    assert callable(jgrapht_Vertex.__init__)


def test_jgrapht_vertex_constructor_args():
    sig = inspect.signature(jgrapht_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jgrapht_vertex_has_name():
    assert hasattr(jgrapht_Vertex, "name")
    descriptor = None
    for klass in jgrapht_Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jgrapht_edge_is_not_abstract():
    assert not inspect.isabstract(jgrapht_Edge)


def test_jgrapht_edge_constructor_exists():
    assert callable(jgrapht_Edge.__init__)


def test_jgrapht_edge_constructor_args():
    sig = inspect.signature(jgrapht_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "relation" in params, "Missing parameter 'relation'"

def test_jgrapht_edge_has_relation():
    assert hasattr(jgrapht_Edge, "relation")
    descriptor = None
    for klass in jgrapht_Edge.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_jgrapht_graph_is_not_abstract():
    assert not inspect.isabstract(jgrapht_Graph)


def test_jgrapht_graph_constructor_exists():
    assert callable(jgrapht_Graph.__init__)


def test_jgrapht_graph_constructor_args():
    sig = inspect.signature(jgrapht_Graph.__init__)
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
jgrapht_Vertex_strategy = st.builds(
    jgrapht_Vertex,
    name=
        safe_text
)
jgrapht_Edge_strategy = st.builds(
    jgrapht_Edge,
    relation=
        safe_text
)
jgrapht_Graph_strategy = st.builds(
    jgrapht_Graph,
)

@given(instance=jgrapht_Vertex_strategy)
@settings(max_examples=50)
def test_jgrapht_vertex_instantiation(instance):
    assert isinstance(instance, jgrapht_Vertex)



@given(instance=jgrapht_Vertex_strategy)
def test_jgrapht_vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jgrapht_Edge_strategy)
@settings(max_examples=50)
def test_jgrapht_edge_instantiation(instance):
    assert isinstance(instance, jgrapht_Edge)



@given(instance=jgrapht_Edge_strategy)
def test_jgrapht_edge_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=jgrapht_Graph_strategy)
@settings(max_examples=50)
def test_jgrapht_graph_instantiation(instance):
    assert isinstance(instance, jgrapht_Graph)
