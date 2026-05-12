import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpletest_X,
    simpletest_N,
    N,
    simpletest_L,
    simpletest_B,
    simpletest_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletest_x_is_not_abstract():
    assert not inspect.isabstract(simpletest_X)


def test_simpletest_x_constructor_exists():
    assert callable(simpletest_X.__init__)


def test_simpletest_x_constructor_args():
    sig = inspect.signature(simpletest_X.__init__)
    params = list(sig.parameters.keys())



def test_simpletest_n_is_not_abstract():
    assert not inspect.isabstract(simpletest_N)


def test_simpletest_n_constructor_exists():
    assert callable(simpletest_N.__init__)


def test_simpletest_n_constructor_args():
    sig = inspect.signature(simpletest_N.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpletest_n_has_name():
    assert hasattr(simpletest_N, "name")
    descriptor = None
    for klass in simpletest_N.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_n_is_not_abstract():
    assert not inspect.isabstract(N)


def test_n_constructor_exists():
    assert callable(N.__init__)


def test_n_constructor_args():
    sig = inspect.signature(N.__init__)
    params = list(sig.parameters.keys())



def test_simpletest_l_is_not_abstract():
    assert not inspect.isabstract(simpletest_L)


def test_simpletest_l_constructor_exists():
    assert callable(simpletest_L.__init__)


def test_simpletest_l_constructor_args():
    sig = inspect.signature(simpletest_L.__init__)
    params = list(sig.parameters.keys())



def test_simpletest_b_is_not_abstract():
    assert not inspect.isabstract(simpletest_B)


def test_simpletest_b_constructor_exists():
    assert callable(simpletest_B.__init__)


def test_simpletest_b_constructor_args():
    sig = inspect.signature(simpletest_B.__init__)
    params = list(sig.parameters.keys())



def test_simpletest_a_is_not_abstract():
    assert not inspect.isabstract(simpletest_A)


def test_simpletest_a_constructor_exists():
    assert callable(simpletest_A.__init__)


def test_simpletest_a_constructor_args():
    sig = inspect.signature(simpletest_A.__init__)
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
simpletest_X_strategy = st.builds(
    simpletest_X,
)
simpletest_N_strategy = st.builds(
    simpletest_N,
    name=
        safe_text
)
N_strategy = st.builds(
    N,
)
simpletest_L_strategy = st.builds(
    simpletest_L,
)
simpletest_B_strategy = st.builds(
    simpletest_B,
)
simpletest_A_strategy = st.builds(
    simpletest_A,
)

@given(instance=simpletest_X_strategy)
@settings(max_examples=50)
def test_simpletest_x_instantiation(instance):
    assert isinstance(instance, simpletest_X)

@given(instance=simpletest_N_strategy)
@settings(max_examples=50)
def test_simpletest_n_instantiation(instance):
    assert isinstance(instance, simpletest_N)



@given(instance=simpletest_N_strategy)
def test_simpletest_n_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=N_strategy)
@settings(max_examples=50)
def test_n_instantiation(instance):
    assert isinstance(instance, N)

@given(instance=simpletest_L_strategy)
@settings(max_examples=50)
def test_simpletest_l_instantiation(instance):
    assert isinstance(instance, simpletest_L)

@given(instance=simpletest_B_strategy)
@settings(max_examples=50)
def test_simpletest_b_instantiation(instance):
    assert isinstance(instance, simpletest_B)

@given(instance=simpletest_A_strategy)
@settings(max_examples=50)
def test_simpletest_a_instantiation(instance):
    assert isinstance(instance, simpletest_A)
