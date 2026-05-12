import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    c_D,
    c_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c_d_is_not_abstract():
    assert not inspect.isabstract(c_D)


def test_c_d_constructor_exists():
    assert callable(c_D.__init__)


def test_c_d_constructor_args():
    sig = inspect.signature(c_D.__init__)
    params = list(sig.parameters.keys())



def test_c_c_is_not_abstract():
    assert not inspect.isabstract(c_C)


def test_c_c_constructor_exists():
    assert callable(c_C.__init__)


def test_c_c_constructor_args():
    sig = inspect.signature(c_C.__init__)
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
c_D_strategy = st.builds(
    c_D,
)
c_C_strategy = st.builds(
    c_C,
)

@given(instance=c_D_strategy)
@settings(max_examples=50)
def test_c_d_instantiation(instance):
    assert isinstance(instance, c_D)

@given(instance=c_C_strategy)
@settings(max_examples=50)
def test_c_c_instantiation(instance):
    assert isinstance(instance, c_C)
