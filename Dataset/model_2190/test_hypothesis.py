import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tree_EObject,
    tree_TreeNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree_eobject_is_not_abstract():
    assert not inspect.isabstract(tree_EObject)


def test_tree_eobject_constructor_exists():
    assert callable(tree_EObject.__init__)


def test_tree_eobject_constructor_args():
    sig = inspect.signature(tree_EObject.__init__)
    params = list(sig.parameters.keys())



def test_tree_treenode_is_not_abstract():
    assert not inspect.isabstract(tree_TreeNode)


def test_tree_treenode_constructor_exists():
    assert callable(tree_TreeNode.__init__)


def test_tree_treenode_constructor_args():
    sig = inspect.signature(tree_TreeNode.__init__)
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
tree_EObject_strategy = st.builds(
    tree_EObject,
)
tree_TreeNode_strategy = st.builds(
    tree_TreeNode,
)

@given(instance=tree_EObject_strategy)
@settings(max_examples=50)
def test_tree_eobject_instantiation(instance):
    assert isinstance(instance, tree_EObject)

@given(instance=tree_TreeNode_strategy)
@settings(max_examples=50)
def test_tree_treenode_instantiation(instance):
    assert isinstance(instance, tree_TreeNode)
