import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    a_c_cc2,
    a_c_cc1,
    a_e_ce2,
    a_e_ce1,
    a_d_cd2,
    a_d_cd1,
    a_b_cb2,
    a_b_cb1,
    a_ca2,
    a_ca1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_c_cc2_is_not_abstract():
    assert not inspect.isabstract(a_c_cc2)


def test_a_c_cc2_constructor_exists():
    assert callable(a_c_cc2.__init__)


def test_a_c_cc2_constructor_args():
    sig = inspect.signature(a_c_cc2.__init__)
    params = list(sig.parameters.keys())



def test_a_c_cc1_is_not_abstract():
    assert not inspect.isabstract(a_c_cc1)


def test_a_c_cc1_constructor_exists():
    assert callable(a_c_cc1.__init__)


def test_a_c_cc1_constructor_args():
    sig = inspect.signature(a_c_cc1.__init__)
    params = list(sig.parameters.keys())



def test_a_e_ce2_is_not_abstract():
    assert not inspect.isabstract(a_e_ce2)


def test_a_e_ce2_constructor_exists():
    assert callable(a_e_ce2.__init__)


def test_a_e_ce2_constructor_args():
    sig = inspect.signature(a_e_ce2.__init__)
    params = list(sig.parameters.keys())



def test_a_e_ce1_is_not_abstract():
    assert not inspect.isabstract(a_e_ce1)


def test_a_e_ce1_constructor_exists():
    assert callable(a_e_ce1.__init__)


def test_a_e_ce1_constructor_args():
    sig = inspect.signature(a_e_ce1.__init__)
    params = list(sig.parameters.keys())



def test_a_d_cd2_is_not_abstract():
    assert not inspect.isabstract(a_d_cd2)


def test_a_d_cd2_constructor_exists():
    assert callable(a_d_cd2.__init__)


def test_a_d_cd2_constructor_args():
    sig = inspect.signature(a_d_cd2.__init__)
    params = list(sig.parameters.keys())



def test_a_d_cd1_is_not_abstract():
    assert not inspect.isabstract(a_d_cd1)


def test_a_d_cd1_constructor_exists():
    assert callable(a_d_cd1.__init__)


def test_a_d_cd1_constructor_args():
    sig = inspect.signature(a_d_cd1.__init__)
    params = list(sig.parameters.keys())



def test_a_b_cb2_is_not_abstract():
    assert not inspect.isabstract(a_b_cb2)


def test_a_b_cb2_constructor_exists():
    assert callable(a_b_cb2.__init__)


def test_a_b_cb2_constructor_args():
    sig = inspect.signature(a_b_cb2.__init__)
    params = list(sig.parameters.keys())



def test_a_b_cb1_is_not_abstract():
    assert not inspect.isabstract(a_b_cb1)


def test_a_b_cb1_constructor_exists():
    assert callable(a_b_cb1.__init__)


def test_a_b_cb1_constructor_args():
    sig = inspect.signature(a_b_cb1.__init__)
    params = list(sig.parameters.keys())



def test_a_ca2_is_not_abstract():
    assert not inspect.isabstract(a_ca2)


def test_a_ca2_constructor_exists():
    assert callable(a_ca2.__init__)


def test_a_ca2_constructor_args():
    sig = inspect.signature(a_ca2.__init__)
    params = list(sig.parameters.keys())



def test_a_ca1_is_not_abstract():
    assert not inspect.isabstract(a_ca1)


def test_a_ca1_constructor_exists():
    assert callable(a_ca1.__init__)


def test_a_ca1_constructor_args():
    sig = inspect.signature(a_ca1.__init__)
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
a_c_cc2_strategy = st.builds(
    a_c_cc2,
)
a_c_cc1_strategy = st.builds(
    a_c_cc1,
)
a_e_ce2_strategy = st.builds(
    a_e_ce2,
)
a_e_ce1_strategy = st.builds(
    a_e_ce1,
)
a_d_cd2_strategy = st.builds(
    a_d_cd2,
)
a_d_cd1_strategy = st.builds(
    a_d_cd1,
)
a_b_cb2_strategy = st.builds(
    a_b_cb2,
)
a_b_cb1_strategy = st.builds(
    a_b_cb1,
)
a_ca2_strategy = st.builds(
    a_ca2,
)
a_ca1_strategy = st.builds(
    a_ca1,
)

@given(instance=a_c_cc2_strategy)
@settings(max_examples=50)
def test_a_c_cc2_instantiation(instance):
    assert isinstance(instance, a_c_cc2)

@given(instance=a_c_cc1_strategy)
@settings(max_examples=50)
def test_a_c_cc1_instantiation(instance):
    assert isinstance(instance, a_c_cc1)

@given(instance=a_e_ce2_strategy)
@settings(max_examples=50)
def test_a_e_ce2_instantiation(instance):
    assert isinstance(instance, a_e_ce2)

@given(instance=a_e_ce1_strategy)
@settings(max_examples=50)
def test_a_e_ce1_instantiation(instance):
    assert isinstance(instance, a_e_ce1)

@given(instance=a_d_cd2_strategy)
@settings(max_examples=50)
def test_a_d_cd2_instantiation(instance):
    assert isinstance(instance, a_d_cd2)

@given(instance=a_d_cd1_strategy)
@settings(max_examples=50)
def test_a_d_cd1_instantiation(instance):
    assert isinstance(instance, a_d_cd1)

@given(instance=a_b_cb2_strategy)
@settings(max_examples=50)
def test_a_b_cb2_instantiation(instance):
    assert isinstance(instance, a_b_cb2)

@given(instance=a_b_cb1_strategy)
@settings(max_examples=50)
def test_a_b_cb1_instantiation(instance):
    assert isinstance(instance, a_b_cb1)

@given(instance=a_ca2_strategy)
@settings(max_examples=50)
def test_a_ca2_instantiation(instance):
    assert isinstance(instance, a_ca2)

@given(instance=a_ca1_strategy)
@settings(max_examples=50)
def test_a_ca1_instantiation(instance):
    assert isinstance(instance, a_ca1)
