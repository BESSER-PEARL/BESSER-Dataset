import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testSubpackages1_subpackage3_class4,
    testSubpackages2_root_class2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testsubpackages1_subpackage3_class4_is_not_abstract():
    assert not inspect.isabstract(testSubpackages1_subpackage3_class4)


def test_testsubpackages1_subpackage3_class4_constructor_exists():
    assert callable(testSubpackages1_subpackage3_class4.__init__)


def test_testsubpackages1_subpackage3_class4_constructor_args():
    sig = inspect.signature(testSubpackages1_subpackage3_class4.__init__)
    params = list(sig.parameters.keys())



def test_testsubpackages2_root_class2_is_not_abstract():
    assert not inspect.isabstract(testSubpackages2_root_class2)


def test_testsubpackages2_root_class2_constructor_exists():
    assert callable(testSubpackages2_root_class2.__init__)


def test_testsubpackages2_root_class2_constructor_args():
    sig = inspect.signature(testSubpackages2_root_class2.__init__)
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
testSubpackages1_subpackage3_class4_strategy = st.builds(
    testSubpackages1_subpackage3_class4,
)
testSubpackages2_root_class2_strategy = st.builds(
    testSubpackages2_root_class2,
)

@given(instance=testSubpackages1_subpackage3_class4_strategy)
@settings(max_examples=50)
def test_testsubpackages1_subpackage3_class4_instantiation(instance):
    assert isinstance(instance, testSubpackages1_subpackage3_class4)

@given(instance=testSubpackages2_root_class2_strategy)
@settings(max_examples=50)
def test_testsubpackages2_root_class2_instantiation(instance):
    assert isinstance(instance, testSubpackages2_root_class2)
