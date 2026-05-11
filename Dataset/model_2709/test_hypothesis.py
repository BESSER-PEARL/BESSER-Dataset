import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    strictSample::D,
    strictSample::C,
    strictSample::B,
    strictSample::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_strictsample::d_is_not_abstract():
    assert not inspect.isabstract(strictSample::D)


def test_strictsample::d_constructor_exists():
    assert callable(strictSample::D.__init__)


def test_strictsample::d_constructor_args():
    sig = inspect.signature(strictSample::D.__init__)
    params = list(sig.parameters.keys())



def test_strictsample::c_is_not_abstract():
    assert not inspect.isabstract(strictSample::C)


def test_strictsample::c_constructor_exists():
    assert callable(strictSample::C.__init__)


def test_strictsample::c_constructor_args():
    sig = inspect.signature(strictSample::C.__init__)
    params = list(sig.parameters.keys())



def test_strictsample::b_is_not_abstract():
    assert not inspect.isabstract(strictSample::B)


def test_strictsample::b_constructor_exists():
    assert callable(strictSample::B.__init__)


def test_strictsample::b_constructor_args():
    sig = inspect.signature(strictSample::B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_strictsample::b_has_b():
    assert hasattr(strictSample::B, "b")
    descriptor = None
    for klass in strictSample::B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_strictsample::a_is_not_abstract():
    assert not inspect.isabstract(strictSample::A)


def test_strictsample::a_constructor_exists():
    assert callable(strictSample::A.__init__)


def test_strictsample::a_constructor_args():
    sig = inspect.signature(strictSample::A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_strictsample::a_has_a():
    assert hasattr(strictSample::A, "a")
    descriptor = None
    for klass in strictSample::A.__mro__:
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
strictSample::D_strategy = st.builds(
    strictSample::D,
)
strictSample::C_strategy = st.builds(
    strictSample::C,
)
strictSample::B_strategy = st.builds(
    strictSample::B,
    b=
        safe_text
)
strictSample::A_strategy = st.builds(
    strictSample::A,
    a=
        safe_text
)

@given(instance=strictSample::D_strategy)
@settings(max_examples=50)
def test_strictsample::d_instantiation(instance):
    assert isinstance(instance, strictSample::D)

@given(instance=strictSample::C_strategy)
@settings(max_examples=50)
def test_strictsample::c_instantiation(instance):
    assert isinstance(instance, strictSample::C)

@given(instance=strictSample::B_strategy)
@settings(max_examples=50)
def test_strictsample::b_instantiation(instance):
    assert isinstance(instance, strictSample::B)

@given(instance=strictSample::B_strategy)
def test_strictsample::b_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=strictSample::B_strategy)
def test_strictsample::b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=strictSample::A_strategy)
@settings(max_examples=50)
def test_strictsample::a_instantiation(instance):
    assert isinstance(instance, strictSample::A)

@given(instance=strictSample::A_strategy)
def test_strictsample::a_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=strictSample::A_strategy)
def test_strictsample::a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
