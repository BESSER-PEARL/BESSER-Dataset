import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tests::ObjectUnionOf::A::B,
    tests::C,
    ObjectIntersectionOf::A::C,
    ObjectUnionOf::A::B,
    tests::B,
    tests::A,
    C,
    A,
    tests::ObjectIntersectionOf::A::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tests::objectunionof::a::b_is_not_abstract():
    assert not inspect.isabstract(tests::ObjectUnionOf::A::B)


def test_tests::objectunionof::a::b_constructor_exists():
    assert callable(tests::ObjectUnionOf::A::B.__init__)


def test_tests::objectunionof::a::b_constructor_args():
    sig = inspect.signature(tests::ObjectUnionOf::A::B.__init__)
    params = list(sig.parameters.keys())



def test_tests::c_is_not_abstract():
    assert not inspect.isabstract(tests::C)


def test_tests::c_constructor_exists():
    assert callable(tests::C.__init__)


def test_tests::c_constructor_args():
    sig = inspect.signature(tests::C.__init__)
    params = list(sig.parameters.keys())



def test_objectintersectionof::a::c_is_not_abstract():
    assert not inspect.isabstract(ObjectIntersectionOf::A::C)


def test_objectintersectionof::a::c_constructor_exists():
    assert callable(ObjectIntersectionOf::A::C.__init__)


def test_objectintersectionof::a::c_constructor_args():
    sig = inspect.signature(ObjectIntersectionOf::A::C.__init__)
    params = list(sig.parameters.keys())



def test_objectunionof::a::b_is_not_abstract():
    assert not inspect.isabstract(ObjectUnionOf::A::B)


def test_objectunionof::a::b_constructor_exists():
    assert callable(ObjectUnionOf::A::B.__init__)


def test_objectunionof::a::b_constructor_args():
    sig = inspect.signature(ObjectUnionOf::A::B.__init__)
    params = list(sig.parameters.keys())



def test_tests::b_is_not_abstract():
    assert not inspect.isabstract(tests::B)


def test_tests::b_constructor_exists():
    assert callable(tests::B.__init__)


def test_tests::b_constructor_args():
    sig = inspect.signature(tests::B.__init__)
    params = list(sig.parameters.keys())



def test_tests::a_is_not_abstract():
    assert not inspect.isabstract(tests::A)


def test_tests::a_constructor_exists():
    assert callable(tests::A.__init__)


def test_tests::a_constructor_args():
    sig = inspect.signature(tests::A.__init__)
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



def test_tests::objectintersectionof::a::c_is_not_abstract():
    assert not inspect.isabstract(tests::ObjectIntersectionOf::A::C)


def test_tests::objectintersectionof::a::c_constructor_exists():
    assert callable(tests::ObjectIntersectionOf::A::C.__init__)


def test_tests::objectintersectionof::a::c_constructor_args():
    sig = inspect.signature(tests::ObjectIntersectionOf::A::C.__init__)
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
tests::ObjectUnionOf::A::B_strategy = st.builds(
    tests::ObjectUnionOf::A::B,
)
tests::C_strategy = st.builds(
    tests::C,
)
ObjectIntersectionOf::A::C_strategy = st.builds(
    ObjectIntersectionOf::A::C,
)
ObjectUnionOf::A::B_strategy = st.builds(
    ObjectUnionOf::A::B,
)
tests::B_strategy = st.builds(
    tests::B,
)
tests::A_strategy = st.builds(
    tests::A,
)
C_strategy = st.builds(
    C,
)
A_strategy = st.builds(
    A,
)
tests::ObjectIntersectionOf::A::C_strategy = st.builds(
    tests::ObjectIntersectionOf::A::C,
)

@given(instance=tests::ObjectUnionOf::A::B_strategy)
@settings(max_examples=50)
def test_tests::objectunionof::a::b_instantiation(instance):
    assert isinstance(instance, tests::ObjectUnionOf::A::B)

@given(instance=tests::C_strategy)
@settings(max_examples=50)
def test_tests::c_instantiation(instance):
    assert isinstance(instance, tests::C)

@given(instance=ObjectIntersectionOf::A::C_strategy)
@settings(max_examples=50)
def test_objectintersectionof::a::c_instantiation(instance):
    assert isinstance(instance, ObjectIntersectionOf::A::C)

@given(instance=ObjectUnionOf::A::B_strategy)
@settings(max_examples=50)
def test_objectunionof::a::b_instantiation(instance):
    assert isinstance(instance, ObjectUnionOf::A::B)

@given(instance=tests::B_strategy)
@settings(max_examples=50)
def test_tests::b_instantiation(instance):
    assert isinstance(instance, tests::B)

@given(instance=tests::A_strategy)
@settings(max_examples=50)
def test_tests::a_instantiation(instance):
    assert isinstance(instance, tests::A)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=tests::ObjectIntersectionOf::A::C_strategy)
@settings(max_examples=50)
def test_tests::objectintersectionof::a::c_instantiation(instance):
    assert isinstance(instance, tests::ObjectIntersectionOf::A::C)
