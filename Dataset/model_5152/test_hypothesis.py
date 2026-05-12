import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tests_ObjectUnionOf_A_B,
    tests_C,
    ObjectIntersectionOf_A_C,
    ObjectUnionOf_A_B,
    tests_B,
    tests_A,
    C,
    A,
    tests_ObjectIntersectionOf_A_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tests_objectunionof_a_b_is_not_abstract():
    assert not inspect.isabstract(tests_ObjectUnionOf_A_B)


def test_tests_objectunionof_a_b_constructor_exists():
    assert callable(tests_ObjectUnionOf_A_B.__init__)


def test_tests_objectunionof_a_b_constructor_args():
    sig = inspect.signature(tests_ObjectUnionOf_A_B.__init__)
    params = list(sig.parameters.keys())



def test_tests_c_is_not_abstract():
    assert not inspect.isabstract(tests_C)


def test_tests_c_constructor_exists():
    assert callable(tests_C.__init__)


def test_tests_c_constructor_args():
    sig = inspect.signature(tests_C.__init__)
    params = list(sig.parameters.keys())



def test_objectintersectionof_a_c_is_not_abstract():
    assert not inspect.isabstract(ObjectIntersectionOf_A_C)


def test_objectintersectionof_a_c_constructor_exists():
    assert callable(ObjectIntersectionOf_A_C.__init__)


def test_objectintersectionof_a_c_constructor_args():
    sig = inspect.signature(ObjectIntersectionOf_A_C.__init__)
    params = list(sig.parameters.keys())



def test_objectunionof_a_b_is_not_abstract():
    assert not inspect.isabstract(ObjectUnionOf_A_B)


def test_objectunionof_a_b_constructor_exists():
    assert callable(ObjectUnionOf_A_B.__init__)


def test_objectunionof_a_b_constructor_args():
    sig = inspect.signature(ObjectUnionOf_A_B.__init__)
    params = list(sig.parameters.keys())



def test_tests_b_is_not_abstract():
    assert not inspect.isabstract(tests_B)


def test_tests_b_constructor_exists():
    assert callable(tests_B.__init__)


def test_tests_b_constructor_args():
    sig = inspect.signature(tests_B.__init__)
    params = list(sig.parameters.keys())



def test_tests_a_is_not_abstract():
    assert not inspect.isabstract(tests_A)


def test_tests_a_constructor_exists():
    assert callable(tests_A.__init__)


def test_tests_a_constructor_args():
    sig = inspect.signature(tests_A.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_tests_objectintersectionof_a_c_is_not_abstract():
    assert not inspect.isabstract(tests_ObjectIntersectionOf_A_C)


def test_tests_objectintersectionof_a_c_constructor_exists():
    assert callable(tests_ObjectIntersectionOf_A_C.__init__)


def test_tests_objectintersectionof_a_c_constructor_args():
    sig = inspect.signature(tests_ObjectIntersectionOf_A_C.__init__)
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
tests_ObjectUnionOf_A_B_strategy = st.builds(
    tests_ObjectUnionOf_A_B,
)
tests_C_strategy = st.builds(
    tests_C,
)
ObjectIntersectionOf_A_C_strategy = st.builds(
    ObjectIntersectionOf_A_C,
)
ObjectUnionOf_A_B_strategy = st.builds(
    ObjectUnionOf_A_B,
)
tests_B_strategy = st.builds(
    tests_B,
)
tests_A_strategy = st.builds(
    tests_A,
)
C_strategy = st.builds(
    C,
)
A_strategy = st.builds(
    A,
)
tests_ObjectIntersectionOf_A_C_strategy = st.builds(
    tests_ObjectIntersectionOf_A_C,
)

@given(instance=tests_ObjectUnionOf_A_B_strategy)
@settings(max_examples=50)
def test_tests_objectunionof_a_b_instantiation(instance):
    assert isinstance(instance, tests_ObjectUnionOf_A_B)

@given(instance=tests_C_strategy)
@settings(max_examples=50)
def test_tests_c_instantiation(instance):
    assert isinstance(instance, tests_C)

@given(instance=ObjectIntersectionOf_A_C_strategy)
@settings(max_examples=50)
def test_objectintersectionof_a_c_instantiation(instance):
    assert isinstance(instance, ObjectIntersectionOf_A_C)

@given(instance=ObjectUnionOf_A_B_strategy)
@settings(max_examples=50)
def test_objectunionof_a_b_instantiation(instance):
    assert isinstance(instance, ObjectUnionOf_A_B)

@given(instance=tests_B_strategy)
@settings(max_examples=50)
def test_tests_b_instantiation(instance):
    assert isinstance(instance, tests_B)

@given(instance=tests_A_strategy)
@settings(max_examples=50)
def test_tests_a_instantiation(instance):
    assert isinstance(instance, tests_A)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=tests_ObjectIntersectionOf_A_C_strategy)
@settings(max_examples=50)
def test_tests_objectintersectionof_a_c_instantiation(instance):
    assert isinstance(instance, tests_ObjectIntersectionOf_A_C)
