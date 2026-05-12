import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    a_AClazz,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_aclazz_is_not_abstract():
    assert not inspect.isabstract(a_AClazz)


def test_a_aclazz_constructor_exists():
    assert callable(a_AClazz.__init__)


def test_a_aclazz_constructor_args():
    sig = inspect.signature(a_AClazz.__init__)
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
a_AClazz_strategy = st.builds(
    a_AClazz,
)

@given(instance=a_AClazz_strategy)
@settings(max_examples=50)
def test_a_aclazz_instantiation(instance):
    assert isinstance(instance, a_AClazz)
