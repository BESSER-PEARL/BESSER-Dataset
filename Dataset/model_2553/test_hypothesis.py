import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    Tree_Tree,
    Tree_Node,
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



def test_tree_tree_is_not_abstract():
    assert not inspect.isabstract(Tree_Tree)


def test_tree_tree_constructor_exists():
    assert callable(Tree_Tree.__init__)


def test_tree_tree_constructor_args():
    sig = inspect.signature(Tree_Tree.__init__)
    params = list(sig.parameters.keys())



def test_tree_node_is_not_abstract():
    assert not inspect.isabstract(Tree_Node)


def test_tree_node_constructor_exists():
    assert callable(Tree_Node.__init__)


def test_tree_node_constructor_args():
    sig = inspect.signature(Tree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_tree_node_has_id():
    assert hasattr(Tree_Node, "id")
    descriptor = None
    for klass in Tree_Node.__mro__:
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
Tree_Tree_strategy = st.builds(
    Tree_Tree,
)
Tree_Node_strategy = st.builds(
    Tree_Node,
    id=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=Tree_Tree_strategy)
@settings(max_examples=50)
def test_tree_tree_instantiation(instance):
    assert isinstance(instance, Tree_Tree)

@given(instance=Tree_Node_strategy)
@settings(max_examples=50)
def test_tree_node_instantiation(instance):
    assert isinstance(instance, Tree_Node)



@given(instance=Tree_Node_strategy)
def test_tree_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
