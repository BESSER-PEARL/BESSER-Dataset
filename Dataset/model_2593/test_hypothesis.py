import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    A,
    package_subpackage_C,
    package_subpackage_B,
    package_subpackage_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_package_subpackage_c_is_not_abstract():
    assert not inspect.isabstract(package_subpackage_C)


def test_package_subpackage_c_constructor_exists():
    assert callable(package_subpackage_C.__init__)


def test_package_subpackage_c_constructor_args():
    sig = inspect.signature(package_subpackage_C.__init__)
    params = list(sig.parameters.keys())



def test_package_subpackage_b_is_not_abstract():
    assert not inspect.isabstract(package_subpackage_B)


def test_package_subpackage_b_constructor_exists():
    assert callable(package_subpackage_B.__init__)


def test_package_subpackage_b_constructor_args():
    sig = inspect.signature(package_subpackage_B.__init__)
    params = list(sig.parameters.keys())



def test_package_subpackage_a_is_not_abstract():
    assert not inspect.isabstract(package_subpackage_A)


def test_package_subpackage_a_constructor_exists():
    assert callable(package_subpackage_A.__init__)


def test_package_subpackage_a_constructor_args():
    sig = inspect.signature(package_subpackage_A.__init__)
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
A_strategy = st.builds(
    A,
)
package_subpackage_C_strategy = st.builds(
    package_subpackage_C,
)
package_subpackage_B_strategy = st.builds(
    package_subpackage_B,
)
package_subpackage_A_strategy = st.builds(
    package_subpackage_A,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=package_subpackage_C_strategy)
@settings(max_examples=50)
def test_package_subpackage_c_instantiation(instance):
    assert isinstance(instance, package_subpackage_C)

@given(instance=package_subpackage_B_strategy)
@settings(max_examples=50)
def test_package_subpackage_b_instantiation(instance):
    assert isinstance(instance, package_subpackage_B)

@given(instance=package_subpackage_A_strategy)
@settings(max_examples=50)
def test_package_subpackage_a_instantiation(instance):
    assert isinstance(instance, package_subpackage_A)
