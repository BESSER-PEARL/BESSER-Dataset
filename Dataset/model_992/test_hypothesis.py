import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DAG::Edge,
    DAG::Node,
    DAG::Revision,
    DAG::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dag::edge_is_not_abstract():
    assert not inspect.isabstract(DAG::Edge)


def test_dag::edge_constructor_exists():
    assert callable(DAG::Edge.__init__)


def test_dag::edge_constructor_args():
    sig = inspect.signature(DAG::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_dag::edge_has_name():
    assert hasattr(DAG::Edge, "name")
    descriptor = None
    for klass in DAG::Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dag::edge_has_ID():
    assert hasattr(DAG::Edge, "ID")
    descriptor = None
    for klass in DAG::Edge.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_dag::node_is_not_abstract():
    assert not inspect.isabstract(DAG::Node)


def test_dag::node_constructor_exists():
    assert callable(DAG::Node.__init__)


def test_dag::node_constructor_args():
    sig = inspect.signature(DAG::Node.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "level" in params, "Missing parameter 'level'"

def test_dag::node_has_ID():
    assert hasattr(DAG::Node, "ID")
    descriptor = None
    for klass in DAG::Node.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_dag::node_has_name():
    assert hasattr(DAG::Node, "name")
    descriptor = None
    for klass in DAG::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dag::node_has_level():
    assert hasattr(DAG::Node, "level")
    descriptor = None
    for klass in DAG::Node.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_dag::revision_is_not_abstract():
    assert not inspect.isabstract(DAG::Revision)


def test_dag::revision_constructor_exists():
    assert callable(DAG::Revision.__init__)


def test_dag::revision_constructor_args():
    sig = inspect.signature(DAG::Revision.__init__)
    params = list(sig.parameters.keys())



def test_dag::graph_is_not_abstract():
    assert not inspect.isabstract(DAG::Graph)


def test_dag::graph_constructor_exists():
    assert callable(DAG::Graph.__init__)


def test_dag::graph_constructor_args():
    sig = inspect.signature(DAG::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dag::graph_has_name():
    assert hasattr(DAG::Graph, "name")
    descriptor = None
    for klass in DAG::Graph.__mro__:
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
DAG::Edge_strategy = st.builds(
    DAG::Edge,
    name=
        safe_text,
    ID=
        st.integers()
)
DAG::Node_strategy = st.builds(
    DAG::Node,
    ID=
        st.integers(),
    name=
        safe_text,
    level=
        st.integers()
)
DAG::Revision_strategy = st.builds(
    DAG::Revision,
)
DAG::Graph_strategy = st.builds(
    DAG::Graph,
    name=
        safe_text
)

@given(instance=DAG::Edge_strategy)
@settings(max_examples=50)
def test_dag::edge_instantiation(instance):
    assert isinstance(instance, DAG::Edge)

@given(instance=DAG::Edge_strategy)
def test_dag::edge_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DAG::Edge_strategy)
def test_dag::edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DAG::Edge_strategy)
def test_dag::edge_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=DAG::Edge_strategy)
def test_dag::edge_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DAG::Node_strategy)
@settings(max_examples=50)
def test_dag::node_instantiation(instance):
    assert isinstance(instance, DAG::Node)

@given(instance=DAG::Node_strategy)
def test_dag::node_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=DAG::Node_strategy)
def test_dag::node_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DAG::Node_strategy)
def test_dag::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DAG::Node_strategy)
def test_dag::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DAG::Node_strategy)
def test_dag::node_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=DAG::Node_strategy)
def test_dag::node_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=DAG::Revision_strategy)
@settings(max_examples=50)
def test_dag::revision_instantiation(instance):
    assert isinstance(instance, DAG::Revision)

@given(instance=DAG::Graph_strategy)
@settings(max_examples=50)
def test_dag::graph_instantiation(instance):
    assert isinstance(instance, DAG::Graph)

@given(instance=DAG::Graph_strategy)
def test_dag::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DAG::Graph_strategy)
def test_dag::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
