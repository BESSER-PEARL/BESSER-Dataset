import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    root_sub_B,
    root_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_sub_b_is_not_abstract():
    assert not inspect.isabstract(root_sub_B)


def test_root_sub_b_constructor_exists():
    assert callable(root_sub_B.__init__)


def test_root_sub_b_constructor_args():
    sig = inspect.signature(root_sub_B.__init__)
    params = list(sig.parameters.keys())



def test_root_a_is_not_abstract():
    assert not inspect.isabstract(root_A)


def test_root_a_constructor_exists():
    assert callable(root_A.__init__)


def test_root_a_constructor_args():
    sig = inspect.signature(root_A.__init__)
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
root_sub_B_strategy = st.builds(
    root_sub_B,
)
root_A_strategy = st.builds(
    root_A,
)

@given(instance=root_sub_B_strategy)
@settings(max_examples=50)
def test_root_sub_b_instantiation(instance):
    assert isinstance(instance, root_sub_B)

@given(instance=root_A_strategy)
@settings(max_examples=50)
def test_root_a_instantiation(instance):
    assert isinstance(instance, root_A)
