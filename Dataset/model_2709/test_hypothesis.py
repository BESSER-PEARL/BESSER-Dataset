import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    strictSample_D,
    strictSample_C,
    strictSample_B,
    strictSample_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_strictsample_d_is_not_abstract():
    assert not inspect.isabstract(strictSample_D)


def test_strictsample_d_constructor_exists():
    assert callable(strictSample_D.__init__)


def test_strictsample_d_constructor_args():
    sig = inspect.signature(strictSample_D.__init__)
    params = list(sig.parameters.keys())



def test_strictsample_c_is_not_abstract():
    assert not inspect.isabstract(strictSample_C)


def test_strictsample_c_constructor_exists():
    assert callable(strictSample_C.__init__)


def test_strictsample_c_constructor_args():
    sig = inspect.signature(strictSample_C.__init__)
    params = list(sig.parameters.keys())



def test_strictsample_b_is_not_abstract():
    assert not inspect.isabstract(strictSample_B)


def test_strictsample_b_constructor_exists():
    assert callable(strictSample_B.__init__)


def test_strictsample_b_constructor_args():
    sig = inspect.signature(strictSample_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_strictsample_b_has_b():
    assert hasattr(strictSample_B, "b")
    descriptor = None
    for klass in strictSample_B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_strictsample_a_is_not_abstract():
    assert not inspect.isabstract(strictSample_A)


def test_strictsample_a_constructor_exists():
    assert callable(strictSample_A.__init__)


def test_strictsample_a_constructor_args():
    sig = inspect.signature(strictSample_A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_strictsample_a_has_a():
    assert hasattr(strictSample_A, "a")
    descriptor = None
    for klass in strictSample_A.__mro__:
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
strictSample_D_strategy = st.builds(
    strictSample_D,
)
strictSample_C_strategy = st.builds(
    strictSample_C,
)
strictSample_B_strategy = st.builds(
    strictSample_B,
    b=
        safe_text
)
strictSample_A_strategy = st.builds(
    strictSample_A,
    a=
        safe_text
)

@given(instance=strictSample_D_strategy)
@settings(max_examples=50)
def test_strictsample_d_instantiation(instance):
    assert isinstance(instance, strictSample_D)

@given(instance=strictSample_C_strategy)
@settings(max_examples=50)
def test_strictsample_c_instantiation(instance):
    assert isinstance(instance, strictSample_C)

@given(instance=strictSample_B_strategy)
@settings(max_examples=50)
def test_strictsample_b_instantiation(instance):
    assert isinstance(instance, strictSample_B)



@given(instance=strictSample_B_strategy)
def test_strictsample_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=strictSample_A_strategy)
@settings(max_examples=50)
def test_strictsample_a_instantiation(instance):
    assert isinstance(instance, strictSample_A)



@given(instance=strictSample_A_strategy)
def test_strictsample_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
