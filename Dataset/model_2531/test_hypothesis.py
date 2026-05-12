import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_E,
    test_C,
    test_ClassB,
    test_ClassA,
    test_G,
    test_H,
    test_F,
    test_D,
    test_I,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_e_is_not_abstract():
    assert not inspect.isabstract(test_E)


def test_test_e_constructor_exists():
    assert callable(test_E.__init__)


def test_test_e_constructor_args():
    sig = inspect.signature(test_E.__init__)
    params = list(sig.parameters.keys())



def test_test_c_is_not_abstract():
    assert not inspect.isabstract(test_C)


def test_test_c_constructor_exists():
    assert callable(test_C.__init__)


def test_test_c_constructor_args():
    sig = inspect.signature(test_C.__init__)
    params = list(sig.parameters.keys())



def test_test_classb_is_not_abstract():
    assert not inspect.isabstract(test_ClassB)


def test_test_classb_constructor_exists():
    assert callable(test_ClassB.__init__)


def test_test_classb_constructor_args():
    sig = inspect.signature(test_ClassB.__init__)
    params = list(sig.parameters.keys())



def test_test_classa_is_not_abstract():
    assert not inspect.isabstract(test_ClassA)


def test_test_classa_constructor_exists():
    assert callable(test_ClassA.__init__)


def test_test_classa_constructor_args():
    sig = inspect.signature(test_ClassA.__init__)
    params = list(sig.parameters.keys())



def test_test_g_is_not_abstract():
    assert not inspect.isabstract(test_G)


def test_test_g_constructor_exists():
    assert callable(test_G.__init__)


def test_test_g_constructor_args():
    sig = inspect.signature(test_G.__init__)
    params = list(sig.parameters.keys())



def test_test_h_is_not_abstract():
    assert not inspect.isabstract(test_H)


def test_test_h_constructor_exists():
    assert callable(test_H.__init__)


def test_test_h_constructor_args():
    sig = inspect.signature(test_H.__init__)
    params = list(sig.parameters.keys())



def test_test_f_is_not_abstract():
    assert not inspect.isabstract(test_F)


def test_test_f_constructor_exists():
    assert callable(test_F.__init__)


def test_test_f_constructor_args():
    sig = inspect.signature(test_F.__init__)
    params = list(sig.parameters.keys())



def test_test_d_is_not_abstract():
    assert not inspect.isabstract(test_D)


def test_test_d_constructor_exists():
    assert callable(test_D.__init__)


def test_test_d_constructor_args():
    sig = inspect.signature(test_D.__init__)
    params = list(sig.parameters.keys())



def test_test_i_is_not_abstract():
    assert not inspect.isabstract(test_I)


def test_test_i_constructor_exists():
    assert callable(test_I.__init__)


def test_test_i_constructor_args():
    sig = inspect.signature(test_I.__init__)
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
test_E_strategy = st.builds(
    test_E,
)
test_C_strategy = st.builds(
    test_C,
)
test_ClassB_strategy = st.builds(
    test_ClassB,
)
test_ClassA_strategy = st.builds(
    test_ClassA,
)
test_G_strategy = st.builds(
    test_G,
)
test_H_strategy = st.builds(
    test_H,
)
test_F_strategy = st.builds(
    test_F,
)
test_D_strategy = st.builds(
    test_D,
)
test_I_strategy = st.builds(
    test_I,
)

@given(instance=test_E_strategy)
@settings(max_examples=50)
def test_test_e_instantiation(instance):
    assert isinstance(instance, test_E)

@given(instance=test_C_strategy)
@settings(max_examples=50)
def test_test_c_instantiation(instance):
    assert isinstance(instance, test_C)

@given(instance=test_ClassB_strategy)
@settings(max_examples=50)
def test_test_classb_instantiation(instance):
    assert isinstance(instance, test_ClassB)

@given(instance=test_ClassA_strategy)
@settings(max_examples=50)
def test_test_classa_instantiation(instance):
    assert isinstance(instance, test_ClassA)

@given(instance=test_G_strategy)
@settings(max_examples=50)
def test_test_g_instantiation(instance):
    assert isinstance(instance, test_G)

@given(instance=test_H_strategy)
@settings(max_examples=50)
def test_test_h_instantiation(instance):
    assert isinstance(instance, test_H)

@given(instance=test_F_strategy)
@settings(max_examples=50)
def test_test_f_instantiation(instance):
    assert isinstance(instance, test_F)

@given(instance=test_D_strategy)
@settings(max_examples=50)
def test_test_d_instantiation(instance):
    assert isinstance(instance, test_D)

@given(instance=test_I_strategy)
@settings(max_examples=50)
def test_test_i_instantiation(instance):
    assert isinstance(instance, test_I)
