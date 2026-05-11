import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpletree::Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletree::tree_is_not_abstract():
    assert not inspect.isabstract(simpletree::Tree)


def test_simpletree::tree_constructor_exists():
    assert callable(simpletree::Tree.__init__)


def test_simpletree::tree_constructor_args():
    sig = inspect.signature(simpletree::Tree.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_simpletree::tree_has_label():
    assert hasattr(simpletree::Tree, "label")
    descriptor = None
    for klass in simpletree::Tree.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
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
simpletree::Tree_strategy = st.builds(
    simpletree::Tree,
    label=
        safe_text
)

@given(instance=simpletree::Tree_strategy)
@settings(max_examples=50)
def test_simpletree::tree_instantiation(instance):
    assert isinstance(instance, simpletree::Tree)

@given(instance=simpletree::Tree_strategy)
def test_simpletree::tree_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=simpletree::Tree_strategy)
def test_simpletree::tree_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original
