import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    example_B,
    example_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example_b_is_not_abstract():
    assert not inspect.isabstract(example_B)


def test_example_b_constructor_exists():
    assert callable(example_B.__init__)


def test_example_b_constructor_args():
    sig = inspect.signature(example_B.__init__)
    params = list(sig.parameters.keys())



def test_example_a_is_not_abstract():
    assert not inspect.isabstract(example_A)


def test_example_a_constructor_exists():
    assert callable(example_A.__init__)


def test_example_a_constructor_args():
    sig = inspect.signature(example_A.__init__)
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
example_B_strategy = st.builds(
    example_B,
)
example_A_strategy = st.builds(
    example_A,
)

@given(instance=example_B_strategy)
@settings(max_examples=50)
def test_example_b_instantiation(instance):
    assert isinstance(instance, example_B)

@given(instance=example_A_strategy)
@settings(max_examples=50)
def test_example_a_instantiation(instance):
    assert isinstance(instance, example_A)
