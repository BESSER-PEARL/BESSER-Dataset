import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TreeNode,
    tree::NonTerminal,
    tree::Leaf,
    tree::TreeNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_treenode_is_not_abstract():
    assert not inspect.isabstract(TreeNode)


def test_treenode_constructor_exists():
    assert callable(TreeNode.__init__)


def test_treenode_constructor_args():
    sig = inspect.signature(TreeNode.__init__)
    params = list(sig.parameters.keys())



def test_tree::nonterminal_is_not_abstract():
    assert not inspect.isabstract(tree::NonTerminal)


def test_tree::nonterminal_constructor_exists():
    assert callable(tree::NonTerminal.__init__)


def test_tree::nonterminal_constructor_args():
    sig = inspect.signature(tree::NonTerminal.__init__)
    params = list(sig.parameters.keys())



def test_tree::leaf_is_not_abstract():
    assert not inspect.isabstract(tree::Leaf)


def test_tree::leaf_constructor_exists():
    assert callable(tree::Leaf.__init__)


def test_tree::leaf_constructor_args():
    sig = inspect.signature(tree::Leaf.__init__)
    params = list(sig.parameters.keys())



def test_tree::treenode_is_not_abstract():
    assert not inspect.isabstract(tree::TreeNode)


def test_tree::treenode_constructor_exists():
    assert callable(tree::TreeNode.__init__)


def test_tree::treenode_constructor_args():
    sig = inspect.signature(tree::TreeNode.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_tree::treenode_has_data():
    assert hasattr(tree::TreeNode, "data")
    descriptor = None
    for klass in tree::TreeNode.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
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
TreeNode_strategy = st.builds(
    TreeNode,
)
tree::NonTerminal_strategy = st.builds(
    tree::NonTerminal,
)
tree::Leaf_strategy = st.builds(
    tree::Leaf,
)
tree::TreeNode_strategy = st.builds(
    tree::TreeNode,
    data=
        safe_text
)

@given(instance=TreeNode_strategy)
@settings(max_examples=50)
def test_treenode_instantiation(instance):
    assert isinstance(instance, TreeNode)

@given(instance=tree::NonTerminal_strategy)
@settings(max_examples=50)
def test_tree::nonterminal_instantiation(instance):
    assert isinstance(instance, tree::NonTerminal)

@given(instance=tree::Leaf_strategy)
@settings(max_examples=50)
def test_tree::leaf_instantiation(instance):
    assert isinstance(instance, tree::Leaf)

@given(instance=tree::TreeNode_strategy)
@settings(max_examples=50)
def test_tree::treenode_instantiation(instance):
    assert isinstance(instance, tree::TreeNode)

@given(instance=tree::TreeNode_strategy)
def test_tree::treenode_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=tree::TreeNode_strategy)
def test_tree::treenode_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original
