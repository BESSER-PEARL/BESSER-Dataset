import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    jgrapht::Vertex,
    jgrapht::Edge,
    jgrapht::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jgrapht::vertex_is_not_abstract():
    assert not inspect.isabstract(jgrapht::Vertex)


def test_jgrapht::vertex_constructor_exists():
    assert callable(jgrapht::Vertex.__init__)


def test_jgrapht::vertex_constructor_args():
    sig = inspect.signature(jgrapht::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jgrapht::vertex_has_name():
    assert hasattr(jgrapht::Vertex, "name")
    descriptor = None
    for klass in jgrapht::Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jgrapht::edge_is_not_abstract():
    assert not inspect.isabstract(jgrapht::Edge)


def test_jgrapht::edge_constructor_exists():
    assert callable(jgrapht::Edge.__init__)


def test_jgrapht::edge_constructor_args():
    sig = inspect.signature(jgrapht::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "relation" in params, "Missing parameter 'relation'"

def test_jgrapht::edge_has_relation():
    assert hasattr(jgrapht::Edge, "relation")
    descriptor = None
    for klass in jgrapht::Edge.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_jgrapht::graph_is_not_abstract():
    assert not inspect.isabstract(jgrapht::Graph)


def test_jgrapht::graph_constructor_exists():
    assert callable(jgrapht::Graph.__init__)


def test_jgrapht::graph_constructor_args():
    sig = inspect.signature(jgrapht::Graph.__init__)
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
jgrapht::Vertex_strategy = st.builds(
    jgrapht::Vertex,
    name=
        safe_text
)
jgrapht::Edge_strategy = st.builds(
    jgrapht::Edge,
    relation=
        safe_text
)
jgrapht::Graph_strategy = st.builds(
    jgrapht::Graph,
)

@given(instance=jgrapht::Vertex_strategy)
@settings(max_examples=50)
def test_jgrapht::vertex_instantiation(instance):
    assert isinstance(instance, jgrapht::Vertex)

@given(instance=jgrapht::Vertex_strategy)
def test_jgrapht::vertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jgrapht::Vertex_strategy)
def test_jgrapht::vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jgrapht::Edge_strategy)
@settings(max_examples=50)
def test_jgrapht::edge_instantiation(instance):
    assert isinstance(instance, jgrapht::Edge)

@given(instance=jgrapht::Edge_strategy)
def test_jgrapht::edge_relation_type(instance):
    assert isinstance(instance.relation, str)


@given(instance=jgrapht::Edge_strategy)
def test_jgrapht::edge_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=jgrapht::Graph_strategy)
@settings(max_examples=50)
def test_jgrapht::graph_instantiation(instance):
    assert isinstance(instance, jgrapht::Graph)
