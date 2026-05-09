import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mydsl::Node,
    mydsl::Edge,
    mydsl::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::node_is_not_abstract():
    assert not inspect.isabstract(mydsl::Node)


def test_mydsl::node_constructor_exists():
    assert callable(mydsl::Node.__init__)


def test_mydsl::node_constructor_args():
    sig = inspect.signature(mydsl::Node.__init__)
    params = list(sig.parameters.keys())
    assert "isInvisible" in params, "Missing parameter 'isInvisible'"
    assert "content" in params, "Missing parameter 'content'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::node_has_isInvisible():
    assert hasattr(mydsl::Node, "isInvisible")
    descriptor = None
    for klass in mydsl::Node.__mro__:
        if "isInvisible" in klass.__dict__:
            descriptor = klass.__dict__["isInvisible"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::node_has_content():
    assert hasattr(mydsl::Node, "content")
    descriptor = None
    for klass in mydsl::Node.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::node_has_name():
    assert hasattr(mydsl::Node, "name")
    descriptor = None
    for klass in mydsl::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::edge_is_not_abstract():
    assert not inspect.isabstract(mydsl::Edge)


def test_mydsl::edge_constructor_exists():
    assert callable(mydsl::Edge.__init__)


def test_mydsl::edge_constructor_args():
    sig = inspect.signature(mydsl::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "parsed_target" in params, "Missing parameter 'parsed_target'"
    assert "label" in params, "Missing parameter 'label'"
    assert "parsed_source" in params, "Missing parameter 'parsed_source'"

def test_mydsl::edge_has_parsed_target():
    assert hasattr(mydsl::Edge, "parsed_target")
    descriptor = None
    for klass in mydsl::Edge.__mro__:
        if "parsed_target" in klass.__dict__:
            descriptor = klass.__dict__["parsed_target"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::edge_has_label():
    assert hasattr(mydsl::Edge, "label")
    descriptor = None
    for klass in mydsl::Edge.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::edge_has_parsed_source():
    assert hasattr(mydsl::Edge, "parsed_source")
    descriptor = None
    for klass in mydsl::Edge.__mro__:
        if "parsed_source" in klass.__dict__:
            descriptor = klass.__dict__["parsed_source"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::graph_is_not_abstract():
    assert not inspect.isabstract(mydsl::Graph)


def test_mydsl::graph_constructor_exists():
    assert callable(mydsl::Graph.__init__)


def test_mydsl::graph_constructor_args():
    sig = inspect.signature(mydsl::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::graph_has_name():
    assert hasattr(mydsl::Graph, "name")
    descriptor = None
    for klass in mydsl::Graph.__mro__:
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
mydsl::Node_strategy = st.builds(
    mydsl::Node,
    isInvisible=
        st.booleans(),
    content=
        safe_text,
    name=
        safe_text
)
mydsl::Edge_strategy = st.builds(
    mydsl::Edge,
    parsed_target=
        safe_text,
    label=
        safe_text,
    parsed_source=
        safe_text
)
mydsl::Graph_strategy = st.builds(
    mydsl::Graph,
    name=
        safe_text
)

@given(instance=mydsl::Node_strategy)
@settings(max_examples=50)
def test_mydsl::node_instantiation(instance):
    assert isinstance(instance, mydsl::Node)

@given(instance=mydsl::Node_strategy)
def test_mydsl::node_isInvisible_type(instance):
    assert isinstance(instance.isInvisible, bool)


@given(instance=mydsl::Node_strategy)
def test_mydsl::node_isInvisible_setter(instance):
    original = instance.isInvisible
    instance.isInvisible = original
    assert instance.isInvisible == original

@given(instance=mydsl::Node_strategy)
def test_mydsl::node_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=mydsl::Node_strategy)
def test_mydsl::node_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=mydsl::Node_strategy)
def test_mydsl::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mydsl::Node_strategy)
def test_mydsl::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mydsl::Edge_strategy)
@settings(max_examples=50)
def test_mydsl::edge_instantiation(instance):
    assert isinstance(instance, mydsl::Edge)

@given(instance=mydsl::Edge_strategy)
def test_mydsl::edge_parsed_target_type(instance):
    assert isinstance(instance.parsed_target, str)


@given(instance=mydsl::Edge_strategy)
def test_mydsl::edge_parsed_target_setter(instance):
    original = instance.parsed_target
    instance.parsed_target = original
    assert instance.parsed_target == original

@given(instance=mydsl::Edge_strategy)
def test_mydsl::edge_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=mydsl::Edge_strategy)
def test_mydsl::edge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=mydsl::Edge_strategy)
def test_mydsl::edge_parsed_source_type(instance):
    assert isinstance(instance.parsed_source, str)


@given(instance=mydsl::Edge_strategy)
def test_mydsl::edge_parsed_source_setter(instance):
    original = instance.parsed_source
    instance.parsed_source = original
    assert instance.parsed_source == original

@given(instance=mydsl::Graph_strategy)
@settings(max_examples=50)
def test_mydsl::graph_instantiation(instance):
    assert isinstance(instance, mydsl::Graph)

@given(instance=mydsl::Graph_strategy)
def test_mydsl::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mydsl::Graph_strategy)
def test_mydsl::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
