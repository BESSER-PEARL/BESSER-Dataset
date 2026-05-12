import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ecore_Y,
    A,
    ecore_X,
    ecore_EOperation,
    C,
    ecore_EClass,
    Y,
    B,
    ecore_C,
    ecore_B,
    EOperation,
    ecore_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecore_y_is_not_abstract():
    assert not inspect.isabstract(ecore_Y)


def test_ecore_y_constructor_exists():
    assert callable(ecore_Y.__init__)


def test_ecore_y_constructor_args():
    sig = inspect.signature(ecore_Y.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_ecore_x_is_not_abstract():
    assert not inspect.isabstract(ecore_X)


def test_ecore_x_constructor_exists():
    assert callable(ecore_X.__init__)


def test_ecore_x_constructor_args():
    sig = inspect.signature(ecore_X.__init__)
    params = list(sig.parameters.keys())



def test_ecore_eoperation_is_not_abstract():
    assert not inspect.isabstract(ecore_EOperation)


def test_ecore_eoperation_constructor_exists():
    assert callable(ecore_EOperation.__init__)


def test_ecore_eoperation_constructor_args():
    sig = inspect.signature(ecore_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_ecore_eclass_is_not_abstract():
    assert not inspect.isabstract(ecore_EClass)


def test_ecore_eclass_constructor_exists():
    assert callable(ecore_EClass.__init__)


def test_ecore_eclass_constructor_args():
    sig = inspect.signature(ecore_EClass.__init__)
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



def test_ecore_c_is_not_abstract():
    assert not inspect.isabstract(ecore_C)


def test_ecore_c_constructor_exists():
    assert callable(ecore_C.__init__)


def test_ecore_c_constructor_args():
    sig = inspect.signature(ecore_C.__init__)
    params = list(sig.parameters.keys())



def test_ecore_b_is_not_abstract():
    assert not inspect.isabstract(ecore_B)


def test_ecore_b_constructor_exists():
    assert callable(ecore_B.__init__)


def test_ecore_b_constructor_args():
    sig = inspect.signature(ecore_B.__init__)
    params = list(sig.parameters.keys())



def test_eoperation_is_not_abstract():
    assert not inspect.isabstract(EOperation)


def test_eoperation_constructor_exists():
    assert callable(EOperation.__init__)


def test_eoperation_constructor_args():
    sig = inspect.signature(EOperation.__init__)
    params = list(sig.parameters.keys())



def test_ecore_a_is_not_abstract():
    assert not inspect.isabstract(ecore_A)


def test_ecore_a_constructor_exists():
    assert callable(ecore_A.__init__)


def test_ecore_a_constructor_args():
    sig = inspect.signature(ecore_A.__init__)
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
ecore_Y_strategy = st.builds(
    ecore_Y,
)
A_strategy = st.builds(
    A,
)
ecore_X_strategy = st.builds(
    ecore_X,
)
ecore_EOperation_strategy = st.builds(
    ecore_EOperation,
)
C_strategy = st.builds(
    C,
)
ecore_EClass_strategy = st.builds(
    ecore_EClass,
)
Y_strategy = st.builds(
    Y,
)
B_strategy = st.builds(
    B,
)
ecore_C_strategy = st.builds(
    ecore_C,
)
ecore_B_strategy = st.builds(
    ecore_B,
)
EOperation_strategy = st.builds(
    EOperation,
)
ecore_A_strategy = st.builds(
    ecore_A,
)

@given(instance=ecore_Y_strategy)
@settings(max_examples=50)
def test_ecore_y_instantiation(instance):
    assert isinstance(instance, ecore_Y)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=ecore_X_strategy)
@settings(max_examples=50)
def test_ecore_x_instantiation(instance):
    assert isinstance(instance, ecore_X)

@given(instance=ecore_EOperation_strategy)
@settings(max_examples=50)
def test_ecore_eoperation_instantiation(instance):
    assert isinstance(instance, ecore_EOperation)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=ecore_EClass_strategy)
@settings(max_examples=50)
def test_ecore_eclass_instantiation(instance):
    assert isinstance(instance, ecore_EClass)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=ecore_C_strategy)
@settings(max_examples=50)
def test_ecore_c_instantiation(instance):
    assert isinstance(instance, ecore_C)

@given(instance=ecore_B_strategy)
@settings(max_examples=50)
def test_ecore_b_instantiation(instance):
    assert isinstance(instance, ecore_B)

@given(instance=EOperation_strategy)
@settings(max_examples=50)
def test_eoperation_instantiation(instance):
    assert isinstance(instance, EOperation)

@given(instance=ecore_A_strategy)
@settings(max_examples=50)
def test_ecore_a_instantiation(instance):
    assert isinstance(instance, ecore_A)
