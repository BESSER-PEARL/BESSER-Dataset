import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bintree::BinTreeNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bintree::bintreenode_is_not_abstract():
    assert not inspect.isabstract(bintree::BinTreeNode)


def test_bintree::bintreenode_constructor_exists():
    assert callable(bintree::BinTreeNode.__init__)


def test_bintree::bintreenode_constructor_args():
    sig = inspect.signature(bintree::BinTreeNode.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_bintree::bintreenode_has_data():
    assert hasattr(bintree::BinTreeNode, "data")
    descriptor = None
    for klass in bintree::BinTreeNode.__mro__:
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
bintree::BinTreeNode_strategy = st.builds(
    bintree::BinTreeNode,
    data=
        safe_text
)

@given(instance=bintree::BinTreeNode_strategy)
@settings(max_examples=50)
def test_bintree::bintreenode_instantiation(instance):
    assert isinstance(instance, bintree::BinTreeNode)

@given(instance=bintree::BinTreeNode_strategy)
def test_bintree::bintreenode_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=bintree::BinTreeNode_strategy)
def test_bintree::bintreenode_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original
