import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::Edge,
    graph::Node,
    graph::GraphModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_graph::edge_has_label():
    assert hasattr(graph::Edge, "label")
    descriptor = None
    for klass in graph::Edge.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_graph::node_has_value():
    assert hasattr(graph::Node, "value")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graph::graphmodel_is_not_abstract():
    assert not inspect.isabstract(graph::GraphModel)


def test_graph::graphmodel_constructor_exists():
    assert callable(graph::GraphModel.__init__)


def test_graph::graphmodel_constructor_args():
    sig = inspect.signature(graph::GraphModel.__init__)
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
graph::Edge_strategy = st.builds(
    graph::Edge,
    label=
        safe_text
)
graph::Node_strategy = st.builds(
    graph::Node,
    value=
        safe_text
)
graph::GraphModel_strategy = st.builds(
    graph::GraphModel,
)

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::Edge_strategy)
def test_graph::edge_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=graph::Edge_strategy)
def test_graph::edge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)

@given(instance=graph::Node_strategy)
def test_graph::node_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=graph::Node_strategy)
def test_graph::node_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graph::GraphModel_strategy)
@settings(max_examples=50)
def test_graph::graphmodel_instantiation(instance):
    assert isinstance(instance, graph::GraphModel)
