import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bug1312_C,
    bug1312_B,
    bug1312_Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bug1312_c_is_not_abstract():
    assert not inspect.isabstract(bug1312_C)


def test_bug1312_c_constructor_exists():
    assert callable(bug1312_C.__init__)


def test_bug1312_c_constructor_args():
    sig = inspect.signature(bug1312_C.__init__)
    params = list(sig.parameters.keys())



def test_bug1312_b_is_not_abstract():
    assert not inspect.isabstract(bug1312_B)


def test_bug1312_b_constructor_exists():
    assert callable(bug1312_B.__init__)


def test_bug1312_b_constructor_args():
    sig = inspect.signature(bug1312_B.__init__)
    params = list(sig.parameters.keys())



def test_bug1312_root_is_not_abstract():
    assert not inspect.isabstract(bug1312_Root)


def test_bug1312_root_constructor_exists():
    assert callable(bug1312_Root.__init__)


def test_bug1312_root_constructor_args():
    sig = inspect.signature(bug1312_Root.__init__)
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
bug1312_C_strategy = st.builds(
    bug1312_C,
)
bug1312_B_strategy = st.builds(
    bug1312_B,
)
bug1312_Root_strategy = st.builds(
    bug1312_Root,
)

@given(instance=bug1312_C_strategy)
@settings(max_examples=50)
def test_bug1312_c_instantiation(instance):
    assert isinstance(instance, bug1312_C)

@given(instance=bug1312_B_strategy)
@settings(max_examples=50)
def test_bug1312_b_instantiation(instance):
    assert isinstance(instance, bug1312_B)

@given(instance=bug1312_Root_strategy)
@settings(max_examples=50)
def test_bug1312_root_instantiation(instance):
    assert isinstance(instance, bug1312_Root)
