import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ex1_G,
    ex1_F,
    ex1_E,
    A,
    ex1_C,
    ex1_B,
    ex1_D,
    F,
    ex1_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ex1_g_is_not_abstract():
    assert not inspect.isabstract(ex1_G)


def test_ex1_g_constructor_exists():
    assert callable(ex1_G.__init__)


def test_ex1_g_constructor_args():
    sig = inspect.signature(ex1_G.__init__)
    params = list(sig.parameters.keys())



def test_ex1_f_is_not_abstract():
    assert not inspect.isabstract(ex1_F)


def test_ex1_f_constructor_exists():
    assert callable(ex1_F.__init__)


def test_ex1_f_constructor_args():
    sig = inspect.signature(ex1_F.__init__)
    params = list(sig.parameters.keys())



def test_ex1_e_is_not_abstract():
    assert not inspect.isabstract(ex1_E)


def test_ex1_e_constructor_exists():
    assert callable(ex1_E.__init__)


def test_ex1_e_constructor_args():
    sig = inspect.signature(ex1_E.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_ex1_c_is_not_abstract():
    assert not inspect.isabstract(ex1_C)


def test_ex1_c_constructor_exists():
    assert callable(ex1_C.__init__)


def test_ex1_c_constructor_args():
    sig = inspect.signature(ex1_C.__init__)
    params = list(sig.parameters.keys())



def test_ex1_b_is_not_abstract():
    assert not inspect.isabstract(ex1_B)


def test_ex1_b_constructor_exists():
    assert callable(ex1_B.__init__)


def test_ex1_b_constructor_args():
    sig = inspect.signature(ex1_B.__init__)
    params = list(sig.parameters.keys())



def test_ex1_d_is_not_abstract():
    assert not inspect.isabstract(ex1_D)


def test_ex1_d_constructor_exists():
    assert callable(ex1_D.__init__)


def test_ex1_d_constructor_args():
    sig = inspect.signature(ex1_D.__init__)
    params = list(sig.parameters.keys())
    assert "dAttr" in params, "Missing parameter 'dAttr'"

def test_ex1_d_has_dAttr():
    assert hasattr(ex1_D, "dAttr")
    descriptor = None
    for klass in ex1_D.__mro__:
        if "dAttr" in klass.__dict__:
            descriptor = klass.__dict__["dAttr"]
            break
    assert isinstance(descriptor, property)



def test_f_is_not_abstract():
    assert not inspect.isabstract(F)


def test_f_constructor_exists():
    assert callable(F.__init__)


def test_f_constructor_args():
    sig = inspect.signature(F.__init__)
    params = list(sig.parameters.keys())



def test_ex1_a_is_not_abstract():
    assert not inspect.isabstract(ex1_A)


def test_ex1_a_constructor_exists():
    assert callable(ex1_A.__init__)


def test_ex1_a_constructor_args():
    sig = inspect.signature(ex1_A.__init__)
    params = list(sig.parameters.keys())
    assert "a1" in params, "Missing parameter 'a1'"

def test_ex1_a_has_a1():
    assert hasattr(ex1_A, "a1")
    descriptor = None
    for klass in ex1_A.__mro__:
        if "a1" in klass.__dict__:
            descriptor = klass.__dict__["a1"]
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
ex1_G_strategy = st.builds(
    ex1_G,
)
ex1_F_strategy = st.builds(
    ex1_F,
)
ex1_E_strategy = st.builds(
    ex1_E,
)
A_strategy = st.builds(
    A,
)
ex1_C_strategy = st.builds(
    ex1_C,
)
ex1_B_strategy = st.builds(
    ex1_B,
)
ex1_D_strategy = st.builds(
    ex1_D,
    dAttr=
        st.booleans()
)
F_strategy = st.builds(
    F,
)
ex1_A_strategy = st.builds(
    ex1_A,
    a1=
        st.integers()
)

@given(instance=ex1_G_strategy)
@settings(max_examples=50)
def test_ex1_g_instantiation(instance):
    assert isinstance(instance, ex1_G)

@given(instance=ex1_F_strategy)
@settings(max_examples=50)
def test_ex1_f_instantiation(instance):
    assert isinstance(instance, ex1_F)

@given(instance=ex1_E_strategy)
@settings(max_examples=50)
def test_ex1_e_instantiation(instance):
    assert isinstance(instance, ex1_E)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=ex1_C_strategy)
@settings(max_examples=50)
def test_ex1_c_instantiation(instance):
    assert isinstance(instance, ex1_C)

@given(instance=ex1_B_strategy)
@settings(max_examples=50)
def test_ex1_b_instantiation(instance):
    assert isinstance(instance, ex1_B)

@given(instance=ex1_D_strategy)
@settings(max_examples=50)
def test_ex1_d_instantiation(instance):
    assert isinstance(instance, ex1_D)



@given(instance=ex1_D_strategy)
def test_ex1_d_dAttr_setter(instance):
    original = instance.dAttr
    instance.dAttr = original
    assert instance.dAttr == original

@given(instance=F_strategy)
@settings(max_examples=50)
def test_f_instantiation(instance):
    assert isinstance(instance, F)

@given(instance=ex1_A_strategy)
@settings(max_examples=50)
def test_ex1_a_instantiation(instance):
    assert isinstance(instance, ex1_A)



@given(instance=ex1_A_strategy)
def test_ex1_a_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original
