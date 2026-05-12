import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    vml_Edge,
    vml_Node,
    vml_Graph,
    vml_Pie,
    vml_Diagram,
    vml_Model,
    vml_Slice,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vml_edge_is_not_abstract():
    assert not inspect.isabstract(vml_Edge)


def test_vml_edge_constructor_exists():
    assert callable(vml_Edge.__init__)


def test_vml_edge_constructor_args():
    sig = inspect.signature(vml_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "relation" in params, "Missing parameter 'relation'"

def test_vml_edge_has_relation():
    assert hasattr(vml_Edge, "relation")
    descriptor = None
    for klass in vml_Edge.__mro__:
        if "relation" in klass.__dict__:
            descriptor = klass.__dict__["relation"]
            break
    assert isinstance(descriptor, property)



def test_vml_node_is_not_abstract():
    assert not inspect.isabstract(vml_Node)


def test_vml_node_constructor_exists():
    assert callable(vml_Node.__init__)


def test_vml_node_constructor_args():
    sig = inspect.signature(vml_Node.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_vml_node_has_title():
    assert hasattr(vml_Node, "title")
    descriptor = None
    for klass in vml_Node.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_vml_graph_is_not_abstract():
    assert not inspect.isabstract(vml_Graph)


def test_vml_graph_constructor_exists():
    assert callable(vml_Graph.__init__)


def test_vml_graph_constructor_args():
    sig = inspect.signature(vml_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "title" in params, "Missing parameter 'title'"

def test_vml_graph_has_ID():
    assert hasattr(vml_Graph, "ID")
    descriptor = None
    for klass in vml_Graph.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_vml_graph_has_title():
    assert hasattr(vml_Graph, "title")
    descriptor = None
    for klass in vml_Graph.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_vml_pie_is_not_abstract():
    assert not inspect.isabstract(vml_Pie)


def test_vml_pie_constructor_exists():
    assert callable(vml_Pie.__init__)


def test_vml_pie_constructor_args():
    sig = inspect.signature(vml_Pie.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_vml_pie_has_title():
    assert hasattr(vml_Pie, "title")
    descriptor = None
    for klass in vml_Pie.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml_pie_has_ID():
    assert hasattr(vml_Pie, "ID")
    descriptor = None
    for klass in vml_Pie.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_vml_diagram_is_not_abstract():
    assert not inspect.isabstract(vml_Diagram)


def test_vml_diagram_constructor_exists():
    assert callable(vml_Diagram.__init__)


def test_vml_diagram_constructor_args():
    sig = inspect.signature(vml_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_vml_diagram_has_title():
    assert hasattr(vml_Diagram, "title")
    descriptor = None
    for klass in vml_Diagram.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_vml_model_is_not_abstract():
    assert not inspect.isabstract(vml_Model)


def test_vml_model_constructor_exists():
    assert callable(vml_Model.__init__)


def test_vml_model_constructor_args():
    sig = inspect.signature(vml_Model.__init__)
    params = list(sig.parameters.keys())



def test_vml_slice_is_not_abstract():
    assert not inspect.isabstract(vml_Slice)


def test_vml_slice_constructor_exists():
    assert callable(vml_Slice.__init__)


def test_vml_slice_constructor_args():
    sig = inspect.signature(vml_Slice.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "value" in params, "Missing parameter 'value'"

def test_vml_slice_has_title():
    assert hasattr(vml_Slice, "title")
    descriptor = None
    for klass in vml_Slice.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_vml_slice_has_value():
    assert hasattr(vml_Slice, "value")
    descriptor = None
    for klass in vml_Slice.__mro__:
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
vml_Edge_strategy = st.builds(
    vml_Edge,
    relation=
        safe_text
)
vml_Node_strategy = st.builds(
    vml_Node,
    title=
        safe_text
)
vml_Graph_strategy = st.builds(
    vml_Graph,
    ID=
        safe_text,
    title=
        safe_text
)
vml_Pie_strategy = st.builds(
    vml_Pie,
    title=
        safe_text,
    ID=
        safe_text
)
vml_Diagram_strategy = st.builds(
    vml_Diagram,
    title=
        safe_text
)
vml_Model_strategy = st.builds(
    vml_Model,
)
vml_Slice_strategy = st.builds(
    vml_Slice,
    title=
        safe_text,
    value=
        st.integers()
)

@given(instance=vml_Edge_strategy)
@settings(max_examples=50)
def test_vml_edge_instantiation(instance):
    assert isinstance(instance, vml_Edge)



@given(instance=vml_Edge_strategy)
def test_vml_edge_relation_setter(instance):
    original = instance.relation
    instance.relation = original
    assert instance.relation == original

@given(instance=vml_Node_strategy)
@settings(max_examples=50)
def test_vml_node_instantiation(instance):
    assert isinstance(instance, vml_Node)



@given(instance=vml_Node_strategy)
def test_vml_node_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml_Graph_strategy)
@settings(max_examples=50)
def test_vml_graph_instantiation(instance):
    assert isinstance(instance, vml_Graph)



@given(instance=vml_Graph_strategy)
def test_vml_graph_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=vml_Graph_strategy)
def test_vml_graph_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml_Pie_strategy)
@settings(max_examples=50)
def test_vml_pie_instantiation(instance):
    assert isinstance(instance, vml_Pie)



@given(instance=vml_Pie_strategy)
def test_vml_pie_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=vml_Pie_strategy)
def test_vml_pie_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=vml_Diagram_strategy)
@settings(max_examples=50)
def test_vml_diagram_instantiation(instance):
    assert isinstance(instance, vml_Diagram)



@given(instance=vml_Diagram_strategy)
def test_vml_diagram_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=vml_Model_strategy)
@settings(max_examples=50)
def test_vml_model_instantiation(instance):
    assert isinstance(instance, vml_Model)

@given(instance=vml_Slice_strategy)
@settings(max_examples=50)
def test_vml_slice_instantiation(instance):
    assert isinstance(instance, vml_Slice)



@given(instance=vml_Slice_strategy)
def test_vml_slice_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=vml_Slice_strategy)
def test_vml_slice_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
