import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HLSTree_HLSNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hlstree_hlsnode_is_not_abstract():
    assert not inspect.isabstract(HLSTree_HLSNode)


def test_hlstree_hlsnode_constructor_exists():
    assert callable(HLSTree_HLSNode.__init__)


def test_hlstree_hlsnode_constructor_args():
    sig = inspect.signature(HLSTree_HLSNode.__init__)
    params = list(sig.parameters.keys())
    assert "hls" in params, "Missing parameter 'hls'"
    assert "name" in params, "Missing parameter 'name'"

def test_hlstree_hlsnode_has_hls():
    assert hasattr(HLSTree_HLSNode, "hls")
    descriptor = None
    for klass in HLSTree_HLSNode.__mro__:
        if "hls" in klass.__dict__:
            descriptor = klass.__dict__["hls"]
            break
    assert isinstance(descriptor, property)

def test_hlstree_hlsnode_has_name():
    assert hasattr(HLSTree_HLSNode, "name")
    descriptor = None
    for klass in HLSTree_HLSNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
HLSTree_HLSNode_strategy = st.builds(
    HLSTree_HLSNode,
    hls=
        safe_text,
    name=
        safe_text
)

@given(instance=HLSTree_HLSNode_strategy)
@settings(max_examples=50)
def test_hlstree_hlsnode_instantiation(instance):
    assert isinstance(instance, HLSTree_HLSNode)



@given(instance=HLSTree_HLSNode_strategy)
def test_hlstree_hlsnode_hls_setter(instance):
    original = instance.hls
    instance.hls = original
    assert instance.hls == original



@given(instance=HLSTree_HLSNode_strategy)
def test_hlstree_hlsnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
