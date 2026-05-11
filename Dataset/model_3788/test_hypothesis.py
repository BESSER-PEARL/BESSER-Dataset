import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    a::AClazz,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::aclazz_is_not_abstract():
    assert not inspect.isabstract(a::AClazz)


def test_a::aclazz_constructor_exists():
    assert callable(a::AClazz.__init__)


def test_a::aclazz_constructor_args():
    sig = inspect.signature(a::AClazz.__init__)
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
a::AClazz_strategy = st.builds(
    a::AClazz,
)

@given(instance=a::AClazz_strategy)
@settings(max_examples=50)
def test_a::aclazz_instantiation(instance):
    assert isinstance(instance, a::AClazz)
