import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    factorydeclorder::D,
    factorydeclorder::B,
    D,
    A,
    B,
    factorydeclorder::A,
    factorydeclorder::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_factorydeclorder::d_is_not_abstract():
    assert not inspect.isabstract(factorydeclorder::D)


def test_factorydeclorder::d_constructor_exists():
    assert callable(factorydeclorder::D.__init__)


def test_factorydeclorder::d_constructor_args():
    sig = inspect.signature(factorydeclorder::D.__init__)
    params = list(sig.parameters.keys())



def test_factorydeclorder::b_is_not_abstract():
    assert not inspect.isabstract(factorydeclorder::B)


def test_factorydeclorder::b_constructor_exists():
    assert callable(factorydeclorder::B.__init__)


def test_factorydeclorder::b_constructor_args():
    sig = inspect.signature(factorydeclorder::B.__init__)
    params = list(sig.parameters.keys())
    assert "fb" in params, "Missing parameter 'fb'"

def test_factorydeclorder::b_has_fb():
    assert hasattr(factorydeclorder::B, "fb")
    descriptor = None
    for klass in factorydeclorder::B.__mro__:
        if "fb" in klass.__dict__:
            descriptor = klass.__dict__["fb"]
            break
    assert isinstance(descriptor, property)



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_factorydeclorder::a_is_not_abstract():
    assert not inspect.isabstract(factorydeclorder::A)


def test_factorydeclorder::a_constructor_exists():
    assert callable(factorydeclorder::A.__init__)


def test_factorydeclorder::a_constructor_args():
    sig = inspect.signature(factorydeclorder::A.__init__)
    params = list(sig.parameters.keys())
    assert "fa" in params, "Missing parameter 'fa'"

def test_factorydeclorder::a_has_fa():
    assert hasattr(factorydeclorder::A, "fa")
    descriptor = None
    for klass in factorydeclorder::A.__mro__:
        if "fa" in klass.__dict__:
            descriptor = klass.__dict__["fa"]
            break
    assert isinstance(descriptor, property)



def test_factorydeclorder::c_is_not_abstract():
    assert not inspect.isabstract(factorydeclorder::C)


def test_factorydeclorder::c_constructor_exists():
    assert callable(factorydeclorder::C.__init__)


def test_factorydeclorder::c_constructor_args():
    sig = inspect.signature(factorydeclorder::C.__init__)
    params = list(sig.parameters.keys())
    assert "fc" in params, "Missing parameter 'fc'"

def test_factorydeclorder::c_has_fc():
    assert hasattr(factorydeclorder::C, "fc")
    descriptor = None
    for klass in factorydeclorder::C.__mro__:
        if "fc" in klass.__dict__:
            descriptor = klass.__dict__["fc"]
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
factorydeclorder::D_strategy = st.builds(
    factorydeclorder::D,
)
factorydeclorder::B_strategy = st.builds(
    factorydeclorder::B,
    fb=
        safe_text
)
D_strategy = st.builds(
    D,
)
A_strategy = st.builds(
    A,
)
B_strategy = st.builds(
    B,
)
factorydeclorder::A_strategy = st.builds(
    factorydeclorder::A,
    fa=
        st.integers()
)
factorydeclorder::C_strategy = st.builds(
    factorydeclorder::C,
    fc=
        st.booleans()
)

@given(instance=factorydeclorder::D_strategy)
@settings(max_examples=50)
def test_factorydeclorder::d_instantiation(instance):
    assert isinstance(instance, factorydeclorder::D)

@given(instance=factorydeclorder::B_strategy)
@settings(max_examples=50)
def test_factorydeclorder::b_instantiation(instance):
    assert isinstance(instance, factorydeclorder::B)

@given(instance=factorydeclorder::B_strategy)
def test_factorydeclorder::b_fb_type(instance):
    assert isinstance(instance.fb, str)


@given(instance=factorydeclorder::B_strategy)
def test_factorydeclorder::b_fb_setter(instance):
    original = instance.fb
    instance.fb = original
    assert instance.fb == original

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=factorydeclorder::A_strategy)
@settings(max_examples=50)
def test_factorydeclorder::a_instantiation(instance):
    assert isinstance(instance, factorydeclorder::A)

@given(instance=factorydeclorder::A_strategy)
def test_factorydeclorder::a_fa_type(instance):
    assert isinstance(instance.fa, int)


@given(instance=factorydeclorder::A_strategy)
def test_factorydeclorder::a_fa_setter(instance):
    original = instance.fa
    instance.fa = original
    assert instance.fa == original

@given(instance=factorydeclorder::C_strategy)
@settings(max_examples=50)
def test_factorydeclorder::c_instantiation(instance):
    assert isinstance(instance, factorydeclorder::C)

@given(instance=factorydeclorder::C_strategy)
def test_factorydeclorder::c_fc_type(instance):
    assert isinstance(instance.fc, bool)


@given(instance=factorydeclorder::C_strategy)
def test_factorydeclorder::c_fc_setter(instance):
    original = instance.fc
    instance.fc = original
    assert instance.fc == original
