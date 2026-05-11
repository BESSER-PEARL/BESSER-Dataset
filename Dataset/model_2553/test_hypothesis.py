import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    Tree::Tree,
    Tree::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_tree::tree_is_not_abstract():
    assert not inspect.isabstract(Tree::Tree)


def test_tree::tree_constructor_exists():
    assert callable(Tree::Tree.__init__)


def test_tree::tree_constructor_args():
    sig = inspect.signature(Tree::Tree.__init__)
    params = list(sig.parameters.keys())



def test_tree::node_is_not_abstract():
    assert not inspect.isabstract(Tree::Node)


def test_tree::node_constructor_exists():
    assert callable(Tree::Node.__init__)


def test_tree::node_constructor_args():
    sig = inspect.signature(Tree::Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_tree::node_has_id():
    assert hasattr(Tree::Node, "id")
    descriptor = None
    for klass in Tree::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
Node_strategy = st.builds(
    Node,
)
Tree::Tree_strategy = st.builds(
    Tree::Tree,
)
Tree::Node_strategy = st.builds(
    Tree::Node,
    id=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=Tree::Tree_strategy)
@settings(max_examples=50)
def test_tree::tree_instantiation(instance):
    assert isinstance(instance, Tree::Tree)

@given(instance=Tree::Node_strategy)
@settings(max_examples=50)
def test_tree::node_instantiation(instance):
    assert isinstance(instance, Tree::Node)

@given(instance=Tree::Node_strategy)
def test_tree::node_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Tree::Node_strategy)
def test_tree::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
