import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FaultyUMLmodel3::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faultyumlmodel3::a_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel3::A)


def test_faultyumlmodel3::a_constructor_exists():
    assert callable(FaultyUMLmodel3::A.__init__)


def test_faultyumlmodel3::a_constructor_args():
    sig = inspect.signature(FaultyUMLmodel3::A.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"
    assert "a" in params, "Missing parameter 'a'"
    assert "b" in params, "Missing parameter 'b'"
    assert "c" in params, "Missing parameter 'c'"

def test_faultyumlmodel3::a_has_d():
    assert hasattr(FaultyUMLmodel3::A, "d")
    descriptor = None
    for klass in FaultyUMLmodel3::A.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel3::a_has_a():
    assert hasattr(FaultyUMLmodel3::A, "a")
    descriptor = None
    for klass in FaultyUMLmodel3::A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel3::a_has_b():
    assert hasattr(FaultyUMLmodel3::A, "b")
    descriptor = None
    for klass in FaultyUMLmodel3::A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel3::a_has_c():
    assert hasattr(FaultyUMLmodel3::A, "c")
    descriptor = None
    for klass in FaultyUMLmodel3::A.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
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
FaultyUMLmodel3::A_strategy = st.builds(
    FaultyUMLmodel3::A,
    d=
        st.integers(),
    a=
        st.integers(),
    b=
        st.integers(),
    c=
        st.integers()
)

@given(instance=FaultyUMLmodel3::A_strategy)
@settings(max_examples=50)
def test_faultyumlmodel3::a_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel3::A)

@given(instance=FaultyUMLmodel3::A_strategy)
def test_faultyumlmodel3::a_d_type(instance):
    assert isinstance(instance.d, int)


@given(instance=FaultyUMLmodel3::A_strategy)
def test_faultyumlmodel3::a_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=FaultyUMLmodel3::A_strategy)
def test_faultyumlmodel3::a_a_type(instance):
    assert isinstance(instance.a, int)


@given(instance=FaultyUMLmodel3::A_strategy)
def test_faultyumlmodel3::a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=FaultyUMLmodel3::A_strategy)
def test_faultyumlmodel3::a_b_type(instance):
    assert isinstance(instance.b, int)


@given(instance=FaultyUMLmodel3::A_strategy)
def test_faultyumlmodel3::a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=FaultyUMLmodel3::A_strategy)
def test_faultyumlmodel3::a_c_type(instance):
    assert isinstance(instance.c, int)


@given(instance=FaultyUMLmodel3::A_strategy)
def test_faultyumlmodel3::a_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original
