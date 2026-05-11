import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    foo::H,
    I,
    foo::E,
    foo::J,
    foo::I,
    B,
    foo::D,
    foo::F,
    J,
    foo::C,
    foo::B,
    foo::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_foo::h_is_not_abstract():
    assert not inspect.isabstract(foo::H)


def test_foo::h_constructor_exists():
    assert callable(foo::H.__init__)


def test_foo::h_constructor_args():
    sig = inspect.signature(foo::H.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_foo::h_has_EAttribute0():
    assert hasattr(foo::H, "EAttribute0")
    descriptor = None
    for klass in foo::H.__mro__:
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



def test_foo::e_is_not_abstract():
    assert not inspect.isabstract(foo::E)


def test_foo::e_constructor_exists():
    assert callable(foo::E.__init__)


def test_foo::e_constructor_args():
    sig = inspect.signature(foo::E.__init__)
    params = list(sig.parameters.keys())



def test_foo::j_is_not_abstract():
    assert not inspect.isabstract(foo::J)


def test_foo::j_constructor_exists():
    assert callable(foo::J.__init__)


def test_foo::j_constructor_args():
    sig = inspect.signature(foo::J.__init__)
    params = list(sig.parameters.keys())



def test_foo::i_is_not_abstract():
    assert not inspect.isabstract(foo::I)


def test_foo::i_constructor_exists():
    assert callable(foo::I.__init__)


def test_foo::i_constructor_args():
    sig = inspect.signature(foo::I.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_foo::d_is_not_abstract():
    assert not inspect.isabstract(foo::D)


def test_foo::d_constructor_exists():
    assert callable(foo::D.__init__)


def test_foo::d_constructor_args():
    sig = inspect.signature(foo::D.__init__)
    params = list(sig.parameters.keys())



def test_foo::f_is_not_abstract():
    assert not inspect.isabstract(foo::F)


def test_foo::f_constructor_exists():
    assert callable(foo::F.__init__)


def test_foo::f_constructor_args():
    sig = inspect.signature(foo::F.__init__)
    params = list(sig.parameters.keys())



def test_j_is_not_abstract():
    assert not inspect.isabstract(J)


def test_j_constructor_exists():
    assert callable(J.__init__)


def test_j_constructor_args():
    sig = inspect.signature(J.__init__)
    params = list(sig.parameters.keys())



def test_foo::c_is_not_abstract():
    assert not inspect.isabstract(foo::C)


def test_foo::c_constructor_exists():
    assert callable(foo::C.__init__)


def test_foo::c_constructor_args():
    sig = inspect.signature(foo::C.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute1" in params, "Missing parameter 'EAttribute1'"

def test_foo::c_has_EAttribute1():
    assert hasattr(foo::C, "EAttribute1")
    descriptor = None
    for klass in foo::C.__mro__:
        if "EAttribute1" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute1"]
            break
    assert isinstance(descriptor, property)



def test_foo::b_is_not_abstract():
    assert not inspect.isabstract(foo::B)


def test_foo::b_constructor_exists():
    assert callable(foo::B.__init__)


def test_foo::b_constructor_args():
    sig = inspect.signature(foo::B.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_foo::b_has_EAttribute0():
    assert hasattr(foo::B, "EAttribute0")
    descriptor = None
    for klass in foo::B.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)



def test_foo::a_is_not_abstract():
    assert not inspect.isabstract(foo::A)


def test_foo::a_constructor_exists():
    assert callable(foo::A.__init__)


def test_foo::a_constructor_args():
    sig = inspect.signature(foo::A.__init__)
    params = list(sig.parameters.keys())
    assert "fooo" in params, "Missing parameter 'fooo'"
    assert "fooA" in params, "Missing parameter 'fooA'"

def test_foo::a_has_fooo():
    assert hasattr(foo::A, "fooo")
    descriptor = None
    for klass in foo::A.__mro__:
        if "fooo" in klass.__dict__:
            descriptor = klass.__dict__["fooo"]
            break
    assert isinstance(descriptor, property)

def test_foo::a_has_fooA():
    assert hasattr(foo::A, "fooA")
    descriptor = None
    for klass in foo::A.__mro__:
        if "fooA" in klass.__dict__:
            descriptor = klass.__dict__["fooA"]
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
foo::H_strategy = st.builds(
    foo::H,
    EAttribute0=
        safe_text
)
I_strategy = st.builds(
    I,
)
foo::E_strategy = st.builds(
    foo::E,
)
foo::J_strategy = st.builds(
    foo::J,
)
foo::I_strategy = st.builds(
    foo::I,
)
B_strategy = st.builds(
    B,
)
foo::D_strategy = st.builds(
    foo::D,
)
foo::F_strategy = st.builds(
    foo::F,
)
J_strategy = st.builds(
    J,
)
foo::C_strategy = st.builds(
    foo::C,
    EAttribute1=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
foo::B_strategy = st.builds(
    foo::B,
    EAttribute0=
        st.booleans()
)
foo::A_strategy = st.builds(
    foo::A,
    fooo=
        safe_text,
    fooA=
        st.booleans()
)

@given(instance=foo::H_strategy)
@settings(max_examples=50)
def test_foo::h_instantiation(instance):
    assert isinstance(instance, foo::H)

@given(instance=foo::H_strategy)
def test_foo::h_EAttribute0_type(instance):
    assert isinstance(instance.EAttribute0, str)


@given(instance=foo::H_strategy)
def test_foo::h_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=I_strategy)
@settings(max_examples=50)
def test_i_instantiation(instance):
    assert isinstance(instance, I)

@given(instance=foo::E_strategy)
@settings(max_examples=50)
def test_foo::e_instantiation(instance):
    assert isinstance(instance, foo::E)

@given(instance=foo::J_strategy)
@settings(max_examples=50)
def test_foo::j_instantiation(instance):
    assert isinstance(instance, foo::J)

@given(instance=foo::I_strategy)
@settings(max_examples=50)
def test_foo::i_instantiation(instance):
    assert isinstance(instance, foo::I)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=foo::D_strategy)
@settings(max_examples=50)
def test_foo::d_instantiation(instance):
    assert isinstance(instance, foo::D)

@given(instance=foo::F_strategy)
@settings(max_examples=50)
def test_foo::f_instantiation(instance):
    assert isinstance(instance, foo::F)

@given(instance=J_strategy)
@settings(max_examples=50)
def test_j_instantiation(instance):
    assert isinstance(instance, J)

@given(instance=foo::C_strategy)
@settings(max_examples=50)
def test_foo::c_instantiation(instance):
    assert isinstance(instance, foo::C)

@given(instance=foo::C_strategy)
def test_foo::c_EAttribute1_type(instance):
    assert isinstance(instance.EAttribute1, float)


@given(instance=foo::C_strategy)
def test_foo::c_EAttribute1_setter(instance):
    original = instance.EAttribute1
    instance.EAttribute1 = original
    assert instance.EAttribute1 == original

@given(instance=foo::B_strategy)
@settings(max_examples=50)
def test_foo::b_instantiation(instance):
    assert isinstance(instance, foo::B)

@given(instance=foo::B_strategy)
def test_foo::b_EAttribute0_type(instance):
    assert isinstance(instance.EAttribute0, bool)


@given(instance=foo::B_strategy)
def test_foo::b_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=foo::A_strategy)
@settings(max_examples=50)
def test_foo::a_instantiation(instance):
    assert isinstance(instance, foo::A)

@given(instance=foo::A_strategy)
def test_foo::a_fooo_type(instance):
    assert isinstance(instance.fooo, str)


@given(instance=foo::A_strategy)
def test_foo::a_fooo_setter(instance):
    original = instance.fooo
    instance.fooo = original
    assert instance.fooo == original

@given(instance=foo::A_strategy)
def test_foo::a_fooA_type(instance):
    assert isinstance(instance.fooA, bool)


@given(instance=foo::A_strategy)
def test_foo::a_fooA_setter(instance):
    original = instance.fooA
    instance.fooA = original
    assert instance.fooA == original
