import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C,
    dispatch_G,
    dispatch_F,
    B,
    dispatch_E,
    dispatch_D,
    A,
    dispatch_C,
    dispatch_B,
    dispatch_A,
    dispatch_Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_dispatch_g_is_not_abstract():
    assert not inspect.isabstract(dispatch_G)


def test_dispatch_g_constructor_exists():
    assert callable(dispatch_G.__init__)


def test_dispatch_g_constructor_args():
    sig = inspect.signature(dispatch_G.__init__)
    params = list(sig.parameters.keys())



def test_dispatch_f_is_not_abstract():
    assert not inspect.isabstract(dispatch_F)


def test_dispatch_f_constructor_exists():
    assert callable(dispatch_F.__init__)


def test_dispatch_f_constructor_args():
    sig = inspect.signature(dispatch_F.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_dispatch_e_is_not_abstract():
    assert not inspect.isabstract(dispatch_E)


def test_dispatch_e_constructor_exists():
    assert callable(dispatch_E.__init__)


def test_dispatch_e_constructor_args():
    sig = inspect.signature(dispatch_E.__init__)
    params = list(sig.parameters.keys())



def test_dispatch_d_is_not_abstract():
    assert not inspect.isabstract(dispatch_D)


def test_dispatch_d_constructor_exists():
    assert callable(dispatch_D.__init__)


def test_dispatch_d_constructor_args():
    sig = inspect.signature(dispatch_D.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_dispatch_c_is_not_abstract():
    assert not inspect.isabstract(dispatch_C)


def test_dispatch_c_constructor_exists():
    assert callable(dispatch_C.__init__)


def test_dispatch_c_constructor_args():
    sig = inspect.signature(dispatch_C.__init__)
    params = list(sig.parameters.keys())



def test_dispatch_b_is_not_abstract():
    assert not inspect.isabstract(dispatch_B)


def test_dispatch_b_constructor_exists():
    assert callable(dispatch_B.__init__)


def test_dispatch_b_constructor_args():
    sig = inspect.signature(dispatch_B.__init__)
    params = list(sig.parameters.keys())



def test_dispatch_a_is_not_abstract():
    assert not inspect.isabstract(dispatch_A)


def test_dispatch_a_constructor_exists():
    assert callable(dispatch_A.__init__)


def test_dispatch_a_constructor_args():
    sig = inspect.signature(dispatch_A.__init__)
    params = list(sig.parameters.keys())



def test_dispatch_container_is_not_abstract():
    assert not inspect.isabstract(dispatch_Container)


def test_dispatch_container_constructor_exists():
    assert callable(dispatch_Container.__init__)


def test_dispatch_container_constructor_args():
    sig = inspect.signature(dispatch_Container.__init__)
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
C_strategy = st.builds(
    C,
)
dispatch_G_strategy = st.builds(
    dispatch_G,
)
dispatch_F_strategy = st.builds(
    dispatch_F,
)
B_strategy = st.builds(
    B,
)
dispatch_E_strategy = st.builds(
    dispatch_E,
)
dispatch_D_strategy = st.builds(
    dispatch_D,
)
A_strategy = st.builds(
    A,
)
dispatch_C_strategy = st.builds(
    dispatch_C,
)
dispatch_B_strategy = st.builds(
    dispatch_B,
)
dispatch_A_strategy = st.builds(
    dispatch_A,
)
dispatch_Container_strategy = st.builds(
    dispatch_Container,
)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=dispatch_G_strategy)
@settings(max_examples=50)
def test_dispatch_g_instantiation(instance):
    assert isinstance(instance, dispatch_G)

@given(instance=dispatch_F_strategy)
@settings(max_examples=50)
def test_dispatch_f_instantiation(instance):
    assert isinstance(instance, dispatch_F)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=dispatch_E_strategy)
@settings(max_examples=50)
def test_dispatch_e_instantiation(instance):
    assert isinstance(instance, dispatch_E)

@given(instance=dispatch_D_strategy)
@settings(max_examples=50)
def test_dispatch_d_instantiation(instance):
    assert isinstance(instance, dispatch_D)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=dispatch_C_strategy)
@settings(max_examples=50)
def test_dispatch_c_instantiation(instance):
    assert isinstance(instance, dispatch_C)

@given(instance=dispatch_B_strategy)
@settings(max_examples=50)
def test_dispatch_b_instantiation(instance):
    assert isinstance(instance, dispatch_B)

@given(instance=dispatch_A_strategy)
@settings(max_examples=50)
def test_dispatch_a_instantiation(instance):
    assert isinstance(instance, dispatch_A)

@given(instance=dispatch_Container_strategy)
@settings(max_examples=50)
def test_dispatch_container_instantiation(instance):
    assert isinstance(instance, dispatch_Container)
