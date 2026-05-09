import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GraphMM::Edge,
    GraphMM::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graphmm::edge_is_not_abstract():
    assert not inspect.isabstract(GraphMM::Edge)


def test_graphmm::edge_constructor_exists():
    assert callable(GraphMM::Edge.__init__)


def test_graphmm::edge_constructor_args():
    sig = inspect.signature(GraphMM::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graphmm::node_is_not_abstract():
    assert not inspect.isabstract(GraphMM::Node)


def test_graphmm::node_constructor_exists():
    assert callable(GraphMM::Node.__init__)


def test_graphmm::node_constructor_args():
    sig = inspect.signature(GraphMM::Node.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_graphmm::node_has_size():
    assert hasattr(GraphMM::Node, "size")
    descriptor = None
    for klass in GraphMM::Node.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_graphmm::node_has_name():
    assert hasattr(GraphMM::Node, "name")
    descriptor = None
    for klass in GraphMM::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphmm::node_has_type():
    assert hasattr(GraphMM::Node, "type")
    descriptor = None
    for klass in GraphMM::Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
GraphMM::Edge_strategy = st.builds(
    GraphMM::Edge,
)
GraphMM::Node_strategy = st.builds(
    GraphMM::Node,
    size=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=GraphMM::Edge_strategy)
@settings(max_examples=50)
def test_graphmm::edge_instantiation(instance):
    assert isinstance(instance, GraphMM::Edge)

@given(instance=GraphMM::Node_strategy)
@settings(max_examples=50)
def test_graphmm::node_instantiation(instance):
    assert isinstance(instance, GraphMM::Node)

@given(instance=GraphMM::Node_strategy)
def test_graphmm::node_size_type(instance):
    assert isinstance(instance.size, float)


@given(instance=GraphMM::Node_strategy)
def test_graphmm::node_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=GraphMM::Node_strategy)
def test_graphmm::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=GraphMM::Node_strategy)
def test_graphmm::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphMM::Node_strategy)
def test_graphmm::node_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=GraphMM::Node_strategy)
def test_graphmm::node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
