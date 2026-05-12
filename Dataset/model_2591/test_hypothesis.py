import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    root_subpackage2_C,
    root_subsubpackage1_D,
    root_subpackage1_B,
    root_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_subpackage2_c_is_not_abstract():
    assert not inspect.isabstract(root_subpackage2_C)


def test_root_subpackage2_c_constructor_exists():
    assert callable(root_subpackage2_C.__init__)


def test_root_subpackage2_c_constructor_args():
    sig = inspect.signature(root_subpackage2_C.__init__)
    params = list(sig.parameters.keys())



def test_root_subsubpackage1_d_is_not_abstract():
    assert not inspect.isabstract(root_subsubpackage1_D)


def test_root_subsubpackage1_d_constructor_exists():
    assert callable(root_subsubpackage1_D.__init__)


def test_root_subsubpackage1_d_constructor_args():
    sig = inspect.signature(root_subsubpackage1_D.__init__)
    params = list(sig.parameters.keys())



def test_root_subpackage1_b_is_not_abstract():
    assert not inspect.isabstract(root_subpackage1_B)


def test_root_subpackage1_b_constructor_exists():
    assert callable(root_subpackage1_B.__init__)


def test_root_subpackage1_b_constructor_args():
    sig = inspect.signature(root_subpackage1_B.__init__)
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
root_subpackage2_C_strategy = st.builds(
    root_subpackage2_C,
)
root_subsubpackage1_D_strategy = st.builds(
    root_subsubpackage1_D,
)
root_subpackage1_B_strategy = st.builds(
    root_subpackage1_B,
)
root_A_strategy = st.builds(
    root_A,
)

@given(instance=root_subpackage2_C_strategy)
@settings(max_examples=50)
def test_root_subpackage2_c_instantiation(instance):
    assert isinstance(instance, root_subpackage2_C)

@given(instance=root_subsubpackage1_D_strategy)
@settings(max_examples=50)
def test_root_subsubpackage1_d_instantiation(instance):
    assert isinstance(instance, root_subsubpackage1_D)

@given(instance=root_subpackage1_B_strategy)
@settings(max_examples=50)
def test_root_subpackage1_b_instantiation(instance):
    assert isinstance(instance, root_subpackage1_B)

@given(instance=root_A_strategy)
@settings(max_examples=50)
def test_root_a_instantiation(instance):
    assert isinstance(instance, root_A)
