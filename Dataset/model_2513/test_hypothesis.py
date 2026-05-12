import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genericTest_OtherType,
    genericTest_D,
    genericTest_C,
    genericTest_B,
    genericTest_SomeType,
    genericTest_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_generictest_othertype_is_not_abstract():
    assert not inspect.isabstract(genericTest_OtherType)


def test_generictest_othertype_constructor_exists():
    assert callable(genericTest_OtherType.__init__)


def test_generictest_othertype_constructor_args():
    sig = inspect.signature(genericTest_OtherType.__init__)
    params = list(sig.parameters.keys())



def test_generictest_d_is_not_abstract():
    assert not inspect.isabstract(genericTest_D)


def test_generictest_d_constructor_exists():
    assert callable(genericTest_D.__init__)


def test_generictest_d_constructor_args():
    sig = inspect.signature(genericTest_D.__init__)
    params = list(sig.parameters.keys())



def test_generictest_c_is_not_abstract():
    assert not inspect.isabstract(genericTest_C)


def test_generictest_c_constructor_exists():
    assert callable(genericTest_C.__init__)


def test_generictest_c_constructor_args():
    sig = inspect.signature(genericTest_C.__init__)
    params = list(sig.parameters.keys())



def test_generictest_b_is_not_abstract():
    assert not inspect.isabstract(genericTest_B)


def test_generictest_b_constructor_exists():
    assert callable(genericTest_B.__init__)


def test_generictest_b_constructor_args():
    sig = inspect.signature(genericTest_B.__init__)
    params = list(sig.parameters.keys())



def test_generictest_sometype_is_not_abstract():
    assert not inspect.isabstract(genericTest_SomeType)


def test_generictest_sometype_constructor_exists():
    assert callable(genericTest_SomeType.__init__)


def test_generictest_sometype_constructor_args():
    sig = inspect.signature(genericTest_SomeType.__init__)
    params = list(sig.parameters.keys())



def test_generictest_a_is_not_abstract():
    assert not inspect.isabstract(genericTest_A)


def test_generictest_a_constructor_exists():
    assert callable(genericTest_A.__init__)


def test_generictest_a_constructor_args():
    sig = inspect.signature(genericTest_A.__init__)
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
genericTest_OtherType_strategy = st.builds(
    genericTest_OtherType,
)
genericTest_D_strategy = st.builds(
    genericTest_D,
)
genericTest_C_strategy = st.builds(
    genericTest_C,
)
genericTest_B_strategy = st.builds(
    genericTest_B,
)
genericTest_SomeType_strategy = st.builds(
    genericTest_SomeType,
)
genericTest_A_strategy = st.builds(
    genericTest_A,
)

@given(instance=genericTest_OtherType_strategy)
@settings(max_examples=50)
def test_generictest_othertype_instantiation(instance):
    assert isinstance(instance, genericTest_OtherType)

@given(instance=genericTest_D_strategy)
@settings(max_examples=50)
def test_generictest_d_instantiation(instance):
    assert isinstance(instance, genericTest_D)

@given(instance=genericTest_C_strategy)
@settings(max_examples=50)
def test_generictest_c_instantiation(instance):
    assert isinstance(instance, genericTest_C)

@given(instance=genericTest_B_strategy)
@settings(max_examples=50)
def test_generictest_b_instantiation(instance):
    assert isinstance(instance, genericTest_B)

@given(instance=genericTest_SomeType_strategy)
@settings(max_examples=50)
def test_generictest_sometype_instantiation(instance):
    assert isinstance(instance, genericTest_SomeType)

@given(instance=genericTest_A_strategy)
@settings(max_examples=50)
def test_generictest_a_instantiation(instance):
    assert isinstance(instance, genericTest_A)
