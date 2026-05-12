import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FaultyUMLmodel3_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faultyumlmodel3_a_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel3_A)


def test_faultyumlmodel3_a_constructor_exists():
    assert callable(FaultyUMLmodel3_A.__init__)


def test_faultyumlmodel3_a_constructor_args():
    sig = inspect.signature(FaultyUMLmodel3_A.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "c" in params, "Missing parameter 'c'"
    assert "a" in params, "Missing parameter 'a'"
    assert "d" in params, "Missing parameter 'd'"

def test_faultyumlmodel3_a_has_b():
    assert hasattr(FaultyUMLmodel3_A, "b")
    descriptor = None
    for klass in FaultyUMLmodel3_A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel3_a_has_c():
    assert hasattr(FaultyUMLmodel3_A, "c")
    descriptor = None
    for klass in FaultyUMLmodel3_A.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel3_a_has_a():
    assert hasattr(FaultyUMLmodel3_A, "a")
    descriptor = None
    for klass in FaultyUMLmodel3_A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_faultyumlmodel3_a_has_d():
    assert hasattr(FaultyUMLmodel3_A, "d")
    descriptor = None
    for klass in FaultyUMLmodel3_A.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
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
FaultyUMLmodel3_A_strategy = st.builds(
    FaultyUMLmodel3_A,
    b=
        st.integers(),
    c=
        st.integers(),
    a=
        st.integers(),
    d=
        st.integers()
)

@given(instance=FaultyUMLmodel3_A_strategy)
@settings(max_examples=50)
def test_faultyumlmodel3_a_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel3_A)



@given(instance=FaultyUMLmodel3_A_strategy)
def test_faultyumlmodel3_a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=FaultyUMLmodel3_A_strategy)
def test_faultyumlmodel3_a_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=FaultyUMLmodel3_A_strategy)
def test_faultyumlmodel3_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=FaultyUMLmodel3_A_strategy)
def test_faultyumlmodel3_a_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original
