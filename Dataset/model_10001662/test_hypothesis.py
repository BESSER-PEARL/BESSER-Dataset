import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    c3,
    c2,
    c,
    B1,
    Z,
    A1,
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
    assert not inspect.isabstract(c3)


def test_c3_constructor_exists():
    assert callable(c3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(c3.__init__)
    params = list(sig.parameters.keys())



def test_c2_is_not_abstract():
    assert not inspect.isabstract(c2)


def test_c2_constructor_exists():
    assert callable(c2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(c2.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(c)


def test_c_constructor_exists():
    assert callable(c.__init__)


def test_c_constructor_args():
    sig = inspect.signature(c.__init__)
    params = list(sig.parameters.keys())
    assert "att2" in params, "Missing parameter 'att2'"
    assert "att1" in params, "Missing parameter 'att1'"

def test_c_has_att2():
    assert hasattr(c, "att2")
    descriptor = None
    for klass in c.__mro__:
        if "att2" in klass.__dict__:
            descriptor = klass.__dict__["att2"]
            break
    assert isinstance(descriptor, property)

def test_c_has_att1():
    assert hasattr(c, "att1")
    descriptor = None
    for klass in c.__mro__:
        if "att1" in klass.__dict__:
            descriptor = klass.__dict__["att1"]
            break
    assert isinstance(descriptor, property)



def test_b1_is_not_abstract():
    assert not inspect.isabstract(B1)


def test_b1_constructor_exists():
    assert callable(B1.__init__)


def test_b1_constructor_args():
    sig = inspect.signature(B1.__init__)
    params = list(sig.parameters.keys())
    assert "attb" in params, "Missing parameter 'attb'"

def test_b1_has_attb():
    assert hasattr(B1, "attb")
    descriptor = None
    for klass in B1.__mro__:
        if "attb" in klass.__dict__:
            descriptor = klass.__dict__["attb"]
            break
    assert isinstance(descriptor, property)



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_a1_is_not_abstract():
    assert not inspect.isabstract(A1)


def test_a1_constructor_exists():
    assert callable(A1.__init__)


def test_a1_constructor_args():
    sig = inspect.signature(A1.__init__)
    params = list(sig.parameters.keys())
    assert "atta" in params, "Missing parameter 'atta'"

def test_a1_has_atta():
    assert hasattr(A1, "atta")
    descriptor = None
    for klass in A1.__mro__:
        if "atta" in klass.__dict__:
            descriptor = klass.__dict__["atta"]
            break
    assert isinstance(descriptor, property)



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
    assert "atty" in params, "Missing parameter 'atty'"

def test_y_has_atty():
    assert hasattr(Y, "atty")
    descriptor = None
    for klass in Y.__mro__:
        if "atty" in klass.__dict__:
            descriptor = klass.__dict__["atty"]
            break
    assert isinstance(descriptor, property)



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())
    assert "att1" in params, "Missing parameter 'att1'"
    assert "att2" in params, "Missing parameter 'att2'"

def test_c_has_att1():
    assert hasattr(C, "att1")
    descriptor = None
    for klass in C.__mro__:
        if "att1" in klass.__dict__:
            descriptor = klass.__dict__["att1"]
            break
    assert isinstance(descriptor, property)

def test_c_has_att2():
    assert hasattr(C, "att2")
    descriptor = None
    for klass in C.__mro__:
        if "att2" in klass.__dict__:
            descriptor = klass.__dict__["att2"]
            break
    assert isinstance(descriptor, property)



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
    assert "atta" in params, "Missing parameter 'atta'"

def test_a_has_atta():
    assert hasattr(A, "atta")
    descriptor = None
    for klass in A.__mro__:
        if "atta" in klass.__dict__:
            descriptor = klass.__dict__["atta"]
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
c3_strategy = st.builds(
    c3,
)
c2_strategy = st.builds(
    c2,
)
c_strategy = st.builds(
    c,
    att2=
        st.booleans(),
    att1=
        st.integers()
)
B1_strategy = st.builds(
    B1,
    attb=
        st.integers()
)
Z_strategy = st.builds(
    Z,
)
A1_strategy = st.builds(
    A1,
    atta=
        safe_text
)
R_strategy = st.builds(
    R,
)
Y_strategy = st.builds(
    Y,
    atty=
        safe_text
)
C_strategy = st.builds(
    C,
    att1=
        st.integers(),
    att2=
        st.booleans()
)
B_strategy = st.builds(
    B,
    attb=
        st.integers()
)
A_strategy = st.builds(
    A,
    atta=
        safe_text
)

@given(instance=c3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, c3)

@given(instance=c2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, c2)

@given(instance=c_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, c)



@given(instance=c_strategy)
def test_c_att2_setter(instance):
    original = instance.att2
    instance.att2 = original
    assert instance.att2 == original



@given(instance=c_strategy)
def test_c_att1_setter(instance):
    original = instance.att1
    instance.att1 = original
    assert instance.att1 == original

@given(instance=B1_strategy)
@settings(max_examples=50)
def test_b1_instantiation(instance):
    assert isinstance(instance, B1)



@given(instance=B1_strategy)
def test_b1_attb_setter(instance):
    original = instance.attb
    instance.attb = original
    assert instance.attb == original

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=A1_strategy)
@settings(max_examples=50)
def test_a1_instantiation(instance):
    assert isinstance(instance, A1)



@given(instance=A1_strategy)
def test_a1_atta_setter(instance):
    original = instance.atta
    instance.atta = original
    assert instance.atta == original

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)



@given(instance=Y_strategy)
def test_y_atty_setter(instance):
    original = instance.atty
    instance.atty = original
    assert instance.atty == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_att1_setter(instance):
    original = instance.att1
    instance.att1 = original
    assert instance.att1 == original



@given(instance=C_strategy)
def test_c_att2_setter(instance):
    original = instance.att2
    instance.att2 = original
    assert instance.att2 == original

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
def test_a_atta_setter(instance):
    original = instance.atta
    instance.atta = original
    assert instance.atta == original
