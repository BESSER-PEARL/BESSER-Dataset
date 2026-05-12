import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mnoq_M,
    mnoq_N,
    mnoq_Q,
    mnoq_O,
    mnoq_Foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mnoq_m_is_not_abstract():
    assert not inspect.isabstract(mnoq_M)


def test_mnoq_m_constructor_exists():
    assert callable(mnoq_M.__init__)


def test_mnoq_m_constructor_args():
    sig = inspect.signature(mnoq_M.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mnoq_m_has_x():
    assert hasattr(mnoq_M, "x")
    descriptor = None
    for klass in mnoq_M.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mnoq_n_is_not_abstract():
    assert not inspect.isabstract(mnoq_N)


def test_mnoq_n_constructor_exists():
    assert callable(mnoq_N.__init__)


def test_mnoq_n_constructor_args():
    sig = inspect.signature(mnoq_N.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mnoq_n_has_x():
    assert hasattr(mnoq_N, "x")
    descriptor = None
    for klass in mnoq_N.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mnoq_q_is_not_abstract():
    assert not inspect.isabstract(mnoq_Q)


def test_mnoq_q_constructor_exists():
    assert callable(mnoq_Q.__init__)


def test_mnoq_q_constructor_args():
    sig = inspect.signature(mnoq_Q.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mnoq_q_has_x():
    assert hasattr(mnoq_Q, "x")
    descriptor = None
    for klass in mnoq_Q.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mnoq_o_is_not_abstract():
    assert not inspect.isabstract(mnoq_O)


def test_mnoq_o_constructor_exists():
    assert callable(mnoq_O.__init__)


def test_mnoq_o_constructor_args():
    sig = inspect.signature(mnoq_O.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mnoq_o_has_x():
    assert hasattr(mnoq_O, "x")
    descriptor = None
    for klass in mnoq_O.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mnoq_foo_is_not_abstract():
    assert not inspect.isabstract(mnoq_Foo)


def test_mnoq_foo_constructor_exists():
    assert callable(mnoq_Foo.__init__)


def test_mnoq_foo_constructor_args():
    sig = inspect.signature(mnoq_Foo.__init__)
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
mnoq_M_strategy = st.builds(
    mnoq_M,
    x=
        st.integers()
)
mnoq_N_strategy = st.builds(
    mnoq_N,
    x=
        st.integers()
)
mnoq_Q_strategy = st.builds(
    mnoq_Q,
    x=
        st.integers()
)
mnoq_O_strategy = st.builds(
    mnoq_O,
    x=
        st.integers()
)
mnoq_Foo_strategy = st.builds(
    mnoq_Foo,
)

@given(instance=mnoq_M_strategy)
@settings(max_examples=50)
def test_mnoq_m_instantiation(instance):
    assert isinstance(instance, mnoq_M)



@given(instance=mnoq_M_strategy)
def test_mnoq_m_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mnoq_N_strategy)
@settings(max_examples=50)
def test_mnoq_n_instantiation(instance):
    assert isinstance(instance, mnoq_N)



@given(instance=mnoq_N_strategy)
def test_mnoq_n_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mnoq_Q_strategy)
@settings(max_examples=50)
def test_mnoq_q_instantiation(instance):
    assert isinstance(instance, mnoq_Q)



@given(instance=mnoq_Q_strategy)
def test_mnoq_q_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mnoq_O_strategy)
@settings(max_examples=50)
def test_mnoq_o_instantiation(instance):
    assert isinstance(instance, mnoq_O)



@given(instance=mnoq_O_strategy)
def test_mnoq_o_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mnoq_Foo_strategy)
@settings(max_examples=50)
def test_mnoq_foo_instantiation(instance):
    assert isinstance(instance, mnoq_Foo)
