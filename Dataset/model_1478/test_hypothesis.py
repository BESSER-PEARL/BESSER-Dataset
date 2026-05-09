import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::HasName,
    graph::Root,
    graph::Edge,
    HasName,
    graph::SubNode,
    graph::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::hasname_is_not_abstract():
    assert not inspect.isabstract(graph::HasName)


def test_graph::hasname_constructor_exists():
    assert callable(graph::HasName.__init__)


def test_graph::hasname_constructor_args():
    sig = inspect.signature(graph::HasName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::hasname_has_name():
    assert hasattr(graph::HasName, "name")
    descriptor = None
    for klass in graph::HasName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::root_is_not_abstract():
    assert not inspect.isabstract(graph::Root)


def test_graph::root_constructor_exists():
    assert callable(graph::Root.__init__)


def test_graph::root_constructor_args():
    sig = inspect.signature(graph::Root.__init__)
    params = list(sig.parameters.keys())



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_hasname_is_not_abstract():
    assert not inspect.isabstract(HasName)


def test_hasname_constructor_exists():
    assert callable(HasName.__init__)


def test_hasname_constructor_args():
    sig = inspect.signature(HasName.__init__)
    params = list(sig.parameters.keys())



def test_graph::subnode_is_not_abstract():
    assert not inspect.isabstract(graph::SubNode)


def test_graph::subnode_constructor_exists():
    assert callable(graph::SubNode.__init__)


def test_graph::subnode_constructor_args():
    sig = inspect.signature(graph::SubNode.__init__)
    params = list(sig.parameters.keys())



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
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
graph::HasName_strategy = st.builds(
    graph::HasName,
    name=
        safe_text
)
graph::Root_strategy = st.builds(
    graph::Root,
)
graph::Edge_strategy = st.builds(
    graph::Edge,
)
HasName_strategy = st.builds(
    HasName,
)
graph::SubNode_strategy = st.builds(
    graph::SubNode,
)
graph::Node_strategy = st.builds(
    graph::Node,
)

@given(instance=graph::HasName_strategy)
@settings(max_examples=50)
def test_graph::hasname_instantiation(instance):
    assert isinstance(instance, graph::HasName)

@given(instance=graph::HasName_strategy)
def test_graph::hasname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::HasName_strategy)
def test_graph::hasname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Root_strategy)
@settings(max_examples=50)
def test_graph::root_instantiation(instance):
    assert isinstance(instance, graph::Root)

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=HasName_strategy)
@settings(max_examples=50)
def test_hasname_instantiation(instance):
    assert isinstance(instance, HasName)

@given(instance=graph::SubNode_strategy)
@settings(max_examples=50)
def test_graph::subnode_instantiation(instance):
    assert isinstance(instance, graph::SubNode)

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)
