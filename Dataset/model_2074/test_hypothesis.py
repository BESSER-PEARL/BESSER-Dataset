import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CST::Node,
    CST::Tree,
    Node,
    CST::TNode,
    CST::RNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cst::node_is_not_abstract():
    assert not inspect.isabstract(CST::Node)


def test_cst::node_constructor_exists():
    assert callable(CST::Node.__init__)


def test_cst::node_constructor_args():
    sig = inspect.signature(CST::Node.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_cst::node_has_kind():
    assert hasattr(CST::Node, "kind")
    descriptor = None
    for klass in CST::Node.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_cst::tree_is_not_abstract():
    assert not inspect.isabstract(CST::Tree)


def test_cst::tree_constructor_exists():
    assert callable(CST::Tree.__init__)


def test_cst::tree_constructor_args():
    sig = inspect.signature(CST::Tree.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_cst::tnode_is_not_abstract():
    assert not inspect.isabstract(CST::TNode)


def test_cst::tnode_constructor_exists():
    assert callable(CST::TNode.__init__)


def test_cst::tnode_constructor_args():
    sig = inspect.signature(CST::TNode.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cst::tnode_has_value():
    assert hasattr(CST::TNode, "value")
    descriptor = None
    for klass in CST::TNode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cst::rnode_is_not_abstract():
    assert not inspect.isabstract(CST::RNode)


def test_cst::rnode_constructor_exists():
    assert callable(CST::RNode.__init__)


def test_cst::rnode_constructor_args():
    sig = inspect.signature(CST::RNode.__init__)
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
CST::Node_strategy = st.builds(
    CST::Node,
    kind=
        safe_text
)
CST::Tree_strategy = st.builds(
    CST::Tree,
)
Node_strategy = st.builds(
    Node,
)
CST::TNode_strategy = st.builds(
    CST::TNode,
    value=
        safe_text
)
CST::RNode_strategy = st.builds(
    CST::RNode,
)

@given(instance=CST::Node_strategy)
@settings(max_examples=50)
def test_cst::node_instantiation(instance):
    assert isinstance(instance, CST::Node)

@given(instance=CST::Node_strategy)
def test_cst::node_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=CST::Node_strategy)
def test_cst::node_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CST::Tree_strategy)
@settings(max_examples=50)
def test_cst::tree_instantiation(instance):
    assert isinstance(instance, CST::Tree)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=CST::TNode_strategy)
@settings(max_examples=50)
def test_cst::tnode_instantiation(instance):
    assert isinstance(instance, CST::TNode)

@given(instance=CST::TNode_strategy)
def test_cst::tnode_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=CST::TNode_strategy)
def test_cst::tnode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CST::RNode_strategy)
@settings(max_examples=50)
def test_cst::rnode_instantiation(instance):
    assert isinstance(instance, CST::RNode)
