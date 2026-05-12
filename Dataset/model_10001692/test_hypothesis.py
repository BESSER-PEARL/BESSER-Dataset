import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MyClass9,
    c3,
    c2,
    c,
    z,
    Y,
    B,
    A,
    R,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myclass9_is_not_abstract():
    assert not inspect.isabstract(MyClass9)


def test_myclass9_constructor_exists():
    assert callable(MyClass9.__init__)


def test_myclass9_constructor_args():
    sig = inspect.signature(MyClass9.__init__)
    params = list(sig.parameters.keys())



def test_c3_is_not_abstract():
    assert not inspect.isabstract(c3)


def test_c3_constructor_exists():
    assert callable(c3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(c3.__init__)
    params = list(sig.parameters.keys())



def test_c2_is_not_abstract():
    assert not inspect.isabstract(c2)


def test_c2_constructor_exists():
    assert callable(c2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(c2.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(c)


def test_c_constructor_exists():
    assert callable(c.__init__)


def test_c_constructor_args():
    sig = inspect.signature(c.__init__)
    params = list(sig.parameters.keys())



def test_z_is_not_abstract():
    assert not inspect.isabstract(z)


def test_z_constructor_exists():
    assert callable(z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(z.__init__)
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



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_r_is_not_abstract():
    assert not inspect.isabstract(R)


def test_r_constructor_exists():
    assert callable(R.__init__)


def test_r_constructor_args():
    sig = inspect.signature(R.__init__)
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
MyClass9_strategy = st.builds(
    MyClass9,
)
c3_strategy = st.builds(
    c3,
)
c2_strategy = st.builds(
    c2,
)
c_strategy = st.builds(
    c,
)
z_strategy = st.builds(
    z,
)
Y_strategy = st.builds(
    Y,
)
B_strategy = st.builds(
    B,
)
A_strategy = st.builds(
    A,
)
R_strategy = st.builds(
    R,
)

@given(instance=MyClass9_strategy)
@settings(max_examples=50)
def test_myclass9_instantiation(instance):
    assert isinstance(instance, MyClass9)

@given(instance=c3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, c3)

@given(instance=c2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, c2)

@given(instance=c_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, c)

@given(instance=z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, z)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)
