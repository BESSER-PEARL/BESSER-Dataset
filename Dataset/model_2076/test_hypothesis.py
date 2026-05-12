import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OverlappingTree_NodeKind,
    OverlappingTree_Tree,
    OverlappingTree_Child,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_overlappingtree_nodekind_is_not_abstract():
    assert not inspect.isabstract(OverlappingTree_NodeKind)


def test_overlappingtree_nodekind_constructor_exists():
    assert callable(OverlappingTree_NodeKind.__init__)


def test_overlappingtree_nodekind_constructor_args():
    sig = inspect.signature(OverlappingTree_NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_overlappingtree_tree_is_not_abstract():
    assert not inspect.isabstract(OverlappingTree_Tree)


def test_overlappingtree_tree_constructor_exists():
    assert callable(OverlappingTree_Tree.__init__)


def test_overlappingtree_tree_constructor_args():
    sig = inspect.signature(OverlappingTree_Tree.__init__)
    params = list(sig.parameters.keys())



def test_overlappingtree_child_is_not_abstract():
    assert not inspect.isabstract(OverlappingTree_Child)


def test_overlappingtree_child_constructor_exists():
    assert callable(OverlappingTree_Child.__init__)


def test_overlappingtree_child_constructor_args():
    sig = inspect.signature(OverlappingTree_Child.__init__)
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
OverlappingTree_NodeKind_strategy = st.builds(
    OverlappingTree_NodeKind,
)
OverlappingTree_Tree_strategy = st.builds(
    OverlappingTree_Tree,
)
OverlappingTree_Child_strategy = st.builds(
    OverlappingTree_Child,
)

@given(instance=OverlappingTree_NodeKind_strategy)
@settings(max_examples=50)
def test_overlappingtree_nodekind_instantiation(instance):
    assert isinstance(instance, OverlappingTree_NodeKind)

@given(instance=OverlappingTree_Tree_strategy)
@settings(max_examples=50)
def test_overlappingtree_tree_instantiation(instance):
    assert isinstance(instance, OverlappingTree_Tree)

@given(instance=OverlappingTree_Child_strategy)
@settings(max_examples=50)
def test_overlappingtree_child_instantiation(instance):
    assert isinstance(instance, OverlappingTree_Child)
