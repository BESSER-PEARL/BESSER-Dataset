import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    root::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root::class_is_not_abstract():
    assert not inspect.isabstract(root::Class)


def test_root::class_constructor_exists():
    assert callable(root::Class.__init__)


def test_root::class_constructor_args():
    sig = inspect.signature(root::Class.__init__)
    params = list(sig.parameters.keys())


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
root::Class_strategy = st.builds(
    root::Class,
)

@given(instance=root::Class_strategy)
@settings(max_examples=50)
def test_root::class_instantiation(instance):
    assert isinstance(instance, root::Class)
