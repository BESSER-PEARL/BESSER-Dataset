import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    A,
    C21,
    C2,
    C1,
    Z,
    R,
    Y,
    B1,
    A1,
    B,
    C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_c21_is_not_abstract():
    assert not inspect.isabstract(C21)


def test_c21_constructor_exists():
    assert callable(C21.__init__)


def test_c21_constructor_args():
    sig = inspect.signature(C21.__init__)
    params = list(sig.parameters.keys())



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
    assert "attrC1" in params, "Missing parameter 'attrC1'"
    assert "attrC2" in params, "Missing parameter 'attrC2'"

def test_c1_has_attrC1():
    assert hasattr(C1, "attrC1")
    descriptor = None
    for klass in C1.__mro__:
        if "attrC1" in klass.__dict__:
            descriptor = klass.__dict__["attrC1"]
            break
    assert isinstance(descriptor, property)

def test_c1_has_attrC2():
    assert hasattr(C1, "attrC2")
    descriptor = None
    for klass in C1.__mro__:
        if "attrC2" in klass.__dict__:
            descriptor = klass.__dict__["attrC2"]
            break
    assert isinstance(descriptor, property)



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_r_is_not_abstract():
    assert not inspect.isabstract(R)


def test_r_constructor_exists():
    assert callable(R.__init__)


def test_r_constructor_args():
    sig = inspect.signature(R.__init__)
    params = list(sig.parameters.keys())



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())
    assert "attry" in params, "Missing parameter 'attry'"

def test_y_has_attry():
    assert hasattr(Y, "attry")
    descriptor = None
    for klass in Y.__mro__:
        if "attry" in klass.__dict__:
            descriptor = klass.__dict__["attry"]
            break
    assert isinstance(descriptor, property)



def test_b1_is_not_abstract():
    assert not inspect.isabstract(B1)


def test_b1_constructor_exists():
    assert callable(B1.__init__)


def test_b1_constructor_args():
    sig = inspect.signature(B1.__init__)
    params = list(sig.parameters.keys())
    assert "attrB" in params, "Missing parameter 'attrB'"

def test_b1_has_attrB():
    assert hasattr(B1, "attrB")
    descriptor = None
    for klass in B1.__mro__:
        if "attrB" in klass.__dict__:
            descriptor = klass.__dict__["attrB"]
            break
    assert isinstance(descriptor, property)



def test_a1_is_not_abstract():
    assert not inspect.isabstract(A1)


def test_a1_constructor_exists():
    assert callable(A1.__init__)


def test_a1_constructor_args():
    sig = inspect.signature(A1.__init__)
    params = list(sig.parameters.keys())
    assert "attrA" in params, "Missing parameter 'attrA'"

def test_a1_has_attrA():
    assert hasattr(A1, "attrA")
    descriptor = None
    for klass in A1.__mro__:
        if "attrA" in klass.__dict__:
            descriptor = klass.__dict__["attrA"]
            break
    assert isinstance(descriptor, property)



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())
    assert "attB" in params, "Missing parameter 'attB'"

def test_b_has_attB():
    assert hasattr(B, "attB")
    descriptor = None
    for klass in B.__mro__:
        if "attB" in klass.__dict__:
            descriptor = klass.__dict__["attB"]
            break
    assert isinstance(descriptor, property)



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())
    assert "attC1" in params, "Missing parameter 'attC1'"
    assert "attrC2" in params, "Missing parameter 'attrC2'"

def test_c_has_attC1():
    assert hasattr(C, "attC1")
    descriptor = None
    for klass in C.__mro__:
        if "attC1" in klass.__dict__:
            descriptor = klass.__dict__["attC1"]
            break
    assert isinstance(descriptor, property)

def test_c_has_attrC2():
    assert hasattr(C, "attrC2")
    descriptor = None
    for klass in C.__mro__:
        if "attrC2" in klass.__dict__:
            descriptor = klass.__dict__["attrC2"]
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
A_strategy = st.builds(
    A,
    attA=
        safe_text
)
C21_strategy = st.builds(
    C21,
)
C2_strategy = st.builds(
    C2,
)
C1_strategy = st.builds(
    C1,
    attrC1=
        st.integers(),
    attrC2=
        st.booleans()
)
Z_strategy = st.builds(
    Z,
)
R_strategy = st.builds(
    R,
)
Y_strategy = st.builds(
    Y,
    attry=
        safe_text
)
B1_strategy = st.builds(
    B1,
    attrB=
        st.integers()
)
A1_strategy = st.builds(
    A1,
    attrA=
        safe_text
)
B_strategy = st.builds(
    B,
    attB=
        safe_text
)
C_strategy = st.builds(
    C,
    attC1=
        st.integers(),
    attrC2=
        st.booleans()
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original

@given(instance=C21_strategy)
@settings(max_examples=50)
def test_c21_instantiation(instance):
    assert isinstance(instance, C21)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=C1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, C1)



@given(instance=C1_strategy)
def test_c1_attrC1_setter(instance):
    original = instance.attrC1
    instance.attrC1 = original
    assert instance.attrC1 == original



@given(instance=C1_strategy)
def test_c1_attrC2_setter(instance):
    original = instance.attrC2
    instance.attrC2 = original
    assert instance.attrC2 == original

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)



@given(instance=Y_strategy)
def test_y_attry_setter(instance):
    original = instance.attry
    instance.attry = original
    assert instance.attry == original

@given(instance=B1_strategy)
@settings(max_examples=50)
def test_b1_instantiation(instance):
    assert isinstance(instance, B1)



@given(instance=B1_strategy)
def test_b1_attrB_setter(instance):
    original = instance.attrB
    instance.attrB = original
    assert instance.attrB == original

@given(instance=A1_strategy)
@settings(max_examples=50)
def test_a1_instantiation(instance):
    assert isinstance(instance, A1)



@given(instance=A1_strategy)
def test_a1_attrA_setter(instance):
    original = instance.attrA
    instance.attrA = original
    assert instance.attrA == original

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)



@given(instance=B_strategy)
def test_b_attB_setter(instance):
    original = instance.attB
    instance.attB = original
    assert instance.attB == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_attC1_setter(instance):
    original = instance.attC1
    instance.attC1 = original
    assert instance.attC1 == original



@given(instance=C_strategy)
def test_c_attrC2_setter(instance):
    original = instance.attrC2
    instance.attrC2 = original
    assert instance.attrC2 == original
