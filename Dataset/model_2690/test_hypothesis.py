import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    refac::K,
    refac::X,
    refac::N99,
    refac::M,
    refac::W,
    refac::C,
    refac::A,
    refac::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_refac::k_is_not_abstract():
    assert not inspect.isabstract(refac::K)


def test_refac::k_constructor_exists():
    assert callable(refac::K.__init__)


def test_refac::k_constructor_args():
    sig = inspect.signature(refac::K.__init__)
    params = list(sig.parameters.keys())



def test_refac::x_is_not_abstract():
    assert not inspect.isabstract(refac::X)


def test_refac::x_constructor_exists():
    assert callable(refac::X.__init__)


def test_refac::x_constructor_args():
    sig = inspect.signature(refac::X.__init__)
    params = list(sig.parameters.keys())



def test_refac::n99_is_not_abstract():
    assert not inspect.isabstract(refac::N99)


def test_refac::n99_constructor_exists():
    assert callable(refac::N99.__init__)


def test_refac::n99_constructor_args():
    sig = inspect.signature(refac::N99.__init__)
    params = list(sig.parameters.keys())



def test_refac::m_is_not_abstract():
    assert not inspect.isabstract(refac::M)


def test_refac::m_constructor_exists():
    assert callable(refac::M.__init__)


def test_refac::m_constructor_args():
    sig = inspect.signature(refac::M.__init__)
    params = list(sig.parameters.keys())



def test_refac::w_is_not_abstract():
    assert not inspect.isabstract(refac::W)


def test_refac::w_constructor_exists():
    assert callable(refac::W.__init__)


def test_refac::w_constructor_args():
    sig = inspect.signature(refac::W.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_refac::w_has_name():
    assert hasattr(refac::W, "name")
    descriptor = None
    for klass in refac::W.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_refac::c_is_not_abstract():
    assert not inspect.isabstract(refac::C)


def test_refac::c_constructor_exists():
    assert callable(refac::C.__init__)


def test_refac::c_constructor_args():
    sig = inspect.signature(refac::C.__init__)
    params = list(sig.parameters.keys())



def test_refac::a_is_not_abstract():
    assert not inspect.isabstract(refac::A)


def test_refac::a_constructor_exists():
    assert callable(refac::A.__init__)


def test_refac::a_constructor_args():
    sig = inspect.signature(refac::A.__init__)
    params = list(sig.parameters.keys())



def test_refac::b_is_not_abstract():
    assert not inspect.isabstract(refac::B)


def test_refac::b_constructor_exists():
    assert callable(refac::B.__init__)


def test_refac::b_constructor_args():
    sig = inspect.signature(refac::B.__init__)
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
refac::K_strategy = st.builds(
    refac::K,
)
refac::X_strategy = st.builds(
    refac::X,
)
refac::N99_strategy = st.builds(
    refac::N99,
)
refac::M_strategy = st.builds(
    refac::M,
)
refac::W_strategy = st.builds(
    refac::W,
    name=
        safe_text
)
refac::C_strategy = st.builds(
    refac::C,
)
refac::A_strategy = st.builds(
    refac::A,
)
refac::B_strategy = st.builds(
    refac::B,
)

@given(instance=refac::K_strategy)
@settings(max_examples=50)
def test_refac::k_instantiation(instance):
    assert isinstance(instance, refac::K)

@given(instance=refac::X_strategy)
@settings(max_examples=50)
def test_refac::x_instantiation(instance):
    assert isinstance(instance, refac::X)

@given(instance=refac::N99_strategy)
@settings(max_examples=50)
def test_refac::n99_instantiation(instance):
    assert isinstance(instance, refac::N99)

@given(instance=refac::M_strategy)
@settings(max_examples=50)
def test_refac::m_instantiation(instance):
    assert isinstance(instance, refac::M)

@given(instance=refac::W_strategy)
@settings(max_examples=50)
def test_refac::w_instantiation(instance):
    assert isinstance(instance, refac::W)

@given(instance=refac::W_strategy)
def test_refac::w_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=refac::W_strategy)
def test_refac::w_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=refac::C_strategy)
@settings(max_examples=50)
def test_refac::c_instantiation(instance):
    assert isinstance(instance, refac::C)

@given(instance=refac::A_strategy)
@settings(max_examples=50)
def test_refac::a_instantiation(instance):
    assert isinstance(instance, refac::A)

@given(instance=refac::B_strategy)
@settings(max_examples=50)
def test_refac::b_instantiation(instance):
    assert isinstance(instance, refac::B)
