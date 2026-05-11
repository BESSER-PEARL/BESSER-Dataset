import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    talltree::TallNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_talltree::tallnode_is_not_abstract():
    assert not inspect.isabstract(talltree::TallNode)


def test_talltree::tallnode_constructor_exists():
    assert callable(talltree::TallNode.__init__)


def test_talltree::tallnode_constructor_args():
    sig = inspect.signature(talltree::TallNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "height" in params, "Missing parameter 'height'"

def test_talltree::tallnode_has_name():
    assert hasattr(talltree::TallNode, "name")
    descriptor = None
    for klass in talltree::TallNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_talltree::tallnode_has_height():
    assert hasattr(talltree::TallNode, "height")
    descriptor = None
    for klass in talltree::TallNode.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
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
talltree::TallNode_strategy = st.builds(
    talltree::TallNode,
    name=
        safe_text,
    height=
        st.integers()
)

@given(instance=talltree::TallNode_strategy)
@settings(max_examples=50)
def test_talltree::tallnode_instantiation(instance):
    assert isinstance(instance, talltree::TallNode)

@given(instance=talltree::TallNode_strategy)
def test_talltree::tallnode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=talltree::TallNode_strategy)
def test_talltree::tallnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=talltree::TallNode_strategy)
def test_talltree::tallnode_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=talltree::TallNode_strategy)
def test_talltree::tallnode_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original
