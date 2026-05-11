import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mnoq::M,
    mnoq::N,
    mnoq::Q,
    mnoq::O,
    mnoq::Foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mnoq::m_is_not_abstract():
    assert not inspect.isabstract(mnoq::M)


def test_mnoq::m_constructor_exists():
    assert callable(mnoq::M.__init__)


def test_mnoq::m_constructor_args():
    sig = inspect.signature(mnoq::M.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mnoq::m_has_x():
    assert hasattr(mnoq::M, "x")
    descriptor = None
    for klass in mnoq::M.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mnoq::n_is_not_abstract():
    assert not inspect.isabstract(mnoq::N)


def test_mnoq::n_constructor_exists():
    assert callable(mnoq::N.__init__)


def test_mnoq::n_constructor_args():
    sig = inspect.signature(mnoq::N.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mnoq::n_has_x():
    assert hasattr(mnoq::N, "x")
    descriptor = None
    for klass in mnoq::N.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mnoq::q_is_not_abstract():
    assert not inspect.isabstract(mnoq::Q)


def test_mnoq::q_constructor_exists():
    assert callable(mnoq::Q.__init__)


def test_mnoq::q_constructor_args():
    sig = inspect.signature(mnoq::Q.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mnoq::q_has_x():
    assert hasattr(mnoq::Q, "x")
    descriptor = None
    for klass in mnoq::Q.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mnoq::o_is_not_abstract():
    assert not inspect.isabstract(mnoq::O)


def test_mnoq::o_constructor_exists():
    assert callable(mnoq::O.__init__)


def test_mnoq::o_constructor_args():
    sig = inspect.signature(mnoq::O.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_mnoq::o_has_x():
    assert hasattr(mnoq::O, "x")
    descriptor = None
    for klass in mnoq::O.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mnoq::foo_is_not_abstract():
    assert not inspect.isabstract(mnoq::Foo)


def test_mnoq::foo_constructor_exists():
    assert callable(mnoq::Foo.__init__)


def test_mnoq::foo_constructor_args():
    sig = inspect.signature(mnoq::Foo.__init__)
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
mnoq::M_strategy = st.builds(
    mnoq::M,
    x=
        st.integers()
)
mnoq::N_strategy = st.builds(
    mnoq::N,
    x=
        st.integers()
)
mnoq::Q_strategy = st.builds(
    mnoq::Q,
    x=
        st.integers()
)
mnoq::O_strategy = st.builds(
    mnoq::O,
    x=
        st.integers()
)
mnoq::Foo_strategy = st.builds(
    mnoq::Foo,
)

@given(instance=mnoq::M_strategy)
@settings(max_examples=50)
def test_mnoq::m_instantiation(instance):
    assert isinstance(instance, mnoq::M)

@given(instance=mnoq::M_strategy)
def test_mnoq::m_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=mnoq::M_strategy)
def test_mnoq::m_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mnoq::N_strategy)
@settings(max_examples=50)
def test_mnoq::n_instantiation(instance):
    assert isinstance(instance, mnoq::N)

@given(instance=mnoq::N_strategy)
def test_mnoq::n_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=mnoq::N_strategy)
def test_mnoq::n_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mnoq::Q_strategy)
@settings(max_examples=50)
def test_mnoq::q_instantiation(instance):
    assert isinstance(instance, mnoq::Q)

@given(instance=mnoq::Q_strategy)
def test_mnoq::q_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=mnoq::Q_strategy)
def test_mnoq::q_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mnoq::O_strategy)
@settings(max_examples=50)
def test_mnoq::o_instantiation(instance):
    assert isinstance(instance, mnoq::O)

@given(instance=mnoq::O_strategy)
def test_mnoq::o_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=mnoq::O_strategy)
def test_mnoq::o_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mnoq::Foo_strategy)
@settings(max_examples=50)
def test_mnoq::foo_instantiation(instance):
    assert isinstance(instance, mnoq::Foo)
