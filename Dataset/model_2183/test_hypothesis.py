import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TreeDsl::Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_treedsl::tree_is_not_abstract():
    assert not inspect.isabstract(TreeDsl::Tree)


def test_treedsl::tree_constructor_exists():
    assert callable(TreeDsl::Tree.__init__)


def test_treedsl::tree_constructor_args():
    sig = inspect.signature(TreeDsl::Tree.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_treedsl::tree_has_label():
    assert hasattr(TreeDsl::Tree, "label")
    descriptor = None
    for klass in TreeDsl::Tree.__mro__:
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
TreeDsl::Tree_strategy = st.builds(
    TreeDsl::Tree,
    label=
        safe_text
)

@given(instance=TreeDsl::Tree_strategy)
@settings(max_examples=50)
def test_treedsl::tree_instantiation(instance):
    assert isinstance(instance, TreeDsl::Tree)

@given(instance=TreeDsl::Tree_strategy)
def test_treedsl::tree_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=TreeDsl::Tree_strategy)
def test_treedsl::tree_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original
