import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bintree_BinTreeNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bintree_bintreenode_is_not_abstract():
    assert not inspect.isabstract(bintree_BinTreeNode)


def test_bintree_bintreenode_constructor_exists():
    assert callable(bintree_BinTreeNode.__init__)


def test_bintree_bintreenode_constructor_args():
    sig = inspect.signature(bintree_BinTreeNode.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_bintree_bintreenode_has_data():
    assert hasattr(bintree_BinTreeNode, "data")
    descriptor = None
    for klass in bintree_BinTreeNode.__mro__:
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
bintree_BinTreeNode_strategy = st.builds(
    bintree_BinTreeNode,
    data=
        safe_text
)

@given(instance=bintree_BinTreeNode_strategy)
@settings(max_examples=50)
def test_bintree_bintreenode_instantiation(instance):
    assert isinstance(instance, bintree_BinTreeNode)



@given(instance=bintree_BinTreeNode_strategy)
def test_bintree_bintreenode_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original
