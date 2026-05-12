import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    root_sub_D,
    root_sub_C,
    root_B,
    root_A,
    root_sub2_E,
    root_subsub_F,
    root_subsub_E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_sub_d_is_not_abstract():
    assert not inspect.isabstract(root_sub_D)


def test_root_sub_d_constructor_exists():
    assert callable(root_sub_D.__init__)


def test_root_sub_d_constructor_args():
    sig = inspect.signature(root_sub_D.__init__)
    params = list(sig.parameters.keys())



def test_root_sub_c_is_not_abstract():
    assert not inspect.isabstract(root_sub_C)


def test_root_sub_c_constructor_exists():
    assert callable(root_sub_C.__init__)


def test_root_sub_c_constructor_args():
    sig = inspect.signature(root_sub_C.__init__)
    params = list(sig.parameters.keys())



def test_root_b_is_not_abstract():
    assert not inspect.isabstract(root_B)


def test_root_b_constructor_exists():
    assert callable(root_B.__init__)


def test_root_b_constructor_args():
    sig = inspect.signature(root_B.__init__)
    params = list(sig.parameters.keys())



def test_root_a_is_not_abstract():
    assert not inspect.isabstract(root_A)


def test_root_a_constructor_exists():
    assert callable(root_A.__init__)


def test_root_a_constructor_args():
    sig = inspect.signature(root_A.__init__)
    params = list(sig.parameters.keys())



def test_root_sub2_e_is_not_abstract():
    assert not inspect.isabstract(root_sub2_E)


def test_root_sub2_e_constructor_exists():
    assert callable(root_sub2_E.__init__)


def test_root_sub2_e_constructor_args():
    sig = inspect.signature(root_sub2_E.__init__)
    params = list(sig.parameters.keys())



def test_root_subsub_f_is_not_abstract():
    assert not inspect.isabstract(root_subsub_F)


def test_root_subsub_f_constructor_exists():
    assert callable(root_subsub_F.__init__)


def test_root_subsub_f_constructor_args():
    sig = inspect.signature(root_subsub_F.__init__)
    params = list(sig.parameters.keys())



def test_root_subsub_e_is_not_abstract():
    assert not inspect.isabstract(root_subsub_E)


def test_root_subsub_e_constructor_exists():
    assert callable(root_subsub_E.__init__)


def test_root_subsub_e_constructor_args():
    sig = inspect.signature(root_subsub_E.__init__)
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
root_sub_D_strategy = st.builds(
    root_sub_D,
)
root_sub_C_strategy = st.builds(
    root_sub_C,
)
root_B_strategy = st.builds(
    root_B,
)
root_A_strategy = st.builds(
    root_A,
)
root_sub2_E_strategy = st.builds(
    root_sub2_E,
)
root_subsub_F_strategy = st.builds(
    root_subsub_F,
)
root_subsub_E_strategy = st.builds(
    root_subsub_E,
)

@given(instance=root_sub_D_strategy)
@settings(max_examples=50)
def test_root_sub_d_instantiation(instance):
    assert isinstance(instance, root_sub_D)

@given(instance=root_sub_C_strategy)
@settings(max_examples=50)
def test_root_sub_c_instantiation(instance):
    assert isinstance(instance, root_sub_C)

@given(instance=root_B_strategy)
@settings(max_examples=50)
def test_root_b_instantiation(instance):
    assert isinstance(instance, root_B)

@given(instance=root_A_strategy)
@settings(max_examples=50)
def test_root_a_instantiation(instance):
    assert isinstance(instance, root_A)

@given(instance=root_sub2_E_strategy)
@settings(max_examples=50)
def test_root_sub2_e_instantiation(instance):
    assert isinstance(instance, root_sub2_E)

@given(instance=root_subsub_F_strategy)
@settings(max_examples=50)
def test_root_subsub_f_instantiation(instance):
    assert isinstance(instance, root_subsub_F)

@given(instance=root_subsub_E_strategy)
@settings(max_examples=50)
def test_root_subsub_e_instantiation(instance):
    assert isinstance(instance, root_subsub_E)
