import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StructuredTree_NodeKind,
    StructuredTree_Tree,
    NodeKind,
    StructuredTree_BranchKind,
    StructuredTree_LeafKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structuredtree_nodekind_is_not_abstract():
    assert not inspect.isabstract(StructuredTree_NodeKind)


def test_structuredtree_nodekind_constructor_exists():
    assert callable(StructuredTree_NodeKind.__init__)


def test_structuredtree_nodekind_constructor_args():
    sig = inspect.signature(StructuredTree_NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_structuredtree_tree_is_not_abstract():
    assert not inspect.isabstract(StructuredTree_Tree)


def test_structuredtree_tree_constructor_exists():
    assert callable(StructuredTree_Tree.__init__)


def test_structuredtree_tree_constructor_args():
    sig = inspect.signature(StructuredTree_Tree.__init__)
    params = list(sig.parameters.keys())



def test_nodekind_is_not_abstract():
    assert not inspect.isabstract(NodeKind)


def test_nodekind_constructor_exists():
    assert callable(NodeKind.__init__)


def test_nodekind_constructor_args():
    sig = inspect.signature(NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_structuredtree_branchkind_is_not_abstract():
    assert not inspect.isabstract(StructuredTree_BranchKind)


def test_structuredtree_branchkind_constructor_exists():
    assert callable(StructuredTree_BranchKind.__init__)


def test_structuredtree_branchkind_constructor_args():
    sig = inspect.signature(StructuredTree_BranchKind.__init__)
    params = list(sig.parameters.keys())



def test_structuredtree_leafkind_is_not_abstract():
    assert not inspect.isabstract(StructuredTree_LeafKind)


def test_structuredtree_leafkind_constructor_exists():
    assert callable(StructuredTree_LeafKind.__init__)


def test_structuredtree_leafkind_constructor_args():
    sig = inspect.signature(StructuredTree_LeafKind.__init__)
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
StructuredTree_NodeKind_strategy = st.builds(
    StructuredTree_NodeKind,
)
StructuredTree_Tree_strategy = st.builds(
    StructuredTree_Tree,
)
NodeKind_strategy = st.builds(
    NodeKind,
)
StructuredTree_BranchKind_strategy = st.builds(
    StructuredTree_BranchKind,
)
StructuredTree_LeafKind_strategy = st.builds(
    StructuredTree_LeafKind,
)

@given(instance=StructuredTree_NodeKind_strategy)
@settings(max_examples=50)
def test_structuredtree_nodekind_instantiation(instance):
    assert isinstance(instance, StructuredTree_NodeKind)

@given(instance=StructuredTree_Tree_strategy)
@settings(max_examples=50)
def test_structuredtree_tree_instantiation(instance):
    assert isinstance(instance, StructuredTree_Tree)

@given(instance=NodeKind_strategy)
@settings(max_examples=50)
def test_nodekind_instantiation(instance):
    assert isinstance(instance, NodeKind)

@given(instance=StructuredTree_BranchKind_strategy)
@settings(max_examples=50)
def test_structuredtree_branchkind_instantiation(instance):
    assert isinstance(instance, StructuredTree_BranchKind)

@given(instance=StructuredTree_LeafKind_strategy)
@settings(max_examples=50)
def test_structuredtree_leafkind_instantiation(instance):
    assert isinstance(instance, StructuredTree_LeafKind)
