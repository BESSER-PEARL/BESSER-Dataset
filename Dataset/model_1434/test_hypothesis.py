import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GraphMM_Edge,
    GraphMM_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graphmm_edge_is_not_abstract():
    assert not inspect.isabstract(GraphMM_Edge)


def test_graphmm_edge_constructor_exists():
    assert callable(GraphMM_Edge.__init__)


def test_graphmm_edge_constructor_args():
    sig = inspect.signature(GraphMM_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graphmm_node_is_not_abstract():
    assert not inspect.isabstract(GraphMM_Node)


def test_graphmm_node_constructor_exists():
    assert callable(GraphMM_Node.__init__)


def test_graphmm_node_constructor_args():
    sig = inspect.signature(GraphMM_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"
    assert "type" in params, "Missing parameter 'type'"

def test_graphmm_node_has_name():
    assert hasattr(GraphMM_Node, "name")
    descriptor = None
    for klass in GraphMM_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphmm_node_has_size():
    assert hasattr(GraphMM_Node, "size")
    descriptor = None
    for klass in GraphMM_Node.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_graphmm_node_has_type():
    assert hasattr(GraphMM_Node, "type")
    descriptor = None
    for klass in GraphMM_Node.__mro__:
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
GraphMM_Edge_strategy = st.builds(
    GraphMM_Edge,
)
GraphMM_Node_strategy = st.builds(
    GraphMM_Node,
    name=
        safe_text,
    size=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text
)

@given(instance=GraphMM_Edge_strategy)
@settings(max_examples=50)
def test_graphmm_edge_instantiation(instance):
    assert isinstance(instance, GraphMM_Edge)

@given(instance=GraphMM_Node_strategy)
@settings(max_examples=50)
def test_graphmm_node_instantiation(instance):
    assert isinstance(instance, GraphMM_Node)



@given(instance=GraphMM_Node_strategy)
def test_graphmm_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=GraphMM_Node_strategy)
def test_graphmm_node_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=GraphMM_Node_strategy)
def test_graphmm_node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
