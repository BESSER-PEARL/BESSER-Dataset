import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    vml::Edge,
    vml::Node,
    vml::Graph,
    vml::Pie,
    vml::Diagram,
    vml::Model,
    vml::Slice,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vml::edge_is_not_abstract():
    assert not inspect.isabstract(vml::Edge)


def test_vml::edge_constructor_exists():
    assert callable(vml::Edge.__init__)


def test_vml::edge_constructor_args():
    sig = inspect.signature(vml::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "relation" in params, "Missing parameter 'relation'"

def test_vml::edge_has_relation():
    assert hasattr(vml::Edge, "relation")
    descriptor = None
    for klass in vml::Edge.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_vml::node_is_not_abstract():
    assert not inspect.isabstract(vml::Node)


def test_vml::node_constructor_exists():
    assert callable(vml::Node.__init__)


def test_vml::node_constructor_args():
    sig = inspect.signature(vml::Node.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_vml::node_has_title():
    assert hasattr(vml::Node, "title")
    descriptor = None
    for klass in vml::Node.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_vml::graph_is_not_abstract():
    assert not inspect.isabstract(vml::Graph)


def test_vml::graph_constructor_exists():
    assert callable(vml::Graph.__init__)


def test_vml::graph_constructor_args():
    sig = inspect.signature(vml::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "title" in params, "Missing parameter 'title'"

def test_vml::graph_has_ID():
    assert hasattr(vml::Graph, "ID")
    descriptor = None
    for klass in vml::Graph.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_vml::graph_has_title():
    assert hasattr(vml::Graph, "title")
    descriptor = None
    for klass in vml::Graph.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_vml::pie_is_not_abstract():
    assert not inspect.isabstract(vml::Pie)


def test_vml::pie_constructor_exists():
    assert callable(vml::Pie.__init__)


def test_vml::pie_constructor_args():
    sig = inspect.signature(vml::Pie.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_vml::pie_has_title():
    assert hasattr(vml::Pie, "title")
    descriptor = None
    for klass in vml::Pie.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml::pie_has_ID():
    assert hasattr(vml::Pie, "ID")
    descriptor = None
    for klass in vml::Pie.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_vml::diagram_is_not_abstract():
    assert not inspect.isabstract(vml::Diagram)


def test_vml::diagram_constructor_exists():
    assert callable(vml::Diagram.__init__)


def test_vml::diagram_constructor_args():
    sig = inspect.signature(vml::Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_vml::diagram_has_title():
    assert hasattr(vml::Diagram, "title")
    descriptor = None
    for klass in vml::Diagram.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_vml::model_is_not_abstract():
    assert not inspect.isabstract(vml::Model)


def test_vml::model_constructor_exists():
    assert callable(vml::Model.__init__)


def test_vml::model_constructor_args():
    sig = inspect.signature(vml::Model.__init__)
    params = list(sig.parameters.keys())



def test_vml::slice_is_not_abstract():
    assert not inspect.isabstract(vml::Slice)


def test_vml::slice_constructor_exists():
    assert callable(vml::Slice.__init__)


def test_vml::slice_constructor_args():
    sig = inspect.signature(vml::Slice.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "value" in params, "Missing parameter 'value'"

def test_vml::slice_has_title():
    assert hasattr(vml::Slice, "title")
    descriptor = None
    for klass in vml::Slice.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml::slice_has_value():
    assert hasattr(vml::Slice, "value")
    descriptor = None
    for klass in vml::Slice.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
vml::Edge_strategy = st.builds(
    vml::Edge,
    relation=
        safe_text
)
vml::Node_strategy = st.builds(
    vml::Node,
    title=
        safe_text
)
vml::Graph_strategy = st.builds(
    vml::Graph,
    ID=
        safe_text,
    title=
        safe_text
)
vml::Pie_strategy = st.builds(
    vml::Pie,
    title=
        safe_text,
    ID=
        safe_text
)
vml::Diagram_strategy = st.builds(
    vml::Diagram,
    title=
        safe_text
)
vml::Model_strategy = st.builds(
    vml::Model,
)
vml::Slice_strategy = st.builds(
    vml::Slice,
    title=
        safe_text,
    value=
        st.integers()
)

@given(instance=vml::Edge_strategy)
@settings(max_examples=50)
def test_vml::edge_instantiation(instance):
    assert isinstance(instance, vml::Edge)

@given(instance=vml::Edge_strategy)
def test_vml::edge_relation_type(instance):
    assert isinstance(instance.relation, str)


@given(instance=vml::Edge_strategy)
def test_vml::edge_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=vml::Node_strategy)
@settings(max_examples=50)
def test_vml::node_instantiation(instance):
    assert isinstance(instance, vml::Node)

@given(instance=vml::Node_strategy)
def test_vml::node_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Node_strategy)
def test_vml::node_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml::Graph_strategy)
@settings(max_examples=50)
def test_vml::graph_instantiation(instance):
    assert isinstance(instance, vml::Graph)

@given(instance=vml::Graph_strategy)
def test_vml::graph_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=vml::Graph_strategy)
def test_vml::graph_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=vml::Graph_strategy)
def test_vml::graph_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Graph_strategy)
def test_vml::graph_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml::Pie_strategy)
@settings(max_examples=50)
def test_vml::pie_instantiation(instance):
    assert isinstance(instance, vml::Pie)

@given(instance=vml::Pie_strategy)
def test_vml::pie_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Pie_strategy)
def test_vml::pie_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml::Pie_strategy)
def test_vml::pie_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=vml::Pie_strategy)
def test_vml::pie_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=vml::Diagram_strategy)
@settings(max_examples=50)
def test_vml::diagram_instantiation(instance):
    assert isinstance(instance, vml::Diagram)

@given(instance=vml::Diagram_strategy)
def test_vml::diagram_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Diagram_strategy)
def test_vml::diagram_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml::Model_strategy)
@settings(max_examples=50)
def test_vml::model_instantiation(instance):
    assert isinstance(instance, vml::Model)

@given(instance=vml::Slice_strategy)
@settings(max_examples=50)
def test_vml::slice_instantiation(instance):
    assert isinstance(instance, vml::Slice)

@given(instance=vml::Slice_strategy)
def test_vml::slice_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=vml::Slice_strategy)
def test_vml::slice_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml::Slice_strategy)
def test_vml::slice_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=vml::Slice_strategy)
def test_vml::slice_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
