import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    d_B,
    d_D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_d_b_is_not_abstract():
    assert not inspect.isabstract(d_B)


def test_d_b_constructor_exists():
    assert callable(d_B.__init__)


def test_d_b_constructor_args():
    sig = inspect.signature(d_B.__init__)
    params = list(sig.parameters.keys())



def test_d_d_is_not_abstract():
    assert not inspect.isabstract(d_D)


def test_d_d_constructor_exists():
    assert callable(d_D.__init__)


def test_d_d_constructor_args():
    sig = inspect.signature(d_D.__init__)
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
d_B_strategy = st.builds(
    d_B,
)
d_D_strategy = st.builds(
    d_D,
)

@given(instance=d_B_strategy)
@settings(max_examples=50)
def test_d_b_instantiation(instance):
    assert isinstance(instance, d_B)

@given(instance=d_D_strategy)
@settings(max_examples=50)
def test_d_d_instantiation(instance):
    assert isinstance(instance, d_D)
