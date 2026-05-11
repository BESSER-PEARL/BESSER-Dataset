import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    coloredTree::HueTree,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coloredtree::huetree_is_not_abstract():
    assert not inspect.isabstract(coloredTree::HueTree)


def test_coloredtree::huetree_constructor_exists():
    assert callable(coloredTree::HueTree.__init__)


def test_coloredtree::huetree_constructor_args():
    sig = inspect.signature(coloredTree::HueTree.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "label" in params, "Missing parameter 'label'"

def test_coloredtree::huetree_has_color():
    assert hasattr(coloredTree::HueTree, "color")
    descriptor = None
    for klass in coloredTree::HueTree.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_coloredtree::huetree_has_label():
    assert hasattr(coloredTree::HueTree, "label")
    descriptor = None
    for klass in coloredTree::HueTree.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "blue",
        "red",
        "green",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
coloredTree::HueTree_strategy = st.builds(
    coloredTree::HueTree,
    color=
        safe_text,
    label=
        safe_text
)

@given(instance=coloredTree::HueTree_strategy)
@settings(max_examples=50)
def test_coloredtree::huetree_instantiation(instance):
    assert isinstance(instance, coloredTree::HueTree)

@given(instance=coloredTree::HueTree_strategy)
def test_coloredtree::huetree_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=coloredTree::HueTree_strategy)
def test_coloredtree::huetree_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=coloredTree::HueTree_strategy)
def test_coloredtree::huetree_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=coloredTree::HueTree_strategy)
def test_coloredtree::huetree_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original
