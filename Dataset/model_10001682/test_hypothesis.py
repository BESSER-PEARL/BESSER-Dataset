import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C2,
    Y,
    Z,
    R,
    C,
    B,
    A,
    B2,
    B1,
    A3,
    A2,
    A1,
    Class,
    C3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())



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



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())
    assert "attC1" in params, "Missing parameter 'attC1'"
    assert "attC2" in params, "Missing parameter 'attC2'"

def test_c_has_attC1():
    assert hasattr(C, "attC1")
    descriptor = None
    for klass in C.__mro__:
        if "attC1" in klass.__dict__:
            descriptor = klass.__dict__["attC1"]
            break
    assert isinstance(descriptor, property)

def test_c_has_attC2():
    assert hasattr(C, "attC2")
    descriptor = None
    for klass in C.__mro__:
        if "attC2" in klass.__dict__:
            descriptor = klass.__dict__["attC2"]
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



def test_b2_is_not_abstract():
    assert not inspect.isabstract(B2)


def test_b2_constructor_exists():
    assert callable(B2.__init__)


def test_b2_constructor_args():
    sig = inspect.signature(B2.__init__)
    params = list(sig.parameters.keys())



def test_b1_is_not_abstract():
    assert not inspect.isabstract(B1)


def test_b1_constructor_exists():
    assert callable(B1.__init__)


def test_b1_constructor_args():
    sig = inspect.signature(B1.__init__)
    params = list(sig.parameters.keys())



def test_a3_is_not_abstract():
    assert not inspect.isabstract(A3)


def test_a3_constructor_exists():
    assert callable(A3.__init__)


def test_a3_constructor_args():
    sig = inspect.signature(A3.__init__)
    params = list(sig.parameters.keys())



def test_a2_is_not_abstract():
    assert not inspect.isabstract(A2)


def test_a2_constructor_exists():
    assert callable(A2.__init__)


def test_a2_constructor_args():
    sig = inspect.signature(A2.__init__)
    params = list(sig.parameters.keys())



def test_a1_is_not_abstract():
    assert not inspect.isabstract(A1)


def test_a1_constructor_exists():
    assert callable(A1.__init__)


def test_a1_constructor_args():
    sig = inspect.signature(A1.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "d" in params, "Missing parameter 'd'"

def test_a1_has_b():
    assert hasattr(A1, "b")
    descriptor = None
    for klass in A1.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_a1_has_d():
    assert hasattr(A1, "d")
    descriptor = None
    for klass in A1.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_c3_is_not_abstract():
    assert not inspect.isabstract(C3)


def test_c3_constructor_exists():
    assert callable(C3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(C3.__init__)
    params = list(sig.parameters.keys())


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
C2_strategy = st.builds(
    C2,
)
Y_strategy = st.builds(
    Y,
)
Z_strategy = st.builds(
    Z,
)
R_strategy = st.builds(
    R,
)
C_strategy = st.builds(
    C,
    attC1=
        st.integers(),
    attC2=
        st.booleans()
)
B_strategy = st.builds(
    B,
    attB=
        st.integers()
)
A_strategy = st.builds(
    A,
    attA=
        safe_text
)
B2_strategy = st.builds(
    B2,
)
B1_strategy = st.builds(
    B1,
)
A3_strategy = st.builds(
    A3,
)
A2_strategy = st.builds(
    A2,
)
A1_strategy = st.builds(
    A1,
    b=
        st.booleans(),
    d=
        st.integers()
)
Class_strategy = st.builds(
    Class,
)
C3_strategy = st.builds(
    C3,
)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)

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
def test_c_attC2_setter(instance):
    original = instance.attC2
    instance.attC2 = original
    assert instance.attC2 == original

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)



@given(instance=B_strategy)
def test_b_attB_setter(instance):
    original = instance.attB
    instance.attB = original
    assert instance.attB == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original

@given(instance=B2_strategy)
@settings(max_examples=50)
def test_b2_instantiation(instance):
    assert isinstance(instance, B2)

@given(instance=B1_strategy)
@settings(max_examples=50)
def test_b1_instantiation(instance):
    assert isinstance(instance, B1)

@given(instance=A3_strategy)
@settings(max_examples=50)
def test_a3_instantiation(instance):
    assert isinstance(instance, A3)

@given(instance=A2_strategy)
@settings(max_examples=50)
def test_a2_instantiation(instance):
    assert isinstance(instance, A2)

@given(instance=A1_strategy)
@settings(max_examples=50)
def test_a1_instantiation(instance):
    assert isinstance(instance, A1)



@given(instance=A1_strategy)
def test_a1_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=A1_strategy)
def test_a1_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)
