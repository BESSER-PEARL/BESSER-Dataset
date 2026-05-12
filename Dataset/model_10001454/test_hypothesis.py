import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    R,
    C3,
    Y,
    Z,
    C2,
    C,
    B,
    A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_r_is_not_abstract():
    assert not inspect.isabstract(R)


def test_r_constructor_exists():
    assert callable(R.__init__)


def test_r_constructor_args():
    sig = inspect.signature(R.__init__)
    params = list(sig.parameters.keys())



def test_c3_is_not_abstract():
    assert not inspect.isabstract(C3)


def test_c3_constructor_exists():
    assert callable(C3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(C3.__init__)
    params = list(sig.parameters.keys())



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())
    assert "Y" in params, "Missing parameter 'Y'"

def test_y_has_Y():
    assert hasattr(Y, "Y")
    descriptor = None
    for klass in Y.__mro__:
        if "Y" in klass.__dict__:
            descriptor = klass.__dict__["Y"]
            break
    assert isinstance(descriptor, property)



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"
    assert "d" in params, "Missing parameter 'd'"

def test_c_has_c():
    assert hasattr(C, "c")
    descriptor = None
    for klass in C.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_c_has_d():
    assert hasattr(C, "d")
    descriptor = None
    for klass in C.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_b_has_b():
    assert hasattr(B, "b")
    descriptor = None
    for klass in B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_a_has_a():
    assert hasattr(A, "a")
    descriptor = None
    for klass in A.__mro__:
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
R_strategy = st.builds(
    R,
)
C3_strategy = st.builds(
    C3,
)
Y_strategy = st.builds(
    Y,
    Y=
        safe_text
)
Z_strategy = st.builds(
    Z,
)
C2_strategy = st.builds(
    C2,
)
C_strategy = st.builds(
    C,
    c=
        st.integers(),
    d=
        st.booleans()
)
B_strategy = st.builds(
    B,
    b=
        st.integers()
)
A_strategy = st.builds(
    A,
    a=
        safe_text
)

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)



@given(instance=Y_strategy)
def test_y_Y_setter(instance):
    original = instance.Y
    instance.Y = original
    assert instance.Y == original

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=C_strategy)
def test_c_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)



@given(instance=B_strategy)
def test_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
