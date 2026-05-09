import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::Edge,
    graph::AbstractNamedObject,
    AbstractNamedObject,
    graph::Node,
    graph::Graph,
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



def test_graph::abstractnamedobject_is_not_abstract():
    assert not inspect.isabstract(graph::AbstractNamedObject)


def test_graph::abstractnamedobject_constructor_exists():
    assert callable(graph::AbstractNamedObject.__init__)


def test_graph::abstractnamedobject_constructor_args():
    sig = inspect.signature(graph::AbstractNamedObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::abstractnamedobject_has_name():
    assert hasattr(graph::AbstractNamedObject, "name")
    descriptor = None
    for klass in graph::AbstractNamedObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractnamedobject_is_not_abstract():
    assert not inspect.isabstract(AbstractNamedObject)


def test_abstractnamedobject_constructor_exists():
    assert callable(AbstractNamedObject.__init__)


def test_abstractnamedobject_constructor_args():
    sig = inspect.signature(AbstractNamedObject.__init__)
    params = list(sig.parameters.keys())



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
    params = list(sig.parameters.keys())



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(graph::Graph.__init__)
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
)
graph::AbstractNamedObject_strategy = st.builds(
    graph::AbstractNamedObject,
    name=
        safe_text
)
AbstractNamedObject_strategy = st.builds(
    AbstractNamedObject,
)
graph::Node_strategy = st.builds(
    graph::Node,
)
graph::Graph_strategy = st.builds(
    graph::Graph,
)

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::AbstractNamedObject_strategy)
@settings(max_examples=50)
def test_graph::abstractnamedobject_instantiation(instance):
    assert isinstance(instance, graph::AbstractNamedObject)

@given(instance=graph::AbstractNamedObject_strategy)
def test_graph::abstractnamedobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::AbstractNamedObject_strategy)
def test_graph::abstractnamedobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractNamedObject_strategy)
@settings(max_examples=50)
def test_abstractnamedobject_instantiation(instance):
    assert isinstance(instance, AbstractNamedObject)

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)
