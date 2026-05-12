import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C3,
    C2,
    C1,
    S1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c3_is_not_abstract():
    assert not inspect.isabstract(C3)


def test_c3_constructor_exists():
    assert callable(C3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(C3.__init__)
    params = list(sig.parameters.keys())
    assert "Integer_k" in params, "Missing parameter 'Integer_k'"
    assert "long_m" in params, "Missing parameter 'long_m'"

def test_c3_has_Integer_k():
    assert hasattr(C3, "Integer_k")
    descriptor = None
    for klass in C3.__mro__:
        if "Integer_k" in klass.__dict__:
            descriptor = klass.__dict__["Integer_k"]
            break
    assert isinstance(descriptor, property)

def test_c3_has_long_m():
    assert hasattr(C3, "long_m")
    descriptor = None
    for klass in C3.__mro__:
        if "long_m" in klass.__dict__:
            descriptor = klass.__dict__["long_m"]
            break
    assert isinstance(descriptor, property)



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_c1_is_not_abstract():
    assert not inspect.isabstract(C1)


def test_c1_constructor_exists():
    assert callable(C1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(C1.__init__)
    params = list(sig.parameters.keys())



def test_s1_is_not_abstract():
    assert not inspect.isabstract(S1)


def test_s1_constructor_exists():
    assert callable(S1.__init__)


def test_s1_constructor_args():
    sig = inspect.signature(S1.__init__)
    params = list(sig.parameters.keys())
    assert "double_v2" in params, "Missing parameter 'double_v2'"
    assert "static_int_v1" in params, "Missing parameter 'static_int_v1'"

def test_s1_has_double_v2():
    assert hasattr(S1, "double_v2")
    descriptor = None
    for klass in S1.__mro__:
        if "double_v2" in klass.__dict__:
            descriptor = klass.__dict__["double_v2"]
            break
    assert isinstance(descriptor, property)

def test_s1_has_static_int_v1():
    assert hasattr(S1, "static_int_v1")
    descriptor = None
    for klass in S1.__mro__:
        if "static_int_v1" in klass.__dict__:
            descriptor = klass.__dict__["static_int_v1"]
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
C3_strategy = st.builds(
    C3,
    Integer_k=
        st.integers(),
    long_m=
        safe_text
)
C2_strategy = st.builds(
    C2,
)
C1_strategy = st.builds(
    C1,
)
S1_strategy = st.builds(
    S1,
    double_v2=
        safe_text,
    static_int_v1=
        safe_text
)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)



@given(instance=C3_strategy)
def test_c3_Integer_k_setter(instance):
    original = instance.Integer_k
    instance.Integer_k = original
    assert instance.Integer_k == original



@given(instance=C3_strategy)
def test_c3_long_m_setter(instance):
    original = instance.long_m
    instance.long_m = original
    assert instance.long_m == original

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=C1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, C1)

@given(instance=S1_strategy)
@settings(max_examples=50)
def test_s1_instantiation(instance):
    assert isinstance(instance, S1)



@given(instance=S1_strategy)
def test_s1_double_v2_setter(instance):
    original = instance.double_v2
    instance.double_v2 = original
    assert instance.double_v2 == original



@given(instance=S1_strategy)
def test_s1_static_int_v1_setter(instance):
    original = instance.static_int_v1
    instance.static_int_v1 = original
    assert instance.static_int_v1 == original
