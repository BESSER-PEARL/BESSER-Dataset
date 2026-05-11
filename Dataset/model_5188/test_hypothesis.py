import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ecore::Y,
    A,
    ecore::X,
    ecore::EOperation,
    C,
    ecore::EClass,
    Y,
    B,
    ecore::C,
    ecore::B,
    EOperation,
    ecore::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecore::y_is_not_abstract():
    assert not inspect.isabstract(ecore::Y)


def test_ecore::y_constructor_exists():
    assert callable(ecore::Y.__init__)


def test_ecore::y_constructor_args():
    sig = inspect.signature(ecore::Y.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_ecore::x_is_not_abstract():
    assert not inspect.isabstract(ecore::X)


def test_ecore::x_constructor_exists():
    assert callable(ecore::X.__init__)


def test_ecore::x_constructor_args():
    sig = inspect.signature(ecore::X.__init__)
    params = list(sig.parameters.keys())



def test_ecore::eoperation_is_not_abstract():
    assert not inspect.isabstract(ecore::EOperation)


def test_ecore::eoperation_constructor_exists():
    assert callable(ecore::EOperation.__init__)


def test_ecore::eoperation_constructor_args():
    sig = inspect.signature(ecore::EOperation.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_ecore::eclass_is_not_abstract():
    assert not inspect.isabstract(ecore::EClass)


def test_ecore::eclass_constructor_exists():
    assert callable(ecore::EClass.__init__)


def test_ecore::eclass_constructor_args():
    sig = inspect.signature(ecore::EClass.__init__)
    params = list(sig.parameters.keys())



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_ecore::c_is_not_abstract():
    assert not inspect.isabstract(ecore::C)


def test_ecore::c_constructor_exists():
    assert callable(ecore::C.__init__)


def test_ecore::c_constructor_args():
    sig = inspect.signature(ecore::C.__init__)
    params = list(sig.parameters.keys())



def test_ecore::b_is_not_abstract():
    assert not inspect.isabstract(ecore::B)


def test_ecore::b_constructor_exists():
    assert callable(ecore::B.__init__)


def test_ecore::b_constructor_args():
    sig = inspect.signature(ecore::B.__init__)
    params = list(sig.parameters.keys())



def test_eoperation_is_not_abstract():
    assert not inspect.isabstract(EOperation)


def test_eoperation_constructor_exists():
    assert callable(EOperation.__init__)


def test_eoperation_constructor_args():
    sig = inspect.signature(EOperation.__init__)
    params = list(sig.parameters.keys())



def test_ecore::a_is_not_abstract():
    assert not inspect.isabstract(ecore::A)


def test_ecore::a_constructor_exists():
    assert callable(ecore::A.__init__)


def test_ecore::a_constructor_args():
    sig = inspect.signature(ecore::A.__init__)
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
ecore::Y_strategy = st.builds(
    ecore::Y,
)
A_strategy = st.builds(
    A,
)
ecore::X_strategy = st.builds(
    ecore::X,
)
ecore::EOperation_strategy = st.builds(
    ecore::EOperation,
)
C_strategy = st.builds(
    C,
)
ecore::EClass_strategy = st.builds(
    ecore::EClass,
)
Y_strategy = st.builds(
    Y,
)
B_strategy = st.builds(
    B,
)
ecore::C_strategy = st.builds(
    ecore::C,
)
ecore::B_strategy = st.builds(
    ecore::B,
)
EOperation_strategy = st.builds(
    EOperation,
)
ecore::A_strategy = st.builds(
    ecore::A,
)

@given(instance=ecore::Y_strategy)
@settings(max_examples=50)
def test_ecore::y_instantiation(instance):
    assert isinstance(instance, ecore::Y)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=ecore::X_strategy)
@settings(max_examples=50)
def test_ecore::x_instantiation(instance):
    assert isinstance(instance, ecore::X)

@given(instance=ecore::EOperation_strategy)
@settings(max_examples=50)
def test_ecore::eoperation_instantiation(instance):
    assert isinstance(instance, ecore::EOperation)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=ecore::EClass_strategy)
@settings(max_examples=50)
def test_ecore::eclass_instantiation(instance):
    assert isinstance(instance, ecore::EClass)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=ecore::C_strategy)
@settings(max_examples=50)
def test_ecore::c_instantiation(instance):
    assert isinstance(instance, ecore::C)

@given(instance=ecore::B_strategy)
@settings(max_examples=50)
def test_ecore::b_instantiation(instance):
    assert isinstance(instance, ecore::B)

@given(instance=EOperation_strategy)
@settings(max_examples=50)
def test_eoperation_instantiation(instance):
    assert isinstance(instance, EOperation)

@given(instance=ecore::A_strategy)
@settings(max_examples=50)
def test_ecore::a_instantiation(instance):
    assert isinstance(instance, ecore::A)
