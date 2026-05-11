import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    uml2::N,
    B,
    N,
    uml2::test2::B,
    uml2::Classe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2::n_is_not_abstract():
    assert not inspect.isabstract(uml2::N)


def test_uml2::n_constructor_exists():
    assert callable(uml2::N.__init__)


def test_uml2::n_constructor_args():
    sig = inspect.signature(uml2::N.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_uml2::n_has_n():
    assert hasattr(uml2::N, "n")
    descriptor = None
    for klass in uml2::N.__mro__:
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



def test_uml2::test2::b_is_not_abstract():
    assert not inspect.isabstract(uml2::test2::B)


def test_uml2::test2::b_constructor_exists():
    assert callable(uml2::test2::B.__init__)


def test_uml2::test2::b_constructor_args():
    sig = inspect.signature(uml2::test2::B.__init__)
    params = list(sig.parameters.keys())
    assert "nb" in params, "Missing parameter 'nb'"
    assert "nb2" in params, "Missing parameter 'nb2'"

def test_uml2::test2::b_has_nb():
    assert hasattr(uml2::test2::B, "nb")
    descriptor = None
    for klass in uml2::test2::B.__mro__:
        if "nb" in klass.__dict__:
            descriptor = klass.__dict__["nb"]
            break
    assert isinstance(descriptor, property)

def test_uml2::test2::b_has_nb2():
    assert hasattr(uml2::test2::B, "nb2")
    descriptor = None
    for klass in uml2::test2::B.__mro__:
        if "nb2" in klass.__dict__:
            descriptor = klass.__dict__["nb2"]
            break
    assert isinstance(descriptor, property)



def test_uml2::classe_is_not_abstract():
    assert not inspect.isabstract(uml2::Classe)


def test_uml2::classe_constructor_exists():
    assert callable(uml2::Classe.__init__)


def test_uml2::classe_constructor_args():
    sig = inspect.signature(uml2::Classe.__init__)
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
uml2::N_strategy = st.builds(
    uml2::N,
    n=
        safe_text
)
B_strategy = st.builds(
    B,
)
N_strategy = st.builds(
    N,
)
uml2::test2::B_strategy = st.builds(
    uml2::test2::B,
    nb=
        st.integers(),
    nb2=
        st.integers()
)
uml2::Classe_strategy = st.builds(
    uml2::Classe,
)

@given(instance=uml2::N_strategy)
@settings(max_examples=50)
def test_uml2::n_instantiation(instance):
    assert isinstance(instance, uml2::N)

@given(instance=uml2::N_strategy)
def test_uml2::n_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=uml2::N_strategy)
def test_uml2::n_n_setter(instance):
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

@given(instance=uml2::test2::B_strategy)
@settings(max_examples=50)
def test_uml2::test2::b_instantiation(instance):
    assert isinstance(instance, uml2::test2::B)

@given(instance=uml2::test2::B_strategy)
def test_uml2::test2::b_nb_type(instance):
    assert isinstance(instance.nb, int)


@given(instance=uml2::test2::B_strategy)
def test_uml2::test2::b_nb_setter(instance):
    original = instance.nb
    instance.nb = original
    assert instance.nb == original

@given(instance=uml2::test2::B_strategy)
def test_uml2::test2::b_nb2_type(instance):
    assert isinstance(instance.nb2, int)


@given(instance=uml2::test2::B_strategy)
def test_uml2::test2::b_nb2_setter(instance):
    original = instance.nb2
    instance.nb2 = original
    assert instance.nb2 == original

@given(instance=uml2::Classe_strategy)
@settings(max_examples=50)
def test_uml2::classe_instantiation(instance):
    assert isinstance(instance, uml2::Classe)
