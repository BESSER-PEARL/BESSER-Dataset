import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pcg_Resource,
    pcg_Edge,
    pcg_Vertex,
    pcg_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pcg_resource_is_not_abstract():
    assert not inspect.isabstract(pcg_Resource)


def test_pcg_resource_constructor_exists():
    assert callable(pcg_Resource.__init__)


def test_pcg_resource_constructor_args():
    sig = inspect.signature(pcg_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_pcg_resource_has_id():
    assert hasattr(pcg_Resource, "id")
    descriptor = None
    for klass in pcg_Resource.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pcg_resource_has_title():
    assert hasattr(pcg_Resource, "title")
    descriptor = None
    for klass in pcg_Resource.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_pcg_edge_is_not_abstract():
    assert not inspect.isabstract(pcg_Edge)


def test_pcg_edge_constructor_exists():
    assert callable(pcg_Edge.__init__)


def test_pcg_edge_constructor_args():
    sig = inspect.signature(pcg_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_pcg_edge_has_kind():
    assert hasattr(pcg_Edge, "kind")
    descriptor = None
    for klass in pcg_Edge.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_pcg_vertex_is_not_abstract():
    assert not inspect.isabstract(pcg_Vertex)


def test_pcg_vertex_constructor_exists():
    assert callable(pcg_Vertex.__init__)


def test_pcg_vertex_constructor_args():
    sig = inspect.signature(pcg_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_pcg_graph_is_not_abstract():
    assert not inspect.isabstract(pcg_Graph)


def test_pcg_graph_constructor_exists():
    assert callable(pcg_Graph.__init__)


def test_pcg_graph_constructor_args():
    sig = inspect.signature(pcg_Graph.__init__)
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
pcg_Resource_strategy = st.builds(
    pcg_Resource,
    id=
        safe_text,
    title=
        safe_text
)
pcg_Edge_strategy = st.builds(
    pcg_Edge,
    kind=
        safe_text
)
pcg_Vertex_strategy = st.builds(
    pcg_Vertex,
)
pcg_Graph_strategy = st.builds(
    pcg_Graph,
)

@given(instance=pcg_Resource_strategy)
@settings(max_examples=50)
def test_pcg_resource_instantiation(instance):
    assert isinstance(instance, pcg_Resource)



@given(instance=pcg_Resource_strategy)
def test_pcg_resource_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=pcg_Resource_strategy)
def test_pcg_resource_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=pcg_Edge_strategy)
@settings(max_examples=50)
def test_pcg_edge_instantiation(instance):
    assert isinstance(instance, pcg_Edge)



@given(instance=pcg_Edge_strategy)
def test_pcg_edge_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=pcg_Vertex_strategy)
@settings(max_examples=50)
def test_pcg_vertex_instantiation(instance):
    assert isinstance(instance, pcg_Vertex)

@given(instance=pcg_Graph_strategy)
@settings(max_examples=50)
def test_pcg_graph_instantiation(instance):
    assert isinstance(instance, pcg_Graph)
