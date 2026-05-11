import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HLSTree::HLSNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hlstree::hlsnode_is_not_abstract():
    assert not inspect.isabstract(HLSTree::HLSNode)


def test_hlstree::hlsnode_constructor_exists():
    assert callable(HLSTree::HLSNode.__init__)


def test_hlstree::hlsnode_constructor_args():
    sig = inspect.signature(HLSTree::HLSNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hls" in params, "Missing parameter 'hls'"

def test_hlstree::hlsnode_has_name():
    assert hasattr(HLSTree::HLSNode, "name")
    descriptor = None
    for klass in HLSTree::HLSNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hlstree::hlsnode_has_hls():
    assert hasattr(HLSTree::HLSNode, "hls")
    descriptor = None
    for klass in HLSTree::HLSNode.__mro__:
        if "hls" in klass.__dict__:
            descriptor = klass.__dict__["hls"]
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
HLSTree::HLSNode_strategy = st.builds(
    HLSTree::HLSNode,
    name=
        safe_text,
    hls=
        safe_text
)

@given(instance=HLSTree::HLSNode_strategy)
@settings(max_examples=50)
def test_hlstree::hlsnode_instantiation(instance):
    assert isinstance(instance, HLSTree::HLSNode)

@given(instance=HLSTree::HLSNode_strategy)
def test_hlstree::hlsnode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HLSTree::HLSNode_strategy)
def test_hlstree::hlsnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HLSTree::HLSNode_strategy)
def test_hlstree::hlsnode_hls_type(instance):
    assert isinstance(instance.hls, str)


@given(instance=HLSTree::HLSNode_strategy)
def test_hlstree::hlsnode_hls_setter(instance):
    original = instance.hls
    instance.hls = original
    assert instance.hls == original
