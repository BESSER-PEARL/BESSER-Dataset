import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CST_Node,
    CST_Tree,
    Node,
    CST_TNode,
    CST_RNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cst_node_is_not_abstract():
    assert not inspect.isabstract(CST_Node)


def test_cst_node_constructor_exists():
    assert callable(CST_Node.__init__)


def test_cst_node_constructor_args():
    sig = inspect.signature(CST_Node.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_cst_node_has_kind():
    assert hasattr(CST_Node, "kind")
    descriptor = None
    for klass in CST_Node.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_cst_tree_is_not_abstract():
    assert not inspect.isabstract(CST_Tree)


def test_cst_tree_constructor_exists():
    assert callable(CST_Tree.__init__)


def test_cst_tree_constructor_args():
    sig = inspect.signature(CST_Tree.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_cst_tnode_is_not_abstract():
    assert not inspect.isabstract(CST_TNode)


def test_cst_tnode_constructor_exists():
    assert callable(CST_TNode.__init__)


def test_cst_tnode_constructor_args():
    sig = inspect.signature(CST_TNode.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cst_tnode_has_value():
    assert hasattr(CST_TNode, "value")
    descriptor = None
    for klass in CST_TNode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cst_rnode_is_not_abstract():
    assert not inspect.isabstract(CST_RNode)


def test_cst_rnode_constructor_exists():
    assert callable(CST_RNode.__init__)


def test_cst_rnode_constructor_args():
    sig = inspect.signature(CST_RNode.__init__)
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
CST_Node_strategy = st.builds(
    CST_Node,
    kind=
        safe_text
)
CST_Tree_strategy = st.builds(
    CST_Tree,
)
Node_strategy = st.builds(
    Node,
)
CST_TNode_strategy = st.builds(
    CST_TNode,
    value=
        safe_text
)
CST_RNode_strategy = st.builds(
    CST_RNode,
)

@given(instance=CST_Node_strategy)
@settings(max_examples=50)
def test_cst_node_instantiation(instance):
    assert isinstance(instance, CST_Node)



@given(instance=CST_Node_strategy)
def test_cst_node_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CST_Tree_strategy)
@settings(max_examples=50)
def test_cst_tree_instantiation(instance):
    assert isinstance(instance, CST_Tree)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=CST_TNode_strategy)
@settings(max_examples=50)
def test_cst_tnode_instantiation(instance):
    assert isinstance(instance, CST_TNode)



@given(instance=CST_TNode_strategy)
def test_cst_tnode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CST_RNode_strategy)
@settings(max_examples=50)
def test_cst_rnode_instantiation(instance):
    assert isinstance(instance, CST_RNode)
