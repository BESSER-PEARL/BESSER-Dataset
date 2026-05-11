import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test2::N,
    B,
    N,
    test2::test22::B,
    test2::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test2::n_is_not_abstract():
    assert not inspect.isabstract(test2::N)


def test_test2::n_constructor_exists():
    assert callable(test2::N.__init__)


def test_test2::n_constructor_args():
    sig = inspect.signature(test2::N.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_test2::n_has_n():
    assert hasattr(test2::N, "n")
    descriptor = None
    for klass in test2::N.__mro__:
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



def test_test2::test22::b_is_not_abstract():
    assert not inspect.isabstract(test2::test22::B)


def test_test2::test22::b_constructor_exists():
    assert callable(test2::test22::B.__init__)


def test_test2::test22::b_constructor_args():
    sig = inspect.signature(test2::test22::B.__init__)
    params = list(sig.parameters.keys())
    assert "nb2" in params, "Missing parameter 'nb2'"
    assert "nb" in params, "Missing parameter 'nb'"

def test_test2::test22::b_has_nb2():
    assert hasattr(test2::test22::B, "nb2")
    descriptor = None
    for klass in test2::test22::B.__mro__:
        if "nb2" in klass.__dict__:
            descriptor = klass.__dict__["nb2"]
            break
    assert isinstance(descriptor, property)

def test_test2::test22::b_has_nb():
    assert hasattr(test2::test22::B, "nb")
    descriptor = None
    for klass in test2::test22::B.__mro__:
        if "nb" in klass.__dict__:
            descriptor = klass.__dict__["nb"]
            break
    assert isinstance(descriptor, property)



def test_test2::a_is_not_abstract():
    assert not inspect.isabstract(test2::A)


def test_test2::a_constructor_exists():
    assert callable(test2::A.__init__)


def test_test2::a_constructor_args():
    sig = inspect.signature(test2::A.__init__)
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
test2::N_strategy = st.builds(
    test2::N,
    n=
        safe_text
)
B_strategy = st.builds(
    B,
)
N_strategy = st.builds(
    N,
)
test2::test22::B_strategy = st.builds(
    test2::test22::B,
    nb2=
        st.integers(),
    nb=
        st.integers()
)
test2::A_strategy = st.builds(
    test2::A,
)

@given(instance=test2::N_strategy)
@settings(max_examples=50)
def test_test2::n_instantiation(instance):
    assert isinstance(instance, test2::N)

@given(instance=test2::N_strategy)
def test_test2::n_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=test2::N_strategy)
def test_test2::n_n_setter(instance):
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

@given(instance=test2::test22::B_strategy)
@settings(max_examples=50)
def test_test2::test22::b_instantiation(instance):
    assert isinstance(instance, test2::test22::B)

@given(instance=test2::test22::B_strategy)
def test_test2::test22::b_nb2_type(instance):
    assert isinstance(instance.nb2, int)


@given(instance=test2::test22::B_strategy)
def test_test2::test22::b_nb2_setter(instance):
    original = instance.nb2
    instance.nb2 = original
    assert instance.nb2 == original

@given(instance=test2::test22::B_strategy)
def test_test2::test22::b_nb_type(instance):
    assert isinstance(instance.nb, int)


@given(instance=test2::test22::B_strategy)
def test_test2::test22::b_nb_setter(instance):
    original = instance.nb
    instance.nb = original
    assert instance.nb == original

@given(instance=test2::A_strategy)
@settings(max_examples=50)
def test_test2::a_instantiation(instance):
    assert isinstance(instance, test2::A)
