import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::C,
    test::B,
    test::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::c_is_not_abstract():
    assert not inspect.isabstract(test::C)


def test_test::c_constructor_exists():
    assert callable(test::C.__init__)


def test_test::c_constructor_args():
    sig = inspect.signature(test::C.__init__)
    params = list(sig.parameters.keys())



def test_test::b_is_not_abstract():
    assert not inspect.isabstract(test::B)


def test_test::b_constructor_exists():
    assert callable(test::B.__init__)


def test_test::b_constructor_args():
    sig = inspect.signature(test::B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_test::b_has_b():
    assert hasattr(test::B, "b")
    descriptor = None
    for klass in test::B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_test::a_is_not_abstract():
    assert not inspect.isabstract(test::A)


def test_test::a_constructor_exists():
    assert callable(test::A.__init__)


def test_test::a_constructor_args():
    sig = inspect.signature(test::A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_test::a_has_a():
    assert hasattr(test::A, "a")
    descriptor = None
    for klass in test::A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)


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
test::C_strategy = st.builds(
    test::C,
)
test::B_strategy = st.builds(
    test::B,
    b=
        safe_text
)
test::A_strategy = st.builds(
    test::A,
    a=
        safe_text
)

@given(instance=test::C_strategy)
@settings(max_examples=50)
def test_test::c_instantiation(instance):
    assert isinstance(instance, test::C)

@given(instance=test::B_strategy)
@settings(max_examples=50)
def test_test::b_instantiation(instance):
    assert isinstance(instance, test::B)

@given(instance=test::B_strategy)
def test_test::b_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=test::B_strategy)
def test_test::b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=test::A_strategy)
@settings(max_examples=50)
def test_test::a_instantiation(instance):
    assert isinstance(instance, test::A)

@given(instance=test::A_strategy)
def test_test::a_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=test::A_strategy)
def test_test::a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
