import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    strictSample1_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_strictsample1_c_is_not_abstract():
    assert not inspect.isabstract(strictSample1_C)


def test_strictsample1_c_constructor_exists():
    assert callable(strictSample1_C.__init__)


def test_strictsample1_c_constructor_args():
    sig = inspect.signature(strictSample1_C.__init__)
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
strictSample1_C_strategy = st.builds(
    strictSample1_C,
)

@given(instance=strictSample1_C_strategy)
@settings(max_examples=50)
def test_strictsample1_c_instantiation(instance):
    assert isinstance(instance, strictSample1_C)
