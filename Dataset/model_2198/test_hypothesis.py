import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Tree_Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree_tree_is_not_abstract():
    assert not inspect.isabstract(Tree_Tree)


def test_tree_tree_constructor_exists():
    assert callable(Tree_Tree.__init__)


def test_tree_tree_constructor_args():
    sig = inspect.signature(Tree_Tree.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_tree_tree_has_label():
    assert hasattr(Tree_Tree, "label")
    descriptor = None
    for klass in Tree_Tree.__mro__:
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
Tree_Tree_strategy = st.builds(
    Tree_Tree,
    label=
        safe_text
)

@given(instance=Tree_Tree_strategy)
@settings(max_examples=50)
def test_tree_tree_instantiation(instance):
    assert isinstance(instance, Tree_Tree)



@given(instance=Tree_Tree_strategy)
def test_tree_tree_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original
