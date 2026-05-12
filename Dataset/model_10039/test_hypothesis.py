import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    t3::Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_t3::tree_is_not_abstract():
    assert not inspect.isabstract(t3::Tree)


def test_t3::tree_constructor_exists():
    assert callable(t3::Tree.__init__)


def test_t3::tree_constructor_args():
    sig = inspect.signature(t3::Tree.__init__)
    params = list(sig.parameters.keys())
    assert "balanced" in params, "Missing parameter 'balanced'"

def test_t3::tree_has_balanced():
    assert hasattr(t3::Tree, "balanced")
    descriptor = None
    for klass in t3::Tree.__mro__:
        if "balanced" in klass.__dict__:
            descriptor = klass.__dict__["balanced"]
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
t3::Tree_strategy = st.builds(
    t3::Tree,
    balanced=
        st.booleans()
)

@given(instance=t3::Tree_strategy)
@settings(max_examples=50)
def test_t3::tree_instantiation(instance):
    assert isinstance(instance, t3::Tree)

@given(instance=t3::Tree_strategy)
def test_t3::tree_balanced_type(instance):
    assert isinstance(instance.balanced, bool)


@given(instance=t3::Tree_strategy)
def test_t3::tree_balanced_setter(instance):
    original = instance.balanced
    instance.balanced = original
    assert instance.balanced == original
