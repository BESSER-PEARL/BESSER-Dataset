import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tree::Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree::tree_is_not_abstract():
    assert not inspect.isabstract(tree::Tree)


def test_tree::tree_constructor_exists():
    assert callable(tree::Tree.__init__)


def test_tree::tree_constructor_args():
    sig = inspect.signature(tree::Tree.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_tree::tree_has_label():
    assert hasattr(tree::Tree, "label")
    descriptor = None
    for klass in tree::Tree.__mro__:
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
tree::Tree_strategy = st.builds(
    tree::Tree,
    label=
        safe_text
)

@given(instance=tree::Tree_strategy)
@settings(max_examples=50)
def test_tree::tree_instantiation(instance):
    assert isinstance(instance, tree::Tree)

@given(instance=tree::Tree_strategy)
def test_tree::tree_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=tree::Tree_strategy)
def test_tree::tree_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original
