import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    strictSample1::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_strictsample1::c_is_not_abstract():
    assert not inspect.isabstract(strictSample1::C)


def test_strictsample1::c_constructor_exists():
    assert callable(strictSample1::C.__init__)


def test_strictsample1::c_constructor_args():
    sig = inspect.signature(strictSample1::C.__init__)
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
strictSample1::C_strategy = st.builds(
    strictSample1::C,
)

@given(instance=strictSample1::C_strategy)
@settings(max_examples=50)
def test_strictsample1::c_instantiation(instance):
    assert isinstance(instance, strictSample1::C)
