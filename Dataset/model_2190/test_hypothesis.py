import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tree::EObject,
    tree::TreeNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree::eobject_is_not_abstract():
    assert not inspect.isabstract(tree::EObject)


def test_tree::eobject_constructor_exists():
    assert callable(tree::EObject.__init__)


def test_tree::eobject_constructor_args():
    sig = inspect.signature(tree::EObject.__init__)
    params = list(sig.parameters.keys())



def test_tree::treenode_is_not_abstract():
    assert not inspect.isabstract(tree::TreeNode)


def test_tree::treenode_constructor_exists():
    assert callable(tree::TreeNode.__init__)


def test_tree::treenode_constructor_args():
    sig = inspect.signature(tree::TreeNode.__init__)
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
tree::EObject_strategy = st.builds(
    tree::EObject,
)
tree::TreeNode_strategy = st.builds(
    tree::TreeNode,
)

@given(instance=tree::EObject_strategy)
@settings(max_examples=50)
def test_tree::eobject_instantiation(instance):
    assert isinstance(instance, tree::EObject)

@given(instance=tree::TreeNode_strategy)
@settings(max_examples=50)
def test_tree::treenode_instantiation(instance):
    assert isinstance(instance, tree::TreeNode)
