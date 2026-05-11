import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    C,
    dispatch::G,
    dispatch::F,
    B,
    dispatch::E,
    dispatch::D,
    A,
    dispatch::C,
    dispatch::B,
    dispatch::A,
    dispatch::Container,
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



def test_dispatch::g_is_not_abstract():
    assert not inspect.isabstract(dispatch::G)


def test_dispatch::g_constructor_exists():
    assert callable(dispatch::G.__init__)


def test_dispatch::g_constructor_args():
    sig = inspect.signature(dispatch::G.__init__)
    params = list(sig.parameters.keys())



def test_dispatch::f_is_not_abstract():
    assert not inspect.isabstract(dispatch::F)


def test_dispatch::f_constructor_exists():
    assert callable(dispatch::F.__init__)


def test_dispatch::f_constructor_args():
    sig = inspect.signature(dispatch::F.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_dispatch::e_is_not_abstract():
    assert not inspect.isabstract(dispatch::E)


def test_dispatch::e_constructor_exists():
    assert callable(dispatch::E.__init__)


def test_dispatch::e_constructor_args():
    sig = inspect.signature(dispatch::E.__init__)
    params = list(sig.parameters.keys())



def test_dispatch::d_is_not_abstract():
    assert not inspect.isabstract(dispatch::D)


def test_dispatch::d_constructor_exists():
    assert callable(dispatch::D.__init__)


def test_dispatch::d_constructor_args():
    sig = inspect.signature(dispatch::D.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_dispatch::c_is_not_abstract():
    assert not inspect.isabstract(dispatch::C)


def test_dispatch::c_constructor_exists():
    assert callable(dispatch::C.__init__)


def test_dispatch::c_constructor_args():
    sig = inspect.signature(dispatch::C.__init__)
    params = list(sig.parameters.keys())



def test_dispatch::b_is_not_abstract():
    assert not inspect.isabstract(dispatch::B)


def test_dispatch::b_constructor_exists():
    assert callable(dispatch::B.__init__)


def test_dispatch::b_constructor_args():
    sig = inspect.signature(dispatch::B.__init__)
    params = list(sig.parameters.keys())



def test_dispatch::a_is_not_abstract():
    assert not inspect.isabstract(dispatch::A)


def test_dispatch::a_constructor_exists():
    assert callable(dispatch::A.__init__)


def test_dispatch::a_constructor_args():
    sig = inspect.signature(dispatch::A.__init__)
    params = list(sig.parameters.keys())



def test_dispatch::container_is_not_abstract():
    assert not inspect.isabstract(dispatch::Container)


def test_dispatch::container_constructor_exists():
    assert callable(dispatch::Container.__init__)


def test_dispatch::container_constructor_args():
    sig = inspect.signature(dispatch::Container.__init__)
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
dispatch::G_strategy = st.builds(
    dispatch::G,
)
dispatch::F_strategy = st.builds(
    dispatch::F,
)
B_strategy = st.builds(
    B,
)
dispatch::E_strategy = st.builds(
    dispatch::E,
)
dispatch::D_strategy = st.builds(
    dispatch::D,
)
A_strategy = st.builds(
    A,
)
dispatch::C_strategy = st.builds(
    dispatch::C,
)
dispatch::B_strategy = st.builds(
    dispatch::B,
)
dispatch::A_strategy = st.builds(
    dispatch::A,
)
dispatch::Container_strategy = st.builds(
    dispatch::Container,
)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=dispatch::G_strategy)
@settings(max_examples=50)
def test_dispatch::g_instantiation(instance):
    assert isinstance(instance, dispatch::G)

@given(instance=dispatch::F_strategy)
@settings(max_examples=50)
def test_dispatch::f_instantiation(instance):
    assert isinstance(instance, dispatch::F)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=dispatch::E_strategy)
@settings(max_examples=50)
def test_dispatch::e_instantiation(instance):
    assert isinstance(instance, dispatch::E)

@given(instance=dispatch::D_strategy)
@settings(max_examples=50)
def test_dispatch::d_instantiation(instance):
    assert isinstance(instance, dispatch::D)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=dispatch::C_strategy)
@settings(max_examples=50)
def test_dispatch::c_instantiation(instance):
    assert isinstance(instance, dispatch::C)

@given(instance=dispatch::B_strategy)
@settings(max_examples=50)
def test_dispatch::b_instantiation(instance):
    assert isinstance(instance, dispatch::B)

@given(instance=dispatch::A_strategy)
@settings(max_examples=50)
def test_dispatch::a_instantiation(instance):
    assert isinstance(instance, dispatch::A)

@given(instance=dispatch::Container_strategy)
@settings(max_examples=50)
def test_dispatch::container_instantiation(instance):
    assert isinstance(instance, dispatch::Container)
