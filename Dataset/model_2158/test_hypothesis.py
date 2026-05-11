import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pcg::Resource,
    pcg::Edge,
    pcg::Vertex,
    pcg::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pcg::resource_is_not_abstract():
    assert not inspect.isabstract(pcg::Resource)


def test_pcg::resource_constructor_exists():
    assert callable(pcg::Resource.__init__)


def test_pcg::resource_constructor_args():
    sig = inspect.signature(pcg::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_pcg::resource_has_title():
    assert hasattr(pcg::Resource, "title")
    descriptor = None
    for klass in pcg::Resource.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_pcg::resource_has_id():
    assert hasattr(pcg::Resource, "id")
    descriptor = None
    for klass in pcg::Resource.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pcg::edge_is_not_abstract():
    assert not inspect.isabstract(pcg::Edge)


def test_pcg::edge_constructor_exists():
    assert callable(pcg::Edge.__init__)


def test_pcg::edge_constructor_args():
    sig = inspect.signature(pcg::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_pcg::edge_has_kind():
    assert hasattr(pcg::Edge, "kind")
    descriptor = None
    for klass in pcg::Edge.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_pcg::vertex_is_not_abstract():
    assert not inspect.isabstract(pcg::Vertex)


def test_pcg::vertex_constructor_exists():
    assert callable(pcg::Vertex.__init__)


def test_pcg::vertex_constructor_args():
    sig = inspect.signature(pcg::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_pcg::graph_is_not_abstract():
    assert not inspect.isabstract(pcg::Graph)


def test_pcg::graph_constructor_exists():
    assert callable(pcg::Graph.__init__)


def test_pcg::graph_constructor_args():
    sig = inspect.signature(pcg::Graph.__init__)
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
pcg::Resource_strategy = st.builds(
    pcg::Resource,
    title=
        safe_text,
    id=
        safe_text
)
pcg::Edge_strategy = st.builds(
    pcg::Edge,
    kind=
        safe_text
)
pcg::Vertex_strategy = st.builds(
    pcg::Vertex,
)
pcg::Graph_strategy = st.builds(
    pcg::Graph,
)

@given(instance=pcg::Resource_strategy)
@settings(max_examples=50)
def test_pcg::resource_instantiation(instance):
    assert isinstance(instance, pcg::Resource)

@given(instance=pcg::Resource_strategy)
def test_pcg::resource_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=pcg::Resource_strategy)
def test_pcg::resource_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=pcg::Resource_strategy)
def test_pcg::resource_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=pcg::Resource_strategy)
def test_pcg::resource_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pcg::Edge_strategy)
@settings(max_examples=50)
def test_pcg::edge_instantiation(instance):
    assert isinstance(instance, pcg::Edge)

@given(instance=pcg::Edge_strategy)
def test_pcg::edge_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=pcg::Edge_strategy)
def test_pcg::edge_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=pcg::Vertex_strategy)
@settings(max_examples=50)
def test_pcg::vertex_instantiation(instance):
    assert isinstance(instance, pcg::Vertex)

@given(instance=pcg::Graph_strategy)
@settings(max_examples=50)
def test_pcg::graph_instantiation(instance):
    assert isinstance(instance, pcg::Graph)
