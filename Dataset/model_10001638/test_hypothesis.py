import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Z1,
    C3,
    C2,
    Z,
    Y,
    R,
    B,
    A,
    C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_z1_is_not_abstract():
    assert not inspect.isabstract(Z1)


def test_z1_constructor_exists():
    assert callable(Z1.__init__)


def test_z1_constructor_args():
    sig = inspect.signature(Z1.__init__)
    params = list(sig.parameters.keys())



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



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())



def test_r_is_not_abstract():
    assert not inspect.isabstract(R)


def test_r_constructor_exists():
    assert callable(R.__init__)


def test_r_constructor_args():
    sig = inspect.signature(R.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())
    assert "altB" in params, "Missing parameter 'altB'"

def test_b_has_altB():
    assert hasattr(B, "altB")
    descriptor = None
    for klass in B.__mro__:
        if "altB" in klass.__dict__:
            descriptor = klass.__dict__["altB"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())
    assert "altA" in params, "Missing parameter 'altA'"

def test_a_has_altA():
    assert hasattr(A, "altA")
    descriptor = None
    for klass in A.__mro__:
        if "altA" in klass.__dict__:
            descriptor = klass.__dict__["altA"]
            break
    assert isinstance(descriptor, property)



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())
    assert "altC1" in params, "Missing parameter 'altC1'"
    assert "altC2" in params, "Missing parameter 'altC2'"

def test_c_has_altC1():
    assert hasattr(C, "altC1")
    descriptor = None
    for klass in C.__mro__:
        if "altC1" in klass.__dict__:
            descriptor = klass.__dict__["altC1"]
            break
    assert isinstance(descriptor, property)

def test_c_has_altC2():
    assert hasattr(C, "altC2")
    descriptor = None
    for klass in C.__mro__:
        if "altC2" in klass.__dict__:
            descriptor = klass.__dict__["altC2"]
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
Z1_strategy = st.builds(
    Z1,
)
C3_strategy = st.builds(
    C3,
)
C2_strategy = st.builds(
    C2,
)
Z_strategy = st.builds(
    Z,
)
Y_strategy = st.builds(
    Y,
)
R_strategy = st.builds(
    R,
)
B_strategy = st.builds(
    B,
    altB=
        safe_text
)
A_strategy = st.builds(
    A,
    altA=
        safe_text
)
C_strategy = st.builds(
    C,
    altC1=
        st.integers(),
    altC2=
        st.booleans()
)

@given(instance=Z1_strategy)
@settings(max_examples=50)
def test_z1_instantiation(instance):
    assert isinstance(instance, Z1)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)



@given(instance=B_strategy)
def test_b_altB_setter(instance):
    original = instance.altB
    instance.altB = original
    assert instance.altB == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_altA_setter(instance):
    original = instance.altA
    instance.altA = original
    assert instance.altA == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_altC1_setter(instance):
    original = instance.altC1
    instance.altC1 = original
    assert instance.altC1 == original



@given(instance=C_strategy)
def test_c_altC2_setter(instance):
    original = instance.altC2
    instance.altC2 = original
    assert instance.altC2 == original
