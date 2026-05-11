import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ASub,
    b::B,
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



def test_b::b_is_not_abstract():
    assert not inspect.isabstract(b::B)


def test_b::b_constructor_exists():
    assert callable(b::B.__init__)


def test_b::b_constructor_args():
    sig = inspect.signature(b::B.__init__)
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
b::B_strategy = st.builds(
    b::B,
)

@given(instance=ASub_strategy)
@settings(max_examples=50)
def test_asub_instantiation(instance):
    assert isinstance(instance, ASub)

@given(instance=b::B_strategy)
@settings(max_examples=50)
def test_b::b_instantiation(instance):
    assert isinstance(instance, b::B)
