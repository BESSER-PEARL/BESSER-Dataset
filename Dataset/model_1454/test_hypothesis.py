import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mydsl_Node,
    mydsl_Edge,
    mydsl_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_node_is_not_abstract():
    assert not inspect.isabstract(mydsl_Node)


def test_mydsl_node_constructor_exists():
    assert callable(mydsl_Node.__init__)


def test_mydsl_node_constructor_args():
    sig = inspect.signature(mydsl_Node.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isInvisible" in params, "Missing parameter 'isInvisible'"

def test_mydsl_node_has_content():
    assert hasattr(mydsl_Node, "content")
    descriptor = None
    for klass in mydsl_Node.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_node_has_name():
    assert hasattr(mydsl_Node, "name")
    descriptor = None
    for klass in mydsl_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_node_has_isInvisible():
    assert hasattr(mydsl_Node, "isInvisible")
    descriptor = None
    for klass in mydsl_Node.__mro__:
        if "isInvisible" in klass.__dict__:
            descriptor = klass.__dict__["isInvisible"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_edge_is_not_abstract():
    assert not inspect.isabstract(mydsl_Edge)


def test_mydsl_edge_constructor_exists():
    assert callable(mydsl_Edge.__init__)


def test_mydsl_edge_constructor_args():
    sig = inspect.signature(mydsl_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "parsed_target" in params, "Missing parameter 'parsed_target'"
    assert "parsed_source" in params, "Missing parameter 'parsed_source'"
    assert "label" in params, "Missing parameter 'label'"

def test_mydsl_edge_has_parsed_target():
    assert hasattr(mydsl_Edge, "parsed_target")
    descriptor = None
    for klass in mydsl_Edge.__mro__:
        if "parsed_target" in klass.__dict__:
            descriptor = klass.__dict__["parsed_target"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_edge_has_parsed_source():
    assert hasattr(mydsl_Edge, "parsed_source")
    descriptor = None
    for klass in mydsl_Edge.__mro__:
        if "parsed_source" in klass.__dict__:
            descriptor = klass.__dict__["parsed_source"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_edge_has_label():
    assert hasattr(mydsl_Edge, "label")
    descriptor = None
    for klass in mydsl_Edge.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_graph_is_not_abstract():
    assert not inspect.isabstract(mydsl_Graph)


def test_mydsl_graph_constructor_exists():
    assert callable(mydsl_Graph.__init__)


def test_mydsl_graph_constructor_args():
    sig = inspect.signature(mydsl_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_graph_has_name():
    assert hasattr(mydsl_Graph, "name")
    descriptor = None
    for klass in mydsl_Graph.__mro__:
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
mydsl_Node_strategy = st.builds(
    mydsl_Node,
    content=
        safe_text,
    name=
        safe_text,
    isInvisible=
        st.booleans()
)
mydsl_Edge_strategy = st.builds(
    mydsl_Edge,
    parsed_target=
        safe_text,
    parsed_source=
        safe_text,
    label=
        safe_text
)
mydsl_Graph_strategy = st.builds(
    mydsl_Graph,
    name=
        safe_text
)

@given(instance=mydsl_Node_strategy)
@settings(max_examples=50)
def test_mydsl_node_instantiation(instance):
    assert isinstance(instance, mydsl_Node)



@given(instance=mydsl_Node_strategy)
def test_mydsl_node_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=mydsl_Node_strategy)
def test_mydsl_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mydsl_Node_strategy)
def test_mydsl_node_isInvisible_setter(instance):
    original = instance.isInvisible
    instance.isInvisible = original
    assert instance.isInvisible == original

@given(instance=mydsl_Edge_strategy)
@settings(max_examples=50)
def test_mydsl_edge_instantiation(instance):
    assert isinstance(instance, mydsl_Edge)



@given(instance=mydsl_Edge_strategy)
def test_mydsl_edge_parsed_target_setter(instance):
    original = instance.parsed_target
    instance.parsed_target = original
    assert instance.parsed_target == original



@given(instance=mydsl_Edge_strategy)
def test_mydsl_edge_parsed_source_setter(instance):
    original = instance.parsed_source
    instance.parsed_source = original
    assert instance.parsed_source == original



@given(instance=mydsl_Edge_strategy)
def test_mydsl_edge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=mydsl_Graph_strategy)
@settings(max_examples=50)
def test_mydsl_graph_instantiation(instance):
    assert isinstance(instance, mydsl_Graph)



@given(instance=mydsl_Graph_strategy)
def test_mydsl_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
