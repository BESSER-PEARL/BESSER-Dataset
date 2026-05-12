import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_C,
    test_B,
    test_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_c_is_not_abstract():
    assert not inspect.isabstract(test_C)


def test_test_c_constructor_exists():
    assert callable(test_C.__init__)


def test_test_c_constructor_args():
    sig = inspect.signature(test_C.__init__)
    params = list(sig.parameters.keys())



def test_test_b_is_not_abstract():
    assert not inspect.isabstract(test_B)


def test_test_b_constructor_exists():
    assert callable(test_B.__init__)


def test_test_b_constructor_args():
    sig = inspect.signature(test_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_test_b_has_b():
    assert hasattr(test_B, "b")
    descriptor = None
    for klass in test_B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_test_a_is_not_abstract():
    assert not inspect.isabstract(test_A)


def test_test_a_constructor_exists():
    assert callable(test_A.__init__)


def test_test_a_constructor_args():
    sig = inspect.signature(test_A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_test_a_has_a():
    assert hasattr(test_A, "a")
    descriptor = None
    for klass in test_A.__mro__:
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
test_C_strategy = st.builds(
    test_C,
)
test_B_strategy = st.builds(
    test_B,
    b=
        safe_text
)
test_A_strategy = st.builds(
    test_A,
    a=
        safe_text
)

@given(instance=test_C_strategy)
@settings(max_examples=50)
def test_test_c_instantiation(instance):
    assert isinstance(instance, test_C)

@given(instance=test_B_strategy)
@settings(max_examples=50)
def test_test_b_instantiation(instance):
    assert isinstance(instance, test_B)



@given(instance=test_B_strategy)
def test_test_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=test_A_strategy)
@settings(max_examples=50)
def test_test_a_instantiation(instance):
    assert isinstance(instance, test_A)



@given(instance=test_A_strategy)
def test_test_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
