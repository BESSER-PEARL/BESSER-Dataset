import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ASub,
    b_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_asub_is_not_abstract():
    assert not inspect.isabstract(ASub)


def test_asub_constructor_exists():
    assert callable(ASub.__init__)


def test_asub_constructor_args():
    sig = inspect.signature(ASub.__init__)
    params = list(sig.parameters.keys())



def test_b_b_is_not_abstract():
    assert not inspect.isabstract(b_B)


def test_b_b_constructor_exists():
    assert callable(b_B.__init__)


def test_b_b_constructor_args():
    sig = inspect.signature(b_B.__init__)
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
ASub_strategy = st.builds(
    ASub,
)
b_B_strategy = st.builds(
    b_B,
)

@given(instance=ASub_strategy)
@settings(max_examples=50)
def test_asub_instantiation(instance):
    assert isinstance(instance, ASub)

@given(instance=b_B_strategy)
@settings(max_examples=50)
def test_b_b_instantiation(instance):
    assert isinstance(instance, b_B)
