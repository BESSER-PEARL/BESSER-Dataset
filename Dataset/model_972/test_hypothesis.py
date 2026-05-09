import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Typed,
    graph::Named,
    graph::Edge,
    graph::Node,
    Named,
    graph::Typed,
    graph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typed_is_not_abstract():
    assert not inspect.isabstract(Typed)


def test_typed_constructor_exists():
    assert callable(Typed.__init__)


def test_typed_constructor_args():
    sig = inspect.signature(Typed.__init__)
    params = list(sig.parameters.keys())



def test_graph::named_is_not_abstract():
    assert not inspect.isabstract(graph::Named)


def test_graph::named_constructor_exists():
    assert callable(graph::Named.__init__)


def test_graph::named_constructor_args():
    sig = inspect.signature(graph::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::named_has_name():
    assert hasattr(graph::Named, "name")
    descriptor = None
    for klass in graph::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_graph::typed_is_not_abstract():
    assert not inspect.isabstract(graph::Typed)


def test_graph::typed_constructor_exists():
    assert callable(graph::Typed.__init__)


def test_graph::typed_constructor_args():
    sig = inspect.signature(graph::Typed.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_graph::typed_has_type():
    assert hasattr(graph::Typed, "type")
    descriptor = None
    for klass in graph::Typed.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



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
Typed_strategy = st.builds(
    Typed,
)
graph::Named_strategy = st.builds(
    graph::Named,
    name=
        safe_text
)
graph::Edge_strategy = st.builds(
    graph::Edge,
)
graph::Node_strategy = st.builds(
    graph::Node,
)
Named_strategy = st.builds(
    Named,
)
graph::Typed_strategy = st.builds(
    graph::Typed,
    type=
        safe_text
)
graph::Graph_strategy = st.builds(
    graph::Graph,
)

@given(instance=Typed_strategy)
@settings(max_examples=50)
def test_typed_instantiation(instance):
    assert isinstance(instance, Typed)

@given(instance=graph::Named_strategy)
@settings(max_examples=50)
def test_graph::named_instantiation(instance):
    assert isinstance(instance, graph::Named)

@given(instance=graph::Named_strategy)
def test_graph::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Named_strategy)
def test_graph::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=graph::Typed_strategy)
@settings(max_examples=50)
def test_graph::typed_instantiation(instance):
    assert isinstance(instance, graph::Typed)

@given(instance=graph::Typed_strategy)
def test_graph::typed_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graph::Typed_strategy)
def test_graph::typed_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)
