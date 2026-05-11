import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ex1::G,
    ex1::F,
    ex1::E,
    A,
    ex1::C,
    ex1::B,
    ex1::D,
    F,
    ex1::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ex1::g_is_not_abstract():
    assert not inspect.isabstract(ex1::G)


def test_ex1::g_constructor_exists():
    assert callable(ex1::G.__init__)


def test_ex1::g_constructor_args():
    sig = inspect.signature(ex1::G.__init__)
    params = list(sig.parameters.keys())



def test_ex1::f_is_not_abstract():
    assert not inspect.isabstract(ex1::F)


def test_ex1::f_constructor_exists():
    assert callable(ex1::F.__init__)


def test_ex1::f_constructor_args():
    sig = inspect.signature(ex1::F.__init__)
    params = list(sig.parameters.keys())



def test_ex1::e_is_not_abstract():
    assert not inspect.isabstract(ex1::E)


def test_ex1::e_constructor_exists():
    assert callable(ex1::E.__init__)


def test_ex1::e_constructor_args():
    sig = inspect.signature(ex1::E.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_ex1::c_is_not_abstract():
    assert not inspect.isabstract(ex1::C)


def test_ex1::c_constructor_exists():
    assert callable(ex1::C.__init__)


def test_ex1::c_constructor_args():
    sig = inspect.signature(ex1::C.__init__)
    params = list(sig.parameters.keys())



def test_ex1::b_is_not_abstract():
    assert not inspect.isabstract(ex1::B)


def test_ex1::b_constructor_exists():
    assert callable(ex1::B.__init__)


def test_ex1::b_constructor_args():
    sig = inspect.signature(ex1::B.__init__)
    params = list(sig.parameters.keys())



def test_ex1::d_is_not_abstract():
    assert not inspect.isabstract(ex1::D)


def test_ex1::d_constructor_exists():
    assert callable(ex1::D.__init__)


def test_ex1::d_constructor_args():
    sig = inspect.signature(ex1::D.__init__)
    params = list(sig.parameters.keys())
    assert "dAttr" in params, "Missing parameter 'dAttr'"

def test_ex1::d_has_dAttr():
    assert hasattr(ex1::D, "dAttr")
    descriptor = None
    for klass in ex1::D.__mro__:
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



def test_ex1::a_is_not_abstract():
    assert not inspect.isabstract(ex1::A)


def test_ex1::a_constructor_exists():
    assert callable(ex1::A.__init__)


def test_ex1::a_constructor_args():
    sig = inspect.signature(ex1::A.__init__)
    params = list(sig.parameters.keys())
    assert "a1" in params, "Missing parameter 'a1'"

def test_ex1::a_has_a1():
    assert hasattr(ex1::A, "a1")
    descriptor = None
    for klass in ex1::A.__mro__:
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
ex1::G_strategy = st.builds(
    ex1::G,
)
ex1::F_strategy = st.builds(
    ex1::F,
)
ex1::E_strategy = st.builds(
    ex1::E,
)
A_strategy = st.builds(
    A,
)
ex1::C_strategy = st.builds(
    ex1::C,
)
ex1::B_strategy = st.builds(
    ex1::B,
)
ex1::D_strategy = st.builds(
    ex1::D,
    dAttr=
        st.booleans()
)
F_strategy = st.builds(
    F,
)
ex1::A_strategy = st.builds(
    ex1::A,
    a1=
        st.integers()
)

@given(instance=ex1::G_strategy)
@settings(max_examples=50)
def test_ex1::g_instantiation(instance):
    assert isinstance(instance, ex1::G)

@given(instance=ex1::F_strategy)
@settings(max_examples=50)
def test_ex1::f_instantiation(instance):
    assert isinstance(instance, ex1::F)

@given(instance=ex1::E_strategy)
@settings(max_examples=50)
def test_ex1::e_instantiation(instance):
    assert isinstance(instance, ex1::E)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=ex1::C_strategy)
@settings(max_examples=50)
def test_ex1::c_instantiation(instance):
    assert isinstance(instance, ex1::C)

@given(instance=ex1::B_strategy)
@settings(max_examples=50)
def test_ex1::b_instantiation(instance):
    assert isinstance(instance, ex1::B)

@given(instance=ex1::D_strategy)
@settings(max_examples=50)
def test_ex1::d_instantiation(instance):
    assert isinstance(instance, ex1::D)

@given(instance=ex1::D_strategy)
def test_ex1::d_dAttr_type(instance):
    assert isinstance(instance.dAttr, bool)


@given(instance=ex1::D_strategy)
def test_ex1::d_dAttr_setter(instance):
    original = instance.dAttr
    instance.dAttr = original
    assert instance.dAttr == original

@given(instance=F_strategy)
@settings(max_examples=50)
def test_f_instantiation(instance):
    assert isinstance(instance, F)

@given(instance=ex1::A_strategy)
@settings(max_examples=50)
def test_ex1::a_instantiation(instance):
    assert isinstance(instance, ex1::A)

@given(instance=ex1::A_strategy)
def test_ex1::a_a1_type(instance):
    assert isinstance(instance.a1, int)


@given(instance=ex1::A_strategy)
def test_ex1::a_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original
