import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TreeNode,
    tree_NonTerminal,
    tree_Leaf,
    tree_TreeNode,
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



def test_tree_nonterminal_is_not_abstract():
    assert not inspect.isabstract(tree_NonTerminal)


def test_tree_nonterminal_constructor_exists():
    assert callable(tree_NonTerminal.__init__)


def test_tree_nonterminal_constructor_args():
    sig = inspect.signature(tree_NonTerminal.__init__)
    params = list(sig.parameters.keys())



def test_tree_leaf_is_not_abstract():
    assert not inspect.isabstract(tree_Leaf)


def test_tree_leaf_constructor_exists():
    assert callable(tree_Leaf.__init__)


def test_tree_leaf_constructor_args():
    sig = inspect.signature(tree_Leaf.__init__)
    params = list(sig.parameters.keys())



def test_tree_treenode_is_not_abstract():
    assert not inspect.isabstract(tree_TreeNode)


def test_tree_treenode_constructor_exists():
    assert callable(tree_TreeNode.__init__)


def test_tree_treenode_constructor_args():
    sig = inspect.signature(tree_TreeNode.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_tree_treenode_has_data():
    assert hasattr(tree_TreeNode, "data")
    descriptor = None
    for klass in tree_TreeNode.__mro__:
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
tree_NonTerminal_strategy = st.builds(
    tree_NonTerminal,
)
tree_Leaf_strategy = st.builds(
    tree_Leaf,
)
tree_TreeNode_strategy = st.builds(
    tree_TreeNode,
    data=
        safe_text
)

@given(instance=TreeNode_strategy)
@settings(max_examples=50)
def test_treenode_instantiation(instance):
    assert isinstance(instance, TreeNode)

@given(instance=tree_NonTerminal_strategy)
@settings(max_examples=50)
def test_tree_nonterminal_instantiation(instance):
    assert isinstance(instance, tree_NonTerminal)

@given(instance=tree_Leaf_strategy)
@settings(max_examples=50)
def test_tree_leaf_instantiation(instance):
    assert isinstance(instance, tree_Leaf)

@given(instance=tree_TreeNode_strategy)
@settings(max_examples=50)
def test_tree_treenode_instantiation(instance):
    assert isinstance(instance, tree_TreeNode)



@given(instance=tree_TreeNode_strategy)
def test_tree_treenode_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original
