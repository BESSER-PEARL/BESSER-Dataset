import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleTree_Tree,
    SimpleTree_NodeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletree_tree_is_not_abstract():
    assert not inspect.isabstract(SimpleTree_Tree)


def test_simpletree_tree_constructor_exists():
    assert callable(SimpleTree_Tree.__init__)


def test_simpletree_tree_constructor_args():
    sig = inspect.signature(SimpleTree_Tree.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_nodekind_is_not_abstract():
    assert not inspect.isabstract(SimpleTree_NodeKind)


def test_simpletree_nodekind_constructor_exists():
    assert callable(SimpleTree_NodeKind.__init__)


def test_simpletree_nodekind_constructor_args():
    sig = inspect.signature(SimpleTree_NodeKind.__init__)
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
SimpleTree_Tree_strategy = st.builds(
    SimpleTree_Tree,
)
SimpleTree_NodeKind_strategy = st.builds(
    SimpleTree_NodeKind,
)

@given(instance=SimpleTree_Tree_strategy)
@settings(max_examples=50)
def test_simpletree_tree_instantiation(instance):
    assert isinstance(instance, SimpleTree_Tree)

@given(instance=SimpleTree_NodeKind_strategy)
@settings(max_examples=50)
def test_simpletree_nodekind_instantiation(instance):
    assert isinstance(instance, SimpleTree_NodeKind)
