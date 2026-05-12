import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    coloredTree_HueTree,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_coloredtree_huetree_is_not_abstract():
    assert not inspect.isabstract(coloredTree_HueTree)


def test_coloredtree_huetree_constructor_exists():
    assert callable(coloredTree_HueTree.__init__)


def test_coloredtree_huetree_constructor_args():
    sig = inspect.signature(coloredTree_HueTree.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "label" in params, "Missing parameter 'label'"

def test_coloredtree_huetree_has_color():
    assert hasattr(coloredTree_HueTree, "color")
    descriptor = None
    for klass in coloredTree_HueTree.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_coloredtree_huetree_has_label():
    assert hasattr(coloredTree_HueTree, "label")
    descriptor = None
    for klass in coloredTree_HueTree.__mro__:
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
        "green",
        "blue",
        "red",
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
coloredTree_HueTree_strategy = st.builds(
    coloredTree_HueTree,
    color=
        safe_text,
    label=
        safe_text
)

@given(instance=coloredTree_HueTree_strategy)
@settings(max_examples=50)
def test_coloredtree_huetree_instantiation(instance):
    assert isinstance(instance, coloredTree_HueTree)



@given(instance=coloredTree_HueTree_strategy)
def test_coloredtree_huetree_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=coloredTree_HueTree_strategy)
def test_coloredtree_huetree_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original
