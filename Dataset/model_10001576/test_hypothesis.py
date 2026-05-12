import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C3,
    C2,
    z,
    R,
    Y,
    C,
    B,
    A,
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



def test_z_is_not_abstract():
    assert not inspect.isabstract(z)


def test_z_constructor_exists():
    assert callable(z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(z.__init__)
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
    assert "attY" in params, "Missing parameter 'attY'"

def test_y_has_attY():
    assert hasattr(Y, "attY")
    descriptor = None
    for klass in Y.__mro__:
        if "attY" in klass.__dict__:
            descriptor = klass.__dict__["attY"]
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
    assert "ATTa" in params, "Missing parameter 'ATTa'"

def test_a_has_ATTa():
    assert hasattr(A, "ATTa")
    descriptor = None
    for klass in A.__mro__:
        if "ATTa" in klass.__dict__:
            descriptor = klass.__dict__["ATTa"]
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
z_strategy = st.builds(
    z,
)
R_strategy = st.builds(
    R,
)
Y_strategy = st.builds(
    Y,
    attY=
        safe_text
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
    ATTa=
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

@given(instance=z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, z)

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)



@given(instance=Y_strategy)
def test_y_attY_setter(instance):
    original = instance.attY
    instance.attY = original
    assert instance.attY == original

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
def test_a_ATTa_setter(instance):
    original = instance.ATTa
    instance.ATTa = original
    assert instance.ATTa == original
