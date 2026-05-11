import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::N,
    B,
    N,
    test::test2::B,
    test::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::n_is_not_abstract():
    assert not inspect.isabstract(test::N)


def test_test::n_constructor_exists():
    assert callable(test::N.__init__)


def test_test::n_constructor_args():
    sig = inspect.signature(test::N.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_test::n_has_n():
    assert hasattr(test::N, "n")
    descriptor = None
    for klass in test::N.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_n_is_not_abstract():
    assert not inspect.isabstract(N)


def test_n_constructor_exists():
    assert callable(N.__init__)


def test_n_constructor_args():
    sig = inspect.signature(N.__init__)
    params = list(sig.parameters.keys())



def test_test::test2::b_is_not_abstract():
    assert not inspect.isabstract(test::test2::B)


def test_test::test2::b_constructor_exists():
    assert callable(test::test2::B.__init__)


def test_test::test2::b_constructor_args():
    sig = inspect.signature(test::test2::B.__init__)
    params = list(sig.parameters.keys())
    assert "nb2" in params, "Missing parameter 'nb2'"
    assert "nb" in params, "Missing parameter 'nb'"

def test_test::test2::b_has_nb2():
    assert hasattr(test::test2::B, "nb2")
    descriptor = None
    for klass in test::test2::B.__mro__:
        if "nb2" in klass.__dict__:
            descriptor = klass.__dict__["nb2"]
            break
    assert isinstance(descriptor, property)

def test_test::test2::b_has_nb():
    assert hasattr(test::test2::B, "nb")
    descriptor = None
    for klass in test::test2::B.__mro__:
        if "nb" in klass.__dict__:
            descriptor = klass.__dict__["nb"]
            break
    assert isinstance(descriptor, property)



def test_test::a_is_not_abstract():
    assert not inspect.isabstract(test::A)


def test_test::a_constructor_exists():
    assert callable(test::A.__init__)


def test_test::a_constructor_args():
    sig = inspect.signature(test::A.__init__)
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
test::N_strategy = st.builds(
    test::N,
    n=
        safe_text
)
B_strategy = st.builds(
    B,
)
N_strategy = st.builds(
    N,
)
test::test2::B_strategy = st.builds(
    test::test2::B,
    nb2=
        st.integers(),
    nb=
        st.integers()
)
test::A_strategy = st.builds(
    test::A,
)

@given(instance=test::N_strategy)
@settings(max_examples=50)
def test_test::n_instantiation(instance):
    assert isinstance(instance, test::N)

@given(instance=test::N_strategy)
def test_test::n_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=test::N_strategy)
def test_test::n_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=N_strategy)
@settings(max_examples=50)
def test_n_instantiation(instance):
    assert isinstance(instance, N)

@given(instance=test::test2::B_strategy)
@settings(max_examples=50)
def test_test::test2::b_instantiation(instance):
    assert isinstance(instance, test::test2::B)

@given(instance=test::test2::B_strategy)
def test_test::test2::b_nb2_type(instance):
    assert isinstance(instance.nb2, int)


@given(instance=test::test2::B_strategy)
def test_test::test2::b_nb2_setter(instance):
    original = instance.nb2
    instance.nb2 = original
    assert instance.nb2 == original

@given(instance=test::test2::B_strategy)
def test_test::test2::b_nb_type(instance):
    assert isinstance(instance.nb, int)


@given(instance=test::test2::B_strategy)
def test_test::test2::b_nb_setter(instance):
    original = instance.nb
    instance.nb = original
    assert instance.nb == original

@given(instance=test::A_strategy)
@settings(max_examples=50)
def test_test::a_instantiation(instance):
    assert isinstance(instance, test::A)
