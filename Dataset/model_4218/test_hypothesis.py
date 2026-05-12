import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    talltree_TallNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_talltree_tallnode_is_not_abstract():
    assert not inspect.isabstract(talltree_TallNode)


def test_talltree_tallnode_constructor_exists():
    assert callable(talltree_TallNode.__init__)


def test_talltree_tallnode_constructor_args():
    sig = inspect.signature(talltree_TallNode.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "name" in params, "Missing parameter 'name'"

def test_talltree_tallnode_has_height():
    assert hasattr(talltree_TallNode, "height")
    descriptor = None
    for klass in talltree_TallNode.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_talltree_tallnode_has_name():
    assert hasattr(talltree_TallNode, "name")
    descriptor = None
    for klass in talltree_TallNode.__mro__:
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
talltree_TallNode_strategy = st.builds(
    talltree_TallNode,
    height=
        st.integers(),
    name=
        safe_text
)

@given(instance=talltree_TallNode_strategy)
@settings(max_examples=50)
def test_talltree_tallnode_instantiation(instance):
    assert isinstance(instance, talltree_TallNode)



@given(instance=talltree_TallNode_strategy)
def test_talltree_tallnode_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=talltree_TallNode_strategy)
def test_talltree_tallnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
