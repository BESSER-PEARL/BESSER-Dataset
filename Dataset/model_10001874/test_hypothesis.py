import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C3,
    C2,
    C,
    Z,
    B,
    A,
    r,
    y,
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
    assert "attc2" in params, "Missing parameter 'attc2'"
    assert "attc1" in params, "Missing parameter 'attc1'"

def test_c_has_attc2():
    assert hasattr(C, "attc2")
    descriptor = None
    for klass in C.__mro__:
        if "attc2" in klass.__dict__:
            descriptor = klass.__dict__["attc2"]
            break
    assert isinstance(descriptor, property)

def test_c_has_attc1():
    assert hasattr(C, "attc1")
    descriptor = None
    for klass in C.__mro__:
        if "attc1" in klass.__dict__:
            descriptor = klass.__dict__["attc1"]
            break
    assert isinstance(descriptor, property)



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())
    assert "attb" in params, "Missing parameter 'attb'"

def test_b_has_attb():
    assert hasattr(B, "attb")
    descriptor = None
    for klass in B.__mro__:
        if "attb" in klass.__dict__:
            descriptor = klass.__dict__["attb"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())
    assert "attA" in params, "Missing parameter 'attA'"

def test_a_has_attA():
    assert hasattr(A, "attA")
    descriptor = None
    for klass in A.__mro__:
        if "attA" in klass.__dict__:
            descriptor = klass.__dict__["attA"]
            break
    assert isinstance(descriptor, property)



def test_r_is_not_abstract():
    assert not inspect.isabstract(r)


def test_r_constructor_exists():
    assert callable(r.__init__)


def test_r_constructor_args():
    sig = inspect.signature(r.__init__)
    params = list(sig.parameters.keys())



def test_y_is_not_abstract():
    assert not inspect.isabstract(y)


def test_y_constructor_exists():
    assert callable(y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(y.__init__)
    params = list(sig.parameters.keys())
    assert "attY" in params, "Missing parameter 'attY'"

def test_y_has_attY():
    assert hasattr(y, "attY")
    descriptor = None
    for klass in y.__mro__:
        if "attY" in klass.__dict__:
            descriptor = klass.__dict__["attY"]
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
)
C2_strategy = st.builds(
    C2,
)
C_strategy = st.builds(
    C,
    attc2=
        st.booleans(),
    attc1=
        st.integers()
)
Z_strategy = st.builds(
    Z,
)
B_strategy = st.builds(
    B,
    attb=
        st.integers()
)
A_strategy = st.builds(
    A,
    attA=
        safe_text
)
r_strategy = st.builds(
    r,
)
y_strategy = st.builds(
    y,
    attY=
        safe_text
)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_attc2_setter(instance):
    original = instance.attc2
    instance.attc2 = original
    assert instance.attc2 == original



@given(instance=C_strategy)
def test_c_attc1_setter(instance):
    original = instance.attc1
    instance.attc1 = original
    assert instance.attc1 == original

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)



@given(instance=B_strategy)
def test_b_attb_setter(instance):
    original = instance.attb
    instance.attb = original
    assert instance.attb == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original

@given(instance=r_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, r)

@given(instance=y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, y)



@given(instance=y_strategy)
def test_y_attY_setter(instance):
    original = instance.attY
    instance.attY = original
    assert instance.attY == original
