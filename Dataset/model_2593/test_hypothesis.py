import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    package::subpackage::C,
    package::subpackage::B,
    package::subpackage::A,
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



def test_package::subpackage::c_is_not_abstract():
    assert not inspect.isabstract(package::subpackage::C)


def test_package::subpackage::c_constructor_exists():
    assert callable(package::subpackage::C.__init__)


def test_package::subpackage::c_constructor_args():
    sig = inspect.signature(package::subpackage::C.__init__)
    params = list(sig.parameters.keys())



def test_package::subpackage::b_is_not_abstract():
    assert not inspect.isabstract(package::subpackage::B)


def test_package::subpackage::b_constructor_exists():
    assert callable(package::subpackage::B.__init__)


def test_package::subpackage::b_constructor_args():
    sig = inspect.signature(package::subpackage::B.__init__)
    params = list(sig.parameters.keys())



def test_package::subpackage::a_is_not_abstract():
    assert not inspect.isabstract(package::subpackage::A)


def test_package::subpackage::a_constructor_exists():
    assert callable(package::subpackage::A.__init__)


def test_package::subpackage::a_constructor_args():
    sig = inspect.signature(package::subpackage::A.__init__)
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
package::subpackage::C_strategy = st.builds(
    package::subpackage::C,
)
package::subpackage::B_strategy = st.builds(
    package::subpackage::B,
)
package::subpackage::A_strategy = st.builds(
    package::subpackage::A,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=package::subpackage::C_strategy)
@settings(max_examples=50)
def test_package::subpackage::c_instantiation(instance):
    assert isinstance(instance, package::subpackage::C)

@given(instance=package::subpackage::B_strategy)
@settings(max_examples=50)
def test_package::subpackage::b_instantiation(instance):
    assert isinstance(instance, package::subpackage::B)

@given(instance=package::subpackage::A_strategy)
@settings(max_examples=50)
def test_package::subpackage::a_instantiation(instance):
    assert isinstance(instance, package::subpackage::A)
