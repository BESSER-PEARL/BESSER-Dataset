import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Master_N,
    B,
    N,
    Master_test2_B,
    Master_Classe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_master_n_is_not_abstract():
    assert not inspect.isabstract(Master_N)


def test_master_n_constructor_exists():
    assert callable(Master_N.__init__)


def test_master_n_constructor_args():
    sig = inspect.signature(Master_N.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"

def test_master_n_has_n():
    assert hasattr(Master_N, "n")
    descriptor = None
    for klass in Master_N.__mro__:
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



def test_master_test2_b_is_not_abstract():
    assert not inspect.isabstract(Master_test2_B)


def test_master_test2_b_constructor_exists():
    assert callable(Master_test2_B.__init__)


def test_master_test2_b_constructor_args():
    sig = inspect.signature(Master_test2_B.__init__)
    params = list(sig.parameters.keys())
    assert "nb" in params, "Missing parameter 'nb'"
    assert "nb2" in params, "Missing parameter 'nb2'"

def test_master_test2_b_has_nb():
    assert hasattr(Master_test2_B, "nb")
    descriptor = None
    for klass in Master_test2_B.__mro__:
        if "nb" in klass.__dict__:
            descriptor = klass.__dict__["nb"]
            break
    assert isinstance(descriptor, property)

def test_master_test2_b_has_nb2():
    assert hasattr(Master_test2_B, "nb2")
    descriptor = None
    for klass in Master_test2_B.__mro__:
        if "nb2" in klass.__dict__:
            descriptor = klass.__dict__["nb2"]
            break
    assert isinstance(descriptor, property)



def test_master_classe_is_not_abstract():
    assert not inspect.isabstract(Master_Classe)


def test_master_classe_constructor_exists():
    assert callable(Master_Classe.__init__)


def test_master_classe_constructor_args():
    sig = inspect.signature(Master_Classe.__init__)
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
Master_N_strategy = st.builds(
    Master_N,
    n=
        safe_text
)
B_strategy = st.builds(
    B,
)
N_strategy = st.builds(
    N,
)
Master_test2_B_strategy = st.builds(
    Master_test2_B,
    nb=
        st.integers(),
    nb2=
        st.integers()
)
Master_Classe_strategy = st.builds(
    Master_Classe,
)

@given(instance=Master_N_strategy)
@settings(max_examples=50)
def test_master_n_instantiation(instance):
    assert isinstance(instance, Master_N)



@given(instance=Master_N_strategy)
def test_master_n_n_setter(instance):
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

@given(instance=Master_test2_B_strategy)
@settings(max_examples=50)
def test_master_test2_b_instantiation(instance):
    assert isinstance(instance, Master_test2_B)



@given(instance=Master_test2_B_strategy)
def test_master_test2_b_nb_setter(instance):
    original = instance.nb
    instance.nb = original
    assert instance.nb == original



@given(instance=Master_test2_B_strategy)
def test_master_test2_b_nb2_setter(instance):
    original = instance.nb2
    instance.nb2 = original
    assert instance.nb2 == original

@given(instance=Master_Classe_strategy)
@settings(max_examples=50)
def test_master_classe_instantiation(instance):
    assert isinstance(instance, Master_Classe)
