import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    foo_H,
    I,
    foo_E,
    B,
    foo_D,
    foo_F,
    J,
    foo_C,
    foo_J,
    foo_I,
    foo_B,
    foo_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_foo_h_is_not_abstract():
    assert not inspect.isabstract(foo_H)


def test_foo_h_constructor_exists():
    assert callable(foo_H.__init__)


def test_foo_h_constructor_args():
    sig = inspect.signature(foo_H.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_foo_h_has_EAttribute0():
    assert hasattr(foo_H, "EAttribute0")
    descriptor = None
    for klass in foo_H.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)



def test_i_is_not_abstract():
    assert not inspect.isabstract(I)


def test_i_constructor_exists():
    assert callable(I.__init__)


def test_i_constructor_args():
    sig = inspect.signature(I.__init__)
    params = list(sig.parameters.keys())



def test_foo_e_is_not_abstract():
    assert not inspect.isabstract(foo_E)


def test_foo_e_constructor_exists():
    assert callable(foo_E.__init__)


def test_foo_e_constructor_args():
    sig = inspect.signature(foo_E.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_foo_d_is_not_abstract():
    assert not inspect.isabstract(foo_D)


def test_foo_d_constructor_exists():
    assert callable(foo_D.__init__)


def test_foo_d_constructor_args():
    sig = inspect.signature(foo_D.__init__)
    params = list(sig.parameters.keys())



def test_foo_f_is_not_abstract():
    assert not inspect.isabstract(foo_F)


def test_foo_f_constructor_exists():
    assert callable(foo_F.__init__)


def test_foo_f_constructor_args():
    sig = inspect.signature(foo_F.__init__)
    params = list(sig.parameters.keys())



def test_j_is_not_abstract():
    assert not inspect.isabstract(J)


def test_j_constructor_exists():
    assert callable(J.__init__)


def test_j_constructor_args():
    sig = inspect.signature(J.__init__)
    params = list(sig.parameters.keys())



def test_foo_c_is_not_abstract():
    assert not inspect.isabstract(foo_C)


def test_foo_c_constructor_exists():
    assert callable(foo_C.__init__)


def test_foo_c_constructor_args():
    sig = inspect.signature(foo_C.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute1" in params, "Missing parameter 'EAttribute1'"

def test_foo_c_has_EAttribute1():
    assert hasattr(foo_C, "EAttribute1")
    descriptor = None
    for klass in foo_C.__mro__:
        if "EAttribute1" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute1"]
            break
    assert isinstance(descriptor, property)



def test_foo_j_is_not_abstract():
    assert not inspect.isabstract(foo_J)


def test_foo_j_constructor_exists():
    assert callable(foo_J.__init__)


def test_foo_j_constructor_args():
    sig = inspect.signature(foo_J.__init__)
    params = list(sig.parameters.keys())



def test_foo_i_is_not_abstract():
    assert not inspect.isabstract(foo_I)


def test_foo_i_constructor_exists():
    assert callable(foo_I.__init__)


def test_foo_i_constructor_args():
    sig = inspect.signature(foo_I.__init__)
    params = list(sig.parameters.keys())



def test_foo_b_is_not_abstract():
    assert not inspect.isabstract(foo_B)


def test_foo_b_constructor_exists():
    assert callable(foo_B.__init__)


def test_foo_b_constructor_args():
    sig = inspect.signature(foo_B.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_foo_b_has_EAttribute0():
    assert hasattr(foo_B, "EAttribute0")
    descriptor = None
    for klass in foo_B.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)



def test_foo_a_is_not_abstract():
    assert not inspect.isabstract(foo_A)


def test_foo_a_constructor_exists():
    assert callable(foo_A.__init__)


def test_foo_a_constructor_args():
    sig = inspect.signature(foo_A.__init__)
    params = list(sig.parameters.keys())
    assert "fooA" in params, "Missing parameter 'fooA'"
    assert "fooo" in params, "Missing parameter 'fooo'"

def test_foo_a_has_fooA():
    assert hasattr(foo_A, "fooA")
    descriptor = None
    for klass in foo_A.__mro__:
        if "fooA" in klass.__dict__:
            descriptor = klass.__dict__["fooA"]
            break
    assert isinstance(descriptor, property)

def test_foo_a_has_fooo():
    assert hasattr(foo_A, "fooo")
    descriptor = None
    for klass in foo_A.__mro__:
        if "fooo" in klass.__dict__:
            descriptor = klass.__dict__["fooo"]
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
foo_H_strategy = st.builds(
    foo_H,
    EAttribute0=
        safe_text
)
I_strategy = st.builds(
    I,
)
foo_E_strategy = st.builds(
    foo_E,
)
B_strategy = st.builds(
    B,
)
foo_D_strategy = st.builds(
    foo_D,
)
foo_F_strategy = st.builds(
    foo_F,
)
J_strategy = st.builds(
    J,
)
foo_C_strategy = st.builds(
    foo_C,
    EAttribute1=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
foo_J_strategy = st.builds(
    foo_J,
)
foo_I_strategy = st.builds(
    foo_I,
)
foo_B_strategy = st.builds(
    foo_B,
    EAttribute0=
        st.booleans()
)
foo_A_strategy = st.builds(
    foo_A,
    fooA=
        st.booleans(),
    fooo=
        safe_text
)

@given(instance=foo_H_strategy)
@settings(max_examples=50)
def test_foo_h_instantiation(instance):
    assert isinstance(instance, foo_H)



@given(instance=foo_H_strategy)
def test_foo_h_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=I_strategy)
@settings(max_examples=50)
def test_i_instantiation(instance):
    assert isinstance(instance, I)

@given(instance=foo_E_strategy)
@settings(max_examples=50)
def test_foo_e_instantiation(instance):
    assert isinstance(instance, foo_E)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=foo_D_strategy)
@settings(max_examples=50)
def test_foo_d_instantiation(instance):
    assert isinstance(instance, foo_D)

@given(instance=foo_F_strategy)
@settings(max_examples=50)
def test_foo_f_instantiation(instance):
    assert isinstance(instance, foo_F)

@given(instance=J_strategy)
@settings(max_examples=50)
def test_j_instantiation(instance):
    assert isinstance(instance, J)

@given(instance=foo_C_strategy)
@settings(max_examples=50)
def test_foo_c_instantiation(instance):
    assert isinstance(instance, foo_C)



@given(instance=foo_C_strategy)
def test_foo_c_EAttribute1_setter(instance):
    original = instance.EAttribute1
    instance.EAttribute1 = original
    assert instance.EAttribute1 == original

@given(instance=foo_J_strategy)
@settings(max_examples=50)
def test_foo_j_instantiation(instance):
    assert isinstance(instance, foo_J)

@given(instance=foo_I_strategy)
@settings(max_examples=50)
def test_foo_i_instantiation(instance):
    assert isinstance(instance, foo_I)

@given(instance=foo_B_strategy)
@settings(max_examples=50)
def test_foo_b_instantiation(instance):
    assert isinstance(instance, foo_B)



@given(instance=foo_B_strategy)
def test_foo_b_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=foo_A_strategy)
@settings(max_examples=50)
def test_foo_a_instantiation(instance):
    assert isinstance(instance, foo_A)



@given(instance=foo_A_strategy)
def test_foo_a_fooA_setter(instance):
    original = instance.fooA
    instance.fooA = original
    assert instance.fooA == original



@given(instance=foo_A_strategy)
def test_foo_a_fooo_setter(instance):
    original = instance.fooo
    instance.fooo = original
    assert instance.fooo == original
